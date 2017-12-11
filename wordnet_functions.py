import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
from nltk.corpus import stopwords

# These two functions extract the hyponyms and the hypernyms for a specific noun 

def get_hyponyms(noun):
    #print("NB: this method only returns the nominal use of the word '", noun, "'")
    list_of_synsets = nltk.corpus.wordnet.synsets(noun)

    filtered_synsets = [i for i in list_of_synsets if noun in i.unicode_repr()[8:-2] ]
    hypo = lambda s: s.hyponyms()
    var_out = [list(i.closure(hypo, depth=1)) for i in filtered_synsets]
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(filtered_synsets)
    pp.pprint(var_out)
    return var_out


def get_hypernyms(noun):
    #print("NB: this method only returns the nominal use of the word '", noun, "'")
    list_of_synsets = nltk.corpus.wordnet.synsets(noun)
    strings_of_synsets = [i.unicode_repr()[8:-2] for i in list_of_synsets if noun in i.unicode_repr()[8:-2] 
                         ]
    hyper = lambda s: s.hypernyms()
    var_out = [list(nltk.corpus.wordnet.synset(i).closure(hyper, depth=8)) for i in strings_of_synsets]
    #import pprint
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint([(i.definition(),i.unicode_repr(), i.max_depth()) for i in list_of_synsets])
    return strings_of_synsets, var_out 

# You want to do POS-tagging and lemmatizaion using NLTK in English. Well... you could use morphy, wordnet own lemmatizer,  
# but it works with a simplified tagset that is NOT the peen treebank tagset universal (of course).
# The two functions below take care of the problem (in a very naive way). 
#
# Basically, if you do:
# lemmatizer(("dogs", "NOUN"))
#
# you get:
# ('dog', 'NOUN')
#
# if you don't understand how this can be useful, go back and check what lemmatization is ;-)

# First change the penn wordnet lable to something "wordnetty". The grammatical categories are limited.
def univ_pos_changer(stringa):
    if stringa=="NOUN":
        return "n"
    elif stringa=="VERB":
        return "v"
    elif stringa=="ADJ":
        return "a"
    elif stringa=="ADV":
        return "r"
    else:
        return None

# Then take care of the lemmatization, via morphy. This assumes that you feed it a list of tuples containing ("word", "tag")

def lemmatizer(tupla):
    if wn.morphy(tupla[0], univ_pos_changer(tupla[1]))==None:
        return tupla[0], tupla[1]
    else:
        return wn.morphy(tupla[0], univ_pos_changer(tupla[1])), tupla[1]
   

# this is an example of how I used it: the function cycles through the mess of lists of lists and applies the lemmatizer
# I said it: naive.
def tag_me(corpus):
    return [[lemmatizer(x) for x in linea] for linea in corpus]

        


