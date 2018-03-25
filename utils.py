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

SENSEVAL_WORDNET_DICT = {
    # LINE
    "cord": ["line.n.18"],          # something (as a cord or rope) that is long and thin and flexible
    "formation": ["line.n.01","line.n.03"], # a formation of people or things one beside another
    "text": ["line.n.05"],                 # text consisting of a row of words written across a page or computer screen
    "phone": ["telephone_line.n.02"],   # a telephone connection
    "product": ["line.n.22"],       # a particular kind of product or merchandise
    "division": ["line.n.29"],      # a conceptual separation or distinction
        
    # HARD
    "HARD1": ["difficult.a.01"],    # Not Easy
    "HARD2": ["hard.a.02",          # Dispassionate
              "difficult.a.01"],
    "HARD3": ["hard.a.03"],         # Resisting weight or pressure

    # SERVE
    "SERVE12": ["serve.v.02"],       # do duty or hold offices; serve in a specific function
    "SERVE10": ["serve.v.06"], # provide (usually but not necessarily food)
    "SERVE2": ["serve.v.01"],       # serve a purpose, role, or function
    "SERVE6": ["service.v.01"],      # be used by; as of a utility

    # INTEREST
    "interest_1": ["interest.n.01"], # readiness to give attention
    "interest_2": ["interest.n.03"], # quality of causing attention to be given to
    "interest_3": ["pastime.n.01"],  # activity, etc. that one gives attention to
    "interest_4": ["sake.n.01"],     # advantage, advancement or favor
    "interest_5": ["interest.n.05"], # a share in a company or business
    "interest_6": ["interest.n.04"] # money paid for the use of money
}

WORDNET_SENSEVAL_DICT = {
    # LINE
    'line.n.01' : 'formation',
    'line.n.02' : 'division',
    'line.n.03' : 'formation',
    'line.n.04' : 'division',
    'line.n.05' : 'text',
    'line.n.06' : 'division',
    'line.n.07' : 'formation',
    'cable.n.02' : 'cord',
    'course.n.02' : 'formation',
    'line.n.11' : 'division',
    'wrinkle.n.01' : 'division',
    'line.n.14' : 'division',
    'telephone_line.n.02' : 'phone',
    'line.n.16' : 'division',
    'lineage.n.01' : 'formation',
    'line.n.18' : 'cord',
    'occupation.n.01' : 'product',
    'line.n.20' : 'division',
    'channel.n.05' : 'phone',
    'line.n.22' : 'product',
    'line.n.23' : 'product',
    'agate_line.n.01' : 'text',
    'tune.n.01' : 'formation',
    'line.n.27' : 'product',
    'line.n.29' : 'division',
    'production_line.n.01' : 'formation',

    # HARD
    'difficult.a.01' : 'HARD1',
    'hard.a.02' : 'HARD2',
    'hard.a.03' : 'HARD3',
    'hard.s.04' : 'HARD3',
    'arduous.s.01' : 'HARD1',
    'unvoiced.a.01' : 'HARD2',
    'hard.a.08' : 'HARD2',
    'intemperate.s.03' : 'HARD2',
    'hard.s.10' : 'HARD2',
    'hard.s.11' : 'HARD2',
    'hard.s.12' : 'HARD3',
    
    # SERVE
    'serve.v.01' : 'SERVE2',
    'serve.v.02' : 'SERVE12',
    'serve.v.03' : 'SERVE2',
    'service.v.01' : 'SERVE6',
    'serve.v.05' : 'SERVE10',
    'serve.v.06' : 'SERVE10',
    'serve.v.07' : 'SERVE12',
    'serve.v.08' : 'SERVE12',
    'serve.v.09' : 'SERVE12',
    'serve.v.10' : 'SERVE12',
    'serve.v.11' : 'SERVE2',
    'suffice.v.01' : 'SERVE6',
    'serve.v.13' : 'SERVE12',
    'serve.v.14' : 'SERVE6',
    'serve.v.15' : 'SERVE6',    
}

def remove_punctuation(tokenList):
    result = [token for token in tokenList if token not in MARKS]
    return result
