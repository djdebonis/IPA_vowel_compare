# import necessary modules
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

def open_and_read(self):
    """
    opens a file and returns a long long long string
    
    :infile_path_and_name: string of the path/path/txtFileName.txt from the current directory
    
    """
    with open(self.infile_path_and_name, 'r') as file:
        string = file.read().replace('\n', '')
        
    return string

def split_sentence(sentence: str) -> list:
    """
    Takes a sentence in IPA and parses it to individual words by breaking according to
    the " # " IPA string pattern.
    
    :sentence: sentence to parse
    
    :returns: list of individual words
    :rtype: list
    
    """
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
    path = ""
    file_name = ""
    file_ext = ""
    
    furthest_dir_index = 0
    extention_index = 0
    
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
                  "direct_path": path, "extention" : file_ext}
    
    return(dictionary)


def imp_collect_clean(ls_of_file_paths):
    ls_of_dictionaries = []
    for index, file_path in enumerate(ls_of_file_paths):
        dictionary = file_finder(file_path)
        
        temp_string = open_and_read(file_path)
        
        temp_raw = split_sentence(temp_string)
        
        temp_partic = rm_stress(temp_raw)
        
        dictionary["import_index"] = index
        
        dictionary["clean_transcript"] = temp_partic
        
        
        ls_of_dictionaries.append(dictionary)
        
    return(ls_of_dictionaries)