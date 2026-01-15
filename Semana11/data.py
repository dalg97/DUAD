import csv 
from actions import student_list, Student

file_name = 'students.csv'
def export_students():
    students_dict = {}
    new_student_list = []
    if not student_list:
        print("No students to export")
        return
    for index in student_list:
        students_dict['full_name'] = index.full_name
        students_dict['section_group'] = index.section_group
        students_dict['spanish_grade'] = index.spanish_grade
        students_dict['english_grade'] = index.english_grade
        students_dict['socials_grade'] = index.socials_grade
        students_dict['science_grade'] = index.science_grade
        students_dict['student_avg_grade'] = index.student_avg_grade
        new_student_list.append(students_dict)

    with open(file_name, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['full_name', 'section_group', 'spanish_grade', 'english_grade', 'socials_grade', 'science_grade', 'student_avg_grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in new_student_list:
            writer.writerow(student)
    print("Exported successfully")

def import_students():
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list.clear()
            for row in reader:
                new_student = Student(
                    row['full_name'],
                    row['section_group'],
                    int(row['spanish_grade']),
                    int(row['english_grade']),
                    int(row['socials_grade']),
                    int(row['science_grade'])
                )
                student_list.append(new_student)
        print("Imported successfully")
    except FileNotFoundError:
        print("CSV file not found, export the students first")