class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Name: {self._name}"


class Student(Person):
    def get_info(self):
        return f"Student name: {self._name}"


person = Person("Samira")
student = Student("Papuri")

print(person.get_info())
print(student.get_info())
