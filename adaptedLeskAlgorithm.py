"""
Created on Tue Mar 13 18:16:11 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as wTok
from functools import reduce

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
    
    result = ''
    length = 0
    
    for i in range(len(gl1)):
        resultTemp = []
        lengthTemp = 0
        
        if gl1[i] in gl2:
            indices = [idx for idx, j in enumerate(gl2) if j == gl1[i]]
            
            for index in indices:
                iCopy = i
                lengthTemp = 1
                resultTemp = [gl1[i]]
                
                cond = True
                
                while cond:
                    if iCopy + 1 < len(gl1) and index + 1 < len(gl2):
                        iCopy += 1
                        nextWord1 = gl1[iCopy]
                        index += 1
                        nextWord2 = gl2[index]
                        
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
    """Calculates the score of the given pair of glosses using the following
    algorithm:\n
    1. Compute the longest overlap between the glosses \n
    2. Add the square of the length of the overlap to the total score \n
    3. Replace the longest overlap with markers in both glosses \n
    4. Repeat from step 1 until there are no overlaps between the glosses

    Arguments:
        gloss1 (str) -- first gloss

        gloss2 (str) -- second gloss

    Returns:
        int type -- the score of the pair of glosses
        
    Example:
        score('The house is full of rabbits and snakes', 'My house is overriden
        by rabbits and snakes') = 13
    """
    
    score = 0
    
    maxOverlap = overlap(gloss1, gloss2)
    score += len(maxOverlap)**2
    
    while maxOverlap != '':
        maxOverlapString = reduce(lambda a, b: a + ' ' + b, maxOverlap, '')[1:]
        gloss1 = gloss1.replace(maxOverlapString, '*')
        gloss2 = gloss2.replace(maxOverlapString, '/')
        
        maxOverlap = overlap(gloss1, gloss2)
        score += len(maxOverlap)**2
    
    return score
    
#print(overlap("ana are mere multe", "ana vrea sa aiba mere multe dar ana are mere multe"))

#print(score("ana are mere multe", "ana vrea sa aiba mere multe dar ana are mere multe"))

print(score('The house is full of rabbits and snakes', 'My house is overriden by rabbits and snakes'))