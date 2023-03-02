# import necessary modules
import glob
import importlib
import os
import re
import sys
import time

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stat
import streamlit as st

import compare_IPA as ipa

def grab_number(string) -> int:
    """
    """
    num_string = string[-2:]
    num = int(num_string)
    
    return(num)

def participant_number(survey_data):
    """
    """
    
    new_index = []
    
    for i,row in survey_data.iterrows():
        partic_string = row["partic_number"]
        partic_number = grab_number(partic_string)
        new_index.append(partic_number)
        
    survey_data["partic_index"] = new_index
        
    return(survey_data)


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


#st.write("Please select the folder with your transcriptions:")
#transcription_folder = folder_selector(key = 1)
#st.write('Your transcriptions are in /`%s`' % transcription_folder)

#st.write("Please select the folder with your descriptive transcriptions:")
#descriptive_transcript_folder = folder_selector(transcription_folder, key =2)
#st.write('Your descriptive transcriptions are in /`%s`' % transcription_folder, '/`%s`' % descriptive_transcript_folder)

#st.write("Please select the folder with your prescriptive transcription:")
#prescriptive_transcript_folder = folder_selector(transcription_folder, key =3)
#st.write('Your descriptive transcriptions are in /`%s`' % transcription_folder, '/`%s`' % prescriptive_transcript_folder)

transcription_folder = 'transcriptions'
descriptive_transcript_folder = 'descriptive'
prescriptive_transcript_folder = 'prescriptive'

st.write('By default your prescriptive transcription is in `%s`' % transcription_folder, '/`%s`' % prescriptive_transcript_folder, '/')
st.write('By default your descriptive transcriptions are in `%s`' % transcription_folder, '/`%s`' % descriptive_transcript_folder, '/')

correct = is_this_correct(key = 1)
if correct:
    desc_folder_path = transcription_folder + "/" + descriptive_transcript_folder + "/"
    presc_folder_path = transcription_folder + "/" + prescriptive_transcript_folder + "/"

#else:
    #st.write("Please alter your information.")

# st.write()

survey_data_raw = pd.read_csv("survey_data/survey_data.csv") # import the data from the survey
survey_data = participant_number(survey_data_raw)
# remove
# survey_data = 

desc_transcript_files = glob.glob(desc_folder_path + '*.txt') # take in all desc filepaths
presc_transcript_file = glob.glob(presc_folder_path + '*.txt') # take in presc transcription file

presc_dictionary_ls = ipa.bring_in_data(presc_transcript_file)
presc_dictionary = presc_dictionary_ls[0]
prescriptive_transcription = presc_dictionary["clean_transcript"]

# create a list of type Participant to store all of the data
participant_classes = [ipa.Participant(file, survey_data, prescriptive_transcription) for file in desc_transcript_files]


# create an ids list to make it easier to access participants by their id number
participant_ids = [partic.id_number for partic in participant_classes]

# create dict for ease of access
participant_data = dict(zip(participant_ids, participant_classes))

# give user options of what they can do
data_explore_keys = ["View participant data", "View descriptive statistics"]
data_explore = st.selectbox("What information would you like to look at?", data_explore_keys)

# if the user wants to explore participant data
if data_explore == data_explore_keys[0]:
    partic_explore = st.selectbox("Select a participant:", participant_data)
    _participant = participant_data[partic_explore]
    # show pronuncaiton
    st.write("Participant ID Number:")
    st.write(_participant.id_number)
    st.write("Participant IPA Transcript")
    st.write(_participant.raw_transcript)
    st.write("Participant Pronunciation Results (compared to prescriptive)")
    st.write(_participant.pronunciation_df)
    st.write("Participant Survey Results")
    st.write(_participant.survey_dict)

# if the user wants to view descriptive statistics
if data_explore == data_explore_keys[1]:
    by_participant_study = ["By participant", "Entire Study"]
    select = st.selectbox("""Would you like to see data by individual participant, or by the entire study?""", by_participant_study)

    # if they want to see individual participants
    if select == by_participant_study[0]:
        partic_explore = st.selectbox("Select a participant to see stats:", participant_data)
        _participant = participant_data[partic_explore]
        
        stat_types = ["Pronunciation Proportions"]
        stat_select = st.selectbox("Select type of statistic:", stat_types)
        
        if stat_select == stat_types[0]:
            by_vowel = ['all','a', 'e', 'i', 'o', 'u']
            vowel_select = st.selectbox("Select a vowel:", by_vowel)
            pronunciation_df = _participant.pronunciation_df
            
            if vowel_select != 'all':
                filtered = pronunciation_df[pronunciation_df["correct_allophone"] == vowel_select]
            else:
                filtered = pronunciation_df
                
            total_vowels = len(filtered)
            correct_vowels = len(filtered[filtered["correct_allophone"] == filtered["student_allophone"]])
            proportion_correct = correct_vowels/total_vowels
            st.write("Proportion of correct vowels: {}%".format(round(proportion_correct * 100, 2)))

          
                
        
        

    # if they want to see the whole study
    if select == by_participant_study[1]:
        stat_types = ["Pronunciation Proportions"]
        stat_select = st.selectbox("Select type of statistic:", stat_types)
        
        
            
        
        
            
        


   
    




# # for index,dictionary in enumerate(participant_classes):
# #     temp_desc_transcript = desc_dictionaries[index].pronunciation_dictionary["clean_transcript"]
# #     presc_transcript = presc_dictionary[0]["clean_transcript"]
    

# survey_dicts = survey_data.to_dict('record') # turn each row into a respective dictionary entry
# for dct_index,dct in enumerate(desc_dictionaries):
#     partic = dct['file_name']

#     for new_dct_index,new_dct in enumerate(survey_dicts): # the double loop allows this to
#         # funciton even though the range does not match between the results and the survey
#         # dictionaries (some participants never finished their participation)
#         if new_dct['partic_number'] == partic:
#             desc_dictionaries[dct_index] = {**desc_dictionaries[dct_index], **survey_dicts[new_dct_index]}
# partic_names = []
# study_data = []
# years_instruct = []
# order = []
# word_data = pd.read_csv("dictionary.csv")

# for index, dictionary in enumerate(desc_dictionaries):
#     df = dictionary['DF']

#     partic_name = dictionary['partic_number']
#     years = dictionary['years_formal_instruct']
#     order.append(index)
#     partic_names.append(partic_name)
#     study_data.append(df)
#     years_instruct.append(years)


# st.write("### Prescriptive Transcript:")
# st.markdown("> " + presc_dictionary[0]['raw_transcript'])

# data_explore_keys = ["Nothing", "View participant data", "View descriptive statistics"]

# data_explore = st.selectbox("What information would you like to look at?", data_explore_keys)

# if data_explore == data_explore_keys[0]:
#     st.write("Please select an option to view data!")

# elif data_explore == data_explore_keys[1]: # view particpant data
#     partic_keys = []
#     for i, dictionary in enumerate(desc_dictionaries):
#         temp_key = dictionary['partic_number']
#         partic_keys.append(temp_key)

#     show_dictionary = st.selectbox("Select a participant's dictionary:", partic_keys)
#     for i, dictionary in enumerate(desc_dictionaries):
#         if dictionary['partic_number'] == show_dictionary:
#             st.write("## Participant MetaData: ")
#             st.write("### Participant Name: ")
#             st.write(dictionary['partic_number'])
#             st.write("### File Name & Path: ")
#             st.write(dictionary['full_path'])

#             st.write("## Summary of Pronunciation")
#             st.write("### Raw Transcript: ")
#             st.markdown("> " + dictionary['raw_transcript'])
#             st.write("### Participants Summary: ")
#             st.write("#### (How this participant matched up against the prescriptive IPA transcript)")
#             st.write("")
#             st.write(dictionary['DF'])

#             st.write("## Survey Results")
#             # questions in the survey (change method of import)
#             questions=["What is your name?",
#                "What is your age?",
#                "How would you self-identify in terms of your Spanish language ability?",
#                "Have you ever traveled to a Spanish-speaking country, and, if so, did you communicate in Spanish while in that Spanish-speaking country?",
#                "Have you ever traveled to a Spanish-speaking country on an education-focused travel-abroad program?",
#                "Did you have any significant exposure to Spanish before the age of 10? (significant could mean: a family member spoke to you; you lived in a Spanish-speaking country; you took a Spanish class; etc.)",
#                "Have you ever received formal Spanish language instruction?",
#                "If you have you received formal Spanish language instruction, approximately how many years? (Assume each college semester = 1 year; each High School course = 1 year) If not, please enter '0'.",
#                "If you have you ever received formal Spanish language instruction, have you every been explicitly taught Spanish pronunciation?",
#                "How often do you have exposure to Spanish (outside of a classroom setting)?",
#                "How often do you speak in Spanish (outside of a classroom setting)?",
#                "When was the last time you spoke Spanish (outside of a classroom setting)?",
#                "Are you currently trying to learn Spanish?"]

#             question_keys = []
#             question_answers = []
#             for i, key in enumerate(list(survey_data.keys())):
#                 question_keys.append(key)
#                 question_answers.append(dictionary[key])
