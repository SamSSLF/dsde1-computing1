import random
greetings = ('Hi','Howdy', 'Hola', 'Greetings', 'Hey')
print ('What is your name?')
name = input()
value = random.choice(greetings)
print (value + ',' + name + '!')
print ('Guess a number between 1 and 10')

random_number = random.randint(1,10)

guess1 = input ()
guess1 = int (guess1)
if random_number == guess1:
    print ('Success!')
else:
    print ('Please try again,' + name + '.') 

guess2 = input()
guess2 = int (guess2)
if random_number == guess2:
    print ('Success!')
else:
    print ('You have one last try.') 

guess3 = input()
guess3 = int (guess3)
if random_number == guess3:
    print ('Success!')
else:
    print ('Better luck next time,' + name + '.') 