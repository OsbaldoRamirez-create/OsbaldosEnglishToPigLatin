# OsbaldosEnglishToPigLatin
Implement a Python-based English text to Pig-Latin converter. The implementation should read in this text file, data.txt Download data.txt, and create a Pig-Latinized output text called out.txt. 
The converter must implement the following Pig-Latin rules:

1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay."
Example: Happy = appyh + ay = appyhay

2. If a word starts with two consonants move the two consonants to the end of the word and add "ay."
Example: Child = Ildch + ay = Ildchay

3. If a word starts with a vowel add the word "way" at the end of the word.
Example: Awesome = Awesome +way = Awesomeway

4. The output file must retain all of the punctuation used in the input text file, including whitespace, quotation marks, periods, and newlines. 
