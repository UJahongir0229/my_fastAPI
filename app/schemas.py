from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: int

class ProductOut(Product):
    pass

class Student(BaseModel):
    id: int
    name: str
    age: int
class StudentOut(Student):
    pass

class Car(BaseModel):
    id: int
    name: str
    price: int
class CarOut(Car):
    pass

class Computer(BaseModel):
    id: int
    name: str
    price: int
class ComputerOut(Computer):
    pass


