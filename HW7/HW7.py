from utils import *

print("Введите номер студента")
user_student_pk = int(input())
student_by_pk = get_student_by_pk(user_student_pk)

for student, skills in student_by_pk.items():
    print(f"Студент {student}")
    print(f"Знает {' '.join(skills)}")

print(f"Выберите специальность для оценки студента {student}")
user_profession_title = input()
profession_by_title = get_profession_by_title(user_profession_title)

fitness = check_fitness(student_by_pk, profession_by_title)

print_fitness(student, fitness)
