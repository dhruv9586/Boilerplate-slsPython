from sqlalchemy import create_engine, text, Column, Integer, String, or_
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql
import json


endpoint = "alchemy.cdgkfoacvf6u.us-east-1.rds.amazonaws.com"
url = f"mysql+pymysql://admin:admin123@{endpoint}:3306/alchemy"
engine = create_engine(url)
session = sessionmaker(bind=engine)()

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    grade = Column(String(50))
    age = Column(Integer)

    def get(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


def create_table():
    Base.metadata.create_all(engine)
    return {
        "message": "Table successfully created!"
    }


def add_records():
    student1 = Student(name="Dhruv", age=24, grade="12th")
    student2 = Student(name="Mitesh", age=24, grade="10th")
    session.add_all([student1, student2])
    session.commit()
    return {
        "message": "Records successfully added!"
    }


def fetch_records():
    students = session.query(Student)
    print(students)
    response = []
    for student in students:
        print(f"Name : {student.name}, Age : {student.age}")
        response.append(student.get())
    return response


def handler(event, context):
    try:
        action = event["action"]
        switcher = {
            "create_table": create_table,
            "add_records": add_records,
            "fetch_records": fetch_records
        }

        response = "{'message': 'Action not found'}"
        if action in switcher:
            response = switcher[action]()
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    except Exception as error:
        print(error)
        body = {
            "message": "CRUD failed!!"
        }
        return {
            "statusCode": 400,
            "body": json.dumps(body)
        }


print(handler({"action": "fetch_records"}, ""))
