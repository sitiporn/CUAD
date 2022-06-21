# Import the various libraries
import re, json, os, itertools
import pandas as pd
from tqdm import tqdm


def pre_process_doc_common(text):
    # Simple replacement for "\n"
    text = text.replace("\n", " ")     
    
    # Simple replacement for "\xa0"
    text = text.replace("\xa0", " ")  
    
    # Simple replacement for "\x0c"
    text = text.replace("\x0c", " ")
    
    # Get rid of multiple dots
    regex = "\ \.\ "
    subst = "."
    text = re.sub(regex, subst, text, 0)
    
    # Get rid of underscores
    regex = "_"
    subst = " "
    text = re.sub(regex, subst, text, 0)
    
    # Get rid of multiple dashes
    regex = "--+"
    subst = " "
    text = re.sub(regex, subst, text, 0)
    
    # Get rid of multiple stars
    regex = "\*+"
    subst = "*"
    text = re.sub(regex, subst, text, 0)
    
    # Get rid of multiple whitespace
    regex = "\ +"
    subst = " "
    text = re.sub(regex, subst, text, 0)
    
    #Strip leading and trailing whitespace
    text = text.strip()
    
    return text

# Function to take in the file list, read each file, clean the text and return all agreements in a list
def text_data(file_list,text_folder_path ,print_text=False, clean_text=True):
    text_list = []
    
    for index, filename in tqdm(file_list):
        agreement = open(text_folder_path+'/'+filename, "r")
        text = agreement.read()
        if print_text:
            print("Text before cleaning: \n", text)
        
        # Run text through cleansing function
        if clean_text:
            text = pre_process_doc_common(text)
        # use maximum len of each docs
        text = text[:]
        len_text = len(text)
        # print(len_text)
        
        if print_text:
            print("Text after cleaning: \n", text)
        
        text_list.append([index,
                  filename,
                  text,
                  len_text])
        
    return text_list

