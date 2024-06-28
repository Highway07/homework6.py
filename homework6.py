my_dict = {"Виталий": 1983,"Андрей": 1979,"Игорь": 1990}
print(my_dict)
print('Existing value:',my_dict['Виталий'])
print('No existing value:',my_dict.get('Елена'))
my_dict.update({'Михайл':1998,
                'Алексей':1973})
print(my_dict)
my_dict.pop('Андрей')
print(my_dict)
my_set = {1.34,2,2.54,5.57,'банан'}
print(my_set)
my_set.add((55,83,'грейпфрут'))
my_set.remove(2.54)
print(my_set)
