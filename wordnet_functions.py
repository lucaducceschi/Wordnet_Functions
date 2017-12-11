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



