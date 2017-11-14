#Lists
#list of (strings/numbers) = array (without key value pair)
performances = ['Ventriloquism', 'Amazing Acrobatics']
# New items can be added in the list using append()
performances.append('Snake Charmer')
performances.append('Bearded Lady')
performances.append('Tiniest Man')
print(performances)
# Items can be removed using remove() and del
# remove()
performances.remove('Bearded Lady')
performances.remove('Tiniest Man')
print(performances)
# del is used when index is know but value is unknown
del performances[1]
print(performances)

# Dictionaries = arrays (with key=>value pair)
# Dictionary = {'key':'value'}
performances = {'Ventriloquism':'9:00am', 'Snake Charmer':'12:00pm'}
# Add new items
performances['Amazing Acrobatics'] = '2:00pm'
performances['Enchanted Elephants'] = '5:00pm'
print(performances)
# update the existing value
performances['Enchanted Elephants'] = '6:00pm'
# items can be deleted using del
del performances['Ventriloquism']
showtime = performances.get('Enchanted Elephants')
if showtime==None:
	print("doesn't exist")
else:
	print(showtime)


#get() example
performances = {'Ventriloquism':'9:00am', 
               'Snake Charmer': '12:00pm', 
               'Amazing Acrobatics': '2:00pm', 
               'Bearded Lady':'5:00pm'}
showtime = performances.get('Bearded Lady')
if showtime==None:
    print("Performance doesn't exist")
else:
    print("The time of the Bearded Lady show is", showtime)

# Comparing: 
# list[a,b,c] != list[b,c,a] (Index matters)
# Dict{a:1,b:2,c:3} == Dict{b:2,a:1,c:3} ( Index doesn't matter as long as key:value pairs are same)

#Loops
#For : for list in lists 
word = 'Welcome!'
for w in word:
    print(w)
#Use the built-in function range() to generate numbers from 0 to 19.
my_list = range(20)
#print 5 number bw 1 & 53
import random
for i in range(5):
    print(random.randint(1,53))    