import random
greetings = ('Hi','Howdy', 'Hola', 'Greetings', 'Hey')
print ('What is your name?')
name = input()
value = random.choice(greetings)
print (value + ',' + name + '!')
print ('Guess a number between 1 and 10')
guess = input ()
guess = int (guess)
random_number = random.randint(1,10)
if random_number == guess:
    print ('Success!')
else:
    print ('Try again')