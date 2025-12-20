import csv 
from actions import student_list

file_name = 'students.csv'
def export_students():
    if not student_list:
        print("No students to export")
        return
    with open(file_name, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['full_name', 'section_group', 'spanish_grade', 'english_grade', 'socials_grade', 'science_grade', 'student_avg_grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student)  
    print("Exported successfully")

def import_students():
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list.clear()
            for row in reader:
                row['full_name'] = row['full_name']
                row['section_group'] = row['section_group']
                row['spanish_grade'] = int(row['spanish_grade'])
                row['english_grade'] = int(row['english_grade'])
                row['socials_grade'] = int(row['socials_grade'])
                row['science_grade'] = int(row['science_grade'])
                row['student_avg_grade'] = float(row['student_avg_grade'])
                student_list.append(row)
        print("Imported successfully")
    except FileNotFoundError:
        print("CSV file not found, export the students first")