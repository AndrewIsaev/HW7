import os
import json
from typing import Union, Any


def load_students() -> list:
    """
    Load students`s list from students.json
    :return list
    """
    student_dir = os.path.join("Data", "students.json")
    with open(student_dir, encoding='utf-8') as file:
        students_data = json.load(file)
    return students_data


def load_professions() -> list:
    """
    Load profession`s list from professions.json
    :return list
    """
    prof_dir = os.path.join("Data", "professions.json")
    with open(prof_dir, encoding='utf-8') as file:
        professions_data = json.load(file)
    return professions_data


def get_student_by_pk(pk: int) -> Union[bool, Any]:
    """
    Get dict with student data by his pk
    """
    for student in load_students():
        if student["pk"] == pk:
            return student
    return False


def get_profession_by_title(title: str) -> Union[bool, Any]:
    """
    Get dict with profession data by title
    """
    for profession in load_professions():
        if profession["title"].lower() == title.lower():
            return profession
    return False


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Get student dict and profession dict return dictionary example:
    {
      "has": ["Python", "Linux"],
      "lacks": ["Docker, SQL"],
      "fit_percent": 50
    }
    """
    user_set = set(student["skills"])
    prof_set = set(profession["skills"])
    fit_percent = len(user_set.intersection(prof_set)) / len(prof_set) * 100
    return {"has": list(user_set.intersection(prof_set)),
            "lacks": list(set(prof_set).difference(set(user_set))),
            "fit_percent": fit_percent
            }


def print_fitness(student: str, fitness_dict: dict) -> None:
    """
    Print fitness
    """
    print(f"Пригодность {int(fitness_dict['fit_percent'])}%")
    print(f"{student} знает {', '.join(fitness_dict['has'])}")
    print(f"{student} не знает {', '.join(fitness_dict['lacks'])}")
