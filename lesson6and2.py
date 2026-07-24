#Оператори в циклах
for i in range(1, 11):

    if i % 2 == 0:
        continue

    if i == 7:
        break

    print("Element:", i)

#Else в циклі
for i in "Hello World":
    if i == "n":
        print("Done")
        break
else:
    print("Not found")