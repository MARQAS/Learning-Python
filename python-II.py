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