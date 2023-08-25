from typing import Optional

from pydantic import BaseModel


class Blog(BaseModel):
    author_id: Optional[int]
    title: str
    slug: Optional[str]
    blog: str
    lang: str

    class Config:
        orm_mode = True


class Author(BaseModel):
    user_id: Optional[int]
    name: str
    title: str
    name_urdu: str
    title_urdu: str
    photo_url: str

    class Config:
        orm_mode = True


class User(BaseModel):
    email: str
    full_name: str
    gender: str
    password: str
    role: str

    class Config:
        orm_mode = True


class DeliveryAddress(BaseModel):
    user_id: Optional[int]
    city_id: Optional[int]
    address: str
    phone: str
    coordinates: str

    class Config:
        orm_mode = True


class BusinessAddress(BaseModel):
    user_id: Optional[int]
    city_id: Optional[int]
    address: str
    phone: str
    coordinates: str

    class Config:
        orm_mode = True


class City(BaseModel):
    name: str
    abbrevation: str
    status: Optional[bool]
    region_id: Optional[int]

    class Config:
        orm_mode = True


class Region(BaseModel):
    country_id: Optional[int]
    name: str
    status: bool

    class Config:
        orm_mode = True


class Country(BaseModel):
    name: str
    country_code: str
    aplha2_code: str
    status: Optional[bool]

    class Config:
        orm_mode = True


class BusinessProduct(BaseModel):
    business_id: Optional[int]
    product_id: Optional[int]
    product_source_id: Optional[int]
    measuring_unit_id: Optional[int]
    minimum_order: float
    maximum_order: float
    unit_price: float
    in_stock: Optional[bool]

    class Config:
        orm_mode = True


class ProductSource(BaseModel):
    source: str

    class Config:
        orm_mode = True


class MeasuringUnit(BaseModel):
    name: str
    status: Optional[bool]

    class Config:
        orm_mode = True


class ProcessingOption(BaseModel):
    business_product_id: Optional[int]
    product_processing_id: Optional[int]
    status: Optional[bool]

    class Config:
        orm_mode = True


class Business(BaseModel):
    name: str
    email: str
    website: str
    status: Optional[bool]
    business_type_id: Optional[int]

    class Config:
        orm_mode = True


class BusinessType(BaseModel):
    business_type: str
    status: Optional[bool]

    class Config:
        orm_mode = True


class BusinessManager(BaseModel):
    business_id: Optional[int]
    user_id: Optional[int]

    class Config:
        orm_mode = True


class Cart(BaseModel):
    user_id: Optional[int]

    class Config:
        orm_mode = True


class CartItem(BaseModel):
    cart_id: Optional[int]
    business_product_id: Optional[int]
    processing_option_id: Optional[int]
    quantity: float
    unit_price: float

    class Config:
        orm_mode = True


class Order(BaseModel):
    order_numer: int
    delivery_charges: float
    total_amount: int
    discount: float
    order_total: float
    instructions: str
    user_id: Optional[int]
    business_id: Optional[int]
    delivery_address_id: Optional[int]

    class Config:
        orm_mode = True


class OrderItem(BaseModel):
    quantity: float
    unit_price: float
    business_product_id: Optional[int]
    processing_option_id: Optional[int]
    order_id: Optional[int]

    class Config:
        orm_mode = True


class OrderTracking(BaseModel):
    order_id: Optional[int]
    order_status_id: Optional[int]
    remarks: str

    class Config:
        orm_mode = True


class OrderStatus(BaseModel):
    order_status: Optional[bool]

    class Config:
        orm_mode = True


class ProductCategory(BaseModel):
    product_category_name: str
    status: Optional[bool]

    class Config:
        orm_mode = True


class ProductImage(BaseModel):
    product_id: Optional[int]
    file_id: int
    status: Optional[bool]

    class Config:
        orm_mode = True


class Product(BaseModel):
    product_category_id: Optional[int]
    name: str
    status: Optional[bool]

    class Config:
        orm_mode = True


class ProductProcessing(BaseModel):
    product_processing: str

    status: Optional[bool]

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):

    email: str
    gender: str
    full_name: str
    password: str
    disabled:bool
    email_verified:bool

    class Config:
        orm_mode = True


class UpdateAuthor(BaseModel):
    name: str
    title: str
    name_urdu: str
    title_urdu: str

    class Config:
        orm_mode = True


class UpdateBlog(BaseModel):
    title: str
    blog: str
    lang: str

    class Config:
        orm_mode = True


class UpdateDaddress(BaseModel):
    address: str
    phone: str
    coordinates: str

    class Config:
        orm_mode = True


class UpdateBaddress(BaseModel):
    address: str
    phone: str
    coordinates: str

    class Config:
        orm_mode = True


class UpdateCity(BaseModel):
    name: str
    abbrevation: str

    class Config:
        orm_mode = True


class UpdateCountry(BaseModel):
    name: str
    aplha2_code: str
    country_code: str

    class Config:
        orm_mode = True


class UpdateRegion(BaseModel):
    name: str
    status: bool

    class Config:
        orm_mode = True


class UpdateBusiness(BaseModel):
    name: str
    email: str
    website: str
    status: bool

    class Config:
        orm_mode = True


class UpdateBtype(BaseModel):
    business_type: str
    status: str

    class Config:
        orm_mode = True


class UpdatePcategory(BaseModel):
    product_category_name: str
    status: bool

    class Config:
        orm_mode = True


class UpdatePimage(BaseModel):
    status: bool

    class Config:
        orm_mode = True


class UpdateProduct(BaseModel):
    name: str
    status: bool

    class Config:
        orm_mode = True


class UpdatePprocessing(BaseModel):
    product_prcocessing: str
    status: bool

    class Config:
        orm_mode = True


class UpdateBproduct(BaseModel):
    minimum_order: str
    maximum_order: str
    unit_price: str
    in_stock: bool
    status: bool

    class Config:
        orm_mode = True


class UpdateSource(BaseModel):
    source: str
    status: bool

    class Config:
        orm_mode = True


class Updateunit(BaseModel):
    name: str
    status: bool

    class Config:
        orm_mode = True


class UpdateCartItem(BaseModel):
    quantity: float
    unit_price: float

    class Config:
        orm_mode = True


class UpdateOrder(BaseModel):
    delivery_charges: float
    order_total: float
    discount: float
    total_amount: float
    instructions: str

    class Config:
        orm_mode = True


class UpdateOItem(BaseModel):
    quantity: float
    unit_price: float

    class Config:
        orm_mode = True


class UpdateOItracking(BaseModel):
    remarks: str

    class Config:
        orm_mode = True


class UpdateOStatus(BaseModel):
    order_status: bool

    class Config:
        orm_mode = True
