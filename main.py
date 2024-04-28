def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters_in_book(book_text):

    text_as_lower = book_text.lower()
    out_counted_letters = dict()
    for letter in text_as_lower:
        if letter in out_counted_letters:
            out_counted_letters[letter] += 1
        else:
            out_counted_letters[letter] = 1
        
    return out_counted_letters


def read_book_and_return(book_name):
    file_contents = ""
    full_path_to_book = "books/" + book_name
    with open(full_path_to_book) as f:
        file_contents = f.read()
    
    return file_contents

def sort_letters_by_num(dict):
    return dict["num"]

def create_report_of_book(book_name):
    book_content = read_book_and_return(book_name)
    num_words = get_num_words(book_content)
    counted_letters = count_letters_in_book(book_content)

    list_of_letters = []
    for letter in counted_letters:
        list_of_letters.append({"name": letter, "num": counted_letters[letter]})

    list_of_letters.sort(reverse=True, key=sort_letters_by_num)

    print(f"--- Begin report of books/{book_name} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for letter_dict in list_of_letters:
        letter = letter_dict['name']
        if not letter.isalpha(): 
            continue
        print(f"The '{letter}' character was found {letter_dict['num']} times")
    print("--- End report ---")

create_report_of_book("frankenstein.txt")