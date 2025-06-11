from fastapi import  HTTPException
from app.fakedb import Students
from app.schemas import StudentOut, Student
from fastapi import APIRouter
router=APIRouter(prefix="/students", tags=["students"])

@router.get("/students", response_model=list[StudentOut])
async def get_students():
    return Students

@router.post("/students", response_model=StudentOut)
async def add_student(student: Student): 
    new_student = student.dict()
    Students.append(new_student)
    return new_student
@router.delete("/students/{student_id}")
async def delete_student(student_id: int):
    global Students
    Students = [student for student in Students if student['id'] != student_id]
    return {"message": "Student deleted"}
@router.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    for index, existing_student in enumerate(Students):
        if existing_student['id'] == student_id:
            updated_student = student.dict()
            updated_student['id'] = student_id 
            Students[index] = updated_student
            return {"message": "Student updated successfully", "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")