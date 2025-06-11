from fastapi import  HTTPException
from app.fakedb import  Computers
from app.schemas import  ComputerOut, Computer
from fastapi import APIRouter
router=APIRouter(prefix="/computers", tags=["Computers"])

@router.get("/computers", response_model=list[ComputerOut])
async def get_computers():
    return Computers
@router.post("/computers", response_model=ComputerOut)
async def add_computer(computer: Computer): 
    new_computer = computer.dict()
    Computers.append(new_computer)
    return new_computer
@router.delete("/computers/{computer_id}")
async def delete_computer(computer_id: int):
    global Computers
    Computers = [computer for computer in Computers if computer['id'] != computer_id]
    return {"message": "Computer deleted"}
@router.put("/computers/{computer_id}")
async def update_computer(computer_id: int, computer: Computer):
    for index, existing_computer in enumerate(Computers):
        if existing_computer['id'] == computer_id:
            updated_computer = computer.dict()
            updated_computer['id'] = computer_id 
            Computers[index] = updated_computer
            return {"message": "Computer updated successfully", "computer": updated_computer}
    raise HTTPException(status_code=404, detail="Computer not found")