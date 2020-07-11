# import necessary modules
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

def vowel_lists_append(prescrip_string, descrip_string, prescrip_vowel_ls, descrip_vowel_ls):
    """
    Takes two lists of strings and two strings and appends the vowels of the new strings on to the list of vowels
    
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
