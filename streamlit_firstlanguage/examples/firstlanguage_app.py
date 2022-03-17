import streamlit_firstlanguage as fl
import streamlit as st

colors = {
    "ADJ": "#a5129e",
    "ADP": "#fe0b44",
    "ADV": "#cc979a",
    "AUX": "#52a26d",
    "CONJ": "#05dddc",
    "CCONJ": "#4f5b9d",
    "DET": "#e59607",
    "INTJ": "#448939",
    "NOUN": "#d66fba",
    "NUM": "#839663",
    "PART": "#c5a331",
    "PRON":"#d66fba",
    "PROPN": "#fee57f",
    "PUNCT": "#1abe47",
    "SCONJ": "#5e5d97",
    "SYM": "#ed5786",
    "VERB": "#f7ce22",
    "X": "#2da640",
    "EOL": "#5e5d97",
    "SPACE": "#a9cf46",
}

st.title("FirstLanguage Streamlit Components Demo")

nlpTask = st.selectbox(
        "Select the NLP Task to test",
        ("Stemmer", "Lemmatizer", "Morphological Analyzer","POSTagger","Text Classification","Question Answering","Table Question Answering",
        "Image Captioning","Named Entity Recognition","Summarization","Translation" )
        )

st.write("If there is any error, it may be due to API throttling. Please wait for a while and try again.")

if nlpTask == "Stemmer":
    fl.firstlanguage_stem("fl_ner",st.secrets["api_key"], title="Stemmer",resTitle="Stemmed Text")

if nlpTask == "Lemmatizer":
    fl.firstlanguage_lemma("fl_lemma",st.secrets["api_key"], title="Lemmatizer",resTitle="Lemmatized Text")

if nlpTask == "Morphological Analyzer":
    fl.firstlanguage_morph("fl_morph",st.secrets["api_key"], title="Morphological Analyzer",resTitle="Morphological Analysis Output")

if nlpTask == "POSTagger":
    fl.firstlanguage_postag("fl_pos",st.secrets["api_key"], title="POSTagger",resTitle="POS Tagger Output", overRideColor=colors)

if nlpTask == "Text Classification":
    fl.firstlanguage_classify("fl_classify",st.secrets["api_key"], title="Text Classification",resTitle="Text Classification Output")

if nlpTask == "Question Answering":
    fl.firstlanguage_qa("fl_qa",st.secrets["api_key"], title="Question Answering",resTitle="Answers")

if nlpTask == "Table Question Answering":
    fl.firstlanguage_tableqa("fl_tableqa",st.secrets["api_key"], title="Table Question Answering",resTitle="Answers")

if nlpTask == "Image Captioning":
    fl.firstlanguage_imagecaption("fl_caption",st.secrets["api_key"], title="Image Captioning",resTitle="Caption output")

if nlpTask == "Named Entity Recognition":
    fl.firstlanguage_ner("fl_ner",st.secrets["api_key"], title="Named Entity Recognition",resTitle="NER Output")

if nlpTask == "Summarization":
    fl.firstlanguage_summary("fl_summarize",st.secrets["api_key"], title="Summarization",resTitle="Summarized Text")

if nlpTask == "Translation":
    fl.firstlanguage_translate("fl_translate",st.secrets["api_key"], title="Translation",resTitle="Translated Text")
