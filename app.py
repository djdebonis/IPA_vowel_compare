# import necessary modules
import streamlit as st
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import glob as glob
import os

# import local .py scripts with function definitions/declarations
import Compare_IPA


def folder_selector(folder_path='./', key=0):
    folder_names = os.listdir(folder_path)
    selected_filename = st.selectbox('Select folder:', folder_names, key = key)
    return selected_filename

def is_this_correct(key=0):
    yes_or_no = ['Yes', 'No']
    correct = st.selectbox('Is this correct?', yes_or_no, key = key)
    if correct == 'Yes':
        boolean = True
    else:
        boolean = False
        
    return(boolean)


st.write("Please select the folder with your transcriptions:")
transcription_folder = folder_selector(key = 1)
st.write('Your transcriptions are in /`%s`' % transcription_folder)

st.write("Please select the folder with your descriptive transcriptions:")
descriptive_transcript_folder = folder_selector(transcription_folder, key =2)
st.write('Your descriptive transcriptions are in /`%s`' % transcription_folder, '/`%s`' % descriptive_transcript_folder)

st.write("Please select the folder with your prescriptive transcription:")
prescriptive_transcript_folder = folder_selector(transcription_folder, key =3)
st.write('Your descriptive transcriptions are in /`%s`' % transcription_folder, '/`%s`' % prescriptive_transcript_folder)

correct = is_this_correct(key = 1)
if correct:
    desc_folder_path = transcription_folder + "/" + descriptive_transcript_folder + "/"
    presc_folder_path = transcription_folder + "/" + prescriptive_transcript_folder + "/"
        
else:
    st.write("Please alter your information.")
    
# st.write()
    

desc_transcript_files = glob.glob(desc_folder_path + '*.txt') # take in all desc filepaths
presc_transcript_file = glob.glob(presc_folder_path + '*.txt') # take in presc transc file


st.write("Files in " + desc_folder_path + ": ")
for i,e in enumerate(desc_transcript_files):
    st.write(e)

st.write("Files in " + presc_folder_path + ": ")
st.write(presc_transcript_file)