# Exceptions
performances = {}
# Try block
try:
    schedule_file = open('schedule.txt', 'r')
# Except block (program won't run without this)
# Catch FileNotFoundError into a variable
except FileNotFoundError as err:
	# print the error
    print(err)
for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)
