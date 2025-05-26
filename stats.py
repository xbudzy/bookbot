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



def sort_on(dict):
    return dict["num"]

# sorted list of dictionaries

def sorted_dicts(char_counts):
    list_of_dicts = [{"char": char, "num": count} for (char, count) in char_counts.items()] 
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts 
    