def main():
    book_path = './books/frankenstein.txt'
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    letters_count = count_letters(book_text)
    converted_letters_count = convert_letter_instances(letters_count)
    sorted_letters_count = sort_letter_instances(converted_letters_count)
    report(book_path, word_count, sorted_letters_count)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents    
    
def count_words(string):
    word_count = len(string.split())
    return word_count

def count_letters(string):
    lowered_string = string.lower()
    letter_instances = {}
    for letter in lowered_string:
        if letter.isalpha() == False:
            continue
        elif letter in letter_instances.keys():
            letter_instances[letter] += 1
        else:
            letter_instances[letter] = 1

    return letter_instances

def convert_letter_instances(letter_instances):
    container = []
    for letter in letter_instances:
        entry = {}
        entry['letter'] = letter
        entry['instances'] = letter_instances[letter]
        container.append(entry)
    return container

def sort_letter_instances(converted_letter_instances):
    def sort_on(dict):
        return dict['instances']
    
    converted_letter_instances.sort(reverse=True, key=sort_on)
    return converted_letter_instances

def report(book_path, word_count, sorted_letter_instances):
    print(f"Begin report of {book_path}.")
    print(f"{word_count} words found in document.")
    for letter in sorted_letter_instances:
        print(f"'{letter['letter']}' was found {letter['instances']} times")
    print("End of report.")

main()