import os
import json


def load_students() -> list:
    """
    Load student`s list from students.json
    return: list
    """
    student_dir = os.path.join("Data", "students.json")
    with open(student_dir, encoding='utf-8') as file:
        students_data = json.load(file)
    return students_data


def load_professions() -> list:
    """
       Load profession`s list from professions.json
       return: list
    """
    prof_dir = os.path.join("Data", "professions.json")
    with open(prof_dir, encoding='utf-8') as file:
        professions_data = json.load(file)
    return professions_data


def get_student_by_pk(pk: int) -> dict:
    """
    Get dict with student data by his pk
    """
    student_dict = {}
    for student in load_students():
        if student["pk"] == pk:
            student_dict[student["full_name"]] = student["skills"]
    return student_dict


def get_profession_by_title(title: str) -> dict:
    """
        Get dict with profession data by title
    """
    prof_dict = {}
    for profession in load_professions():
        if profession["title"] == title:
            prof_dict[profession["title"]] = profession["skills"]
    return prof_dict


def check_fitness(student, profession) -> dict:
    """

    """
    user_set = set(list(student.values())[0])
    prof_set = set(list(profession.values())[0])
    fit_percent = len(user_set.intersection(prof_set)) / len(prof_set) * 100
    return {"has": list(user_set.intersection(prof_set)),
            "lacks": list(set(prof_set).difference(set(user_set))),
            "fit_percent": fit_percent
            }


def print_fitness(student, fitness_dict):
    print(f"Пригодность {int(fitness_dict['fit_percent'])}%")
    print(f"{student} знает {', '.join(fitness_dict['has'])}")
    print(f"{student} не знает {', '.join(fitness_dict['lacks'])}")
