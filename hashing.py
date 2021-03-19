def hash_f(a_string, table_size):
    value = 0
    for letter in a_string:
        value = value + ord(letter)
    return value % table_size


def hash_position(a_string, table_size):
    value = 0
    position = 1
    for letter in a_string:
        value = value + ord(letter) * position
        position += 1
    return value % table_size
