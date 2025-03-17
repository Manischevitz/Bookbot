import sys
character_list = {}

def get_word_count(bookpath):
    with open(bookpath) as f:
        text_read = f.read()
        word_number = text_read.split()
    raw_word_number = len(word_number)
    return raw_word_number

def get_character_dictionary(bookpath):
    with open(bookpath) as f:
        text = f.read()
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in character_list:
                character_list[lower_char] +=1
            else:
                character_list[lower_char] = 1
    return character_list

def big_to_small(dict):
    return dict["count"]

def bigger_dictionary(dictionary):
    dictionary_list = [{"character": char, "count": count} for char, count in character_list.items()]
    dictionary_list.sort(reverse=True, key=big_to_small)
    return dictionary_list

def test():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
        character_list = get_character_dictionary(bookpath)
        word_count = get_word_count(bookpath)
        real_character_list = bigger_dictionary(character_list)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in real_character_list:
            print(f"{item['character']}: {item['count']}")
        print("============= END ===============")


    
    
test()
