class Person:
    def __init__(self, name, age):
        self.name = name # private
        self.age = age

    def __str__(self):
        return f"{self.name} has age {self.age}"

    def print_marks(self):
        print("Grade is A")


class Student(Person):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

    def __str__(self):
        return super().__str__()+f" {self.city}"

    def print_marks(self):
        print("Grade is B")

x = Person("John Doe", 30)
y = Student("Abraham Lincon", 60, "Mumbai")

print(x)
print(y)
x.print_marks()
y.print_marks()
