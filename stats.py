def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowercase_text = text.lower()
    characters = {}
    for character in lowercase_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(dict_list):
    return dict_list["num"]

def listed_dicts(characters):
    dict_list = []
    char_dict = {}
    for character in characters:
        char_dict["char"] = character
        char_dict["num"] = characters[character]
        dict_list.append(char_dict)
        char_dict = {}
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list