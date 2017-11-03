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
knights = 2
if knights < 3 :
	print('Retreat')

else:
	print('Truce?')
#Let's test Input
paper = input("\nEnter the paper\t")
num_of_papers = input("\nEnter the number of papers\t")
print(paper, num_of_papers)	