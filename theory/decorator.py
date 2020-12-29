import datetime as dt


def timeit(func):
    def result(*args, **kwargs):

        start = dt.datetime.now()
        f = func(*args, **kwargs)

        print(dt.datetime.now() - start)
        return f

    return result


@timeit
def test(n):
    k = [i**i for i in range(n*2)]
    return k


y = test(4)