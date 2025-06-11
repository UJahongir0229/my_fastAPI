from fastapi import  HTTPException
from app.fakedb import  Cars
from app.schemas import CarOut,Car
from fastapi import APIRouter
router=APIRouter(prefix="/cars", tags=["cars"])

@router.get("/cars", response_model=list[CarOut])
async def get_cars():
    return Cars
@router.post("/cars", response_model=CarOut)
async def add_car(car: Car): 
    new_car = car.dict()
    Cars.append(new_car)
    return new_car
@router.delete("/cars/{car_id}")
async def delete_car(car_id: int):
    global Cars
    Cars = [car for car in Cars if car['id'] != car_id]
    return {"message": "Car deleted"}
@router.put("/cars/{car_id}")
async def update_car(car_id: int, car: Car):
    for index, existing_car in enumerate(Cars):
        if existing_car['id'] == car_id:
            updated_car = car.dict()
            updated_car['id'] = car_id 
            Cars[index] = updated_car
            return {"message": "Car updated successfully", "car": updated_car}
    raise HTTPException(status_code=404, detail="Car not found")