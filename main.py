from stats import word_count, num_characters # Refactored project by importing word_count function into stats.py.

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read() # defines a function that, when given a file path, will open the file and read all of its text

# def word_count(text):
	# words = text.split()
	# return len(words) # defines a function that takes some text, splits it into individual words, and counts how many words there are.

def main():
	filepath = 'books/frankenstein.txt'
	book_contents = get_book_text(filepath)
	num_words = word_count(book_contents)
	chara_count = num_characters(book_contents)
	print(f"{num_words} words found in the document")
	print(f"{chara_count}") # decides which file to look at (books/frankenstein), reads in all the text from that file, counts the number of words, and prints out a message saying how many words it found.

if __name__ == "__main__":
	main() # If you run this file directly, go ahead and run the main function.
# 1) main() gets called when you run the script. 2) Inside main(), it calls get_book_text(filepath), sending in the filename to read. 3) In get_book_text, the with block opens the file and reads all its content. The with block ensures the file is properly opened and then closed after reading, even if an error occurs. 4) The text read from the file is then returned by get_book_text back to main(). 5) Now main() has the contents of the file and can continue its work (counting words, printing the result).
# main() never directly interacts with the with block -- instead it calls another function (get_book_text) which handles file opening and closing safely inside the with block. 


