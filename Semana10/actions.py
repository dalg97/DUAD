def add_student():
    global student_list
    students = {}
    full_name = input("Enter the full name: ")
    section_group = input("Enter the section group: ")
    spanish_grade = int(input("Enter Spanish grade: "))
    english_grade = int(input("Enter English grade: "))
    socials_grade = int(input("Enter Socials grade: "))
    science_grade = int(input("Enter Science grade: "))
    total_grade = spanish_grade+english_grade+socials_grade+science_grade
    students['full_name'] = full_name
    students['section_group'] = section_group
    students['spanish_grade'] = spanish_grade
    students['english_grade'] = english_grade
    students['socials_grade'] = socials_grade
    students['science_grade '] = science_grade
    students['student_avg_grade'] = total_grade/4
    student_list.append(students)
    return student_list

def get_all_students(student_list):
    for index in student_list:
        for key,value in index.items():
            print(f"{key}: {value}")

def get_top_3_students():
    print("code the logic here")

def get_total_avg(student_list):
    total_avg = 0
    for index in student_list:
        total_avg += index.get('student_avg_grade')
    print(f"The Total average is: {total_avg}")