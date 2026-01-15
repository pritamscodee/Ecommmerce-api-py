from orm_init import Base,engine
from sqlalchemy import Integer, String, Boolean, ForeignKey,List
from sqlalchemy.orm import Mapped, mapped_column, relationship
class Customer(Base):
    __tablename__ = "customers"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    address:Mapped[str]=mapped_column(String)
    city:Mapped[str]=mapped_column(String)
    phone_number:Mapped[int]=mapped_column(Integer)
    reviews:Mapped[str]=mapped_column(String)

    Added_cart:Mapped[List["Cart"]]=relationship(
         back_populates="customer_cart" )

    Buied_items:Mapped["Buieditems"]=relationship(
           back_populates="customer_buied"
    )

    
class Cart(Base):
    __tablename__ = "carts"
    item_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    item_name:Mapped[str]=mapped_column(String)
    item_price:Mapped[int]=mapped_column(Integer)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    item_Instock:Mapped[bool]=mapped_column(Boolean)

    customer_cart:Mapped["Customer"]=relationship(
        back_populates="Added_cart"
    ) 
     


class Buieditems(Base):
    __tablename__ = "buyiedItems"
    item_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    item_name:Mapped[str]=mapped_column(String)
    item_price:Mapped[int]=mapped_column(Integer)

    customer_buied:Mapped["Customer"]=relationship(
        back_populates="Buied_items"
    ) 


#-----------------------db creation--------------------------#
Base.metadata.create_all(bind=engine)
print("Tables created successfully!🚀🔥✅🎯🥳🎉💪")
#---------------------------------------------------------------#