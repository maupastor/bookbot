def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    print(f"Word Count: {get_words_count(text)}")

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(text):
    return len(text.split())

main()