import argparse
import re

def arguments():
	"""
	Get input and output files from command line
	"""
	parser = argparse.ArgumentParser(description = 'English to PigLatin')
	parser.add_argument('--input', type = str, help = 'Input text file', required = True)	
	parser.add_argument('--output',type = str, help = 'Output text file', required = True)
	return parser.parse_args()
	
def hasVowel(char):
	"""
	stores all the vowels into vowels
	"""
	vowels = 'aeiouAEIOU'
	return char in vowels

def pigLatin(word):
		
	if hasVowel(word[0]):
		return word + 'way'
		
	elif len(word)>=2 and not hasVowel(word[0]) and not hasVowel(word[1]):
		return word[2:] + word[:2] +'ay'
		
	else:
		return word[1:] + word[0] +'ay'

def main():

	"""
	main function to run
	"""
	args = arguments()
	input_file = args.input
	output_file = args.output
	"""
	open file and read and store into text
	"""
	with open(input_file,'r') as f:
		text = f.read()
	"""
	find any spaces in file to keep same for output file
	"""
	words = re.findall(r'\w+|\s+',text)
	
	pigLatinWords = [pigLatin(word) if word.isalnum() else word for word in words]

	pigLatinText = ''.join(pigLatinWords)

	with open(output_file, 'w') as f:
		f.write(pigLatinText)
	
if __name__ == '__main__':
	main()

