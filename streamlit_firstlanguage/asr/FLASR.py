import io
import os
import base64
import sys
import time
import warnings
from copy import deepcopy
from pathlib import Path
from typing import (Iterable, List, Optional,
                    TextIO, Union)
import riva.client
import riva.client.audio_io
import riva.client.proto.riva_asr_pb2 as rasr
import streamlit as st
import json
from st_on_hover_tabs import on_hover_tabs


uri = st.secrets["riva_url"]  # Default value

lang="en-US"
qryParam =st.experimental_get_query_params()


if "lang" in qryParam:
    if qryParam["lang"][0]:
        lang=qryParam["lang"][0]

auth = riva.client.Auth(uri=uri)

asr_service = riva.client.ASRService(auth)

offline_config = riva.client.RecognitionConfig(
    encoding=riva.client.AudioEncoding.LINEAR_PCM,
    max_alternatives=1,
    language_code = lang,
    enable_automatic_punctuation=True,
    verbatim_transcripts=False,
)
streaming_config = riva.client.StreamingRecognitionConfig(config=deepcopy(offline_config), interim_results=False)

st.set_page_config(layout="wide")
st.image("Original.png", width=100)
st.title("FirstLanguage ASR Demo")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

riva.client.add_word_boosting_to_config(offline_config, ["AntiBERTA"], 20)
riva.client.add_word_boosting_to_config(offline_config, ["ABLooper"], 10)



PRINT_STREAMING_ADDITIONAL_INFO_MODES = ['no', 'time', 'confidence']
textReturned = ''

def print_streaming(
    responses: Iterable[rasr.StreamingRecognizeResponse],
    output_file: Optional[Union[Union[os.PathLike, str, TextIO], List[Union[os.PathLike, str, TextIO]]]] = None,
    additional_info: str = 'no',
    word_time_offsets: bool = False,
    show_intermediate: bool = False,
    file_mode: str = 'w',
):
    global textReturned 
     
    if additional_info not in PRINT_STREAMING_ADDITIONAL_INFO_MODES:
        raise ValueError(
            f"Not allowed value '{additional_info}' of parameter `additional_info`. "
            f"Allowed values are {PRINT_STREAMING_ADDITIONAL_INFO_MODES}"
        )
    if additional_info != PRINT_STREAMING_ADDITIONAL_INFO_MODES[0] and show_intermediate:
        warnings.warn(
            f"`show_intermediate=True` will not work if "
            f"`additional_info != {PRINT_STREAMING_ADDITIONAL_INFO_MODES[0]}`. `additional_info={additional_info}`"
        )
    if additional_info != PRINT_STREAMING_ADDITIONAL_INFO_MODES[1] and word_time_offsets:
        warnings.warn(
            f"`word_time_offsets=True` will not work if "
            f"`additional_info != {PRINT_STREAMING_ADDITIONAL_INFO_MODES[1]}`. `additional_info={additional_info}"
        )
    if output_file is None:
        output_file = [sys.stdout]
    elif not isinstance(output_file, list):
        output_file = [output_file]
    file_opened = [False] * len(output_file)
    try:
        for i, elem in enumerate(output_file):
            if isinstance(elem, io.TextIOBase):
                file_opened[i] = False
            else:
                file_opened[i] = True
                output_file[i] = Path(elem).expanduser().open(file_mode)
        start_time = time.time()  # used in 'time` additional_info
        num_chars_printed = 0  # used in 'no' additional_info
        for response in responses:
            if not response.results:
                continue
            partial_transcript = ""
            for result in response.results:
                if not result.alternatives:
                    continue
                transcript = result.alternatives[0].transcript
                if additional_info == 'no':
                    if result.is_final:
                        if show_intermediate:
                            overwrite_chars = ' ' * (num_chars_printed - len(transcript))
                            # for i, f in enumerate(output_file):
                            #     f.write("## " + transcript + (overwrite_chars if not file_opened[i] else '') + "\n")
                            num_chars_printed = 0
                        else:
                            for i, alternative in enumerate(result.alternatives):
                                # for f in output_file:
                                #     f.write(
                                #         f'##'
                                #         + (f'(alternative {i + 1})' if i > 0 else '')
                                #         + f' {alternative.transcript}\n'
                                #     )
                                textReturned+=(f'(alternative {i + 1})' if i > 0 else '') + f' {alternative.transcript}'  
                            print('###########'+textReturned)
                            st.markdown(f"**Text:** {textReturned}")
                            textReturned=''
                            #q.put(textReturned) 
                    else:
                        partial_transcript += transcript
                elif additional_info == 'time':
                    if result.is_final:
                        for i, alternative in enumerate(result.alternatives):
                            for f in output_file:
                                f.write(
                                    f"Time {time.time() - start_time:.2f}s: Transcript {i}: {alternative.transcript}\n"
                                )
                        if word_time_offsets:
                            for f in output_file:
                                f.write("Timestamps:\n")
                                f.write('{: <40s}{: <16s}{: <16s}\n'.format('Word', 'Start (ms)', 'End (ms)'))
                                for word_info in result.alternatives[0].words:
                                    f.write(
                                        f'{word_info.word: <40s}{word_info.start_time: <16.0f}'
                                        f'{word_info.end_time: <16.0f}\n'
                                    )
                    else:
                        partial_transcript += transcript
                else:  # additional_info == 'confidence'
                    if result.is_final:
                        for f in output_file:
                            f.write(f'## {transcript}\n')
                            f.write(f'Confidence: {result.alternatives[0].confidence:9.4f}\n')
                    else:
                        for f in output_file:
                            f.write(f'>> {transcript}\n')
                            f.write(f'Stability: {result.stability:9.4f}\n')
            if additional_info == 'no':
                if show_intermediate and partial_transcript != '':
                    overwrite_chars = ' ' * (num_chars_printed - len(partial_transcript))
                    for i, f in enumerate(output_file):
                        f.write(">> " + partial_transcript + ('\n' if file_opened[i] else overwrite_chars + '\r'))
                    num_chars_printed = len(partial_transcript) + 3
            elif additional_info == 'time':
                for f in output_file:
                    if partial_transcript:
                        f.write(f">>>Time {time.time():.2f}s: {partial_transcript}\n")
            else:
                for f in output_file:
                    f.write('----\n')
    finally:        
        for fo, elem in zip(file_opened, output_file):
            if fo:
                elem.close()


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Offline ASR', 'Streaming ASR'], 
                         iconName=['play_circle', 'record_voice_over'], default_choice=0)

if tabs =='Offline ASR':
    st.header("Offline ASR Demo")
    st.caption("Ensure the audio file framerate is 16KHz")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.read()
        my_wav_file = uploaded_file.name
        offline_config.sample_rate_hertz = 16000
        #offline_config.audio_channel_count = 1        
        
        with st.spinner('Transcribing...'):
            response = asr_service.offline_recognize(bytes_data, offline_config)
            asr_best_transcript = response.results[0].alternatives[0].transcript
        
        #st.write("ASR Transcript:", asr_best_transcript)
        st.markdown("##### ASR Transcript:   \n"
        +asr_best_transcript)

elif tabs == 'Streaming ASR':
    st.header("Streaming ASR Demo")
    
       

    default_device_info = riva.client.audio_io.get_default_input_device_info()
    print(default_device_info)
    default_device_index = None if default_device_info is None else default_device_info['index']
    responses=[]
    default_device_index = 7
    input_device = 7  # default device
    streaming_config.config.sample_rate_hertz = 16000
    
    col1, col2 = st.columns(2)
    with col1:
        start_execution = st.button('Start Streaming')
    with col2:
        stop_exec = st.button('Stop Streaming')
    
    if start_execution:        
        file_ = open("sound.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="sound gif">',
            unsafe_allow_html=True,
        )
                
        micInput = riva.client.audio_io.MicrophoneStream(
            rate=16000,
            chunk=16000,
            device=input_device,
        )
        with micInput as audio_chunk_iterator:     
            if stop_exec:
                micInput.close()   
            print_streaming(
                responses=asr_service.streaming_response_generator(
                    audio_chunks=audio_chunk_iterator,
                    streaming_config=streaming_config,
                ),
                show_intermediate=False,
                additional_info = 'no',
            )
    
       



