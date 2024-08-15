my_dict = {'Petya': 2000, 'Dima': 2004, 'Vasya': 1995}
print("Dict: ",
      my_dict)
print("Existing value:",
      my_dict.get('Petya'))
print("Not existing value: ",
      my_dict.get('Kolya'))
my_dict.update({'Kolya': 1999,
                'Tanya': 2001})
name_1 = my_dict.pop('Petya')
print("Deleted value: ",
      name_1)
print("Modified dictionary:",
      my_dict)

print()

my_set = {1, 1, True, True, False, 2, 3, 4, 3, 4, 'a', 'a', 'b'}
print(my_set)
print(my_set.add(5), my_set.add('c'))
print(my_set.discard(False))
print(my_set)
