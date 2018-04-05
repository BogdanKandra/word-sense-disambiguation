"""
Created on Tue Mar 27 13:31:52 2018

@author: Bogdan
"""

from nltk.corpus import senseval
from adaptedLeskAlgorithm import adapted_lesk as alesk
import wsd_utils as utils
import sys

def senseval_test_adapted_lesk(corpus=None):
    """
    Tests the Adapted Lesk Algorithm against the Senseval-2 corpus.
    
    Arguments:
        corpus (str) -- one of the corpora contained in Senseval-2
    
    Returns:
        float type -- the percentage of correct results
        
        0 -- if the argument provided is not 'line', 'hard', 'serve' or 'interest'
    """
    if corpus in ['line', 'hard', 'serve', 'interest']:
        instances = senseval.instances(corpus + '.pos')
        total_cases = 0
        correct_cases = 0
        
        for instance in instances:
            total_cases += 1
            context = utils.get_context(instance)
            sense = alesk(corpus, context)
            if utils.WORDNET_SENSEVAL_DICT.get(sense.name()) is not None:
                if utils.WORDNET_SENSEVAL_DICT[sense.name()] == instance.senses[0]:
                    correct_cases += 1
                    print(correct_cases, "out of", total_cases, " (correct)")
                else:
                    print(correct_cases, "out of", total_cases, " (incorrect) - Got ", sense.name(), 'correct was ', instance.senses[0])
            else:
                print(correct_cases, "out of", total_cases, " (not found) - ", sense.name())
        
        return correct_cases / total_cases
    else:
        return 0

print(senseval_test_adapted_lesk('line'))
#print(sys.path)