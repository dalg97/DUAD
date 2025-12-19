from actions import *
from data import *
student_list = []
def show_menu():
    print("""
    1. Add a new student
    2. See all students
    3. See top 3 students
    4. See the grade average in total
    5. Export students in CSV
    6. Import new students
    7. Exit""")
    option = int(input("Enter an option: "))
    if option == 1:
        add_student()
    elif option == 2:
        print(student_list)
        get_all_students(student_list)
    elif option == 3:
        get_top_3_students()
    elif option == 4:
        get_total_avg(student_list)
    elif option == 5:
        export_students()
    elif option == 6:
        import_students()
    elif option == 7:
        exit()

show_menu()