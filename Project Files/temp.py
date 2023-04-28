import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import os
from scraping import scrap
from nltk.tokenize import word_tokenize



# data = pd.read_excel(os.getcwd()[:70]+"Blackcoffer\Input.xlsx")
# url = (data["URL"][62])
# file_name = (data["URL_ID   "][62])

# browser = webdriver.Edge(executable_path="Blackcoffer/Project Files/msedgedriver.exe")
# browser.get("https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/")
# browser.maximize_window()

# value = browser.find_elements(By.XPATH,"//h3[normalize-space()='Ooops... Error 404']")
# print(len(value))
# print(os.getcwd())
# D:\Academics\Data Science\Project\Internshala Submissions\Blackcoffer\Project Files\text files\37.txt
# print(os.path.exists(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt"))
# scrap(file_name,url)

# scrap("90","https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/")
# print(len(os.listdir("text files")))
# print(os.path.exists(f"{(os.getcwd()[:70])}Blackcoffer\\MasterDictionary\\negative-words.txt"))
# print(os.getcwd()[:70])


# making one stopwords file.
# for i in os.listdir(f"{(os.getcwd()[:70])}Blackcoffer\\StopWords"):
#         with open(f"{(os.getcwd()[:70])}Blackcoffer\\StopWords\\{i}",'r') as f:
#             with open("All_Stopwords.txt",'a',encoding='utf-8') as f2:
#                 f2.write(f.read().lower())

# lst = list()
# with open("All_Stopwords.txt",'r') as f:
#     data = f.read()
#
# lst = data.replace("\n",' ').split(".")
# print(lst)
# f.close()


# f = open("text files/38.txt",'r')
# text= (f.read())
# import spacy
# nlp = spacy.load("en_core_web_sm")
# import en_core_web_sm
# nlp = en_core_web_sm.load()
# doc = nlp(text)
# tokens = ([w.text for w in doc])
# # print(tokens)
# tokens = [i for i in tokens if i not in ('-','"',' \n','\n',' \\n','\\n','',' ',':',',','.','!','?','(',')','“',', ',' \n \n')]
# tokens = [i.lower() for i in tokens]
#
# print(tokens)


# lst = list()
# with open("All_Stopwords.txt", 'r') as f:
#     data = f.read()
#
# # lst = data.replace("\n", ' ').split(" ")
# lst = data.split("\n")
# # print(len(lst))
# lst = [i for i in lst if i not in ('-','"',' \n','\n',' \\n','\\n','',' ',':',',','.','!','?','(',')','“',', ',' \n \n')]
# # print(len(lst))
# f.close()
# return lst






#
# def percentage_of_complex_word(f):
#     complex_words = complex_words_count(f)
#     f.seek(0)
#     total_words = len(tokenizer(f,remove_stopwords=False)) # if total words contains stop words then percentage is 13 and without stopwords percentage is 34.
#     return complex_words/total_words
#
#
# def fog_index(f):
#     percent_comple_word = percentage_of_complex_word(f)
#     f.seek(0)
#     avg_sen_len = avg_sen_length(f)
#     return (0.4*(avg_sen_len + percent_comple_word))


from main import  tokenizer

# tokens = tokenizer(f,remove_stopwords=False)
#
# def syllables_per_word(f):
#     import spacy
#     from spacy_syllables import SpacySyllables
#     nlp = spacy.load("en_core_web_sm")
#     nlp.add_pipe("syllables", after="tagger")
#     nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
#     doc = nlp(f.read())
#     # data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
#     # complex_words = [(token,token._.syllables_count) for token in doc if (token._.syllables_count!=None and token._.syllables_count>2 )]
#     total_syllable_counts = 0
#     for token in doc:
#         if token._.syllables_count!=None:
#             total_syllable_counts += token._.syllables_count
#     total_tokens = len([token.text for token in doc if token._.syllables_count!=None])
#     return total_syllable_counts/total_tokens
#
#
#
#
# def Personal_pronouns(f):
#     import en_core_web_sm
#     nlp = en_core_web_sm.load()
#     tokenized = nlp(f.read())
#     total_personal_pronouns = 0
#     for tok in tokenized:
#         if tok.tag_=="PRP":
#             # print(f"{tok.text:<10} {tok.tag_:<10} {tok.pos_:<10}")
#             total_personal_pronouns+=1
#     return(total_personal_pronouns)
#
#
#
#
# print(len("Rohit"))
#
# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns', 15)
# pd.set_option('display.max_rows', 113)
# output = pd.read_excel(os.getcwd()[:70] + "Blackcoffer\Output Data Structure.xlsx")
# for i,j in enumerate(output.columns):
#     print(i,j)


# def syllables_per_word(f):
#     import spacy
#     from spacy_syllables import SpacySyllables
#     nlp = spacy.load("en_core_web_sm")
#     nlp.add_pipe("syllables", after="tagger")
#     nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
#     doc = nlp(f.read())
#     # data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
#     # complex_words = [(token,token._.syllables_count) for token in doc if (token._.syllables_count!=None and token._.syllables_count>2 )]
#     total_syllable_counts = 0
#     for token in doc:
#         if token._.syllables_count!=None:
#             total_syllable_counts += token._.syllables_count
#     tokens = [token.text for token in doc if token._.syllables_count != None]
#     total_tokens = len([token.text for token in doc if token._.syllables_count!=None])
#     print(tokens)
#     print(total_tokens,total_syllable_counts)
#     f.seek(0)
#     return (total_syllable_counts/total_tokens)
#
# f = open("text files/39.txt","r")
# from main import tokenizer
# print(tokenizer(f))



desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 113)
output = pd.read_excel(os.getcwd()[:70] + "Blackcoffer\Output Data Structure.xlsx")

error = open("Error_Files.txt", 'r')
url_ids_error = [int(i) for i in error.read().split("\n") if i != ""]

# print(output)
output = (output[output.URL_ID.isin(url_ids_error) == False])

output.reset_index(inplace=True, drop=True)
# print(output["URL"][1])
# print(output.loc[1,"URL"])
# 123 125 126 127 132 137 140 141 142 146 147 148 149
#
# for i in range(0, len(output)):
#     # for i in range(0,5):
#     f = open(f"text files/{output[output.columns[0]][i]}.txt", 'r',errors="ignore")
#     try:
#         # print(f.read())
#         f.read()
#     except Exception as e:
#         print(f"{output[output.columns[0]][i]}")
#         print(e)

f = open("text files\\125.txt",'r',errors="ignore")
# f.seek(546)
# print(f.read(546))

import spacy
from spacy_syllables import SpacySyllables


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("syllables", after="tagger")
nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
doc = nlp(f.read())
# data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
complex_words = [(token, token._.syllables_count) for token in doc if
                 (token._.syllables_count != None and token._.syllables_count > 2)]
f.seek(0)
print(len(complex_words))
print(complex_words)