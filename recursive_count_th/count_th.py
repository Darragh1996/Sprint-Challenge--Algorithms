'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    th_count = 0
    th_index = word.find("th")
    if th_index >= 0 and th_index+2 >= len(word):
        return 1
    elif th_index >= 0:
        th_count += 1
        slice_word = word[(th_index+2):]
        th_count += count_th(slice_word)

    return th_count


count_th("thhtthht")
