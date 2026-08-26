#Декоратор
import webbrowser


def validator(func):
    def wrapper(url):
        if '.' in url:
        # print('Before')
            func(url)
        else:
            print('Посилання не правильне')

        # print('After')
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://itprogercom/ua")