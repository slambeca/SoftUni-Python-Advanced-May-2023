count_students = int(input())

students = {}

for _ in range(count_students):
    current_student_args = input().split()

    name = current_student_args[0]
    grade = float(current_student_args[1])

    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

for key, values in students.items():
    average_grade = sum(values) / len(values)
    print(f"{key} ->", end=" ")
    for value in values:
        print(f'{value:.2f}', end=" ")
    print(f"(avg: {average_grade:.2f})")

# # Variant 2
# n = int(input())
#
# students_data = {}
#
# for _ in range(n):
#     student_name, grade = input().split(' ')
#
#     if student_name not in students_data:
#         students_data[student_name] = []
#
#     students_data[student_name].append(float(grade))
#
# for student, grades in students_data.items():
#     convert_grades_to_string = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
#     average_grade = sum(grades) / len(grades)
#     print(f"{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})")

# Variant 3
# n = int(input())
#
# student_grades = {}
#
# for _ in range(n):
#     name, grade = tuple(input().split())
#     grade = float(grade)
#
#     if name not in student_grades.keys():
#         student_grades[name] = []
#     student_grades[name].append(grade)
#
# for student, grades in student_grades.items():
#     avg = sum(grades) / len(grades)
#     print(f"{student} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg:.2f})")
