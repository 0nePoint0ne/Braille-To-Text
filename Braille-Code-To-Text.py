import pandas as pd

dic = {' ': '000000','b': '101000', 'a': '100000'}


def importData():
	data = pd.read_csv("data.csv", header=None)
	values = data[0].to_string(index = False).split()
	codes = data[1].to_string(index = False).split()
	
	
	for i in range(len(values)):
		temp1 = values[i-1]
		temp2 = codes[i-1]
		dic.update({temp1: temp2})
	#print(values)
	#dic[]
	print(dic)
	print(dic['a'])
def exportData():
	codes = []
	values = []
	
	for i in dic:
		codes.append(dic[i])
		values.append(i)
	
	df = pd.DataFrame(codes, values)
	
	df.to_csv("data.csv",header=None)
	
def learnCharacter(text):#, binaryText):
	for i in range(len(text)):
		tempText = text[i-1]
		#code = binaryText[i-]
		if(dic.get(text[i-1]) == None):
			dic.update({tempText: temp2})
			
	

def main():
	importData()
	learnCharacter('test')
	exportData()
main()