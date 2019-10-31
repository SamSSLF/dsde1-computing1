'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name = '', place = ''):
    if user_name == '' and place == '':
        print('Hello and welcome')
    elif user_name != '' and place == '':
        print('Hello,' + user_name + ', and welcome')
    elif place != '' and user_name == '':
        print('Hello and welcome to ' + place)
    elif user_name != '' and place != '':
        print('Hello, ' + user_name + ', and welcome to ' + place)   



# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(list, avg_type = 'mean'):
    if avg_type = 'mean':
        n_num = [1, 2, 3, 4, 5] 
        n = len(n_num) 
        get_sum = sum(n_num) 
        mean = get_sum / n 
        print("Mean / Average is: " + str(mean)) 
    
    if avg_type = 'mode':
    
    if avg_type = 'median':
        if n % 2 == 0: 
            median1 = n_num[n//2] 
            median2 = n_num[n//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = n_num[n//2] 
        print("Median is: " + str(median)) 
    