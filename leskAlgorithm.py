"""
Created on Wed Mar  7 19:40:20 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as w_tok
import wordnet_utils as utils

def simplified_lesk(word, sentence):
    """Determines the WordNet sense of **word** in the given **context**,
    using the Simplified Lesk Algorithm. \n

    Arguments:
        *word* (str) -- the word to be disambiguated

        *sentence* (str) -- the context phrase which contains the *word* to be
        disambiguated

    Returns:
        Synset type -- the WordNet sense of the disambiguated word
    """
    
    senses = wn.synsets(word) # Take all WordNet senses of the target word
    
    bestSense = senses[0] # Initialise as the most frequent sense of the word
    maxOverlap = 0
    
    sentence = w_tok(sentence)  # Tokenize the context phrase
    sentence = utils.remove_punctuation(sentence)
    context = set(sentence).difference(utils.STOPWORDS)  # Remove Stopwords
    
    for sense in senses:
        # For each sense, build its gloss by taking its definition, examples,
        # hyponyms and examples of hyponyms
        # TODO -- Maybe hyponyms shouldn't be included
        gloss = set(utils.remove_punctuation(w_tok(sense.definition())))
        for ex in sense.examples():
            gloss.union(w_tok(ex))
        gloss = gloss.difference(utils.STOPWORDS)
        overlap = len(gloss.intersection(context))
        
        for h in sense.hyponyms():
            gloss = set(utils.remove_punctuation(w_tok(h.definition())))
            for ex in h.examples():
                gloss.union(w_tok(ex))
            gloss = gloss.difference(utils.STOPWORDS)
            overlap += len(gloss.intersection(context))
        
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    
    return bestSense

#print(simplified_lesk('bank', 'The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.').definition())
#print(simplified_lesk('pine', 'pine cone').definition())
#print(simplified_lesk('bass', 'I am cooking basses').definition())
#print(simplified_lesk('hard', 'hard cash').definition())

#for sin in wn.synsets('bank'):
#    print(sin.definition())
