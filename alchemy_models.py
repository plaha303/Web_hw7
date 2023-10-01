from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from db_connect import session

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)


session.close()
