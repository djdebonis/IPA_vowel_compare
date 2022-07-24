# import necessary modules
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import os
import streamlit as st

class Partic:
    """
    A class to represent a participant of the study (hence `Partic`)

    ...

    Attributes
    ----------
    id : int
        unique identifier for participant
    dictionary : dict
        stores data of the participant's pronunciation transcription
    

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, _partic_ID, _filename):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            _partic_ID : int
                a unique identifier of the participant (compare with
                another data set to identify)
            _filename : str
                name of path and file where document is stored
            
        """

        self.id = _partic_ID
        self.dictionary = bring_in_data(_filename)

    def open_and_read(infile_path_and_name):
        """
        opens a file and returns a long long long string

        Parameters
        ----------
        infile_path_and_name : str
            string of the path/path/txtFileName.txt from the current directory

        Returns
        -------
        string : str
            string of the data within the designated file

        """
        path = infile_path_and_name

        with open(path, 'r') as file:
            string = file.read().replace('\n', '')

        return string

    def split_sentence(sentence: str) -> list:
        """
        Takes a sentence in IPA and parses it to individual words by breaking according to
        the " # " IPA string pattern, meaning in the import file each word should be
        seperated by " # ".

        Parameters
        ----------
        sentence : str
            a sentence or list of words to parse

        Returns
        -------
        words : list of str
            a list of individual words/transcriptions


        """
        
        # split by traditional IPA word seperator (in IPA, ## traditionally marks the
        # end of a sentence
        words = sentence.split(" # ")
        return words

    def rm_stress(word_list):
        """
        Takes a list of strings in IPA that contain prosodic accent marks and removes
        the dashes to clean the data.

        :word_list: list of strings

        :returns: list of strings without prosodic accent marks
        :rtype: list of strings

        """
        new_list = []
        # for each word in the word list, search for IPA stress marks ("'")
        # and remove
        for s in range(len(word_list)):
            word = word_list[s]
            new_word = re.compile(r"'").sub("",word)
            new_list.append(new_word)
        return(new_list)

    def syllabize_further(word: str) -> list:
        """
        Takes a string with syllable hyphens and breaks it apart into a list of syllables

        :word: str: word form with hyphens marking syllable

        :returns: list of individual syllables
        :rtype: list

        """
        # split
        syllables = word.split("-")
        return syllables

    def file_finder(filepath):
        """
        Takes a filepath (str) and exracts: (1) its path, (2) its name, and (3) its extension.
        This metadata is filtered into a dictionary.

        For example, the filepath 'folder/directory/repository/file_name.txt' would return:

            File path: 'folder/directory/repository/'
            File name: 'file_name'
            File extention: '.txt'

        :param: filepath: string of a filepath (from current working directory)

        :returns: dictionary with orginal filepath as well as sorted metadata

        """
        prefix = ""
        file_name = ""
        file_ext = ""

        furthest_dir_index = 0
        extention_index = 0

        # if there are subdirectories
        if "/" in filepath:
            index_ls = []
            for index,char in enumerate(filepath):
                if char == "/":
                    index_ls.append(index)

            furthest_dir_index = max(index_ls)

            path = filepath[:(furthest_dir_index + 1)]



        if "." in filepath:
            for i,c in enumerate(filepath):
                if c == ".":
                    extention_index = i
                    file_ext = filepath[extention_index:]

            file_name = filepath[(furthest_dir_index + 1):(extention_index)]

        else:
            file_name = filepath[furthest_dir_index:]


        dictionary = {"full_path": filepath, "file_name": file_name,
                      "prefix": prefix, "extention" : file_ext}

        return(dictionary)


    
    def bring_in_data(file_path):
        """
        Takes in data from the file_paths and sorts its respective information to dictionaries.
        """
        
        dictionary = file_finder(file_path)

        temp_string = open_and_read(file_path)

        temp_raw = split_sentence(temp_string)

        temp_partic = rm_stress(temp_raw)

        dictionary['import_index'] = index

        dictionary['raw_transcript'] = temp_string

        dictionary['clean_transcript'] = temp_partic

        return(dictionary)


    def vowel_lists_append(prescrip_string, descrip_string, prescrip_vowel_ls, descrip_vowel_ls):
        """
        Takes two lists of strings and two strings and appends the vowels of the new strings on to the list of vowels
        
        
        *It's important to note that prescriptive Spanish only contains some diphthongs and some vowels from the below
        lists. However, Native English Speakers (NES) tend to pronounce Spanish with all sorts of long vowels (ones
        ending with ':', pure vowels that are not in Spanish (e.g. the schwa, 'ə'), or other diphthongs not seen in 
        most Native Spanish Speakers (NSS). Thus, although the function below seems to be haphazardly constructed,
        it is actually set up for the sake of following Spanish Language Acquisition by NES students.*

        :prescrip_string: the syllable with the 'correct' vowell
        :descrip_string: the syllable with the student's pronunciation of the vowel
        :prescrip_vowel_ls: the list of all of the 'correct' vowel pronunciations
        :descrip_vowel_ls: the list with all of the student's pronunciations of the vowels


        :returns: dataframe with lots of good data
        :rtype: pandas DataFrame

        """

        long_vowel_list = ['a:','e:','i:','o:','u:','ɛ:','æ:','ə:','ʌ:','ɪ:','ɔ:','ɑ:','ʊ:']
        diphthong_list =['au̯','eu̯','iu̯','ou̯','uu̯','ɛu̯','æu̯','əu̯','ʌu̯','ɪu̯','ɔu̯','ɑu̯','ʊu̯',
                         'ai̯','ei̯','ii̯','oi̯','ui̯','ɛi̯','æi̯','əi̯','ʌi̯','ɪi̯','ɔi̯','ɑi̯','ʊi̯',
                         'i̯a','i̯e','i̯i','i̯o','i̯u','i̯ɛ','i̯æ','i̯ə','i̯ʌ','i̯ɪ','i̯ɔ','i̯ɑ','i̯ʊ',
                         'u̯a','u̯e','u̯i','u̯o','u̯u','u̯ɛ','u̯æ','u̯ə','u̯ʌ','u̯ɪ','u̯ɔ','u̯ɑ','u̯ʊ']

        vowel_list = ['a', 'e', 'i', 'o', 'u']
        semivowwel_list =['i̯','u̯',]
        pure_vowel_list = ['a','e','i','o','u','ɛ','æ','ə','ʌ','ɪ','ɔ','ɑ','ʊ','ɚ']

        boolean = True

        while boolean == True:
            if boolean == True:
                for s in range(len(diphthong_list)):
                    if diphthong_list[s] in prescrip_string:
                        prescrip_vowel_ls.append(diphthong_list[s])
                        boolean = False
                        break
                    else:
                        boolean = True


                if boolean == True:
                    for i in range(len(vowel_list)):
                        if vowel_list[i] in prescrip_string:
                            prescrip_vowel_ls.append(vowel_list[i])
                            boolean = False
                            break
                        else:
                            boolean = True


        boolean1 = True

        while boolean1 == True:

            if boolean1 == True:
                for j in range(len(long_vowel_list)):
                    if long_vowel_list[j] in descrip_string:
                        descrip_vowel_ls.append(long_vowel_list[j])
                        boolean1 = False
                        break

                if boolean1 == True:
                    for q in range(len(diphthong_list)):
                        if diphthong_list[q] in descrip_string:
                            descrip_vowel_ls.append(diphthong_list[q])
                            boolean1 = False
                            break

                if boolean1 == True:
                    for z in range(len(pure_vowel_list)):
                        if pure_vowel_list[z] in descrip_string:
                            descrip_vowel_ls.append(pure_vowel_list[z])
                            boolean1 = False
                            break



        #print("Prescriptive vowel list:")
        #print(prescrip_vowel_ls)
        #print("Descriptive vowel list:")
        #print(descrip_vowel_ls)

    def string_list_phoneme_compare(response,answer):
        """
        Takes two lists of (IPA) strings--the student response (response) and the correct answer (answer)--
        and compares them against eachother. Then, the function will (1) find mismatches, and
        (2) return the word, the string index, the correct allophone, and the discrepancy (i.e. the incorrect
        allophone[s].)

        Parameters
        ----------
        response : list of strings
        answer : list of strings

        AS OF RIGHT NOW:
            (1) lists of strings must be of equal length
            (2) the number of syllables per string must be of equal length
            (3) for now it's **absoultuely necessary** that each and every syllable has a vowel


        :returns: a table with the aforementioned data
        :rtype: dataframe

        """
        word_index = []
        word = []
        student_pronunciation = []
        indexes = []
        student_allophones = []
        prescriptive_allophones = []
        binary = []

        p_syllable_lengths = []
        d_syllable_lengths = []

        syllable_header =[]
        p_syllables = []
        d_syllables = []
        syllable_number =[]

        if len(response) == len(answer):

            for s in range(len(response)): # first nested loop iterates through the strings in the list

                # assign variables to both of the strings because you will be appending them multiple times later on
                answer_word = answer[s]
                response_word = response[s]

                # break each string into a smaller list of individual syllables
                d_list_of_syllables = syllabize_further(response[s])
                p_list_of_syllables = syllabize_further(answer[s])

                #p_syllables[s] = p_list_of_syllables
                #d_syllables[s] = d_list_of_syllables

                if len(d_list_of_syllables) == len(p_list_of_syllables): # check to see if there are the same amount of syllables inside each word

                    for j in range(len(p_list_of_syllables)): # now iterating through each syllable in the word list (j = syllable number)

                        # assign each syllable to a unique string variable for further iteration
                        descriptive_syllable = d_list_of_syllables[j]
                        prescriptive_syllable = p_list_of_syllables[j]

                        vowel_lists_append(prescriptive_syllable, descriptive_syllable, prescriptive_allophones, student_allophones)

                        word_index.append(s)
                        word.append(answer_word)
                        student_pronunciation.append(response_word)
                        syllable_number.append(j)
                        d_syllables.append(descriptive_syllable)
                        p_syllables.append(prescriptive_syllable)


                else:
                    print("Word " + (str(s)) + " in the student response has the wrong number of syllables." )


        #else:
            #print("The two lists do not contain the same amount of strings.")

        data = pd.DataFrame(list(zip(word_index, word, student_pronunciation, syllable_number, p_syllables, d_syllables, prescriptive_allophones,
                                     student_allophones)), columns =['word_number','prescriptive_pronunciation','student_pronunciation','syllable_number','prescriptive_syllable','student_syllable','correct_allophone','student_allophone'])




        return(data)


    def datasheet_compile(list_of_lists, prescriptive_list):
        """
        Takes a list of lists of strings and turns them into a list of dataframes that contain all of the information we are looking for
        (see string_list_phoneme_compare function for more information)

        Parameters
        ----------
        :list_of_lists: a list of lists of strings; all lists must be the same length
        :prescriptive_list: a list of strings; prescriptive list must be same len as all lists in list_of_lists

        Returns
        --------
        :returns: list of dataframes with all of the good data we want
        :rtype: list of pandas DataFrames

        """
        ls_of_dfs = []
        for i in range(len(list_of_lists)):
            current_list = list_of_lists[i]
            current_df = string_list_phoneme_compare(current_list, prescriptive_list)
            ls_of_dfs.append(current_df)

        return(ls_of_dfs)



    def filter_by_dictionary(dictionary_df, column_criteria, equivelancy_criteria, ls_of_dfs):
        """
        Uses the categorical/meta information from one dataframe (in this case, the dictionary dataframe), and uses some criteria
        within it to filter another dataframe.

        Parameters
        ----------
            dictionary_df : a pandas DataFrame with information relating to how you might want to filter the df

            column_criteria : a string that is the column name of what you want to filter by in in dictionary_df

            equivelancy_criteria : what the cells in dictionary_df[column_criteria] are equal to (e.g. 1, False, "<a>", etc.)

            ls_of_dfs : a list of pandas DataFrames that you want to filter by some criteria

        Returns
        --------
            returns : a list of filtered dataframes

            rtype : list of pd DataFrames

        """

        word_selects = dictionary_df[dictionary_df[column_criteria] == equivelancy_criteria]

        new_ls_of_dfs = []

        for i in range(len(ls_of_dfs)):
            temp_df = ls_of_dfs[i]
            temp_df = temp_df[temp_df['word_number'].isin(word_selects['list_number'])]
            new_ls_of_dfs.append(temp_df)

        return(new_ls_of_dfs)

    def filter_by_dictionary_mult_criteria(dictionary_df, ls_of_dfs, column_criteria0 = '', equivelancy_criteria0 = '', column_criteria1 = '', equivelancy_criteria1 = '', column_criteria2 = '', equivelancy_criteria2 = '', column_criteria3 = '', equivelancy_criteria3 = '', column_criteria4 = '', equivelancy_criteria4 = '', column_criteria5 = '', equivelancy_criteria5 = ''):
        """
        Uses the categorical/meta information from one dataframe (in this case, the dictionary dataframe), and uses some criteria
        within it to filter another dataframe.

        Parameters
        ----------
            dictionary_df : a pandas DataFrame with information relating to how you might want to filter the df

            column_criteria : a string that is the column name of what you want to filter by in in dictionary_df

            equivelancy_criteria : what the cells in dictionary_df[column_criteria] are equal to (e.g. 1, False, "<a>", etc.)

            ls_of_dfs : a list of pandas DataFrames that you want to filter by some criteria

        Returns
        --------
            returns : a list of filtered dataframes

            rtype : list of pd DataFrames

        """

       # Filter the dictionary by the criteria passed as arguments

        dictionary_ls_dfs = []
        if len(column_criteria0) > 0:
            dictionary_df0 = dictionary_df[dictionary_df[column_criteria0] == int(equivelancy_criteria0)]
            dictionary_ls_dfs.append(dictionary_df0)

        if len(column_criteria1) > 0:
            dictionary_df1 = dictionary_df[dictionary_df[column_criteria1] == int(equivelancy_criteria1)]
            dictionary_ls_dfs.append(dictionary_df1)

        if len(column_criteria2) > 0:
            dictionary_df2 = dictionary_df[dictionary_df[column_criteria2] == int(equivelancy_criteria2)]
            dictionary_ls_dfs.append(dictionary_df2)

        if len(column_criteria3) > 0:
            dictionary_df3 = dictionary_df[dictionary_df[column_criteria3] == int(equivelancy_criteria3)]
            dictionary_ls_dfs.append(dictionary_df3)

        if len(column_criteria4) > 0:
            dictionary_df4 = dictionary_df[dictionary_df[column_criteria4] == int(equivelancy_criteria4)]
            dictionary_ls_dfs.append(dictionary_df4)

        if len(column_criteria5) > 0:
            dictionary_df5 = dictionary_df[dictionary_df[column_criteria5] == int(equivelancy_criteria5)]
            dictionary_ls_dfs.append(dictionary_df5)


        new_dictionary_df = pd.concat(dictionary_ls_dfs)


        new_ls_of_dfs =[]
        for i in range(len(ls_of_dfs)):
            temp_df = ls_of_dfs[i]
            temp_df = temp_df[temp_df['prescriptive_pronunciation'].isin(new_dictionary_df['transcription'])]
            new_ls_of_dfs.append(temp_df)

        return(new_ls_of_dfs)

    def filter_by_allophone(ls_of_dfs, allophone0  = '', allophone1 = '', allophone2 = '', allophone3 = '', allophone4 = '', allophone5 = ''):
        """
        Filter the entire list of dataframes by a specific allophone.

        Parameters
        ----------
        :allophone[x]: the allophone that you want to focus on, e.g. 'a', 'e', etc.
        :ls_of_dfs: a list of pandas DataFrames that you want to filter by some criteria

        Returns
        --------
        :returns: a list of filtered dataframes
        :rtype: list of pd DataFrames

        """

        new_ls_of_dfs = []

        for i in range(len(ls_of_dfs)):
            temp_df = ls_of_dfs[i]
            temp_df0 = temp_df[temp_df['correct_allophone'] == allophone0]
            temp_df1 = temp_df[temp_df['correct_allophone'] == allophone1]
            temp_df2 = temp_df[temp_df['correct_allophone'] == allophone2]
            temp_df3 = temp_df[temp_df['correct_allophone'] == allophone3]
            temp_df4 = temp_df[temp_df['correct_allophone'] == allophone4]
            temp_df5 = temp_df[temp_df['correct_allophone'] == allophone5]

            temp_ls_dfs = [temp_df0, temp_df1, temp_df2, temp_df3, temp_df4, temp_df5]
            new_temp_df = pd.concat(temp_ls_dfs)
                              # == allophone] # right now the code doesn't account for any diphtongs
            new_ls_of_dfs.append(new_temp_df)

        return(new_ls_of_dfs)


    def get_proportions(ls_of_dfs):
        """

        """
        ls_of_proportions = []

        for i in range(len(ls_of_dfs)):
            temp_df = ls_of_dfs[i]

            boolean = temp_df['correct_allophone'] == temp_df['student_allophone']
            denominat = len(boolean)
            numerat = boolean.sum()
            proportion = numerat/denominat

            ls_of_proportions.append(proportion)

        return(ls_of_proportions)


    def descriptive_stats(ls_of_dfs, allophone):
        """
        Returns some basic descriptive statistics about the selected allophone in the input dataframes.

        """


        new_ls_dfs = filter_by_allophone(ls_of_dfs, allophone0 = allophone) # because filter_by_allophone changed, there will have to be some corresponding changes
        # to make sure everything else still runs smoothly
        allophone_frequency = len(new_ls_dfs[0])

        print("In this word list, the allophone [" + allophone + "] occured in " + str(allophone_frequency) + " syllables.")

        accuracy_ls = get_proportions(new_ls_dfs)
        accuracy_mean = np.mean(accuracy_ls)
        accuracy_std = np.std(accuracy_ls)

        print("For this allophone:")
        print("The particpants scored an average of " + str(accuracy_mean * 100) +
          "% accuracy with standard deviation of: " + str(accuracy_std * 100) + "%")
        print()


        allophonic_errors = []
        nex_ls_dfs = []

        for i in range(len(ls_of_dfs)):
            temp_df = new_ls_dfs[i]
            errors_df = temp_df[temp_df['correct_allophone'] != temp_df['student_allophone']]
            #print(errors_df)
            nex_ls_dfs.append(errors_df)


        for j in range(len(nex_ls_dfs)):
            errors = nex_ls_dfs[j]['student_allophone']
            errors_ls = list(errors)
            print(errors_ls)

            #for s in range(len(errors_ls)):
             #   error = errors_ls[s]
              #  allophonic_errors.append(error)

        allophonic_errors= np.array(allophonic_errors)
        return(allophonic_errors)


    def extract_from_dictionary(ls_of_dictionaries, key_name):
        """
        Iterates through a list of dictionaries and, based on the inserted key name, extracts that data.

        :param: ls_of_dictionaries: a list of dictionaries
        :param: key_name: a string with ('') that indexes which set of the dictionary you want to extract

        :returns: list with the specified (keyed) datatype


        """

        #index = []
        partic_name = []
        data_element = []

        for index, dictionary in enumerate(ls_of_dictionaries):
                data = dictionary[key_name]
                partic_name = dictionary['partic_number']
                data_element.append(data)

        return(data_element)
