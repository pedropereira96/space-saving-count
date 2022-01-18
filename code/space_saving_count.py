from collections import  defaultdict
import os
import re
import nltk
from nltk.corpus import stopwords



class counter():

    def __init__(self, file_path):
        self.file_path = file_path
        self.words=[]
        self.exact_counter = defaultdict(int)

        self.space_saving_count = defaultdict(int)
        self.ammount_of_words=0

    def read_file(self):
        stops = []
        with open("content/texts/stopwords.txt",'r') as stop: 
            for word in stop: 
                stops.append(word.replace("\n",''))
        print(stops)

        with open(self.file_path,'r') as file:  
            for line in file:       
                for word in line.strip().split(): 
                    word_cleaned = self.clean_word(word)
                    if word_cleaned not in stops and word_cleaned != "":
                        self.exact_counter[word_cleaned]+=1 #Exact  counter
                        self.words.append(word_cleaned)
        self.exact_counter = dict(sorted(self.exact_counter.items(),key=lambda item:item[1],reverse=True))
        self.ammount_of_words=len(self.words)

    
    def space_saving_counter(self, k):
        counters = {}                   
        for word in self.words:            
            if word in counters:        
                counters[word] += 1
            elif len(counters) + 1 < k:
                counters[word] = 1
            else:
                min_counter = min(counters, key=counters.get)       
                counters[word] = counters.pop(min_counter) + 1      
        self.space_saving_count = counters

    def clean_word(self, word):
        return re.sub('[^A-Za-z]+', '', word).lower()

