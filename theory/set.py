# не повторяющиеся элементы в случайном порядке
# t = set('hello')
# t = {1, 2, 2}
# x = [i**2 for i in range(34)]
# x = (1, 2, 2)
# x = {'a': 1, 'b': 2}
x = [1, 2, 3, 3, 3, 3]
y = {4, 3, 2, 1}
t = set(x)
# объединение нескольких множеств
t = t.union(y)

# все элементы set принадлежат множеству
z = y == t

print(z)
print(t)
print(len(t))
print(type(t))


