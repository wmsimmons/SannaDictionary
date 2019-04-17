"""Converts Greek letters of Cypriot Arabic to Latin letters"""
import re
from nltk.tag.util import str2tupl

"""go through the alphabet section of the CMA grammar book, copy and paste each letter
   from the custom alphabet, paste the letter directly, return the result
   put the result (latin letters) into sanna_latined_words, put sanna_latined_words into
   a file that stores all the Cypriot Arabic latinized words for linguistic study

   """

letter_to_letter = 'β/v, α/a, ε/e, ι/i, ο/o, ου/ou, θ/i, γ/y, γ/gh, δ/th, δδ/dh, ζ/z, Δ/d, τζ'
new_letters = str2tupl(letter_to_letter)

def transliterate(text):
	sanna_latined_words = []
	old_letter = [letter[0] for letter in new_letters]
	new_letter = [letter[1] for letter in new_letters]
	for word in text:
		for letter in word:
			#change the letter(the key) to the new_letter of the new_letters and add it to sanna_latined_letters
			if letter in old_letter:
				#need to replace the letter(key in new_letters tuple) to the latin one, re.sub() or something like is needed.
				letter.replace(letter, old_letter, new_letter)
		sanna_latined_words.append(word)
	sanna_latin_text = str(sanna_latined_words)
	return sanna_latin_text	
