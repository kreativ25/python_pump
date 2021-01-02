
def decorator(func):
    """
    Описание декоратора \n
    :param func:
    :return:
    """
    def f(*args, **kwargs):
        print('start')
        d = func(*args, **kwargs)*2
        print(d)
        print('end')

    return f


@decorator
def test(n):
    k = [i ** i for i in range(n * 2)]
    print(k)
    return k


y = test(3)

# print(test(3))

