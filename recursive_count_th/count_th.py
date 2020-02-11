'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    i = 0

    def search_word(word, i):

        if(len(word) < 2):
            return i
        else:
            print(f'as int: {word[0]}')
            if(word[0] == "t" and word[1] == "h"):
                i += 1
                word = word[2:]
                print(word)
                return search_word(word, i)
            else:
                word = word[1:]
                return search_word(word, i)

    return search_word(word, i)


count_th("shithth")
