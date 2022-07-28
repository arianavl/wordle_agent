__author__ = "<your name>"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "<your e-mail>"

# first start with a good word - most used letters in alphabet
# Go a step further and go with most common letters in that row
import helper
from collections import Counter


def count_occurrences(diction, word_length):
	"""
	A method that counts the occurrences of letters at an index and
	returns that information
	:param diction: The current list of words/precepts
	:param word_length: the length of the word
	:return: the next word
	"""

	count = {}

	for i in range(word_length):
		count[i] = {}
		for word in diction:
			if word[i] not in count[i]:
				count[i][word[i]] = 1
			else:
				count[i][word[i]] += 1

	print(count[0])
	return count


def revise_dict(diction, letter_indices, letter_states):
	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
	last_word = helper.letter_indices_to_word(letter_indices, letters)
	count = Counter(last_word)
	# print(count)
	print(last_word)
	print("letter_states: " + str(letter_states))

	if last_word in diction:
		print("last_word: " + last_word)
		diction.remove(last_word)

	invalid_letters = ""
	for i in range(len(letter_states)):
		if letter_states[i] == 0 and count[letters[letter_indices[i]]] > 1:
			if letters[letter_indices[i]] not in invalid_letters:  # if it is not an already found wrong letter
				invalid_letters += letters[letter_indices[i]]
				print("invalid_letter: " + invalid_letters)

	wrong_word_list = []
	for word in diction:
		# print(word)
		for letter in invalid_letters:
			if letter in word:
				if word not in wrong_word_list:
					wrong_word_list.append(word)

	for word in wrong_word_list:
		print("word being removed: " + word)
		diction.remove(word)
	return diction


class WordleAgent():
	"""
       A class that encapsulates the code dictating the
       behaviour of the Wordle playing agent

       ...

       Attributes
       ----------
       dictionary : list
           a list of valid words for the game
       letter : list
           a list containing valid characters in the game
       word_length : int
           the number of letters per guess word
       num_guesses : int
           the max. number of guesses per game
       mode: str
           indicates whether the game is played in 'easy' or 'hard' mode

       Methods
       -------
       AgentFunction(percepts)
           Returns the next word guess given state of the game in percepts
       """

	def __init__(self, dictionary, letters, word_length, num_guesses, mode):
		"""
    		:param dictionary: a list of valid words for the game
    		:param letters: a list containing valid characters in the game
    		:param word_length: the number of letters per guess word
    		:param num_guesses: the max. number of guesses per game
    		:param mode: indicates whether the game is played in 'easy' or 'hard' mode
    	"""

		self.dictionary = dictionary
		self.letters = letters
		self.word_length = word_length
		self.num_guesses = num_guesses
		self.mode = mode

	def AgentFunction(self, percepts):
		"""
		Returns the next word guess given state of the game in percepts

    	:param percepts: a tuple of three items: guess_counter, letter_indexes, and letter_states;
               guess_counter is an integer indicating which guess this is, starting with 0 for initial guess;
               letter_indexes is a list of indexes of letters from self.letters corresponding to
                           the previous guess, a list of -1's on guess 0;
               letter_states is a list of the same length as letter_indexes, providing feedback about the
                           previous guess (conveyed through letter indexes) with values of 0 (the corresponding
                           letter was not found in the solution), -1 (the correspond letter is found in the
                           solution, but not in that spot), 1 (the corresponding letter is found in the solution
                           in that spot).
		:return: string - a word from self.dictionary that is the next guess
		"""

		# This is how you extract three different parts of percepts.
		guess_counter, letter_indexes, letter_states = percepts

		# letter_indexes e.g. abcde = [0,1,2,3,4]

        # Here's where you should put in your code
        # .
        # .
        # .

		# print(letter_indexes)

		occurrences = count_occurrences(self.dictionary, self.word_length)

		if guess_counter == 0:
			next_guess = self.dictionary[1]
		else:
			self.dictionary = revise_dict(self.dictionary, letter_indexes, letter_states)
			next_guess = self.dictionary[0]

		# Currently this agent always returns the first word from the dictionary-probably
        # a good idea to replace this with a better guess based on your code above.
        # return self.dictionary[0]
		return next_guess