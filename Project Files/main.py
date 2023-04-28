import pandas as pd
import os
import numpy as np
import spacy
import en_core_web_sm
import spacy
from spacy_syllables import SpacySyllables
# nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()
nlp.add_pipe("syllables", after="tagger")
nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
p = open(f"{(os.getcwd()[:70])}Blackcoffer\\MasterDictionary\\negative-words.txt",'r')
negative_words = (p.read().split("\n"))
p.close()
p = open(f"{(os.getcwd()[:70])}Blackcoffer\\MasterDictionary\\positive-words.txt",'r')
positive_words = (p.read().split("\n"))
p.close()

# creating the list of stopwords
def stop_words_list():
    lst = list()
    with open("All_Stopwords.txt", 'r') as f:
        data = f.read()

    # lst = data.replace("\n", ' ').split(" ")
    lst = data.split("\n")
    # print(len(lst))
    lst = [i for i in lst if i not in (
    '-', '"', ' \n', '\n', ' \\n', '\\n', '', ' ', ':', ',', '.', '!', '?', '(', ')', '“', ', ', ' \n \n')]
    # print(len(lst))
    f.close()
    return lst

stp_words = stop_words_list()
def tokenizer(f,remove_stopwords=True):
    """Accepts file object for txt file and removes all the stopwords by default and return token list, if keyword arg is false then
    stopwords are not removed"""
    # f = open("text files/38.txt",'r')
    text= f.read()
    doc = nlp(text)
    tokens = ([w.text for w in doc])
    # print(tokens)
    tokens = [i for i in tokens if i not in ('-','"',' \n','\n',' \\n','\\n','',' ',':',',','.','!','?','(',')','“',', ',' \n \n')]
    tokens = [i.lower() for i in tokens]
    # print(len(tokens))
    if remove_stopwords:
        tokens = [i for i in tokens if i not in stp_words]
        return tokens
    # print(len(tokens))
    f.seek(0)
    return tokens


def calcualate_negative_score(tokens):
    # p = open(f"{(os.getcwd()[:70])}Blackcoffer\\MasterDictionary\\negative-words.txt",'r')
    # negative_words = (p.read().split("\n"))
    # print(negative_words)
    negative_score = 0
    for i in tokens:
        if i in negative_words:
            negative_score+=1
    return negative_score

def calcualate_positive_score(tokens):
    # p = open(f"{(os.getcwd()[:70])}Blackcoffer\\MasterDictionary\\positive-words.txt",'r')
    # positive_words = (p.read().split("\n"))
    # print(negative_words)
    positive_score = 0
    for i in tokens:
        if i in positive_words:
            positive_score+=1
    return positive_score

def polarity_score(positive_score,negative_score):
    if (positive_score+negative_score)==0:
        return 0
    return (((positive_score - negative_score)/(positive_score + negative_score)) + 0.000001)



def subjectivity_score(positive_score,negative_score,tota_words):
    return  ((positive_score + negative_score) / ((tota_words))+ 0.000001)

def avg_sen_length(f,tokens):

    total_sentences = len(f.read().replace("\n"," ").split("."))
    f.seek(0)
    # word = [i for i in (f.read().split(" ")) if i not in ('-','"',' \n','\n',' \\n','\\n','',' ',':',',','.','!','?','(',')','“',', ',' \n \n')]
    # tokens = tokenizer(f,remove_stopwords=False)
    total_words = len(tokens)
    # print(word)
    f.seek(0)
    return int(total_words / total_sentences)



def complex_words_count(f):
    import spacy
    from spacy_syllables import SpacySyllables
    # nlp = spacy.load("en_core_web_sm")
    # nlp.add_pipe("syllables", after="tagger")
    # nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
    f.seek(0)
    doc = nlp(f.read())
    # data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
    complex_words = [(token,token._.syllables_count) for token in doc if (token._.syllables_count!=None and token._.syllables_count>2 )]
    f.seek(0)
    return (len(complex_words))

def percentage_of_complex_word(f,complex_words):
    # complex_words = complex_words_count(f)
    f.seek(0)
    total_words = len(tokenizer(f,remove_stopwords=False)) # if total words contains stop words then percentage is 13 and without stopwords percentage is 34.
    f.seek(0)
    return complex_words/total_words


def fog_index(f,percent_comple_word,avg_sen_len):
    # percent_comple_word = percentage_of_complex_word(f)
    # f.seek(0)
    # avg_sen_len = avg_sen_length(f)
    f.seek(0)
    return (0.4*(avg_sen_len + percent_comple_word))


# def avg_words_per_sen(f):
#     return avg_sen_length(f)

# def word_count(f):
#     return len(tokenizer(f))

def syllables_per_word(f,total_tokens):

    # nlp = spacy.load("en_core_web_sm")
    # nlp.add_pipe("syllables", after="tagger")
    # nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser",  "attribute_ruler", "lemmatizer", "ner"]
    doc = nlp(f.read())
    # data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
    # complex_words = [(token,token._.syllables_count) for token in doc if (token._.syllables_count!=None and token._.syllables_count>2 )]
    total_syllable_counts = 0
    for token in doc:
        if token._.syllables_count!=None:
            total_syllable_counts += token._.syllables_count
    # total_tokens = len([token.text for token in doc if token._.syllables_count!=None])
    f.seek(0)
    # total_tokens = len(tokenizer(f,remove_stopwords=False))
    return (total_syllable_counts/total_tokens)

def personal_pronouns(f):
    # import en_core_web_sm
    # nlp = en_core_web_sm.load()
    tokenized = nlp(f.read())
    total_personal_pronouns = 0
    for tok in tokenized:
        if tok.tag_=="PRP":
            # print(f"{tok.text:<10} {tok.tag_:<10} {tok.pos_:<10}")
            total_personal_pronouns+=1
    f.seek(0)
    return(total_personal_pronouns)


def avg_word_len(f,tokens):
    # tokens = tokenizer(f, remove_stopwords=False)
    sum_word_len = 0
    for i in tokens:
        sum_word_len += len(i)
    f.seek(0)
    return sum_word_len/len(tokens)

if __name__=="__main__":

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
    # print(output)
    for i in range(0,len(output)):
    # for i in range(0,5):

        try:
            f = open(f"text files/{output[output.columns[0]][i]}.txt",'r',errors="ignore")
            print(output[output.columns[0]][i])
        except Exception as e:
            with open("charmap_error.txt","a") as e:
                e.write(f"{output[output.columns[0]][i]}\n")
            continue
        tokens_with_stp = tokenizer(f,remove_stopwords=False)
        tokens_without_stp = tokenizer(f)
        pos_val = calcualate_positive_score(tokens_with_stp)
        neg_val = calcualate_negative_score(tokens_with_stp)
        com_word_count = complex_words_count(f)
        percet_of_complex_words = percentage_of_complex_word(f,com_word_count)
        avg_sentence_len = avg_sen_length(f,tokens_with_stp)
        # filling dataframe.
        # output[output.columns[2]][i] = pos_val
        # output[output.columns[3]][i] = neg_val
        # output[output.columns[4]][i] = polarity_score(pos_val,neg_val)
        # output[output.columns[5]][i] = subjectivity_score(neg_val,pos_val,len(tokens_without_stp))
        # output[output.columns[6]][i] = avg_sentence_len
        # output[output.columns[7]][i] = percet_of_complex_words
        # output[output.columns[8]][i] = fog_index(f,percet_of_complex_words,avg_sentence_len)
        # output[output.columns[9]][i] = avg_sentence_len
        # output[output.columns[10]][i] = com_word_count
        # output[output.columns[11]][i] = len(tokens_with_stp)
        # output[output.columns[12]][i] = syllables_per_word(f,len(tokens_with_stp))
        # output[output.columns[13]][i] = personal_pronouns(f)
        # output[output.columns[14]][i] = avg_word_len(f,tokens_with_stp)

        output.loc[i,output.columns[2]] = pos_val
        output.loc[i,output.columns[3]] = neg_val
        output.loc[i,output.columns[4]] = polarity_score(pos_val, neg_val)
        output.loc[i,output.columns[5]] = subjectivity_score(neg_val, pos_val, len(tokens_without_stp))
        output.loc[i,output.columns[6]] = avg_sentence_len
        output.loc[i,output.columns[7]] = percet_of_complex_words
        output.loc[i,output.columns[8]]= fog_index(f, percet_of_complex_words, avg_sentence_len)
        output.loc[i,output.columns[9]]= avg_sentence_len
        output.loc[i,output.columns[10]]= com_word_count
        output.loc[i,output.columns[11]]= len(tokens_with_stp)
        output.loc[i,output.columns[12]]= syllables_per_word(f, len(tokens_with_stp))
        output.loc[i,output.columns[13]] = personal_pronouns(f)
        output.loc[i,output.columns[14]]= avg_word_len(f, tokens_with_stp)
        f.close()
    print(output)
    output.to_excel("final_output.xlsx",index=False)
