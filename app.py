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
import altair as alt

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

#correct = is_this_correct(key = 1)
#if correct:
desc_folder_path = transcription_folder + "/" + descriptive_transcript_folder + "/"
presc_folder_path = transcription_folder + "/" + prescriptive_transcript_folder + "/"

#else:
    #st.write("Please alter your information.")

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

survey_dicts = survey_data.to_dict('record') # turn each row into a respective dictionary entry
for dct_index,dct in enumerate(desc_dictionaries):
    partic = dct['file_name']

    for new_dct_index,new_dct in enumerate(survey_dicts): # the double loop allows this to
        # funciton even though the range does not match between the results and the survey
        # dictionaries (some participants never finished their participation)
        if new_dct['partic_number'] == partic:
            desc_dictionaries[dct_index] = {**desc_dictionaries[dct_index], **survey_dicts[new_dct_index]}
partic_names = []
study_data = []
years_instruct = []
order = []
word_data = pd.read_csv("dictionary.csv")

for index, dictionary in enumerate(desc_dictionaries):
    df = dictionary['DF']

    partic_name = dictionary['partic_number']
    years = dictionary['years_formal_instruct']
    order.append(index)
    partic_names.append(partic_name)
    study_data.append(df)
    years_instruct.append(years)


st.write("### Prescriptive Transcript:")
st.markdown("> " + presc_dictionary[0]['raw_transcript'])

data_explore_keys = ["Nothing", "View participant data", "View descriptive statistics"]

data_explore = st.selectbox("What information would you like to look at?", data_explore_keys)

if data_explore == data_explore_keys[0]:
    st.write("Please select an option to view data!")

elif data_explore == data_explore_keys[1]: # view particpant data
    partic_keys = []
    for i, dictionary in enumerate(desc_dictionaries):
        temp_key = dictionary['partic_number']
        partic_keys.append(temp_key)

    show_dictionary = st.selectbox("Select a participant's dictionary:", partic_keys)
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
            # questions in the survey (change method of import)
            questions=["What is your name?",
               "What is your age?",
               "How would you self-identify in terms of your Spanish language ability?",
               "Have you ever traveled to a Spanish-speaking country, and, if so, did you communicate in Spanish while in that Spanish-speaking country?",
               "Have you ever traveled to a Spanish-speaking country on an education-focused travel-abroad program?",
               "Did you have any significant exposure to Spanish before the age of 10? (significant could mean: a family member spoke to you; you lived in a Spanish-speaking country; you took a Spanish class; etc.)",
               "Have you ever received formal Spanish language instruction?",
               "If you have you received formal Spanish language instruction, approximately how many years? (Assume each college semester = 1 year; each High School course = 1 year) If not, please enter '0'.",
               "If you have you ever received formal Spanish language instruction, have you every been explicitly taught Spanish pronunciation?",
               "How often do you have exposure to Spanish (outside of a classroom setting)?",
               "How often do you speak in Spanish (outside of a classroom setting)?",
               "When was the last time you spoke Spanish (outside of a classroom setting)?",
               "Are you currently trying to learn Spanish?"]

            question_keys = []
            question_answers = []
            for i, key in enumerate(list(survey_data.keys())):
                question_keys.append(key)
                question_answers.append(dictionary[key])


            # st.selectbox("Please select the question: ", questions)
            partic_survey_results = pd.DataFrame(zip(question_keys, questions, question_answers), columns = ['question_key', 'questions', 'answer'])
            st.table(partic_survey_results)

elif data_explore == data_explore_keys[2]:


    descriptive_stats_options = ["Nothing","The wordlist", "Survey results", "Pronunciation outcomes"]

    descriptive_stats_choice = st.selectbox("Chose what stats you would like to explore", descriptive_stats_options)

    if descriptive_stats_choice == descriptive_stats_options[1]:
        st.write(word_data.keys())

        words = word_data['word']
        word_size = len(words)

        def filter_dict(dictionary_df, column_criteria, equivelancy_criteria):
            row_selects = dictionary_df[dictionary_df[column_criteria] == equivelancy_criteria]
            words = row_selects['word']
            return(words)

        terminal_vowels = filter_dict(word_data, 'term_vowel', 1)
        terminal_vowel_prop = len(terminal_vowels) / word_size

        init_vowels = filter_dict(word_data, 'init_vowel', 1)
        init_vowels_prop = len(init_vowels) / word_size
        cognates = filter_dict(word_data, 'cognate', 1)

        ls_types = ['initial letter', 'terminal letter', 'cognate status', 'initial letter', 'terminal letter', 'cognate status']


        alt.Chart(word_data).mark_text(filled=True).encode(
            alt.X('term_vowel:O', axis=None),
            alt.Y('animal:O', axis=None),
            alt.Row('country:N', header=alt.Header(title='')),
            alt.SizeValue(60),
            text='emoji'
        ).properties(width=800, height=200)

        # https://vega.github.io/vega-lite/examples/isotype_bar_chart_emoji.html


    elif descriptive_stats_choice == descriptive_stats_options[3]:
        # write information on total dataset
        total_accuracy = ipa.get_proportions(study_data)
        total_accuracy_mean = np.mean(total_accuracy)
        total_accuracy_std = np.std(total_accuracy)
        st.write("### All participants")
        st.write("Across all of the sample, the particpants scored an average of " + str(round((total_accuracy_mean * 100), 2)) + "% vowel pronunciation accuracy with a standard deviation of: " + str(round((total_accuracy_std * 100), 2)) + "%")
        # time.sleep()

        # write information on cognates
        non_cognate_dfs = ipa.filter_by_dictionary(word_data, "cognate", 0, study_data)
        non_cognate_accuracy = ipa.get_proportions(non_cognate_dfs)
        non_cognate_accuracy_mean = np.mean(non_cognate_accuracy)
        non_cognate_accuracy_std = np.std(non_cognate_accuracy)
        st.write("For non-cognates words, the particpants scored an average of " + str(round((non_cognate_accuracy_mean * 100), 2)) + "% vowel pronunciation accuracy with a standard deviation of: " + str(round((non_cognate_accuracy_std * 100), 2)) + "%")

    # calculate mean and std for cognate pronunciation accuracy across the *entrie* sample
        cognate_dfs = ipa.filter_by_dictionary(word_data, "cognate", 1, study_data) # create a list of dfs that only accounts for the cognates in the study
        cognate_accuracy = ipa.get_proportions(cognate_dfs)
        cognate_accuracy_mean = np.mean(cognate_accuracy)
        cognate_accuracy_std = np.std(cognate_accuracy)
        st.write("For cognates, the particpants scored an average of " + str(round((cognate_accuracy_mean * 100), 2)) + "% vowel pronunciation accuracy with a standard deviation of: " + str(round((cognate_accuracy_std * 100), 2)) + "%")


        stat = stat.ttest_ind(cognate_accuracy, non_cognate_accuracy, equal_var=False)
        pvalue = stat[1]

        st.write("According to a two sample t-test (p < 0.05, equal varience = False):")

        if pvalue >= 0.05:
            st.markdown("> We fail to reject the null hypothesis. There is not enough evidence (p = " + str(pvalue) + ") to support a statistically significant difference of the average pronunciation accuarcy between cognates and non-cognaates in the sample.")
        else:
            st.markdown("> We choose to reject the null hypothesis. There is enough evidence (p = " + str(pvalue) + ") to support a statistically significant difference of the average pronunciation accuarcy between cognates and non-cognaates in the sample.")



        newito = ipa.filter_by_allophone(study_data, allophone0 = 'a', allophone1 = 'e')
        st.write(newito[1])

#st.write("Files in " + desc_folder_path + ": ")
#for i,e in enumerate(desc_transcript_files):
 #   st.write(e)

#st.write("Files in " + presc_folder_path + ": ")
#st.write(presc_transcript_file)
