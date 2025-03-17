from stats import get_num_words, count_characters, sort_on
import sys 

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()    
    return content

def main(book_path):
    print(f"sys argv: {sys.argv}")
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    character_counts = count_characters(book_text)
    sort_character_count = sort_on(character_counts)
    for item in sort_character_count:
        print(f"{item['character']}: {item['count']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(book_path=sys.argv[1])