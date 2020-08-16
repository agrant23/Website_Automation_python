#Useful python tools
import string
import random

class Tools():

    def generate_random_string(self,excluded_chars, string_len):
        for char in excluded_chars: 
            string_chars = string.printable.replace(char,'')
            random_string = ''.join(random.choice(string_chars) for x in range(string_len))
        return random_string