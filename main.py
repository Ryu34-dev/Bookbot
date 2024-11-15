import re

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase for accurate word counting
    text = re.sub(r'[^\w\s]', '', text).lower()

    words = text.split()
    return len(words)

def characters(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()

    char_counts = {}
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def main():
    file_path = "/home/ryu34/workspace/github.com/Ryu34-dev/Bookbot/Books/frankenstein.txt"
    word_count = count_words(file_path)
    character_count = characters(file_path)

    print(f"The book contains {word_count} words.")

    for char, count in sorted(character_count.items()):
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times.")

if __name__ == "__main__":
    main()