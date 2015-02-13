from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
import xlrd
from xlwt import Workbook

def synonym_Checker(word1, word2):
        """Checks if word1 and word2 and synonyms. Returns True if they are, otherwise False"""
        syn1 = wn.synsets(word1, pos=wn.VERB)
        syn2 = wn.synsets(word2, pos=wn.VERB)
        for a in syn1:
                for b in syn2:
                        if (a.lch_similarity(b) > 1.8):
                                return a.lch_similarity(b)
       	return 0

def get_verbs(sentence):
        #we tokenize the verbs in each sentence
        tokens = word_tokenize(sentence)
        tags = pos_tag(tokens)
        verbs = [e1 for (e1,e2) in tags if e2 == 'VBG']
        
        return verbs

def iterate(filename):
        #we open a given excel file and iterate through it's first col
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        newBook = Workbook()
        newSheet = newBook.add_sheet('Processed verbs')
        for row in range(sheet.nrows):
                verbs = get_verbs(sheet.cell(row,0).value)
                newSheet.write(row,0,verbs)
        newBook.save('verbs.xls')
        
#def syn(word1, word2):
        #we will need to get the synsets of each word.
        
   #     return word1.res_similarity(word2, brown_ic)

def main():
        print synonym_Checker('smoking','acting')
        
	iterate('myfile.xlsx')
        
if __name__ == "__main__":
        main()
