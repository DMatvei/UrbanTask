# Словари
my_dict = {'Sasha': 1984, 'Masya': 1997}

print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get('Rudy'))
my_dict.update({'Rudy': 1374,
                'Vano': 1975
                })
print(f'Delete value: {my_dict.pop('Rudy')}')
print(my_dict)

# множества

my_set = {1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 'Dog', 'Dog', 'Cat', (1, 2, 3), (1, 2, 3), 3.14, 3.14}
print(my_set)
my_set.add('не изменяемый тип')
my_set.add(113)
print(my_set) #Вывод множества с добавленными значениями
my_set.pop()

print(my_set)

