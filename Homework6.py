   #Задание 1
my_dict = {'Sofya': 2007, 'Igor': 2005, 'Nataly': 1989, 'Alex': 2000}
print('Dict: ', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Mark'))
my_dict.update({'Sasha': 1978,
                'Rita': 2002})
value = my_dict.pop('Sofya')
print('Deleted value:', value)
print('Modified diktionary:', my_dict)
   #Задание 2
my_set = {1, 1, 2, 45.987, 'Hello' , 'Hello', 3, 2}
print('Set:', my_set)
my_set.add((1,2,3),)
my_set.add(9)
my_set.discard(1)
print('Modified set:', my_set)



