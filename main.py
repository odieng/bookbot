from stats import count_words, count_characters
import sys
def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        #file_path = './books/frankenstein.txt'
        text = get_book_text(file_path)
        words, num_words = count_words(text)
        count_char = count_characters(words)
        print("==============BOOKBOT===============")
        print(f"Analyzing book found at {file_path}")
        print("--------------word Count--------------")
        print(f"Found {num_words} total words")
        print("--------------Character Count--------------")
        for char, count in count_char.items():
            print(f"{char}: {count}")
        #words, num_words = count_words(text)
        #print(f"{num_words} words found in the document")
if __name__ == "__main__":
    main()