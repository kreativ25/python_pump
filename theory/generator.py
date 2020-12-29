import cProfile


def generator(value):
    x = value
    while value > 0:
        yield x - value
        value -= 1


# g = generator(5)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

x = [i for i in generator(10544654) if i % 3 == 0]
# print(x)
cProfile.run('x')