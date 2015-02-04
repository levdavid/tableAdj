from nltk.corpus import wordnet as wn


def SynonymChecker(word1, word2):
        a = wn.synsets(word1, pos=wn.VERB)[0]
        b = wn.synsets(word2, pos=wn.VERB)[0]
        print a.lch_similarity(b)
print SynonymChecker('wash', 'talk')
