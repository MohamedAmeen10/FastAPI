from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    name: str
    age: int

# Use a dictionary to simulate a database
students_db: Dict[int, Student] = {
    1: Student(name="steve", age=21),
}

app = FastAPI()

@app.get("/")
async def example():
    return {'Hello': 'World'}

@app.get("/studentid/{stud_id}")
async def get_student(stud_id: int):
    student = students_db.get(stud_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/getbyname")
async def get_student_by_name(name: str):
    for student in students_db.values():
        if student.name == name:
            
            return student
    return {"data": "not found"}

@app.post("/createstudent/{stud_id}")
async def create_student(stud_id: int, student: Student):
    if stud_id in students_db:
        raise HTTPException(status_code=400, detail="Student already exists")
    students_db[stud_id] = student
    return student

@app.put("/updatestudent/{stud_id}")
async def update_student(stud_id: int, student: Student):
    if stud_id not in students_db:
        raise HTTPException(status_code=404, detail="Student does not exist")
    students_db[stud_id] = student
    return student


@app.delete("/deletestudent/{stud_id}")
async def delete_student(stud_id: int):
    if stud_id not in students_db:
        raise HTTPException(status_code=404, detail="Student does not exist")
    del students_db[stud_id]
    return {"detail": "Student deleted successfully"}
@app.get("/students/")
async def get_all_students():
    return students_db