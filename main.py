def main():
    book_path = "books/frankenstein.txt"
    txt = get_file_text(book_path)
    print_report(book_path, get_total_words(txt), get_chars_count(txt))

def print_report(path, words_num, chars_count):
    print(f"--- Begin report of {path} ---")
    print(f"{words_num} words found in the document")
    print()

    chars_list = get_sorted_list_by_count(chars_count)
    for c in chars_list:
        if c["char"].isalpha():
            print(f"The '{c['char']}' character was found {c['count']} times")
    
    print("--- End report ---")

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_total_words(txt):
    return len(txt.split())

def get_chars_count(txt):
    lower_txt = txt.lower()
    chars = {}
    for c in lower_txt:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def get_sorted_list_by_count(d):
    ld = convert_to_list_of_dicts(d)
    ld.sort(reverse=True, key=sort_by_count)
    return ld

def convert_to_list_of_dicts(d):
    ld = []
    for key in d:
        ld.append({"char" : key, "count" : d[key]})
    return ld

def sort_by_count(d):
    return d["count"]

main()