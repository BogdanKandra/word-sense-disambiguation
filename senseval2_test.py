"""
Created on Tue Mar 27 13:31:52 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.corpus import senseval
from adaptedLeskAlgorithm import adapted_lesk as alesk
import wordnet_utils as utils

def line_test():        
        instances = senseval.instances('hard.pos')
        
        
        
        