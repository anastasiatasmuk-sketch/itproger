#Власний модуль в пайтон
# import mymodule
from mymodule import add_3_numbers as add

# mymodule.hi()
# print(mymodule.name)
res = add(3, 8, 12)
print(res)

#Сторонні модулі. Пакетний менеджер PIP
import cowsay


cowsay.cow('Hello itproger')
