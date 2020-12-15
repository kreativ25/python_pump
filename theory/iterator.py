# f = [1, 2]
# i = iter(f)
#
# print(i.__next__())
# print(next(i))

class Iterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

t = Iterator(2)
# print(next(t))
# print(next(t))

for i in t:
    print(i)