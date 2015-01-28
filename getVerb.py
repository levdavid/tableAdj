from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import xlrd
from xlwt import Workbook
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
        
def syn(word1, word2):
        #we will need to get the synsets of each word.
        
        return word1.res_similarity(word2, brown_ic)

def main():
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        print syn('cleaning','washing')
        #iterate('myfile.xlsx')
        
if __name__ == "__main__":
        main()
