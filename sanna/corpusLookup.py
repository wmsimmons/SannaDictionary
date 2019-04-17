from imp import reload
from nltk import * 
from nltk.text import Text
from nltk.tokenize import word_tokenize
import sys


 
def get_concordance(target_word, tar_passage, left_margin = 10, right_margin = 10):
	"""
	Function to get all the phases that contain the target word in a text/passage tar_passage.
	Workaround to save the output given by nltk Concordance function
	 
	str target_word, str tar_passage int left_margin int right_margin --> list of str
	left_margin and right_margin allocate the number of words/pununciation before and after target word
	Left margin will take note of the beginning of the text
	"""
	# check for punkt tokenizer
	if nltk.download('punkt') == False:
		nltk.download('punkt')

	## Create list of tokens using nltk function
	tokens = word_tokenize(tar_passage)

	## Create the text of tokens
	text = Text(tokens)

	## Collect all the index or offset position of the target word
	c = ConcordanceIndex(text.tokens, key = lambda s: s.lower())

	## Collect the range of the words that is within the target word by using text.tokens[start;end].
	## The map function is use so that when the offset position - the target range < 0, it will be default to zero
	concordance_txt = ([text.tokens[list(map(lambda x: x-5 if (x-left_margin) > 0 else 0, [offset]))[0]: offset + right_margin]
	                for offset in c.offsets(target_word)])
	                 
	## join the sentences for each of the target phrase and return it
	return [' '.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]
