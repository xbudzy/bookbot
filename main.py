# get book text function and return it as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text_content):
    return len(text_content.split())



def main():

    book_text = get_book_text("/home/jakub/workspace/github.com/xbudzy/bookbot/books/frankenstein.txt")

    word_count = count_words(book_text)

    print(f"{word_count} words found in the document")



main()

    



    