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
        not_found = 0
        
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
                not_found += 1
                file_notFound = open("notFound.txt", "a")
                file_notFound.write(sense.name() + '\n')
                file_notFound.close()
                
            file_results = open("results.txt", "a")
            line_write = "correct: " + str(correct_cases) + "; incorrect: " + str(total_cases - correct_cases) + "; not found: " + str(not_found) + '\n'
            file_results.write(line_write)
            file_results.close()
        
        return correct_cases / total_cases
    else:
        return 0

print(senseval_test_adapted_lesk('line'))
#print(sys.path)
