# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence)/ len(sequence)

# print(average(student["grades"]))



class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (89, 90, 93, 78, 90)

    

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob")
print(student.name)
print(student.grades)
print(student.average_grade())