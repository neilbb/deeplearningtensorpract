

import nltk
import nltk.tokenize as word_tokenize
from nltk.stem import WordNetLemmatizer

import numpy as np 
import random 
import pickle
from collections import Counter

lemmatizer = WordNetLemmatizer()
hm_lines = 10000000

def create_lexicon(pos,neg):
	lexicon = []
	for fi in [pos,neg]:





