# Base Class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Child Class 1
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


# Child Class 2
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        self.display_person()
        print("Sport:", self.sport_name)


# Hybrid Child Class
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        self.display_student()
        print("Sport:", self.sport_name)
        print("College:", self.college_name)


# Object Creation
cs = CollegeStudent("Rahul", "S123", "Cricket", "ABC College")

cs.display_college_student()
