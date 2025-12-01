def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    result = []
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result