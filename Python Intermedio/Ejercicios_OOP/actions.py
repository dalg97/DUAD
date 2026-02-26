student_list = []
class Student:
    def __init__(self, full_name, section_group, spanish_grade, english_grade, socials_grade, science_grade):
        self.full_name = full_name
        self.section_group = section_group
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade
        self.student_avg_grade = (spanish_grade + english_grade + socials_grade + science_grade) / 4

    def show_student_info(self,student):
        print(f"Full Name: {student.full_name}")
        print(f"Section Group: {student.section_group}")
        print(f"Spanish Grade: {student.spanish_grade}")
        print(f"English Grade: {student.english_grade}")
        print(f"Socials Grade: {student.socials_grade}")
        print(f"Science Grade: {student.science_grade}")
        print(f"Average Grade: {student.student_avg_grade}")
        

def add_student():
    full_name = input("Enter the full name: ")
    section_group = input("Enter the section group: ")
    spanish_grade = verify_grade("Spanish")
    english_grade = verify_grade("English")
    socials_grade = verify_grade("Socials")
    science_grade = verify_grade("Science")
    new_student = Student(full_name, section_group, spanish_grade, english_grade, socials_grade, science_grade)
    student_list.append(new_student)


def get_all_students():
    for index in student_list:
        index.show_student_info(index)
        print("---------------")

def get_top_3_students():
    sorted_list = sorted(student_list, key=lambda x: x.student_avg_grade, reverse=True)
    top_3 = sorted_list[:3]
    for student in top_3:
        student.show_student_info(student)
        print("---------------")

def get_total_avg():
    total_avg = 0
    for index in student_list:
        total_avg += index.student_avg_grade
    total = total_avg / len(student_list)
    print(f"The Total average is: {total}")

def verify_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Enter {subject_name} grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

