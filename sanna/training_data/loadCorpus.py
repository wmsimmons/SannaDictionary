import nltk
from nltk.corpus import PlaintextCorpusReader

def load_corpus():
	corpus_root = '/home/linguistlovepc/Documents/PythonProjects/maltese_nlp_app/kongugator_ta_feghel/qafasTaMalti/maltese_training_data/'
	wordlists = PlaintextCorpusReader(corpus_root, '.*')
	print(wordlists.fileids())
	return wordlists

#wordlists.words(any_work)

def open_mt_file(filename):
	f = open('C:/Users/wkeil/Desktop/qafastamalti/qafasTaMalti/ilsien_sannaja/' + filename
	 + '.txt', 'r')
	text = f.read().decode('utf-8')
	tokens = word_tokenize(text)
	words = [w.lower() for w in tokens]
	vocab = sorted(set(words))
	#text1 = text.split()
	#abstracts = nltk.Text(text1) #attach NLTK func
	return vocab

def open(filename):
	f = open('/home/linguistlovepc/Documents/PythonProjects/maltese_nlp_app/kongugator_ta_feghel/qafasTaMalti/nltkbook/' + filename
	 + '.txt', 'r')
	text = f.read().decode('utf-8')
	#text1 = text.split()
	abstracts = nltk.Text(text1) #attach NLTK func
	return abstracts


'''#wordlists.words(any_work)
#f=open('/home/linguistlovepc/nltk_data/corpora/maltese/ProverbjiBilMalti.txt', 'rU')
#text=f.read()
#text1=text.split()
#abstracts=nltk.Text(text1) #attach NLTK func'''

#/home/linguistlovepc/Documents/PythonProjects/maltese_nlp_app/maltese_training_data/
