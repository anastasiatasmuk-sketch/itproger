#цикл for
for i in range(5, 16, 5):
    print("Element:", i)

print("\n\n")

word = "Some text"
for i in word:
    if i == "m":
        print("Літера m є у слові")

#цикл while
i = 100
while i >=10:
    print(i)
    i -= 10

#практичне використання
print("\n\n")
work = True
while work:
    user_input = input("Enter word STOP:")
    if user_input == "STOP":
        work = False
print("While loop is done")
