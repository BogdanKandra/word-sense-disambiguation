"""
Created on Wed Mar  7 19:40:20 2018

@author: Bogdan
"""
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as w_tok

marks = ['.', ',', '?', '!', ':', ';', '(', ')',
         '[', ']', '...', '\'', '\"', "\''"]

functionWords = ['about', 'across', 'against', 'along', 'around', 'at',
                 'behind', 'beside', 'besides', 'by', 'despite', 'down',
                 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of',
                 'off', 'on', 'onto', 'over', 'through', 'to', 'toward',
                 'with', 'within', 'without', 'anything', 'everything',
                 'anyone', 'everyone', 'ones', 'such', 'it', 'itself',
                 'something', 'nothing', 'someone', 'the', 'some', 'this',
                 'that', 'every', 'all', 'both', 'one', 'first', 'other',
                 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a',
                 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second',
                 'another', 'last', 'few', 'little', 'less', 'least', 'own',
                 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what',
                 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since',
                 'while', 'although', 'though', 'who', 'whose', 'can', 'may',
                 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would',
                 'should', 'must', 'here', 'there', 'now', 'then', 'always',
                 'never', 'sometimes', 'usually', 'often', 'therefore',
                 'however', 'besides', 'moreover', 'though', 'otherwise',
                 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

def remove_punctuation(tokenList):
    result = [token for token in tokenList if token not in marks]
    return result

def compute_overlap(gloss, context):
    gloss.difference(functionWords)
    context.difference(functionWords)
    return len(gloss.intersection(context))

def lesk(word, sentence):
    senses = wn.synsets(word)
    
    bestSense = senses[0] # The most frequent sense of the word
    maxOverlap = 0
    
    sentTokenized = w_tok(sentence)
    sentNormalized = remove_punctuation(sentTokenized)
    context = set(sentNormalized)
    
    for sense in senses:
        gloss = set(remove_punctuation(w_tok(sense.definition())))
        for ex in sense.examples():
            gloss.union(w_tok(ex))
        overlap = compute_overlap(gloss, context)
        
        for h in sense.hyponyms():
            gloss = set(remove_punctuation(w_tok(h.definition())))
            for ex in h.examples():
                gloss.union(w_tok(ex))
            overlap += compute_overlap(gloss, context)
        
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    
    return bestSense

print(lesk('bank', 'The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.').definition())
print(lesk('pine', 'pine cone').definition())

#for sin in wn.synsets('bank'):
#    print(sin.definition())