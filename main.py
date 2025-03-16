from stats import *
from sys   import *



def main():
    if(len(argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path = argv[1]




    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_word_count(path))
    chars = get_char_count(path)
    sorted_chars = get_char_count_sorted(chars)
    
    print()

main()
