def main():
    book_path = "books/frankenstein.txt"
    txt = get_file_text(book_path)
    print(f"Word Count: {get_words_count(txt)}")
    print(f"Char dict: {get_chars_count(txt)}")

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(txt):
    return len(txt.split())

def get_chars_count(txt):
    lower_txt = txt.lower()
    chars = {}
    for i in range(0,len(lower_txt)):
        count = chars.get(lower_txt[i]) or 0
        chars[lower_txt[i]] = count + 1
    return chars

main()