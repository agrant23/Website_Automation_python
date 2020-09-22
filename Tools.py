import string
import random
from random import choice
import time


class Tools():
    
    def generate_random_num_with_excluded_nums(self,min_range, max_range,*excluded_nums):
        return choice([num for num in range(min_range,max_range) if num not in excluded_nums])
    
    def dictionay_value_from_key(self,dictionary,_key):
        value1 = ""
        for key, value in dictionary.items():
            try:
                if key == _key:
                    value1 = value
            except:
                raise NameError(_key + " not a key")    
        return value1
    
    #String Manipulation

    def generate_random_string(self,excluded_chars, string_len):
        for char in excluded_chars: 
            string_chars = string.printable.replace(char,'')
            random_string = ''.join(random.choice(string_chars) for x in range(string_len))
        return random_string


    #Unused Methods

    """
    The method below takes a WebElement as input. It will then toggle the border and background colors
    red and yellow for 2 seconds. Running this will allow you to see very clearly what element,
    if any, your automation is targeting. If no element flashes on the screen, either its not selecting
    anything, or there is a visibility issue. You may have overlapping elements on the screen that mask
    the element you are targeting. Good for diagnosing an element that is not clicking.
    """
    def highlight(self,element):
        """Highlights a Selenium WebDriver element to indicate successful selector targeting."""
        driver = element._parent
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        count = 0
        colors = ['yellow', 'red']
        while count < 10:
            if ((count % 2) == 0):
                background = colors[0]
                border = colors[1]
            else:
                background = colors[1]
                border = colors[0]
            apply_style("background: %s; border: 2px solid %s;" % (background, border))
            time.sleep(.2)
            count += 1
        apply_style(original_style)



    def del_replace_words_and_spaces_of_string(self, string_in, new_space_char=None, word_del1=None, word_del2=None, word_del3=None, word_del4=None, word_rep1=None,with_word_repl1=None,word_rep2=None,with_word_repl2=None):
        _string_in = str.lower(string_in)
        word_list = _string_in.split(' ')
        string_out = ""
        for word in word_list:
            if word == word_del1 or word == word_del2 or word == word_del3 or word == word_del4:     
                del(word)
            elif word == word_rep1:
                del(word)
                string_out = string_out + with_word_repl1 + new_space_char
            elif word == word_rep2:
                del(word)
                string_out = string_out + with_word_repl2 + new_space_char
            else:
                string_out = string_out + word + new_space_char
        return string_out[ :-1: ]

