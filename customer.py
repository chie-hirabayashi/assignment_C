class Customer:
    def __init__(self, first_name, family_name, age):
        self.num1 = first_name
        self.num2 = family_name
        self.age = age

    def full_name(self):
        return f"{self.num1} {self.num2}"

    def entry_free(self):
        if self.age <= 3:
            return "無料"
        if 3 < self.age < 20:
            return 1000
        if 20 <= self.age < 65:
            return 1500
        if 65 <= self.age < 75:
            return 1200
        if 75 <= self.age:
            return 500

    def info_csv(self):
        return f"{self.full_name()}, {self.age}, {self.entry_free()}"

    def info_tab(self):
        return f"{self.full_name()} {self.age} {self.entry_free()}"

    def info_pype(self):
        return f"{self.full_name()}|{self.age}|{self.entry_free()}"


ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
mika = Customer("Mika", "kobayashi", 3)
clint = Customer("Clint", "Eastwood", 92)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


print("<フルネーム>")
print(ken.full_name())
print(tom.full_name())
print(ieyasu.full_name())
print(mika.full_name())
print(clint.full_name())
print(sep="")


print("<年齢>")
print(ken.age)
print(tom.age)
print(ieyasu.age)
print(mika.age)
print(clint.age)
print(sep="")

print("<入場料>")
print(ken.entry_free())
print(tom.entry_free())
print(ieyasu.entry_free())
print(mika.entry_free())
print(clint.entry_free())
print(sep="")

print("<csv形式>")
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(mika.info_csv())
print(clint.info_csv())
print(sep="")

print("<tab形式>")
print(tom.info_tab())
print(ken.info_tab())
print(ieyasu.info_tab())
print(mika.info_tab())
print(clint.info_tab())
print(sep="")

print("<pype形式>")
print(tom.info_pype())
print(ken.info_pype())
print(ieyasu.info_pype())
print(mika.info_pype())
print(clint.info_pype())
