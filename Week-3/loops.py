'''These functions count from 1 to 10 in ascending and descending order'''

def count1():
    '''counts up using a for loop'''
    for i in range(11):
        print(i)

def count2():
    '''counts down using  for loop'''
    for i in range(10, 0, -1):
        print(i)

def count3():
    '''counts up using a while loop'''
    spam = 0
    while spam <= 10:
        print(spam)
        spam = spam + 1

def count4():
    '''counts down using a while loop'''
    spam = 10
    while spam >= 0:
        print(spam)
        spam = spam - 1
