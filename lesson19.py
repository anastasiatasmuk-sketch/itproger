#Спадкування
class Build:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

        # self.get_info()

    def get_info(self):
        print('Year: ', self.year, '. City: ', self.city, sep='')

class School(Build):
    __pupils = None

    def __init__(self, year, city, pupils=500):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print('Pupils: ', self.pupils, sep='')

class House(Build):
    pass

class Shop(Build):
    pass



school = School(1990, 'Seattle', 800)
school.__pupils = 500               #інкапсуляція
school.get_info()
# school.pupils = 500
# print(school.pupils)
house = House(2000, 'San Jose')
house.get_info()
shop = Shop(2020, 'Vinnytsia')