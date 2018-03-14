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
    """Determines the longest sequence of common words between two glosses.
    
    Arguments:
        gloss1 (str) -- first gloss

        gloss2 (str) -- second gloss
    
    Returns:
        str type -- the longest sequence of common words
        
    Example:
        overlap('The house is full of rabbits and snakes', 
        'My house is overriden by rabbits and snakes') = 'rabbits and snakes'
    """

    gl1 = wTok(gloss1)
    gl2 = wTok(gloss2)
    
    gl1Enum = enumerate(gl1)
    
    result = ''
    length = 0
    
    for index, word in gl1Enum:
        lengthTemp = 0
        resultTemp = []
        
        if word in gl2:
            wIndex = gl2.index(word)  # Take the index of the word in the second gloss
            lengthTemp += 1   # Increment the length of the greatest overlap
            resultTemp.append(word)   # Construct a temp list with the word
            cond = True
            
            while cond:   # While words overlap
                nextIter = next(gl1Enum, None)
                if nextIter is not None:
                    nextWord1 = nextIter[1]
                    wIndex += 1
                    nextWord2 = gl2[wIndex]
                    
                    if nextWord1 == nextWord2:
                        lengthTemp += 1
                        resultTemp.append(nextWord1)
                    else:
                        cond = False
                        if lengthTemp > length:
                            length = lengthTemp
                            result = resultTemp
                else:
                    cond = False
                    if lengthTemp > length:
                        length = lengthTemp
                        result = resultTemp
    
    return result
            

def score(gloss1, gloss2):
    """Calculates the score of the given pair of glosses.\n
    1. Compute the longest overlap between the glosses \n
    2. 

    Arguments:
        gloss1 (str) -- first gloss

        gloss2 (str) -- second gloss

    Returns:
        int type -- the score of the pair of glosses
    """
    
    maxOverlap = overlap(gloss1, gloss2)
    
    