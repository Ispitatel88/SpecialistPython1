# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

dictionary_2.update(dictionary_1)
print(dictionary_2)

z = {**dictionary_1, **dictionary_2}
print(z)
