'''
fuzzy.py

Lint this file using PyLint.
'''

def maths(input_a, input_b, input_c):
    '''This function does some maths on three numbers.'''
    result = input_a * 3 - input_b + input_c
    return result

def choices(question):
    '''This function returns True or False.'''
    result = bool(question)
    return result


def main():
    '''this function does something'''
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    new_answer = choices(True)
    print(new_answer)

if __name__ == '__main__':
    main()
