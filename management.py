class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = input("Please enter the person's name:\n")
        self.age = input("Please enter the person's age:\n")
        self.gender = input("Please enter the person's gender:\n")
    
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}.")
    
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.studentid = student_id
        self.course = course
        self.grades = []
    
    def set_student_details(self, student_id, course):
        self.studentid = input("Please enter the student's Student ID:\n")
        self.course = input("Please enter the student's course:\n")
    
    def add_grades(self):
        while True:
            gradenum = input("How many grades of the student will you enter?\n")
            if gradenum.isdigit():
                for i in gradenum:
                    n = 1
                    while True:
                        grade = input(f"Please enter the student's grade #{n}.")
                        if grade.isdigit():
                            self.grades.append(grade)
                            n += 1
            else:
                print("Please enter a number.")
    
    def calculate_average_grade(self):
        gradenum = len(self.grades)
        totalgrades = sum(self.grades)
        average = totalgrades / gradenum
        print(f"The average grade is {average}.")
        return average

    def get_student_summary(self):
        av = Student.calculate_average_grade()
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.studentid}, Course: {self.course}, Average Grade: {av}.")