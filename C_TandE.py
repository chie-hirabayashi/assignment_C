"""
print(tanaka.name)
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す
"""

# from curses import ACS_GEQUAL, KEY_NEXT


from turtle import circle


class Customer:  # 同じ名前classつくるな！っていってる？
    def __init__(self, first_name, family_name):
        self.num1 = first_name
        self.num2 = family_name

    def full_name(self):
        return self.num1 + " " + self.num2


ken = Customer("Ken", "Tanaka")
tom = Customer("Tom", "Ford")


print(ken.full_name())
print(tom.full_name())


# ベース
class UserName:
    def __init__(self, name):
        # 4文字以上20文字以内のチェック
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")
        self.name = name

    def screen_name(self):
        return self.name.upper()


tanaka = UserName(name="tanaka")
# bob = UserName(name="baba")

print(tanaka.screen_name())
# print(bob.name)

"""
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す

"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.num1 = first_name
        self.num2 = family_name
        self.age = age

    def full_name(self):
        return self.num1 + " " + self.num2

    def self_age(self):
        return self.age


ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


print(ken.full_name())
print(tom.full_name())
print(ken.age)
print(tom.age)
print(ieyasu.age)

"""
料金の計算ルール
 こども料金(20歳未満): 1000円
 おとな料金(20歳以上65歳未満): 1500円
 シニア料金(65歳以上): 1200円
"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.num1 = first_name
        self.num2 = family_name
        self.age = age

    def full_name(self):
        return self.num1 + " " + self.num2

    def self_age(self):
        return self.age

    def entry_free(self):
        if self.age < 20:
            return 1000
        if 20 <= self.age < 65:
            return 1500
        if 65 <= self.age:
            return 1200


ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

print(ken.entry_free())
print(tom.entry_free())

"""

"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.num1 = first_name
        self.num2 = family_name
        self.age = age

    def full_name(self):
        return self.num1 + " " + self.num2

    def entry_free(self):
        if self.age < 20:
            return 1000
        if 20 <= self.age < 65:
            return 1500
        if 65 <= self.age:
            return 1200

    def info_csv(self):
        if self.age < 20:
            return f"{self.num1} {self.num2},{self.age},1000"
        if 20 <= self.age < 65:
            return f"{self.num1} {self.num2},{self.age},1500"
        if 65 <= self.age:
            return f"{self.num1} {self.num2},{self.age},1200"


ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

print(ken.entry_free())
print(ieyasu.age)
print(ieyasu.num1)
print(ken.info_csv())

print("ーーーーーーーーーーーーーーーーー")

"""
D-1~3
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


circle1 = Circle(1)
circle2 = Circle(2)

print(circle2.radius)
print(circle1.area())
print(circle1.perimeter())


import math


class Rectangle:
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt((self.height) ** 2 + (self.width) ** 2)


rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

print(rectangle1.height)
print(rectangle1.area())
print(rectangle1.diagonal())
print(rectangle2.area())
print(rectangle2.diagonal())
print(math.sqrt(2))


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return "%.2f" % self.side**2

    def diagonal(self):
        return "%.2f" % math.sqrt(((self.side) ** 2) * 2)


square1 = Square(side=1.5)
square2 = Square(side=15)


print(square1.area())
print(square1.diagonal())
print(square2.area())
print(square2.diagonal())

# 小数点以下2
n1 = 1.234567
n2 = 5
print(math.ceil(n1))  # 切り上げ
print(math.floor(n1))  # 切り下げ
print(round(n1))  # 四捨五入
print(round(n1, 2))  # 丸め
print(round(n2, 2))  # 丸め
print(f"{n1:.1f}")
print(f"{n2:.03f}")  # ゼロ埋め
print("%03d" % n1)
print("%.3f" % n1)

print("ーーーーーーーーーーーーーーーーー")

"""
D-5~6
"""
# takes no arguments///タイプミスに注意 init int とか


class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1
        return self.value


counter1 = MyCounterV1(value=0)

print(counter1.value)
counter1.count_up()
print(counter1.value)


class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        for n in range(1, self.step + 1):
            self.value += 1
        return self.value


counter1 = MyCounterV2(value=0, step=5)

print(counter1.value)
counter1.count_up()
print(counter1.value)
counter1.count_up()
print(counter1.value)


class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        for n in range(1, self.step + 1):
            self.value += 1
        return self.value

    def count_down(self):
        for n in range(1, self.step + 1):
            self.value -= 1
        return self.value


counter1 = MyCounterV3(value=1, step=2)
counter2 = MyCounterV3(value=3, step=4)

print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_down()
print(counter1.value)


print(counter2.value)

counter2.count_down()
print(counter2.value)

counter2.count_down()
print(counter2.value)
