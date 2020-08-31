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
    
    def generate_randon_number(self,max_num):
        return random.randrange(max_num)
    
    
    
    
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