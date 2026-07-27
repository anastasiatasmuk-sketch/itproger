#Словники
person = {'name': 'Alex', 'age': 15, 5:12, True: 'False'}
# person[5] = 'five'
# print(person[5])

# person1 = dict(name='Alex', age=15)
# # print(person1['name'])
#
# # print(person.items())
#
# # for key, values in person.items():
# #     print(key, values, sep=" - ")
#
# for el in person.values(): # функція для витягу значень з кожного елемента
#     print(el)

# print(person.get('name')) # додаткова функція для витягу інформації з елементу
# person.clear()
# person.popitem() # видаляє останній елемент з словника
person['bio'] = 'Text'
print(person)