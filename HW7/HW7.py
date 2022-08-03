from utils import *


def main():
    print("Введите номер студента")
    user_student_pk = int(input())

    student_by_pk = get_student_by_pk(user_student_pk)
    # Check student`s availability
    if not student_by_pk:
        quit("У нас нет такого студента")
    else:
        print(f"Студент {student_by_pk['full_name']}")
        print(f"Знает {' '.join(student_by_pk['skills'])}")

    print(f"Выберите специальность для оценки студента "
          f"{student_by_pk['full_name']}")
    user_profession_title = input()

    profession_by_title = get_profession_by_title(user_profession_title)

    # Check profession`s availability
    if not profession_by_title:
        quit("У нас нет такой специальности")
    else:
        fitness = check_fitness(student_by_pk, profession_by_title)
        print_fitness(student_by_pk['full_name'], fitness)


if __name__ == '__main__':
    main()
