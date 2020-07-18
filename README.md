# IPA_vowel_compare
> Jupyter notebook & streamlit app running Python code for comparative analysis of International Phonetic Alphabet (IPA) strings. Repository also includes data and research from a Spanish phonetic acquisition project currently underway.

## Repository

The intention of this repo is to perform contrastive data analysis between prescriptive and descriptive IPA strings. (Don't know anything about IPA? Learn more [here](README_ext/IPA.md).) 

### Data

I have made all of the data I collected for this study open-source. 

The bulk of the data collected is in the [transcriptions/descriptive/](/transcriptions/descriptive/) folder. Here there are a number of files named particX.txt; each doc contains a long string of the participant's recording (their pronunciation of the [wordlist](wordlist.txt)) transcribed into IPA. I did all of the transcriptions using the [fantastic open-source 'keyboard' that my research group and I use](https://ipa.typeit.org/full/)

There are also two .csv files in the root directory: [dictionary.csv](dictionary.csv), and [survey_data.csv](survey_data.csv). The former contains meta-information about the word-list sample and its linguistic properties, while the latter has responses to the survey that participants took before recording their pronunciation. Note that many the functions are designed specifically for these datasets.

### Notebook

Currently the notebook has been put by-the-wayside to emphasize the Streamlit app. Both the notebook and the app share many similar features, but in the notebook you see the code as you go, whereas in the app you have more opportunity for data exploration.

### Module & functions

As of right now, all of the functions have been thrown into [Compare_IPA.py](Compare_IPA.py); there are also no class divisions ATM.

### Streamlit web App

The streamlit app was designed for users to explore data (and the relationships between datasets) before jumping into in-depth analysis. The app is still in daily development, however it is in working order.

## Study

The study that accompanies the code in this repo was conducted as a final project for Spanish Applied Linguistics: Second Language Acquisition, a course @ The University of Colorado, Denver, taught by my professor & research advisor, Dr. Alyssa Martoccio. Read more about the study [here](README_ext/study.md).



