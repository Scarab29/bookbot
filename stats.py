def get_word_count(filepath):
        with open(filepath) as f:
                file_contents = f.read()
                words = file_contents.split()
        return("Found " + str(len(words)) +  " total words")

def get_char_count(filepath):
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        for char in file_contents:
            char = char.lower()
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def get_char_count_sorted(d):
    sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print("--------- Character Count -------")
    for i, j in sorted_items:
        if(i.isalpha()):
            print(i, ': ', j, sep='')

    print("============= END ===============")
