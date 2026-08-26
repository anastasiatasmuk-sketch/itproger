#Конструктори, перевизначення методів
# взято з 17 уроку
class Dog:
    name = None
    age = None
    isHappy = None

    def __init__(self, name='Oskar', age=1, isHappy=True):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, dog_name, age=1, isHappy = True):
        self.name = dog_name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy: ", self.isHappy)


dog1 = Dog(age=3)
# dog1.set_data('Alex', 5)
dog2 = Dog('Skubby', 5, False)



