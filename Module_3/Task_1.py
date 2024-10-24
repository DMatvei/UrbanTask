

calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string : str):
    count_calls()
    length_ = len(string)
    string_up = string.upper()
    string_down = string.lower()

    return length_, string_up, string_down


def is_contains(word : str, word_list):
    count_calls()
    word = word.upper()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].upper()

    return word in word_list


print(string_info('Kaboom'))
print(string_info('kalabanga'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)