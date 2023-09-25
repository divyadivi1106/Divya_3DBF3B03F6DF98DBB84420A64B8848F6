class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students 


students = [
    Student("Ravi", "A101", 9.3),
    Student("Babu", "B102", 7.8),
    Student("Chandru", "C103", 8.0),
    Student("Dinesh", "D104", 8.5),
]

sorted_students = sort_students(students)


for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))