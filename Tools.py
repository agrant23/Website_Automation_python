#Useful python tools
import string
import random
import time

class Tools():

    def generate_random_string(self,excluded_chars, string_len):
        for char in excluded_chars: 
            string_chars = string.printable.replace(char,'')
            random_string = ''.join(random.choice(string_chars) for x in range(string_len))
        return random_string
    
    def generate_randon_number_with_excluded_nums(self,max_num,ex_num1=None,ex_num2=None,ex_num3=None,ex_num4=None,ex_num5=None,ex_num6=None,ex_num7=None):    #where the numbers excluded are the arguments
        _num =None
        while _num == None or _num == ex_num1 or _num == ex_num2 or _num == ex_num3 or _num == ex_num4 or _num == ex_num5 or _num == ex_num6 or _num == ex_num7:
            _num = random.randrange(max_num)
        return _num
        


    #String Manipulation

    def del_words_replace_space_of_string(self, string_in, char_replacing=None, word_replace1=None,word_replace2=None):  #where up to three deleted words are the arguments 
        string_in = str.lower(string_in)
        word_list = string_in.split(' ')
        string_out = ""
        for word in word_list:
            if word == word_replace1 or word == word_replace2:     #or word == args or word ==args:
                del(word)
            else:
                string_out = string_out + word + char_replacing
        return string_out[ :-1: ]

    
    
    """
    The method below takes a WebElement as input. It will then toggle the border and background colors
    red and yellow for 2 seconds. Running this will allow you to see very clearly what element,
    if any, your automation is targeting. If no element flashes on the screen, either its not selecting
    anything, or there is a visibility issue. You may have overlapping elements on the screen that mask
    the element you are targeting.
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