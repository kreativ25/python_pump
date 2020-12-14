# хеш таблица
# ассоциативный массив

# d = dict(a=1, b=2)
# d = {}
# d = {'a': 1, 'b': 2}
# d = dict([(1, 2), (3, 4)])
# d = dict.fromkeys(['a', 'b'], [1, 2, 3, 4, 5])
# d = dict.fromkeys(['a'], 4)

key = {i for i in range(5)}
value = [i for i in range(3)]
d = {i: value for i in range(len(key))}
# d = [{i: value for i in range(len(key))}]*2

# c = dict.keys(d)


print(d.items())
print(type(d))
