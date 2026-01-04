import sys
def main():
    if len(sys.argv) == 2 :
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    characters = character_count(text)
    dictionary_list = listed_dicts(characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in dictionary_list:
        if entry["char"].isalpha() == False:
            pass
        else:
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_num_words, character_count, listed_dicts

main()
