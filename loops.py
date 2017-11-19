# Loops
# IF
knights = 2
if knights < 3 :
    print('Retreat')

else:
    print('Truce?')
# example    
performances = {'Ventriloquism':'9:00am', 
               'Snake Charmer': '12:00pm', 
               'Amazing Acrobatics': '2:00pm', 
               'Bearded Lady':'5:00pm'}
showtime = performances.get('Bearded Lady')
if showtime==None:
    print("Performance doesn't exist")
else:
    print("The time of the Bearded Lady show is", showtime)

# For : for list in lists 
word = 'Welcome!'
for w in word:
    print(w)
# Use the built-in function range() to generate numbers from 0 to 19.
my_list = range(20)
# print 5 number bw 1 & 53
import random
for i in range(5):
    print(random.randint(1,53))

# For loop for dictionaries (to print key value pairs)
performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}
# Use for key,value in dictionary.items() to get the key=>value pairs in for loops    
for name,time in performances.items():
    print(name, ': ', time, sep='')

# While Loop
import random
num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))
while guess!=num:
    guess=int(input('Guess again'))
print('You win!') 

# example
import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))
times=1
while guess != num:
    if times==3:
        break
    guess = int(input('Guess again'))
    times=times+1
  
if guess==num:
    print('You win!')
else:
    print('You lose! The number was ',num)  