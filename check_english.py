#Project 2 - MapReduce Program - Checking for non-english words in song lyrics


import os,glob
import read_english_dictionary
import re

#Navigating to the directory 
paths = [os.getcwd()+"\McCutchionAndBhowmick_Songs",os.getcwd()+"\Weslyan_Songs"]

#Enter paths as full directory. If files are in the same folder as check_english.py enter os.getcwd() as "file_paths"
def split_files(file_paths):
    for path in file_paths:
    #Looping through all files in the each folder
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with open(filename, 'r') as f:
               contents = f.read().split()
               num=1
               #If a file's length is longer than 5000 words, we split the file
               #saving each paragraph as a different file and adding a part number to the file name.
               if len(contents) > 5000:
                   split = f.read().split("\n\n")
                   for paragraph in split:
                       paths.append(os.getcwd()+"\split+files")
                       indexed_filename=filename[:-4]+str(num)+".txt"
                       file = open(os.path.join(os.getcwd()+'\split_files' ,indexed_filename), "w")
                       file.write(str(paragraph))
                       file.close()
                       num+=1
                   
                   
# Creating list of vocabulary - "unique_words" serves as the Document Frequency
# & "unique_words_by_file" serves as the Term Frequency (local)
def freq(file_paths):
    unique_words={}
    unique_words_by_file={}
    for path in file_paths:
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with open(filename, 'r') as f:
                #splitting file by word and removing all special characters, special characters are not permitted as dict keys.
                #also converting all files to lowercase only as the dictionary is all lowercase.
                contents=f.read()
                contents=contents.lower()
                contents=re.sub(r'[^\w]',' ',contents)
                contents=contents.split()
                words_by_file={}
                #loop through each word in the file.
                #each unique word is added to the dictionary with their frequency
                for word in contents:
                    if word in unique_words:
                        unique_words[word]=unique_words[word]+1
                    if word not in unique_words:
                        unique_words[word]=1
                    if word in words_by_file:
                        words_by_file[word]=words_by_file[word]+1
                    if word not in words_by_file:
                        words_by_file[word]=1
                unique_words_by_file[os.path.split(filename)[1]]=words_by_file
    return unique_words_by_file


#Checking for non english words
def check_english(file_paths):
    #run "Frequency" function and get list of Unique words in each file
    unique_words_by_file=freq(file_paths)
    #loading english dictionary from english-words library / source - https://github.com/dwyl/english-words
    english=read_english_dictionary.load_words()
    nonenglish_byfile={}
    #loop through each file's unique word list
    for filename in unique_words_by_file:
        count=0
        words={}
        #loop through each word in each files unique word list
        for word in unique_words_by_file[filename] :
            #check if word is contained in english dictionary
            if word not in english:
                count=count+unique_words_by_file[filename][word]
                words[word]=unique_words_by_file[filename][word]
        nonenglish_byfile[filename]={'Count of Non-English Words':count, 'List of Non-English Words & their frequency':words}
    return nonenglish_byfile
                
    
                   
    

                    
                    
                    
                    
    
                
                    
                    
                
            
               
        
        
        