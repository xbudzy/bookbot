#function that counts words in text of the book

def count_words(text_content):
    return len(text_content.split())


#function that takes text as a string returns number of times each character used

def count_characters(booktext):
    character_count = dict()
    booktext = booktext.lower()

    for text in booktext:
        if text not in character_count:
            character_count[text] = 1

        else:
            character_count[text] += 1



    return character_count






