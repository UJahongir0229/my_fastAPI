from fastapi import  HTTPException
from app.fakedb import products
from app.schemas import Product, ProductOut
from fastapi import APIRouter
router=APIRouter(prefix="/products", tags=["Products"])

@router.get("/products", response_model=list[ProductOut])
async def get_products():
    return products

@router.post("/products", response_model=ProductOut)
async def add_product(product: Product): 
    new_product = product.dict()
    products.append(new_product)
    return new_product  

@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    global products
    products = [product for product in products if product['id'] != product_id]
    return {"message": "Product deleted"} 

@router.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    for index, existing_product in enumerate(products):
        if existing_product['id'] == product_id:
            updated_product = product.dict()
            updated_product['id'] = product_id 
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    raise HTTPException(status_code=404, detail="Product not found") 