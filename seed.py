from faker import Faker
import random
from datetime import datetime, timedelta
from alchemy_models import Student, Group, Teacher, Subject, Grade
from db_connect import session

fake = Faker()

if __name__ == '__main__':
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        group = Group(group_name=group_name)
        session.add(group)
        session.commit()

    for _ in range(50):
        student_name = fake.name()
        group_id = random.randint(1, 3)
        student = Student(student_name=student_name, group_id=group_id)
        session.add(student)
        session.commit()

    for _ in range(3):
        teacher_name = fake.name()
        teacher = Teacher(teacher_name=teacher_name)
        session.add(teacher)
        session.commit()

    subjects = ['Math', 'Physics', 'Chemistry', 'History', 'Biology']
    for subject_name in subjects:
        teacher_id = random.randint(1, 3)
        subject = Subject(subject_name=subject_name, teacher_id=teacher_id)
        session.add(subject)
        session.commit()

    for student_id in range(1, 51):
        for gr in range(20):
            grade = Grade(student_id=student_id,
                          subject_id=random.randint(1, 5),
                          grade=random.randint(1, 100),
                          date=datetime.now()-timedelta(random.randint(1, 200))
                          )
            session.add(grade)
            session.commit()

    session.close()
