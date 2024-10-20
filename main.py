def main():
    book_path = "books/frankenstein.txt"
    txt = get_file_text(book_path)
    print_report(get_words_count(txt), get_chars_count(txt))

def print_report(words_count, chars_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")

    chars_list = get_sorted_list_by_count(chars_count)

    for c in chars_list:
        if c["char"].isalpha():
            print(f"The '{c['char']}' character was found {c['count']} times")
    
    print("--- End report ---")

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

def get_sorted_list_by_count(d):
    ld = dic_to_list_of_dicts(d)
    ld.sort(reverse=True, key=sort_by_count)
    return ld

def dic_to_list_of_dicts(d):
    ld = []
    for key in d:
        ld.append({"char" : key, "count" : d[key]})
    return ld

def sort_by_count(d):
    return d["count"]

main()