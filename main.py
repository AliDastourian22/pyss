from tkinter import *
from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base

engine=create_engine("sqlite:///ttkj.db",echo=True)
Base=declarative_base()
sessions=sessionmaker(bind=engine)

session=sessions()



class Employee(Base):
    __tablename__="Employee"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

    def __init__(self,name,age):
        self.name=name
        self.age = age




Base.metadata.create_all(engine)

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWiget()

    def createWiget(self):
        self.txtname=Entry(self.master)
        self.txtname.place(x=50,y=160)
        self.namelbl=Label(self.master,text="name")
        self.namelbl.place(x=10,y=160)
        self.txtage=Entry(self.master)
        self.txtage.place(x=50,y=50)
        self.agelbl=Label(self.master,text="age")
        self.agelbl.place(x=10,y=50)

        self.btn=Button(self.master,text="register",command=self)
        self.btn.place(x=20,y=90)
    def OnclickRegister(self):
        employee1=Employee(name=self.txtname.get(),age=self.txtage.get())
        self.Register(employee1)
    def Register(self,value):
        sessions.add(value)
        sessions.commit()
if __name__ == '__main__':
     root=Tk()
     root.geometry('600x400')
     app = Application(master=root)

     root.mainloop()