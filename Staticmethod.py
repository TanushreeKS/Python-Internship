class Student:
    college_name = "ABC College"
    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name
    # Static Method
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"
    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("------------------")
# Create Objects
s1 = Student("Rahul", 101)
s2 = Student("Anita", 102)
# Display Before Change
s1.display()
s2.display()
# Change College Name Using Class Method
Student.change_college("XYZ College")
print("After Changing College Name")
# Display After Change
s1.display()
s2.display()
# Static Method Example
print("Rahul Result:", Student.is_pass(80))
print("Anita Result:", Student.is_pass(30))
