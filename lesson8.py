#Робота з текстом
# word = list('itproger')
# word[0] = 'I'
# word.append('!')
# result = ''.join(word)
# print(result)

text = 'football,basketball,skate,drive'
hobbies = text.split(',')

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()
result = ','.join(hobbies)

print(result)