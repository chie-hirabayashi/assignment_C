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

print("<フルネーム>")
print(ken.full_name())
print(tom.full_name())
print(sep="")


print("<年齢>")
print(ken.age)
print(tom.age)
print(ieyasu.age)
print(sep="")

print("<入場料>")
print(ken.entry_free())
print(tom.entry_free())
print(ieyasu.entry_free())
print(sep="")

print("<csv形式>")
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
