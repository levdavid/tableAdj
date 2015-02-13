import xlrd
from xlwt import Workbook

def iterate(filename):
        #we open a given excel file and iterate through it's first col
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        newBook = Workbook()
        newSheet = newBook.add_sheet('new table')
	counter = 0
        for row in range(1,sheet.nrows):
		flag = False
        	if((sheet.cell(row, 4).value!='None') & (sheet.cell(row, 4).value!=0)&(sheet.cell(row, 4).value!='')):
			for col in range(5):
				if((sheet.cell(row-1, 4).value=='None')|(sheet.cell(row-1,4).value==0)):
					newSheet.write(counter,col, sheet.cell(row-1,col).value)
					newSheet.write(counter+1,col, sheet.cell(row,col).value)
					flag = True
				else:
					newSheet.write(counter,col, sheet.cell(row,col).value)
			if(flag):
				counter = counter + 2
			else:
				counter = counter + 1
	newBook.save('adjusted.xls')

def main():

        iterate('myfile.xlsx')

if __name__ == "__main__":
        main()
                
