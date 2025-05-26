import sys

# get book text function and return it as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

#import the counting function from stats.py
from stats import count_words


#import character counting function from stats.py
from stats import count_characters

#import dictionary sorting function from stats.py
from stats import sorted_dicts

#print word count in a book
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    word_count = count_words(book_text)

    counted_characters = count_characters(book_text)

    
    print("============ BOOKBOT ============")
    print(f"Alanyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_dictionary = sorted_dicts(counted_characters)
    for entry in sorted_dictionary:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")




if __name__ == "__main__":
    main()

    



    