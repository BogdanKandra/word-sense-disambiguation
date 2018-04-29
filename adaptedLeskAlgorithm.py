"""
Created on Tue Mar 13 18:16:11 2018

@author: Bogdan
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize as w_tok
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import wsd_utils as utils

def overlap(gloss1, gloss2):
    """Determines the longest sequence of common words between two **glosses**.
    
    Arguments:
        *gloss1* (str) -- first gloss

        *gloss2* (str) -- second gloss
    
    Returns:
        list(str) type -- the longest sequence of common words, as a list
        
    Examples:
        overlap('The house is full of rabbits and snakes', 
        'My house is overriden by rabbits and snakes') = ['rabbits', 'and', 'snakes']\n
        overlap('ghost player', 'baseball superstar') = []
    """

    gl1 = w_tok(gloss1)
    gl2 = w_tok(gloss2)
    
    result = []
    length = 0
    
    for i in range(len(gl1)):
        resultTemp = []
        lengthTemp = 0
        
        if gl1[i] in gl2:
            # The current word is also in gloss2, take the indices of their occurences
            indices = [idx for idx, word in enumerate(gl2) if word == gl1[i]]
            
            for index in indices: # For each occurence
                iCopy = i
                resultTemp = [gl1[i]]
                lengthTemp = 1
                
                cond = True
                
                while cond:  # Check how many consecutive words match
                    if iCopy + 1 < len(gl1) and index + 1 < len(gl2):
                        iCopy += 1
                        index += 1
                        nextWord1 = gl1[iCopy]
                        nextWord2 = gl2[index]
                        
                        if nextWord1 == nextWord2:
                            lengthTemp += 1
                            resultTemp.append(nextWord1)
                        else:
                            cond = False
                            if lengthTemp > length:
                                result = resultTemp
                                length = lengthTemp
                    else:  # We have reached the end of one of the glosses
                        cond = False
                        if lengthTemp > length:
                            result = resultTemp
                            length = lengthTemp
        
    return result

def score(gloss1, gloss2):
    """Calculates the score of the given pair of **glosses** using the
    following algorithm:\n
    1. Compute the longest overlap between the glosses \n
    2. Add the square of the length of the overlap to the total score \n
    3. Replace the longest overlap with markers in both glosses \n
    4. Repeat from step 1 until there are no overlaps between the glosses

    Arguments:
        *gloss1* (str) -- first gloss

        *gloss2* (str) -- second gloss

    Returns:
        int type -- the score of the pair of glosses

    Examples:
        score('The house is full of rabbits and snakes', 'My house is overriden
        by rabbits and snakes') = 13 (= 9 + 4)\n
        score('ghost player', 'baseball superstar') = 0
    """
    
    score = 0
    maxOverlap = ['.']
    
    gl1 = w_tok(gloss1)
    gl2 = w_tok(gloss2)
    
    gl1 = [w for w in gl1 if w not in utils.STOPWORDS]
    gl2 = [w for w in gl2 if w not in utils.STOPWORDS]
    
    gloss1 = ' '.join(gl1)
    gloss2 = ' '.join(gl2)
    
    while maxOverlap != []:
        maxOverlap = overlap(gloss1, gloss2)
        score += len(maxOverlap)**2

        maxOverlapString = ' '.join(maxOverlap)
        gloss1 = gloss1.replace(maxOverlapString, '*')
        gloss2 = gloss2.replace(maxOverlapString, '/')
        
    return score

def similarity(synset1, synset2):
    """Calculates the similarity score between two Synsets by summing the
    scores between two glosses (using the *score* procedure) obtained by applying
    all relations in RELPAIRS over the synsets.
    
    Arguments:
        synset1 (Synset) -- first Synset
        
        synset2 (Synset) -- second Synset
        
    Returns:
        int type -- the overall similarity score
    """
    
    totalScore = 0
    
    for (r1, r2) in utils.RELPAIRS:
        if r1 == 'gloss':
            synset1gloss = synset1.definition() + ' '
        elif r1 == 'hyponyms':
            synset1gloss = ''
            for hypo in synset1.hyponyms():
                synset1gloss += hypo.definition() + ' '
        elif r1 == 'hypernyms':
            synset1gloss = ''
            for hyper in synset1.hypernyms():
                synset1gloss += hyper.definition() + ' '
                
        syn1examples = ' '.join(synset1.examples())
        if syn1examples != '':
            synset1gloss += syn1examples
        
        if r2 == 'gloss':
            synset2gloss = synset2.definition()
        elif r2 == 'hyponyms':
            synset2gloss = ''
            for hypo in synset2.hyponyms():
                synset2gloss += hypo.definition() + ' '
        elif r2 == 'hypernyms':
            synset2gloss = ''
            for hyper in synset2.hypernyms():
                synset2gloss += hyper.definition() + ' '
        
        syn2examples = ' '.join(synset2.examples())
        if syn2examples != '':
            synset2gloss += syn2examples
        
        totalScore += score(synset1gloss, synset2gloss)
    
    return totalScore

def adapted_lesk(word, sentence, context_window_size = 3):

    # Tokenize input sentence, remove punctuation and stopwords
    sentence = utils.remove_stopwords(utils.remove_punctuation(w_tok(sentence)))

    # Perform lemmatization on sentence
    lemmatizer = WordNetLemmatizer()
    tagged_sentence = pos_tag(sentence)
    
    sentence = [lemmatizer.lemmatize(tup[0], utils.get_wordnet_pos(tup[1])) 
                for tup in tagged_sentence]
    
    # Perform lemmatization on target word
    tagged_word = pos_tag(word)
    word = lemmatizer.lemmatize(tagged_word[0], utils.get_wordnet_pos(tagged_word[1]))
    
    # Extract the context window from the sentence
    if word in sentence:
        word_index = sentence.index(word)
        if word_index - context_window_size < 0:
            window_words = sentence[0 : word_index + context_window_size + 1]
        else:
            window_words = sentence[word_index - context_window_size : 
                                    word_index + context_window_size + 1]
    
        # Take the Synsets of the target word
        senses = wn.synsets(word)
        best_sense = senses[0]
        best_score = 0
        
        for sense in senses:
            score = 0
    
            for w in window_words:
                if w != word:
                    w_senses = wn.synsets(w)
    
                    for w_sense in w_senses:
                        score += similarity(sense, w_sense)
    
            if score > best_score:
                best_score = score
                best_sense = sense
    else:  # If target word is not in context, after lemmatizing, return first wordnet sense
        print('guessed:')
        return wn.synsets(word)[0]
    
    print('computed:')
    return best_sense

    
#print(overlap("ana are mere multe", "ana vrea sa aiba mere multe dar ana are mere multe"))
#print(score("ana are mere multe", "ana vrea sa aiba mere multe dar ana are mere multe"))
#print(similarity(wn.synset('hard.r.03'), wn.synset('hard.a.02')))

#print(adapted_lesk('bank', 'The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.').definition())
#print(adapted_lesk('pine', 'pine cone').definition())
#print(adapted_lesk('bass', 'I am cooking basses').definition())

### TODO
# Check the considered RELS
# If pos tagging, I should take into consideration only relations pertaining to the pos of target words
#   and should look only to relevant pos words
# If not pos tagging, I should take into account all relations
