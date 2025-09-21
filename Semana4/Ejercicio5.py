amount_grades = int(input("Ingrese la cantidad de notas: "))
counter = 1
under_70 = 0
above_70 = 0
under_average = 0
above_average = 0
total_average = 0
while counter <= amount_grades:
    grade = int(input(f"Ingrese la nota{counter}: "))
    if grade < 70:
        under_70 = under_70 + 1
        under_average = under_average + grade
    else:
        above_70 = above_70 + 1
        above_average = above_average + grade
    total_average = total_average + (grade/amount_grades)
    counter = counter + 1

if under_70 != 0:
    under_average = under_average / under_70

if above_70 != 0:
    above_average = above_average / above_70

print(f"El estudiante tiene {above_70} notas aprobadas")
print(f"El promedio de notas aprobadas es {above_average}")
print(f"El estudiantes tiene {under_70} notas desaprobadas")
print(f"El promedio de notas desaprobadas es {under_average}")
print(f"El promedio total es {total_average}")
        