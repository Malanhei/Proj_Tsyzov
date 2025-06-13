import math

# Класс Круг
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


# Класс Человек
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


# Класс Мужчина
class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Мужчина")

    def show_gender(self):
        print("Это мужчина.")


# Класс Женщина
class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Женщина")

    def show_gender(self):
        print("Это женщина.")
# Использование класса Circle
c = Circle(5)
print("Площадь:", c.area())
print("Длина окружности:", c.circumference())
print("Диаметр:", c.diameter())

# Использование классов Person, Man и Woman
m = Man("Алексей", 30)
m.show_info()
m.show_gender()

w = Woman("Елена", 28)
w.show_info()
w.show_gender()
