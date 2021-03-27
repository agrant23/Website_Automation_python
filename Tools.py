from selenium.common.exceptions import StaleElementReferenceException
import string
import re
import random
from random import choice
import time


def generate_random_num(min_range, max_range, excluded_nums=[None]):
    return choice([num for num in range(min_range-1, max_range)
                  if num not in excluded_nums])


# String Manipulation

def generate_random_string(length, excluded_chars=str(None)):
    clean_string = re.sub("|".join(excluded_chars), "", string.printable)
    random_string = ''.join(random.choice(clean_string)
                            for i in range(length))
    return random_string


# Expected Condition

def attribute_value_is_not(
          locator, attribute_type, not_attribute_value):
    """
    An expectated condition to check that an attribute's value for a
    element is not a specified attribute_value

    Parameters
    ----------
    locator : a tuple used to find the same locator for both the argument's
              not_attribute_value and method's found attribute_value
    attribute_type : string of the attribute type for this element
    not_attribute_value : string of the attribute value that is not the the
                          value this Expected Condition find's
    """
    def _predicate(driver):
        try:
            attribute_value = driver.find_element(*locator).get_attribute(
                attribute_type)
            return attribute_value != not_attribute_value
        except StaleElementReferenceException:
            return False

    return _predicate


"""
The method below takes a WebElement as input. It will then toggle
the border and background colors red and yellow for 2 seconds.
Running this will allow you to see very clearly what element, if
any, your automation is targeting. If no element flashes on the
screen, either its not selecting anything, or there is a visibility
issue. You may have overlapping elements on the screen that mask the
element you are targeting. Good for diagnosing an element that is
not clicking.
"""


def highlight(element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script(
           "arguments[0].setAttribute('style', arguments[1]);", element, s)
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
        apply_style(
            "background: %s; border: 2px solid %s;" % (background, border))
        time.sleep(.2)
        count += 1
    apply_style(original_style)
