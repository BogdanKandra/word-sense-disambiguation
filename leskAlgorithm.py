"""
Created on Wed Mar  7 19:40:20 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as w_tok
import utils

def compute_overlap(gloss, context):
    gloss.difference(utils.FUNCTION_WORDS)
    context.difference(utils.FUNCTION_WORDS)
    return len(gloss.intersection(context))

def lesk(word, sentence):
    senses = wn.synsets(word)
    
    bestSense = senses[0] # The most frequent sense of the word
    maxOverlap = 0
    
    sentTokenized = w_tok(sentence)
    sentNormalized = utils.remove_punctuation(sentTokenized)
    context = set(sentNormalized)
    
    for sense in senses:
        gloss = set(utils.remove_punctuation(w_tok(sense.definition())))
        for ex in sense.examples():
            gloss.union(w_tok(ex))
        overlap = compute_overlap(gloss, context)
        
        for h in sense.hyponyms():
            gloss = set(utils.remove_punctuation(w_tok(h.definition())))
            for ex in h.examples():
                gloss.union(w_tok(ex))
            overlap += compute_overlap(gloss, context)
        
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    
    return bestSense

print(lesk('bank', 'The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.').definition())
print(lesk('pine', 'pine cone').definition())
print(lesk('bass', 'I am cooking basses').definition())

#for sin in wn.synsets('bank'):
#    print(sin.definition())
