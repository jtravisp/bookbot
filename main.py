def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_count_list = char_to_list_dict(char_count)
    print_char_count(char_count_list)
    print(f"{word_count} words found in the document")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    lowered_text = text.lower()
    for w in lowered_text:
        if w in chars:
            chars[w] += 1
        else:
            chars[w] = 1
    return chars

def char_to_list_dict(char_dict):
    return [{"char": k, "num": v} for k, v in char_dict.items()]

def sort_on(dict):
    return dict["num"]

def print_char_count(chars):
    print("Character count:")
    chars.sort(reverse=True, key=sort_on)
    for c in chars:
        if c["char"].isalpha():
            print(f"The '{c['char']}' character was found {c['num']} times")
    print("---------------")

if __name__ == '__main__':
    main()
