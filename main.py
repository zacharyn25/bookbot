def main(book_filepath):
    book_text = get_book_text(book_filepath) 
    word_count = get_word_count(book_text)
    character_count_dictionary = get_character_dictionary(book_text) #alternative function that could be used: get_character_dictionary_1()
    generate_report(book_filepath,word_count,character_count_dictionary)

def get_book_text(book_filepath):
    #Take book filepath and read it, returning a string of the entire book
    with open(book_filepath) as book:
        return book.read()

def get_word_count(book_text):
    #Take entire book text as string and return the number of words
    words = book_text.split()
    return len(words)

def get_character_dictionary(book_text):
    #Take entire book text as string and return a dictionary with all the characters used as the key, and number of times used as the value
    lowercase_string_full_text = book_text.lower()
    word_vector = lowercase_string_full_text.split()
    character_count_dictionary = {}

    for ii in range(0,len(word_vector)):
        for character in word_vector[ii]:
            if character in character_count_dictionary:
                character_count_dictionary[character] += 1
            else:
                character_count_dictionary[character] = 1
    return character_count_dictionary

def get_character_dictionary_1(book_text):
    #Take entire book text as string and return a dictionary with all the characters used as the key, and number of times used as the value
    #More efficient version
    lowercase_string_full_text = book_text.lower()
    character_count_dictionary = {}
    
    for character in lowercase_string_full_text:
        if character in character_count_dictionary:
            character_count_dictionary[character] += 1
        else:
            character_count_dictionary[character] = 1
    return character_count_dictionary

def generate_report(book_filepath,word_count,character_count_dictionary):
    #Generate a report of the characters used in the book belonging to the alphabet
    #Sorted from most used character to least used
    print(f"--- Begin report of {book_filepath} ---")
    print(f"{word_count} words found in the document")

    character_count_dictionary_list = make_dictionary_into_list(character_count_dictionary)
    character_count_dictionary_list.sort(reverse=True, key=sort_on)

    for character_dictonary in character_count_dictionary_list:
        print(f"The {character_dictonary['character']} character was found {character_dictonary['value']} times")
    print('--- End report ---')

def make_dictionary_into_list(character_count_dictionary):
    #Make a dictionary into a list of dictionaries so that the .sort method can be used
    character_count_dictionary_list = []
    for key in character_count_dictionary:
        #Only store characters in the Alphabet
        if(key.isalpha()):
            character_count_dictionary_list.append({'character' : key, 'value': character_count_dictionary[key]})
    return character_count_dictionary_list

# A function that takes a dictionary and returns the value of the "value" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["value"]

main('books/frankenstein.txt')
