#just_play
import random
from Tools import *

myList = ["Bran",11,22,33,"Stark",22,33,11]
 
print(myList.pop(1))
print(myList)


#print(random.randrange(11))


class ClassName():
    def method_name(self):
        print(Tools().generate_randon_number(10))

classname = ClassName()
#classname.method_name()

i=0
while i<35:
    #print(Tools().generate_randon_number(10))
    i += 1          #same as i = i + 1

class A():
    def foo(self,a):
        for b in a:
            return b or b
        #return b

a = A()
#print(*a.foo(['a','b','c']))

#print(Tools().generate_randon_number_with_excluded_nums(10,5,6,7,8,0))

def random1(max_num,*discarded_nums):       #doesn't work
    while True:
        _rand_num = 2  #random.randrange(max_num)
        for bad_num in discarded_nums:
            if _rand_num == bad_num:
                print(_rand_num)
                pass
            else:
                return _rand_num
                #break
    

print('\n'+'please work')
print(random1(10, 2, 5, 6, 8, 1, 3, 4, 7, 0))

def random2(max_num,ex_num1=None,ex_num2=None,ex_num3=None,ex_num4=None,ex_num5=None,ex_num6=None,ex_num7=None):
    #random.randrange
    #_rand_num = random.randrange(max_num)
    num = None
    while  num == None or num == ex_num1 or num == ex_num2 or num == ex_num3 or num == ex_num4 or num == ex_num5 or num == ex_num6 or num == ex_num7:           #if true go down
        num = random.randrange(max_num) 
        print(num)        
    return num
print('\n')
print(random2(10,2,3,4,5,6,1,7))

Tools().generate_randon_number_with_excluded_nums(9,)

random.randrange
num = None
while random.randrange(10) == 5: 
    print(num)
    pass
print('\n')
#print(Tools().generate_randon_number_with_excluded_nums(10, 2, 5, 6, 8))


def convert_option_title_to_url_block(drop_down_option_title):
    excluded_word1 = 'the'
    exclude_word2 = 'column'
    excluded_word2 = 'word'
    replace_space= '~'
    replace_word1 = 'this'
    replace_word2 = 'a'
    with_word1 = 'HELLO'
    with_word2 = "TONY HERE"
    return Tools().del_replace_words_and_spaces_of_string(drop_down_option_title,replace_space, excluded_word1,None,replace_word1,replace_word2,with_word1,with_word2)

print(convert_option_title_to_url_block("the column word Let this work please with a cherry on top"))
