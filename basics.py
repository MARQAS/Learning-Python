# Variables
first_name = 'Mohammed '
last_name = 'Razzaq'
#Concatenation
full_name = first_name + last_name
nickname = 'Marqas'
#Printing on the screen
print(full_name, nickname)
born = 1994
# Wrong: sent =  nickname + ' was born in ' + born
#correct:
sent =  nickname + ' was born in ' + str(born)
print(sent)
print(nickname,'was born in', born)
# Wrong: second_line = 'That's interesting'
#correct:
second_line = "\n \t \t That's interesting"
first = "\n \t \t Python"
print('What are you learning?', first,second_line)
#word[start:end+1]
part = first_name[:3]
print(part)
word1 = 'Good'
word2 = 'Evening'

# Normal Division results in whole numbers or floats
# half1 = len(word1)/2
# half2 = len(word2)/2 

#Integer division 
half1 = len(word1)//2
half2 = len(word2)//2
end1 = word1[half1:]
end2 = word2[half2:]
print(end1, end2)

#Let's test Input
paper = input("\nEnter the paper\t")
num_of_papers = input("\nEnter the number of papers\t")
print(paper, num_of_papers)
 
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
# del is used when index is known but value is unknown
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

#get() example
showtime = performances.get('Enchanted Elephants')

# Comparing: 
# list[a,b,c] != list[b,c,a] (Index matters)
# Dict{a:1,b:2,c:3} == Dict{b:2,a:1,c:3} ( Index doesn't matter as long as key:value pairs are same)
