class Person:
    def __init__(self, name, age):
        self.myname = name
        self.myage = age

    def __str__(self):
        return "Name: " + self.myname + "\nAge: " + str(self.myage)

    def get_myName(self):
        return self.myname

    def get_myAge(self):
        return self.myage


class Student(Person):
    total = 0

    def __init__(self, person, math_grade, eng_grade):
        super().__init__(person.get_myName(), person.get_myAge())
        self.math_grade = math_grade
        self.eng_grade = eng_grade
        Student.total += 1

    def set_math_grade(self, math_grade):
        self.math_grade = math_grade

    def set_eng_grade(self, eng_grade):
        self.eng_grade = eng_grade

    def get_math_grade(self):
        return self.math_grade

    def get_eng_grade(self):
        return self.eng_grade

    def get_score_average(self):
        return (self.math_grade + self.eng_grade) / 2

    def __str__(self):
        return super().__str__() + f"\nMath Grade: {self.math_grade}\nEnglish Grade: {self.eng_grade}\n"

p1 = Person("Steve Jobs", 25)
p2 = Person("Liam Lee", 50)
p3 = Person("Seokyul Yoon", 60)

std1 = Student(p1, 80, 90)
std2 = Student(p2, 100, 100)
std3 = Student(p3, 0, 0)

print(std1)
print(std2)
print(std3)

std3.set_eng_grade(10)
std3.set_math_grade(20)
print(std3.get_myName(), ":\nMath: ", std3.get_math_grade(), " and English: ", std3.get_eng_grade())

print(p1.get_myName(), "test score average:", std1.get_score_average())
print(p2.get_myName(), "test score average:", std2.get_score_average())
print(p3.get_myName(), "test score average:", std3.get_score_average())

if Student.total < 1:
    print("We have one student.")
elif Student.total > 1:
    print("We have", Student.total, "students.")
else:
    print("We don't have any students here.")
