def main():
    book_path = "books/frankenstein.txt"
    print(get_file_text(book_path))

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()