# упорядоченные изменяемые коллекции объектов произвольных типов
# t = list('hello')
# t = ['a', 'b', 'b'].count('b')
# t = [i for i in range(5)]
# x = ('a', 'b', 'c')

# t = [i * 2 for i in x]
# y = lambda i: i * 3 if i != 'a' else i
# t = map(lambda i: i * 3 if i != 'a' else i, x)
#
# for i in t:
#     print(i)

y = []
a = [i for i in range(3)]
b = [i for i in range(5)]
a.extend(b)
y = a

# c = y.count(1)
# c = y.remove(1)
# c = y.index(1)

# c = y.insert(3, 5555)
y.sort()
y.reverse()

print(y)
print(type(y))
