from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base



engine=create_engine("sqlite:///crud.db",echo=True)
Base=declarative_base()
sessions=sessionmaker(bind=engine)

session=sessions()

class Employee(Base):
    __tablename__="Employee"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    salary=Column(Integer)
    lastname=Column(String)
    phone=Column(Integer)
    def __init__(self,name,age,salary,lastname,phone):
        self.name=name
        self.age = age
        self.salary = salary
        self.lastname = lastname
        self.phone = phone

Base.metadata.create_all(engine)

employee1=Employee(name="ali",age="22",salary=4500000,lastname="dastourian",phone=45555555)
employee2=Employee(name="reza",age="22",salary=4500033,lastname="rezaii",phone=5555555)

session.add(employee1)
session.add(employee2)
session.commit()