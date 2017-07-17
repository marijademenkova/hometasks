from collections import OrderedDict
keys = ['a', 'b']
values = ['1', '2', '3']
dictionary = {}
for x in range(0, len(values)):
    if x < len(keys):
        dictionary.update({values[x]: keys[x]})
    else:
        dictionary.update({values[x]: None})
print dictionary
sorted_x = OrderedDict(sorted(dictionary.items(), key=lambda keys: keys[0]))
print sorted_x.items()
