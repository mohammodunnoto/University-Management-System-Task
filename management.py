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
        self.mentors = []
    
    def set_student_details(self):
        self.studentid = input("Please enter the student's Student ID:\n")
        self.course = input("Please enter the student's course:\n")
    
    def add_grades(self):
        while True:
            gradenum = input("How many grades of the student will you enter?\n")
            if gradenum.isdigit():
                for i in gradenum:
                    n = 1
                    while n <= int(gradenum):
                        grade = input(f"Please enter the student's grade #{n}.\n")
                        if grade.isdigit():
                            self.grades.append(int(grade))
                            n += 1
                break
            else:
                print("Please enter a number.")
    
    def calculate_average_grade(self):
        gradenum = len(self.grades)
        totalgrades = sum(self.grades)
        if gradenum == 0:
            average = "Grades Not Available"
        else:
            average = totalgrades / gradenum
        print(f"The average grade is: {average}.")
        return average

    def get_mentor(self, Professor):
        if self.name in Professor.mentored_students:
            print(f"The student is being mentored by {Professor.name}")
        else:
            print(f"The student is not being mentored by {Professor.name}.")

    def get_student_summary(self):
        av = Student.calculate_average_grade(self)
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.studentid}, Course: {self.course}, Average Grade: {av}.")

class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staffid = staff_id
        self.department = department
        self.salary = salary
        self.mentored_students = []

    
    def set_professor_details(self):
        self.staffid = input("Enter the Staff ID:\n")
        self.department = input("Enter the department:\n")
        self.salary = input("Enter the salary:\n")
    
    def give_feedback(self, Student, feedback):
        print(f"Feedback for {Student.name}: {feedback}")

    def mentor_student(self, Student):
        print(f"Professor {self.name} is now mentoring {Student.name} on {Student.course}.")
        self.mentored_students.append(Student.name)
        Student.mentors.append(self.name)
    
    def get_mentored_students(self):
        for student in self.mentored_students:
            print(f"Professor {self.name} is tutoring {student}.")


    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + (percentage / 100))
        print(f"The professor's new salary is {self.salary}.")
        return self.salary
    
    def get_professor_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Staff ID: {self.staffid}, Department: {self.department}, Salary: £{self.salary}")
    
class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.adminid = admin_id
        self.office = office
        self.yearsofservice = years_of_service
    
    def set_admin_details(self):
        self.adminid = input("Enter the Admin ID:\n")
        self.office = input("Enter the Office Location:\n")
        self.yearsofservice = input("Enter the Years of Service:\n")
    
    def increment_service_years(self):
        self.yearsofservice += 1
        print(f"The new years of service is: {self.yearsofservice}.")
    
    def get_admin_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Admin ID: {self.adminid}, Office: {self.office}, Years of Service: {self.yearsofservice}")
    
student1 = Student("Bob", 20, "Male", "S1234", "Maths")
student2 = Student("James", 20, "Male", "S2345", "Physics")
professor1 = Professor("Mr Hank", 38, "Male", "P1234", "Maths", 55000)
professor2 = Professor("Dr Kate", 54, "Female", "P2345", "Physics", 60000)
administrator1 = Administrator("Mr Tom", 43, "Male", "A1234", "Room 101", 5)
student1.add_grades()
student1.calculate_average_grade()
professor1.give_feedback(student1,"Good work")
professor2.increase_salary(10)
administrator1.increment_service_years()
student1.get_student_summary()
student2.get_student_summary()
professor1.get_professor_summary()
professor2.get_professor_summary()
administrator1.get_admin_summary()
professor1.mentor_student(student1)
professor2.mentor_student(student1)
professor2.mentor_student(student2)
professor1.get_mentored_students()
professor2.get_mentored_students()
student1.get_mentor(professor1)
student1.get_mentor(professor2)
student2.get_mentor(professor1)
student2.get_mentor(professor2)
professor1.get_mentored_students()
professor2.get_mentored_students()