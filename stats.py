def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for c in chars_dict:
        if c.isalpha():
            sorted_list.append({"char": c, "num": chars_dict[c]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list