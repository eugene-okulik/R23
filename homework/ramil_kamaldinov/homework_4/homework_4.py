my_dict = {
    'tuple': ('2pl', 78, 23, None, 'Yes'),
    'list': ['play', 13, 'text', False, 3.14],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'sixx': 5},
    'set': {'six', 7, 1.2, True, 'no'}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('Go')
del my_dict['list'][1]
my_dict['dict'][('i am a tuple')] = 23
del my_dict['dict']['four']
my_dict['set'].add('Morning')
my_dict['set'].remove('six')
print(my_dict)
