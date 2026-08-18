#робота з файлами
# data = input('Hobby:')
# file = open('data/myfile.txt', 'a')
# file.write(data + '\n')

file = open('data/myfile.txt', 'r')
# print(file.read(4))
for line in file:
    print(line, end='')
file.close()