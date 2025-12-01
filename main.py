from stats import count_words, count_characters

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    print(f"Found {num_words} total words")
    print("Character counts:")
    print(char_counts)
    
if __name__ == "__main__":
    main()