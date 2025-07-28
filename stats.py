def word_count(text):
        words = text.split()
        return len(words)

def num_characters(text):
	lowercase_text = text.lower() # takes input text and calls its .lower() method. Returns a new string where all characters are converted to lowercase equivalents. 
	chara_dict = {} # initializes an empty dictionary named chara_dict. Keys of this dictionary are the individual characters, and the values will be the number of times each character appears in the lowercase_text. 
	for chara in lowercase_text: # begins a for loop that iterates over each individual chara in the lowercase_text string. In each iteration, chara will hold one character from the string until all characters have been processed.
		chara_dict[chara] = chara_dict.get(chara, 0) + 1 # core of the counting logic. chara_dict[chara] = : This part is assigning a new value to the key chara in the chara_dict. If chara doesn't exist as a key yet, it will be created. If it does exist, its current value will be overwritten. | chara_dict.get(chara, 0): The get() method is called on the chara_dict. It tries to retrieve the value associated with the chara key. If chara is found as a key in chara_dict, get() returns its current value. If chara is not found as a key in chara_dict (it's the first time we've encountered this character), get() returns the default_value provided as the second argument, which is 0 in this case. ... + 1: Whatever value chara_dict.get(chara, 0) returns (either the current count or 0, we add 1 to it. Increments the count for the character. For a new character, get() returns 0, we add 1, and chara_dict[chara] becomes 1. For an existing character, get() returns its current count, we add 1, and chara_dict[chara] is updated to the new incremented count. 
	return chara_dict # after the loop has finished processing all characters in lowercase_text, this line returns the chara_dict. The dictionary now contains a complete count of each unique character in the original input string. 

def sort_on(char):
	return char["num"]

def dict_list(chara_dict):
	character_count = []
	for char in chara_dict:
		num = chara_dict[char]
		if char.isalpha():
			character_count.append({"char": char, "num": num})
	character_count.sort(reverse=True, key=sort_on)
	return character_count
# dictionary.get() function.
# Syntax: dictionary.get(key, default_value). Key = key whose value you want to retrieve. default_value = (optional) the value to return if the key is not found in the dictionary. If this argument is omitted and the key is not found, get() will return None.

# Alternative approach:
# def num_characters(text):
# lowercase_text = text.lower()
# chara_dict = {}
# for chara in lowercase_text:
# 	if chara in chara_dict:
# 		chara_dict[chara] += 1
# 	else:
# 		chara_dict[chara] = 1
# return chara_dict
#
# += is an augmented assignment operator. Shorthand for "take the current value of the variable, add something to it, and then assign the result back to the same variable."
# = is the basic assignment operator. "Assign the value on the right-hand side to the variable on the left-hand side.
