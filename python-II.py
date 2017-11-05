#Lists
#list of (strings/numbers) = array
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