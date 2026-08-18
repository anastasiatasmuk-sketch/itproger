#обробка винятків
# num = None
#
# while num is None:
#     try:
#         num = int(input('Enter num: '))
#         num +=5
#         print(num)
#     except ValueError:
#         print('Ви ввели щось не те')

try:
    a = 10
    b = int(input('Enter a number: '))
    print(a / b)
except ValueError:
    print('Ви ввели щось не те')
except ZeroDivisionError:
    print('Ділити на 0 не можна')
# except Exception: #універсальна, використовується для всіх помилок
#     print('Ви ввели щось не те')
else:
    print('Ви молодець')
finally:
    print('Finally')
