import nltk
import itertools
import win32com.client as win32



def Synonym_Checker(word1, word2):
    """Checks if word1 and word2 and synonyms. Returns True if they are, otherwise False"""
    equivalence = WordNetLemmatizer()
    word1 = equivalence.lemmatize(word1)
    word2 = equivalence.lemmatize(word2)
    
    word1_synonyms = wordnet.synsets(word1)
    word2_synonyms = wordnet.synsets(word2)

    scores = [i.wup_similarity(j) for i, j in list(itertools.product(word1_synonyms, word2_synonyms))]
    max_index = scores.index(max(scores))
    best_match = (max_index/len(word1_synonyms), max_index % len(word1_synonyms)-1)

    word1_set = word1_synonyms[best_match[0]].lemma_names
    word2_set = word2_synonyms[best_match[1]].lemma_names


    match = False
    for word in word1_synonyms:
        if(word in word2_synonyms):
            match = True
            break
    #match = [match or word in word2_set for word in word1_set][0]

    return match

def excel_parse(file_path):
	wb = excel.Workbooks.Open(file_path);
	ws = wb.Worksheets("Sheet1")
	#I assumed we have a table header in the first row
	col = ws.Range("A2:A100")
	for cell in col:
		#we need to tokenize each row in the col, so we can compare the verbs
		tokens = nltk.word_tokenize(cell)
		print tokens
	return 

def main():
	excel = win32.gencache.EnsureDispatch('Excel.Application')
	excel.Visible = 1; 
	excel_parse("temp")

print main()

#print Synonym_Checker("tomato", "Lycopersicon_esculentum")