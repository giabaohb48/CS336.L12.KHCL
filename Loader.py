import pickle
# import spacy
import re
import numpy as np
def load_doc(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()    
    return text

def replace_char(filename):
    doc = load_doc(filename)

    for line in doc.split('\n'):
        line = line.replace("\\", "/")
    return filename
#Image Identifier --- TrainImage.txt
#2513260012_03d33305cf.jpg
def load_set(filename):
    doc = load_doc(filename)
    dataset = list()
    
    for line in doc.split('\n'):
        if len(line)<1:
            continue
        identifier = line.split('.')[0]
        dataset.append(identifier)
    return set(dataset)


def load_clean_descriptions(filename, dataset):
    doc = load_doc(filename)
    descriptions = dict()
    
    for line in doc.split('\n'):
        tokens = line.split()
        image_id, image_desc = tokens[0],tokens[1:]
        
        #if image_id not in dataset ignore
        if image_id in dataset:
            if image_id not in descriptions:
                descriptions[image_id] = list()
            desc = 'startseq ' + ' '.join(image_desc) + ' endseq'
            descriptions[image_id].append(desc)
    return descriptions


def load_all_words(filename, dataset):
    doc = load_doc(filename)
    descriptions = dict()
    
    for line in doc.split('\n'):
        tokens = line.split()
        image_id, image_desc = tokens[0],tokens[1:]
        
        #if image_id not in dataset ignore
        if image_id in dataset:
            if image_id not in descriptions:
                descriptions[image_id] = list()
            desc = ' '.join(image_desc)
            
            descriptions[image_id] = ''.join(desc)
            
    return descriptions


def load_clean_descriptions_tf(filename,dataset):
    doc = load_doc(filename)
    descriptions = dict()
    
    for line in doc.split('\n'):
        tokens = line.split()
        image_id, image_desc = tokens[0],tokens[1:]
        
        #if image_id not in dataset ignore
        if image_id in dataset:
            if image_id not in descriptions:
                descriptions[image_id] = list()
            desc = ' '.join(image_desc)
            descriptions[image_id].append(desc)
    return descriptions




# if __name__ == "__main__":
#     testFile = 'H:\\1UNIVERSITY\\2020_1\\Truy vấn thông tin đa pt\\project\\Dataset\\Flickr8k_text\\Flickr_8k.testImages.txt'
#     testImagesLabel = load_set(testFile)
#     test_descriptions = load_collection_and_store_data('H:\\1UNIVERSITY\\2020_1\\Truy vấn thông tin đa pt\\project\\Dataset\\Image Caption Generator\\descriptions.txt', testImagesLabel)
   
# desc = generate_term("two mAn on the beach")
# print(desc)

