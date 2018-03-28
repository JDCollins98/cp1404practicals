string = input("Enter your string here: ")

while string:
    words = string.split()

    word_list = {}
    for word in words:
        if not word in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1

    print('Text: {}'.format(string))
    sorted_word_list = sorted(word_list.keys())

    spacing = len(max(sorted_word_list))

    for word in sorted_word_list:
        space = (spacing - len(word)) + 1
        #print(space, word, word_list[word])
        print("{:{}}: {}".format(word, space, word_list[word]))

    string = input("Enter your string here: ")
