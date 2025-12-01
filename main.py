from stats import count_words, count_characters, sort_character_counts

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_character_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        char = entry["char"]
        count = entry["num"]
        print(f"{char}: {count}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()