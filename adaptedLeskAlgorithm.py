"""
Created on Tue Mar 13 18:16:11 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as wTok

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

def overlap(gloss1, gloss2):
    """Determines the longest sequence of common words between the two glosses.
    
    Arguments:
        gloss1 (str) -- first gloss

        gloss2 (str) -- second gloss
    
    Returns:
        str type -- the longest sequence of common words
    """
    result = ''
    
    for word in gloss1:
        if word in gloss2:
            

def score(gloss1, gloss2):
    """Calculates the score of the given pair of glosses.\n
    1. Compute the longest overlap between the glosses

    Arguments:
        gloss1 (str) -- first gloss

        gloss2 (str) -- second gloss

    Returns:
        int type -- the score of the pair of glosses
    """
    