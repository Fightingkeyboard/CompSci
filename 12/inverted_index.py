import csv 

def LetterOnlyString(text):
	s = ''
	for w in text.split():
		w = w.lower()
		word = ''
		for x in w:
			if x.isalpha():
				word += x
		if word != '':
			s += word
	return s

def CsvDict(filename):
	l=[]
	f = open(filename, encoding = 'UTF-8')
	csv_dict_reader = csv.DictReader(f)
	for line in csv_dict_reader:
		l.append(line)
	f.close()
	return l[:-1]

def WhoSaidWhatDict(dict):
	result = {}
	for column in dict:
		for LastStatements in column['Last Statement'].split():
			result.setdefault(LetterOnlyString(LastStatements),[])
			LastStatement = LetterOnlyString(LastStatements)
			if column['TDCJ Number'] not in result[LastStatement]:
				result[LastStatement].append(column['TDCJ Number'])
	return result

def WhoSaidThat(string):
	string = string.lower()
	d = WhoSaidWhatDict(CsvDict('offenders-clean.csv'))
	if (string in d):
		return(d[string])
	else:
		return 'no matches'

print ('TDCJ Numbers of people who said sorry')
print (str(WhoSaidThat('sorry')))
print ('TDCJ Numbers of people who said thanks')
print (str(WhoSaidThat('thanks')))
print ('TDCJ Numbers of people who said bamboozle')
print (str(WhoSaidThat('bamboozle')))
print ('TDCJ Numbers of people who said Jesus')
print (str(WhoSaidThat('Jesus')))