# import necessary modules
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat


def filter_by_dictionary(dictionary_df, column_criteria, equivelancy_criteria, ls_of_dfs):
    """
    Uses the categorical/meta information from one dataframe (in this case, the dictionary dataframe), and uses some criteria
    within it to filter another dataframe.
    
    Parameters
    ----------
    :dictionary_df: a pandas DataFrame with information relating to how you might want to filter the df
    :column_criteria: a string that is the column name of what you want to filter by in in dictionary_df
    :equivelancy_criteria: what the cells in dictionary_df[column_criteria] are equal to (e.g. 1, False, "<a>", etc.)
    :ls_of_dfs: a list of pandas DataFrames that you want to filter by some criteria
    
    Returns
    --------
    :returns: a list of filtered dataframes
    :rtype: list of pd DataFrames
    
    """

    word_selects = dictionary_df[dictionary_df[column_criteria] == equivelancy_criteria]
    
    new_ls_of_dfs = []
    
    for i in range(len(ls_of_dfs)):
        temp_df = ls_of_dfs[i]
        temp_df = temp_df[temp_df['word_number'].isin(word_selects['list_number'])]
        new_ls_of_dfs.append(temp_df)
        
    return(new_ls_of_dfs)


def filter_by_allophone(ls_of_dfs, allophone):
    """
    Filter the entire list of dataframes by a specific allophone.
    
    Parameters
    ----------
    :allophone: the allophone that you want to focus on, e.g. 'a', 'e', etc.
    :ls_of_dfs: a list of pandas DataFrames that you want to filter by some criteria
    
    Returns
    --------
    :returns: a list of filtered dataframes
    :rtype: list of pd DataFrames
    
    """
    
    new_ls_of_dfs = []
    
    for i in range(len(ls_of_dfs)):
        temp_df = ls_of_dfs[i]
        temp_df = temp_df[temp_df['correct_allophone'] == allophone] # right now the code doesn't account for any diphtongs
        new_ls_of_dfs.append(temp_df)
        
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
    
    
    new_ls_dfs = filter_by_allophone(ls_of_dfs, allophone)
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
        