# Table of Contents

* [\_\_init\_\_](#__init__)
  * [firstlanguage\_postag](#__init__.firstlanguage_postag)
  * [firstlanguage\_ner](#__init__.firstlanguage_ner)
  * [firstlanguage\_stem](#__init__.firstlanguage_stem)
  * [firstlanguage\_lemma](#__init__.firstlanguage_lemma)
  * [firstlanguage\_classify](#__init__.firstlanguage_classify)
  * [firstlanguage\_morph](#__init__.firstlanguage_morph)
  * [firstlanguage\_qa](#__init__.firstlanguage_qa)
  * [firstlanguage\_imagecaption](#__init__.firstlanguage_imagecaption)
  * [firstlanguage\_summary](#__init__.firstlanguage_summary)
  * [firstlanguage\_tableqa](#__init__.firstlanguage_tableqa)
  * [firstlanguage\_translate](#__init__.firstlanguage_translate)

<a id="__init__"></a>

# \_\_init\_\_

<a id="__init__.firstlanguage_postag"></a>

#### firstlanguage\_postag

```python
def firstlanguage_postag(name,
                         apiKey,
                         posText=True,
                         title=None,
                         txtAreaLabel=None,
                         resTitle=None,
                         showAnnotated=True,
                         helpText=None,
                         height=None,
                         showLang=True,
                         overRideColor=None,
                         selectLabel=None,
                         lineBreak=4,
                         key=None)
```

Create a new instance of "firstlanguage_postag".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
posText: bool
    If True, the component will render a text area for the user to enter
    content to determine the POSTag. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to determine POSTag.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showAnnotated: bool
    If True, the component will display the annotated text in the result. 
    If False, the component will just return the list of strings and tuples 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language dropdown in the frontend.
    If false, the dropdown will not be visible and the default value of 'en' 
    wil be passed to the API.
overRideColor: str
    A Dict object in the format {"NOUN": "`a5129e`", "VERB": "`4f5b9d`"} to over-ride 
    the default color values for the POSTags annotation.
selectLabel: str
    The label for the language dropdown to display in the frontend.
lineBreak: int
    The number of words after which to introduce a line break. This helps in fitting the 
    output inside the container. Default value is 4.


Returns
-------
list
    The component will return a list of tuples and strings
    with annotation details and postags.

<a id="__init__.firstlanguage_ner"></a>

#### firstlanguage\_ner

```python
def firstlanguage_ner(name,
                      apiKey,
                      nerText=True,
                      title=None,
                      txtAreaLabel=None,
                      resTitle=None,
                      showAnnotated=True,
                      helpText=None,
                      height=None,
                      showLang=True,
                      overRideColor=None,
                      selectLabel=None,
                      key=None)
```

Create a new instance of "firstlanguage_ner".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
nerText: bool
    If True, the component will render a text area for the user to enter
    content to determine the NER. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to determine NER.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showAnnotated: bool
    If True, the component will display the annotated text in the result. 
    If False, the component will just return the list of strings and tuples 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language dropdown in the frontend.
    If false, the dropdown will not be visible and the default value of 'en' 
    wil be passed to the API.
overRideColor: str
    A Dict object in the format {"LOC": "`a5129e`", "PER": "`4f5b9d`"} to over-ride 
    the default color values for the NER annotation.
selectLabel: str
    The label for the language dropdown to display in the frontend.    

Returns
-------
list
    The component will return a list of tuples and strings
    with annotation details and NER entities.

<a id="__init__.firstlanguage_stem"></a>

#### firstlanguage\_stem

```python
def firstlanguage_stem(name,
                       apiKey,
                       stemText=True,
                       title=None,
                       txtAreaLabel=None,
                       resTitle=None,
                       showTable=True,
                       helpText=None,
                       height=None,
                       showLang=True,
                       langLabel=None,
                       key=None)
```

Create a new instance of "firstlanguage_stem".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
stemText: bool
    If True, the component will render a text area for the user to enter
    content to stem. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to stem the words.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showTable: bool
    If True, the component will display the stemmed text in the result. 
    If False, the component will just return the dict with stemmed words 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.

Returns
-------
dict
    The component will return a dict in the format {"originalText": [], "stemmedText": []}
    with originalText list and stemmedText list filled in.

<a id="__init__.firstlanguage_lemma"></a>

#### firstlanguage\_lemma

```python
def firstlanguage_lemma(name,
                        apiKey,
                        lemmaText=True,
                        title=None,
                        txtAreaLabel=None,
                        resTitle=None,
                        showTable=True,
                        helpText=None,
                        height=None,
                        showLang=True,
                        langLabel=None,
                        key=None)
```

Create a new instance of "firstlanguage_lemma".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
lemmaText: bool
    If True, the component will render a text area for the user to enter
    content to lemmatize. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to lemmatize the words.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showTable: bool
    If True, the component will display the lemmatize text in the result. 
    If False, the component will just return the dict with lemmatized words 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.

Returns
-------
dict
    The component will return a dict in the format {"originalText": [], "lemmatizedText": []}
    with originalText list and lemmatizedText list filled in.

<a id="__init__.firstlanguage_classify"></a>

#### firstlanguage\_classify

```python
def firstlanguage_classify(name,
                           apiKey,
                           classifyText=True,
                           title=None,
                           txtAreaLabel=None,
                           resTitle=None,
                           showGraph=True,
                           helpText=None,
                           height=None,
                           showLang=True,
                           langLabel=None,
                           showLabels=True,
                           labelTitle=None,
                           key=None)
```

Create a new instance of "firstlanguage_classify".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
classifyText: bool
    If True, the component will render a text area for the user to enter
    content to classify. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to classify.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showGraph: bool
    If True, the component will display the classification output as a graph. 
    If False, the component will just return the dict with classification results 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.
showLabels: bool
    Show the lebels to be classified in the frontend.
labelTitle: str
    The title of the labels section to display in the frontend.

Returns
-------
dict
    The component will return a dict in the format {"Labels": [], "Scores": []}
    with Labels list and Scores list filled in.

<a id="__init__.firstlanguage_morph"></a>

#### firstlanguage\_morph

```python
def firstlanguage_morph(name,
                        apiKey,
                        morphText=True,
                        title=None,
                        txtAreaLabel=None,
                        resTitle=None,
                        showTable=True,
                        helpText=None,
                        height=None,
                        showLang=True,
                        langLabel=None,
                        key=None)
```

Create a new instance of "firstlanguage_morph".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
morphText: bool
    If True, the component will render a text area for the user to enter
    content to find morphological features. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to find morphological features.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showTable: bool
    If True, the component will display the morphological featuresin the result. 
    If False, the component will just return the dict with morphological features 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.

Returns
-------
dict
    The component will return a dict in the format {"originalText": [], "morphFeatures": []}
    with originalText list and morphFeatures list filled in.

<a id="__init__.firstlanguage_qa"></a>

#### firstlanguage\_qa

```python
def firstlanguage_qa(name,
                     apiKey,
                     qaText=True,
                     title=None,
                     txtAreaLabel=None,
                     resTitle=None,
                     showAnnotated=True,
                     helpText=None,
                     height=None,
                     showLang=True,
                     langLabel=None,
                     qLabel=None,
                     key=None)
```

Create a new instance of "firstlanguage_qa".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
qaText: bool
    If True, the component will render a text area for the user to enter
    context to find answers for the questions passed. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to pass as the context.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showAnnotated: bool
    If True, the component will display the highlighted answer in the result. 
    If False, the component will just return the dict with answer 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.
qLabel: str
    The label for the question text field to display in the frontend.

Returns
-------
dict
    The component will return a dict in the original API response format.

<a id="__init__.firstlanguage_imagecaption"></a>

#### firstlanguage\_imagecaption

```python
def firstlanguage_imagecaption(name,
                               apiKey,
                               showURL=True,
                               title=None,
                               urlInputLabel=None,
                               resTitle=None,
                               showImage=True,
                               key=None)
```

Create a new instance of "firstlanguage_imagecaption".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
showURL: bool
    If True, the component will render a text input for the user to enter
    the image url to caption. If False, the component will not render the input
title: str
    The title of the component to display in the frontend.
urlInputLabel: str
    The label for the url input to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showImage: bool
    If True, the component will display the image with the generated caption. 
    If False, the component will just return a string with the generated caption.


Returns
-------
string
    The component will return the generated caption as a string.

<a id="__init__.firstlanguage_summary"></a>

#### firstlanguage\_summary

```python
def firstlanguage_summary(name,
                          apiKey,
                          summaryText=True,
                          title=None,
                          txtAreaLabel=None,
                          resTitle=None,
                          showSummaryResult=True,
                          helpText=None,
                          height=None,
                          showLang=True,
                          langLabel=None,
                          key=None)
```

Create a new instance of "firstlanguage_summary".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
summaryText: bool
    If True, the component will render a text area for the user to enter
    context to summarize. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to summarize.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showSummaryResult: bool
    If True, the component will display the summary result. 
    If False, the component will just return a string with the summary 
    for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.


Returns
-------
sring
    The component will return the summary as a string.

<a id="__init__.firstlanguage_tableqa"></a>

#### firstlanguage\_tableqa

```python
def firstlanguage_tableqa(name,
                          apiKey,
                          flatTableInput=True,
                          title=None,
                          inputLabel=None,
                          resTitle=None,
                          showResult=True,
                          helpText=None,
                          height=None,
                          showQuestions=True,
                          qLabel=None,
                          sendBackRows=False,
                          key=None)
```

Create a new instance of "firstlanguage_tableqa".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
flatTableInput: bool
    If True, the component will render a text area for the user to enter
    a flattable in JSON format. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract table.
title: str
    The title of the component to display in the frontend.
inputLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showResult: bool
    If True, the component will display the qa result. 
    If False, the component will just return a string with the answers for  
    questions for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showQuestions: bool
    If True, the component will display the questions text box in the frontend.
    If false, the text box will not be visible.    
qLabel: str
    The label for the language text box to display in the frontend.
sendBackRows: bool
    If True, the component will send back the rows of the table corresponding to the answer
    If False, the component will not send back the rows of the table corresponding to the answer

Returns
-------
dict
    The component will return a dict with questions,answers,rows and aggregrate used in the format
    {"Questions": [], "Anwsers": [], "Rows": [], "Aggregrate": "[]"}

<a id="__init__.firstlanguage_translate"></a>

#### firstlanguage\_translate

```python
def firstlanguage_translate(name,
                            apiKey,
                            translateText=True,
                            title=None,
                            txtAreaLabel=None,
                            resTitle=None,
                            showResult=True,
                            helpText=None,
                            height=None,
                            showLang=True,
                            langLabel=None,
                            pathToTmpFile=None,
                            key=None)
```

Create a new instance of "firstlanguage_translate".

Parameters
----------
name: str
    A short name for the component to identify it.
key: str or None
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.
apiKey: str
    The API key for the firstlanguage API. You can get the free API Key 
    from https://www.firstlanguage.in
translateText: bool
    If True, the component will render a text area for the user to enter
    text to translate. If False, the component will render
    an input field and contenType dropdown for the user to enter URL from 
    which the API wil extract the text to translate.
title: str
    The title of the component to display in the frontend.
txtAreaLabel: str
    The label for the text area to display in the frontend.
resTitle: str
    The title of the result section to display in the frontend.
showResult: bool
    If True, the component will display the translation result. Applicable only for Text Translation. 
    If False, the component will just return a string with the summary for the developer to process it further.
helpText: str
    Help text for the Text Area to display in the frontend.
height: int
    The height of the text area to display in the frontend.
showLang: bool
    If True, the component will display the language text box in the frontend.
    If false, the text box will not be visible and the default value of 'en' 
    wil be passed to the API.    
langLabel: str
    The label for the language text box to display in the frontend.
pathToTmpFile: str
    Temproray output dir for translation by URL with contentType as PDF or DOCX. File name
    will be of the format <timestamp>output.pdf or <timestamp>output.docx.
    If value is not provided, the component will create a temp file in the system temp dir

Returns
-------
sring
    The component will return the translated text as a string. This applies
    for text transaltion and URL translation with preserveFormat flag set to False. Dir path should end with /
    For preserveFormat flag set to True, the component will return the translated file as pdf or docx format.

