# Change value of a key in a nested dictionary
dict_3 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

dict_3['emp3']['salary'] = 8500
print(dict_3)