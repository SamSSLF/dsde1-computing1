'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0],the_list[-1]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    i = the_list[beginning,end]
    return i[::-1] 



# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    for n in range(1,index):
        the_list.insert(index, the_list[index])    
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        print("It's a palindrome!")
    else:
        print ('Not a palindrome.')

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence_edit = sentence.replace(' ','').replace(',','').replace('.','').lower()
    if sentence_edit == sentence_edit[::-1]:
        print('This sentence is a palindrome!')
    else:
        print('This sentence is not a palindrome.')


# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    sentence1.strip()
    sentence2.strip()
    new_sentence = sentence1 + ' ' + sentence2
    if new_sentence[0].isupper() and new_sentence[-1] = '.':
        return new_sentence
    else:
        print('Please capitalze the first letter of your first sentence and add a full stop to the end of your last sentence.')


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    return

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    return
