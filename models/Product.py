from pydantic import BaseModel

class Product(BaseModel):
    id:str
    product_name:str
    product_price:int
    usecase:list

    class Config:
        allow_population_by_field_name = True
   
    

   