"""
Created on Sun Mar 18 16:51:15 2018

@author: Bogdan
"""

MARKS = ['.', ',', '?', '!', ':', ';', '(', ')', '[', ']', 
         '...', '\'', '\"', "\''", '``', '--', '-', '$']

STOPWORDS = ['her', 'most', 'much', 'although', 'an', 'at', 'that', 'along', 
                  'would', 'then', 'therefore', 'when', 'or', 'two', 'through', 
                  'another', 'across', 'whose', 's', 'of', 'many', 'in', 'few', 
                  'least', 'if', 'here', 'was', 'because', 'must', 'being',
                  'something', 'should', 'than', 'me', 'for', 'since', 'against',
                  'around', 'often', 'instead', 'are', 'where', 'about', 'a', 
                  'might', 'over', "'re", 'ones', 'they', 'it', 'own', 'its', 
                  'nothing', 'besides', 'can', 'next', 'have', "'m", 'during',
                  "'d", 'toward', 'but', 'could', 'twice', 'though', 'us', 
                  'after', 'last', 'inside', 'second', 'how', 'behind', 'did',
                  'said', 'down', 'anyone', 'what', 'now', 'has', 'there', 
                  "'ll", 'sometimes', 'every', 'she', 'the', 'all', 'always', 
                  'don', 'someone', 'else', 'into', 'we', 'half', 'more', "'ve", 
                  'their', 'such', 'from', 'usually', 'while', 'your', 'first',
                  'do', 'incidentally', 'you', 'beside', 'he', 'shall', 'years',
                  'so', 'his', 'everyone', 'n', 'meanwhile', 'several', 'with',
                  'may', 'is', 'never', 'says', 'onto', 'both', "'t", "'s", 
                  'one', 'on', 'were', 'which', 'otherwise', 'my', 'within', 
                  'no', "don'", 'itself', 'had', 'anyway', 'anything', 'each',
                  'not', 'up', 'some', 'them', 'also', 'despite', 'near', 'to',
                  'this', 'who', 'any', 'off', 'before', 'will', 'been', 'other',
                  'be', 'less', 'and', 'without', 'him', 'however', 'by', 
                  'moreover', 'as', 'little', 'everything', 'say']

def remove_punctuation(tokenList):
    result = [token for token in tokenList if token not in MARKS]
    return result
