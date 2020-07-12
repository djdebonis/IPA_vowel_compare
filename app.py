# import necessary modules
import streamlit as st
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import glob as glob
import os
import time

# import local .py scripts with function definitions/declarations
import Compare_IPA as ipa


def folder_selector(folder_path='./', key=0):
    folder_names = os.listdir(folder_path)
    #x = 5
    #for index, folder in enumerate(folder_names):
        #if folder == "transcriptions":
            #x = index
        
    selected_filename = st.selectbox('Select folder:', folder_names, key = key)#, format_func=lambda x: folder_names[x])
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

desc_dictionaries = ipa.bring_in_data(desc_transcript_files)
presc_dictionary = ipa.bring_in_data(presc_transcript_file)



for index,dictionary in enumerate(desc_dictionaries):
    temp_desc_transcript = desc_dictionaries[index]["clean_transcript"]
    presc_transcript = presc_dictionary[0]["clean_transcript"]
    temp_df = ipa.string_list_phoneme_compare(temp_desc_transcript, 
presc_transcript)
    desc_dictionaries[index]['DF'] = temp_df
    
survey_data = pd.read_csv("survey_data.csv") # import the data from the survey 

survey_dicts = survey_data.to_dict('record') # turn each row into a respective dictionary
for dct_index,dct in enumerate(desc_dictionaries): 
    partic = dct['file_name']
    
    for new_dct_index,new_dct in enumerate(survey_dicts): # the double loop allows this to 
        # funciton even though the range does not match between the results and the survey
        # dictionaries (some participants never finished their participation)
        if new_dct['partic_number'] == partic:
            desc_dictionaries[dct_index] = {**desc_dictionaries[dct_index], **survey_dicts[new_dct_index]}
    
    
partic_keys = []
for i, dictionary in enumerate(desc_dictionaries):
    temp_key = dictionary['partic_number']
    partic_keys.append(temp_key)

st.write("### Prescriptive Transcript:")
st.markdown("> " + presc_dictionary[0]['raw_transcript'])

show_dictionary = st.selectbox("Select a dictionary:", partic_keys)
for i, dictionary in enumerate(desc_dictionaries):
    if dictionary['partic_number'] == show_dictionary:
        st.write("## Participant MetaData: ")
        st.write("### Participant Name: ")
        st.write(dictionary['partic_number'])
        st.write("### File Name & Path: ")
        st.write(dictionary['full_path'])
        
        st.write("## Summary of Pronunciation")
        st.write("### Raw Transcript: ")
        st.markdown("> " + dictionary['raw_transcript'])
        st.write("### Participants Summary: ")
        st.write("#### (How this participant matched up against the prescriptive IPA transcript)")
        st.write("")
        st.write(dictionary['DF'])

        st.write("## Survey Results")
        st.write("### Questions: ")
        st.markdown("""
        | Question                                                               	| Response                       	|
|------------------------------------------------------------------------	|--------------------------------	|
| What is your age?                                                      	| {{(dictionary['age'])}}          	|
| How would you self-identify in terms of your Spanish language ability? 	| {{dictionary['self_identify'}} 	|
        """)


#st.write("Files in " + desc_folder_path + ": ")
#for i,e in enumerate(desc_transcript_files):
 #   st.write(e)

#st.write("Files in " + presc_folder_path + ": ")
#st.write(presc_transcript_file)

