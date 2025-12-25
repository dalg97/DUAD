student_list = []
def add_student():
    full_name = input("Enter the full name: ")
    section_group = input("Enter the section group: ")
    spanish_grade = verify_grade("Spanish")
    english_grade = verify_grade("English")
    socials_grade = verify_grade("Socials")
    science_grade = verify_grade("Science")
    students = {}
    full_name = input("Enter the full name: ")
    section_group = input("Enter the section group: ")
    spanish_grade = verify_grade("Spanish")
    english_grade = verify_grade("English")
    socials_grade = verify_grade("Socials")
    science_grade = verify_grade("Science")
    total_grade = spanish_grade+english_grade+socials_grade+science_grade
    students['full_name'] = full_name
    students['section_group'] = section_group
    students['spanish_grade'] = spanish_grade
    students['english_grade'] = english_grade
    students['socials_grade'] = socials_grade
    students['science_grade'] = science_grade
    students['student_avg_grade'] = total_grade/4
    student_list.append(students)

def get_all_students():
    for index in student_list:
        for key,value in index.items():
            if key != 'student_avg_grade':
                print(f"{key}: {value}")
        print("---------------")

def get_top_3_students():
    sorted_list = sorted(student_list, key=lambda x: x['student_avg_grade'], reverse=True)
    top_3 = sorted_list[:3]
    for student in top_3:
        for key, value in student.items():
            if key == 'student_avg_grade' or key == 'full_name':
                print(f"{key}: {value}")
        print("---------------")

def get_total_avg():
    total_avg = 0
    for index in student_list:
        total_avg += index.get('student_avg_grade')
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

