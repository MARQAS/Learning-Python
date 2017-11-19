# Write into a file
# Create a dictionary
performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}
# Open a file in write mode (Note: If file doesn't exist, python will automatically creates it)    
schedule_file = open('schedule.txt','w')
# loop over dictionary items
for key,val in performances.items():
	# write each key value pair in a file
    schedule_file.write(key + ' - ' + val + '\n')
# Close the file
schedule_file.close()

# Read from a file
# empty dictionary
performances2 = {}
# open a file and print its content
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
	# assign the values to the (key,value) pair directly using split function(by passing '-' as a parameter)
    (show,time)=line.split(' - ')  
    print(show,time)
    # strip all leading and trailing whitespace.
    time=time.strip()
    # Add them into the dictionary
    performances2[show]=time
schedule_file.close()
print(performances2)