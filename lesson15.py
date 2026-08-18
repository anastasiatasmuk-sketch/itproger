#Менеджер "With...as"
# file = None
try:
    # file = open('text.txt', 'r')
    # print(file.read())
    with open('data/myfile.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('файл не знайдено')
# finally:
#     file.close()

