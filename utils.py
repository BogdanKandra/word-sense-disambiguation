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

SENSEVAL_SENSE_DICT = {
    "HARD1": ["difficult.a.01"],    # not easy, requiring great physical or mental
    "HARD2": ["hard.a.02",          # dispassionate
              "difficult.a.01"],
    "HARD3": ["hard.a.03"],         # resisting weight or pressure

    "interest_1": ["interest.n.01"], # readiness to give attention
    "interest_2": ["interest.n.03"], # quality of causing attention to be given to
    "interest_3": ["pastime.n.01"],  # activity, etc. that one gives attention to
    "interest_4": ["sake.n.01"],     # advantage, advancement or favor
    "interest_5": ["interest.n.05"], # a share in a company or business
    "interest_6": ["interest.n.04"], # money paid for the use of money

    "cord": ["line.n.18"],          # something (as a cord or rope) that is long and thin and flexible
    "formation": ["line.n.01","line.n.03"], # a formation of people or things one beside another
    "text": ["line.n.05"],                 # text consisting of a row of words written across a page or computer screen
    "phone": ["telephone_line.n.02"],   # a telephone connection
    "product": ["line.n.22"],       # a particular kind of product or merchandise
    "division": ["line.n.29"],      # a conceptual separation or distinction

    "SERVE12": ["serve.v.02"],       # do duty or hold offices; serve in a specific function
    "SERVE10": ["serve.v.06"], # provide (usually but not necessarily food)
    "SERVE2": ["serve.v.01"],       # serve a purpose, role, or function
    "SERVE6": ["service.v.01"]      # be used by; as of a utility
}

# TODO
SENSE_SENSEVAL_DICT = {
        
        
        
        }

def remove_punctuation(tokenList):
    result = [token for token in tokenList if token not in MARKS]
    return result
