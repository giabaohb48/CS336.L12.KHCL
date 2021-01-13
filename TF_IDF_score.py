import string
import numpy as np
import pandas as pd
from pyvi import ViTokenizer
import glob
from collections import Counter
from string import punctuation
import Loader
import pickle
import re
import math
import os
import Text_Preprocess
import shutil


paths= glob.glob('H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\Dataset\\Flickr8k\\Image Caption Generator\\descriptions.txt')

def load_doc(filename):
    for img in filename:
        with open(img,encoding="utf-8") as f:
            text=f.read()  
        f.close()
    return text

# def load_all_words(filename):
#     doc=load_doc(filename)
#     descriptions = dict()
#     temp="1000268201_693b08cb0e"
#     temp1=""

#     for line in doc.split('\n'):
        
#         tokens = line.split()
#         image_id, image_desc = tokens[0],tokens[1:]
#         if(image_id==temp):
#             temp1=temp1 + " "+' '.join(image_desc)

#         if(image_id!=temp):
#             descriptions[temp] =''.join(temp1)
#             temp1=""
#         temp=tokens[0] 
#     return descriptions





# dic_description=dict()
# dic_description=load_all_words(paths)

# # np.save('D:\\UIT\\HK3\\Truy vấn thông tin đa phương tiện\\New folder\\vs_CBIR\\dic_description.npy',dic_description)

# decription=dict()

# for dic in dic_description:
#     text=dic_description[dic]
#     text_lower =text.lower()
#     text_token=ViTokenizer.tokenize(text_lower)
#     decription[dic]=text_token

# print(decription)
# print("Sucessful...1")

stop_word=[]
with open("H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\Dataset\\Flickr8k\\stop-word.txt",encoding="utf-8") as f:
    text=f.read()
    for word in text.split():
        stop_word.append(word)
    f.close
    punc=list(punctuation)
stop_word=stop_word+punc
print("------------------")

path2=glob.glob('H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\clean_desc.txt')

# def save_description(description, filename):
#     lines = list()
#     for key, desc_list in description.items():
        
#         lines.append(key + ' ' + desc_list)
#     data = ('\n').join(lines)
#     file = open(filename,'w')
#     file.write(data)
#     file.close()

# save_description(decription,paths)

def load_description(filename):
    doc=load_doc(filename)
    mapping = dict()
    #one entry in each line
    for line in doc.split('\n'):
        tokens = line.split()
        #if no of tokens less than 2 --> incorrect desc
        if len(line)<2:
            continue
        #first -- id rest -- desc
        image_id, image_desc = tokens[0], tokens[1:]
        
        #convert description token back to string
        
        #create a list (containing all desc of a given image)
        mapping[image_id]=' '.join(image_desc)
    return mapping

decription=dict()
decription=load_description(path2)



def stopWork(text):
    sent=[]
    for word in text.split():
        if(word not in stop_word):
            if("_" in word) or(word.isalpha()==True):
                sent.append(word)
    return sent

final_desciption=dict()
for key in decription:        
    text=tuple(stopWork(decription[key]))           
    final_desciption[key]=text
    

def change(msg_set):
    text=""
    for word in msg_set:
        text=''.join(word)
    return text

def build_dic(text):
    temp=[]
    temp=text
    dictionary = set()
    for content in temp:
        dictionary.add(content)
        
    return dictionary

def calc_tf_weighting(vocab, contents):
    TF = np.zeros((len(vocab), len(contents)))
    for i, word in enumerate(vocab):
        for j, content in enumerate(contents):
            TF[i,j] = content.count(word)
    # Chuan hoa
    TF = TF / np.sum(TF, axis=0)
    return TF

def f(term,doc):
    result=0
    for word in doc:
        if(word==term):
            result=result+1
    return result

def number_tf_idf(text):
    count=len(text.split())
    if(count>1 and count <= 3):
        result=3.2
    else:
         result=4
    return result


input_file = open('C:\\xampp\\htdocs\\uploads\\description.txt', 'r')
input_query = input_file.readline()
table = str.maketrans('','',string.punctuation)
desc = input_query.split()
desc = [word.lower() for word in desc]
desc = [word.translate(table) for word in desc]
desc = [word for word in desc if len(word)>1]
desc = [word for word in desc if word.isalpha()]
input_query =  ' '.join(desc)


sent=""
for word in input_query.split():
    
    if(word not in stop_word):
        if("_" in word) or(word.isalpha()==True):
            sent= sent+" "+''.join(word)

out_stop=sent
# print(out_stop)
# print(len(out_stop.split()))
out_word=[]
for word in out_stop.split():
    out_word.append(word)
print(out_word)
out=[]
for word in out_word:
    out.append(word.split())


imgs=[]
nan=float('nan')



for key in final_desciption:
    count=0
    for word in out:
        temp2=''
        result1=0
        count_word=0
        temp2=''.join(word)

        result1=result1+f(temp2,final_desciption[key])
        
        tf=calc_tf_weighting(build_dic(final_desciption[key]),final_desciption[key])
        qTF=calc_tf_weighting(build_dic(final_desciption[key]),[word])
        
        DF=np.sum(tf!=0,axis=1)
        IDF=1+np.log(len(final_desciption[key])/DF)
        IDF=np.array([IDF]).T
        
        tf_idf=tf*IDF
        qTF_IDF=qTF*IDF
        
        dists = np.linalg.norm(qTF_IDF - tf_idf, axis=0)
        
        for value in dists:
            
            if(math.isnan(value)):
                break
            elif(value==0):
                count_word=count_word+1
        if(count_word==result1 and result1!=0):
            count=count+1
        if(result1 >4):
            imgs.append(key)
    if(count==len(out_stop.split())):
        imgs.append(key)


    

path = 'H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\Dataset\\Flickr8k\\Flicker8k_Dataset\\'
matched_imgcaption_file = open('C:\\xampp\\htdocs\\uploads\\matched_images_caption.txt','w')

folder = 'C:\\xampp\\htdocs\\uploads\\matched_images\\'

desc_text = Text_Preprocess.load_text('H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\Dataset\\Flickr8k\\Flickr8k_text\\Flickr8k.token.txt')
descriptions = Text_Preprocess.load_description(desc_text)


testFile = str('H:\\1UNIVERSITY\\2020_1\\truy_van_thong_tin_da_pt\\project\\vs_CBIR\\Dataset\\Flickr8k\\Flickr8k_text\\Flickr_8k.testImages.txt')
testImagesLabel = Loader.load_set(testFile)

pathDel=os.listdir(folder)
for f in pathDel:
    os.remove(folder +f)
i=0


for img in imgs:
    if img in testImagesLabel:
        i+=1
        matched_imgcaption_file.write(descriptions[img][1] + '\n')
        shutil.copy2(path+img+'.jpg',folder)
        # if(i==21):
        #     break
