# get book text function and return it as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

#import the counting function from stats.py
from stats import count_words


#import character counting function from stats.py
from stats import count_characters

#print word count in a book
def main():

    book_text = get_book_text("/home/jakub/workspace/github.com/xbudzy/bookbot/books/frankenstein.txt")

    word_count = count_words(book_text)

    counted_characters = count_characters(book_text)

    print(f"{word_count} words found in the document")
    print(counted_characters)



main()

    



    