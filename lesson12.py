#робота з функціями
def test_func(word):
    # pass #пуста функція, нічого не виводиться в консоль
    print(word, end='')
    print('!')


# test_func('hello')
# word = 'home'
# test_func(word)
# test_func('Hi')

def info(word):
    print(word, end='')
    print('!')

func = lambda x, y: x * y
print(func(5, 6))

def summa(a, b):
    res = a + b
    info(res)
    return res


res1 = summa(5, 6)
res2 = summa(5.6, 4.4)
res3 = summa('hi', ' world')
print(res1)



