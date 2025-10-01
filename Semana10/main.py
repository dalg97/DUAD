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
        get_all_students()
    elif option == 3:
        get_top_3_students()
    elif option == 4:
        get_total_avg()
    elif option == 5:
        export_students()
    elif option == 6:
        import_students()
    elif option == 7:
        exit()

def add_student():
    print("code the logic here")

def export_students():
    print("code the logic here")

def import_students():
    print("code the logic here")

def get_all_students():
    print("code the logic here")

def get_top_3_students():
    print("code the logic here")

def get_total_avg():
    print("code the logic here")

show_menu()