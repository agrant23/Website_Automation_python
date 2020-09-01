#play_tests.py
import time
from Yahoo_Page import *
from Tools import *


driver = webdriver.Chrome(options=options)  
yahoo_page = Yahoo_Page(driver)
#yahoo_page.click_sign_in_button()

yahoo_page.click_news_link()

#print(driver.title)
driver.maximize_window()

#https://docs.python.org/3/tutorial/errors.html
#https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception

""" try:
    originals_drop_down_loc = (By.XPATH,'//a[@title="Originals"]')
    wait(driver,15).until(EC.visibility_of_element_located(originals_drop_down_loc))
    drop_down_element = driver.find_element(*originals_drop_down_loc)
    ActionChains(driver).move_to_element(drop_down_element).perform()    
except TimeoutError as exception:
    print(exception)
    raise exception """


#title_array = str.lower(self._rand_tab_title).split(' ')
#for word in title_array:
#    yield word
#return next(word or word)

#print(exception)
yahoo_page.hover_originals_drop_down()
yahoo_page.click_random_option_from_originals_drop_down()
print(yahoo_page._rand_option_title)

def _random_option_title2():
        title = str.lower(yahoo_page._rand_option_title)
        _title_list_in = title.split(' ')
        _title_string_out = {}
        for word in _title_list_in:
            if word == 'the' or word == "2020":
                del(word)
            else:
                _title_string_out = word + ' ' 
                yield _title_string_out             #want the return at the same indent as the for loop so it doesn't break out prematurely 

#print(*_random_option_title2()) #this is now a generator function, may not work in asserts 

def _random_option_title3():
        title = str.lower(yahoo_page._rand_option_title)
        print(title)
        _title_list_in = title.split(' ')
        print(_title_list_in)
        _title_string_out = ""
        for word in _title_list_in:
            if word == 'the' or word == "2020":
                print(word)
                del(word)
            else:
                print(word)
                _title_string_out = _title_string_out + word + '~' 
        return _title_string_out[ : -1: ]                                       #without this at the correct indent then the return would break out of the string on the first letter, duh

#print(_random_tab_title3())    

tools = Tools()
#print(tools.del_words_replace_space_of_string("Will this work please",'!','this', None))
print(Tools().del_words_replace_space_of_string(str.lower(yahoo_page._rand_option_title),'~','the','column'))

def convert_option_title_to_url_block(drop_down_option_title):
    excluded_word1 = 'the'
    exclude_word2 = 'column'
    excluded_word2 = 'word'
    replace_space= '~'
    return Tools().del_words_replace_space_of_string(drop_down_option_title,replace_space, excluded_word1,exclude_word2)

print(convert_option_title_to_url_block(str.lower(yahoo_page._rand_option_title)))

print(Tools().del_words_replace_space_of_string("Let this work please with a cherry on top",'*','this','with','a' ))
#rand_num = Tools().generate_randon_number(6)

#yahoo_page.click_random_tab_from_originals_drop_down()
print('\n')
#print(element_list[0])
print('\n')
#element_list.pop(0)

#print(element_list)

#yahoo_page.click_The_Ideas_Election_tab()
time.sleep(2)
#yahoo_page.new_page_loads_off_News()
#print(driver.__getattribute__('title'))

#yahoo_page.input_search_field('kendrick lamar')   
#print(yahoo_page.search_field().get_attribute('value'))
#print(yahoo_page.search_field_contents())   
print('\n')
#print(yahoo_page.current_cursor_element().__dict__)
print('\n')
#print(id(yahoo_page.current_cursor_element()))
print('\n')
#print(type(yahoo_page.current_cursor_element()))
print('\n')
#print(yahoo_page.current_cursor_id)