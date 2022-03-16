<a href="https://www.firstlanguage.in"><img src="https://img.firstlanguage.in/img/Original_9M3zC4lrHRd.webp?tr=w-100" width="125" height="125" align="right" />
</a>

# streamlit-firstlanguage: Streamlit Components to access FirstLanguage NLP API


This package provides interactive Streamlit components to access FirstLanguage NLP API. For full FirstLanguage API documentation, please visit our site [FirstLanguage API](https://firstlanguage.in)

For direct SDK options, please visit:

[Python SDK](https://github.com/FirstLanguage/firstlanguage_python)

[TypeScript SDK](https://github.com/FirstLanguage/firstlanguage-typescript)

## 🚀 Quickstart

You can install streamlit-firstlanguage from PyPi using pip:
```bash
pip install streamlit-firstlanguage
```

You will need API Key to access our API. Please register with us to get your life-time FREE API Key. Credit Card not required!!!

[Regsitration Page Link](https://www.firstlanguage.in/auth/create-account)


You can then access our API with one line of code.

For example, you can implement a Named Entity Recognition App with below code

```python
#ner.py
import streamlit_firstlanguage as fl

fl.firstlanguage_ner(name="fl_ner",apiKey="<Your_API_Key>")
```

You can then run your app with 
```bash
streamlit run streamlit_app.py
```
The app should pop up in your web browser.

