import re 
import nltk
from nltk.tokenize import word_tokenize
import sys

def cmaStopWord(text):
	"""To search and filter out stop words"""
	
def wOpenFile(filename):
	f = open('C:/Users/wkeil/Desktop/qafastamalti/qafasTaMalti/ilsien_sannaja/' + filename
	 + '.txt', 'r')
	text = f.read()
	f.close()
	# tokens = word_tokenize(text)
	# words = [w.lower() for w in tokens]
	# vocab = sorted(set(words))
	#text1 = text.split()
	#abstracts = nltk.Text(text1) #attach NLTK funcc
	# return set(vocab)
	return text

def openfile():
	#takes the result from annotator and adds it to a file
	nameOfText = raw_input("Enter the name of the file to tag (no ext): ")
	directory = '//home/linguistlovepc/Documents/PythonProjects/maltese_nlp_app/kongugator_ta_feghel/qafasTaMalti/ilsien_sannaja/training_data/'
	text = open(directory + nameOfText + '.txt','rU')
	rtext = text.read()
	tokens = nltk.word_tokenize(rtext)
	#text = nltk.Text(tokens)

	return text

def cmaPresVerb(text):
	"""To find possible present and progressive verbs"""
	allVerbs = []

	matches = re.findall(r'\b\spi[a-zA-Z]+|\spk[a-zA-Z]+', text, re.I)
	for match in matches:
		allVerbs.append(match)
	return allVerbs

def cmaPronoun(text):
	"""To search for any pronouns in a CMA text"""
	pronouns = []

	matches = re.findall(r'\bana|\sint|\snaxni|\sintou|\sinti|\sinnen|\souo|\sie', text, re.I)
	for match in matches:
		pronouns.append(match)
	return pronouns

def annotator(text):
	processedText = text.split()
	annotatedText = []
	"""annotator needs to tag the punc marks seperate from the words"""

	"ask the user what p.o.s a word is, for every word in the text"
	for word in processedText:
		word_pos = raw_input("Insert the POS of the word " + word + ": ")
		if word:
			annotatedText.append(word + "/" + word_pos)
		
	annotatedText = str(annotatedText)
	annotatedText = annotatedText.lower().encode('utf-8')
	#this needs to be joined before list conversion #annotatedText = list(annotatedText)

	nameOfFile = raw_input("Which file is this to be placed in? ")

	filename = open('//home/linguistlovepc/Desktop/lingApps/qafasTaMalti/ilsien_sannaja/training_data/' + nameOfFile + '.txt','a')
	filename.write(annotatedText)

	print(filename)
	return annotatedText

	"take the input from the user and add a '/' between the pos and the word"

	"""punctuation may be a problem, how to deal with seperating words from punctuation
	and tag them as a punc mark"""