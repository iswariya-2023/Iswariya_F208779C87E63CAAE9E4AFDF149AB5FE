def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
students_list = [
    Student("Arun", "2022001", 2.9),
    Student("Bala", "2022002", 3.7),
    Student("Anitha", "2022003", 4.9),
    Student("Chandra", "2022004", 4.7)
]
sorted_students = sort_students(students_list)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
