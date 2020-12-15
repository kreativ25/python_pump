import requests

# print(1/0)
# print(3 + 'dd')


# try:
#     f = 1 / 0
# except ZeroDivisionError:
#     f = 0
#
# print(f)

# try:
#     x = 2 + '3'
# except Exception:
#     x = 2
# print(x)

# try:
#     f = requests.get('https://jsonplaceholder.typicode.com/users')
# except Exception:
#     data = {}
# else:
#     data = f.json()[0]
#
# print(data)


# while True:
#     try:
#         x = int(input("Введите номер: "))
#         break
#     except ValueError:
#         print("Это не номер!!!")
#

# гарантированное / стабильное подключение
while True:
    try:
        f = requests.get('https://jsonplaceholder.typicode.com/users')
        data = f.json()[0]
        break
    except Exception:
        pass

print(data)

