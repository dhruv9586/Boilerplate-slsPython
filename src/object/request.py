from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)
engine = create_engine("postgresql://postgres:dhruv@123@localhost:5432/alchemy")
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


Base.metadata.create_all(engine)
student1 = Student(name="Dhruv", age=24, grade="12th")
session.add(student1)
with engine.connect() as conn:
    result = conn.execute(text("SELECT * from student"))
    print(result)
    for row in result.mappings():
        print(row)
