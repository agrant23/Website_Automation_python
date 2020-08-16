import string
import random

def generate_random_string(excluded_chars, string_len):
    for char in excluded_chars: 
        string_chars = string.printable.replace(char,'')
        random_string = ''.join(random.choice(string_chars) for x in range(string_len))
    return random_string


def random_password(password_len): 
    excluded_password_chars = ['\n','\t','\r','\x0b','\x0c']
    password = generate_random_string(excluded_password_chars, password_len)
    return password    

print(random_password(8))