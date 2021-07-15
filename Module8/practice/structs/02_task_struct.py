lst = [1, 2, 4, 5, 6, 2, 5, 2]

new_list_0 = list(set(l))
print(new_list_0)

new_list = list(filter(lambda x: l.count(x) == 1, l))
print(new_list)
