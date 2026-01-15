from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    address: str
    city: str
    phonno: int
    reviews:str
    added_cart:Added_to_cart
    buied_items:Buied_items


class Added_to_cart(BaseModel):
    item_id:int
    item_name:str
    item_price:int
    cutomer_id:int
    item_inStock:bool
class Buied_items(BaseModel):
     item_id:int
     item_name:str
     item_price:int
     cutomer_id:int
     item_inStock:bool
