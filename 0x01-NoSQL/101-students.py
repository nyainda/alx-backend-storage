#!/usr/bin/env python3
""" 101-main """


def top_students(mongo_collection):
    """
    Returns the top students of a given collection
    """
    students = list(mongo_collection.find())
    for student in students:
        student['averageScore'] = sum(topic.get('score')
                                      for topic in student.get(
            'topics')) / len(student.get('topics'))

    students.sort(key=lambda student: student.get('averageScore'),
                  reverse=True)
    return students
