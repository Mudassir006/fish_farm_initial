from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


# User Model

class User(SQLModel, table=True,index=True):
    __tablename__ = "users"
    user_id: Optional[int] = Field(default=None, primary_key=True, )
    email: str = Field(unique=True)
    full_name: str
    gender: str
    password: str
    email_verified: bool = Field(default=False)
    disabled: bool = Field(default=True)
    role: str = Field(default='user')
    delivery_addresses: List['DeliveryAddress'] = Relationship(back_populates='user_relation')
    business_addresses: List['BusinessAddress'] = Relationship(back_populates='user_relation')
    author_relation: Optional['Author'] = Relationship(back_populates='user_relation')
    cart: Optional['Cart'] = Relationship(back_populates='user_relation')
    orders: List['Order'] = Relationship(back_populates='user_relation')


# address Models

class DeliveryAddress(SQLModel, table=True, index=True):
    __tablename__ = 'delivery_address'

    address_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key='users.user_id')
    city_id: int = Field(foreign_key='city.city_id')
    address : str
    phone : str
    coordinates : str
    city_relations:'City' = Relationship(back_populates='address')
    user_relation: 'User' = Relationship(back_populates='delivery_addresses')
    orders: List['Order'] = Relationship(back_populates='delivery_address_relation')


class BusinessAddress(SQLModel, table=True):
    __tablename__ = 'business_address'
    address_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key='users.user_id')
    city_id: int = Field(foreign_key='city.city_id')
    address: str
    phone: str
    coordinates: str
    user_relation: 'User' = Relationship(back_populates='business_addresses')


class City(SQLModel, table=True):
    __tablename__ = 'city'
    city_id: int = Field(primary_key=True)
    name: str
    abbrevation: str

    region_id: int = Field(foreign_key='region.region_id')
    status: bool = Field(default=True)
    address: 'DeliveryAddress' = Relationship(back_populates='city_relations')
    region_relation: 'Region' = Relationship(back_populates='cities')


class Region(SQLModel, table=True):
    __tablename__ = 'region'

    region_id: int = Field(primary_key=True)
    name: str
    country_id: int = Field(foreign_key='country.country_id')
    status: bool = Field(default=True)

    country_relation: 'Country' = Relationship(back_populates='regions')
    cities: List['City'] = Relationship(back_populates='region_relation')


class Country(SQLModel, table=True):
    __tablename__ = 'country'
    country_id: int = Field(primary_key=True)
    name: str
    aplha2_code: str
    country_code: str
    status: bool = Field(default=True)
    regions: List['Region'] = Relationship(back_populates='country_relation')


# blog Models

class Author(SQLModel, table=True):
    __tablename__ = 'authors'

    author_id: int = Field(primary_key=True, )
    user_id: int = Field(foreign_key='users.user_id')
    name: str
    title: str
    name_urdu: str
    title_urdu: str
    photo_url: str
    user_relation: Optional['User'] = Relationship(back_populates='author_relation')
    blogs: List['Blog'] = Relationship(back_populates='author_relation')


class Blog(SQLModel, table=True):
    __tablename__ = "blogs"
    blog_id: int = Field(primary_key=True, )
    image_url: str
    author_id: int = Field(foreign_key='authors.author_id')
    title: str
    slug: str = Field(unique=True)
    blog: str
    lang: str
    is_published: bool = Field(default=True)
    views: int = 0
    author_relation: 'Author' = Relationship(back_populates='blogs')


# Business Products


class BusinessProduct(SQLModel, table=True ,index=True):
    __tablename__ = 'business_product'
    business_product_id: int = Field(primary_key=True)
    business_id: int = Field(foreign_key='business.business_id')
    product_id: int = Field(foreign_key='product.product_id')
    product_source_id: int = Field(foreign_key='product_source.product_source_id')
    measuring_unit_id: int = Field(foreign_key='measuring_unit.measuring_unit_id')
    minimum_order: float
    maximum_order: float
    unit_price: float
    in_stock: bool = Field(default=True)
    status: bool = Field(default=True)
    business_relation: 'Business' = Relationship(back_populates='products')
    product_relation: 'Product' = Relationship(back_populates='business_products')
    product_source_relation: 'ProductSource' = Relationship(back_populates='products')
    measuring_unit_relation: 'MeasuringUnit' = Relationship(back_populates='products')
    processing_options: List['ProcessingOption'] = Relationship(back_populates='business_product')
    cart_obj_relation: 'CartItem' = Relationship(back_populates="business_product_relation")


class ProductSource(SQLModel, table=True):
    __tablename__ = 'product_source'
    product_source_id: int = Field(primary_key=True)
    source: str
    status: bool = Field(default=True)
    products: List['BusinessProduct'] = Relationship(back_populates='product_source_relation')


class MeasuringUnit(SQLModel, table=True):
    __tablename__ = 'measuring_unit'
    measuring_unit_id: int = Field(primary_key=True)
    name: str
    status: bool = Field(default=True)
    products: List['BusinessProduct'] = Relationship(back_populates='measuring_unit_relation')


class ProcessingOption(SQLModel, table=True):
    __tablename__ = 'processing_option'
    processing_option_id: int = Field(primary_key=True)
    business_product_id: int = Field(foreign_key='business_product.business_product_id')
    product_processing_id: int = Field(foreign_key='product_processing.product_processing_id')
    status: bool = Field(default=True)
    processing_option_relation :"ProductProcessing"= Relationship(back_populates='product_processings')

    business_product: 'BusinessProduct' = Relationship(back_populates='processing_options')


# Business APIS


class Business(SQLModel, table=True):
    __tablename__ = 'business'
    business_id: int = Field(primary_key=True)
    business_type_id: int = Field(foreign_key='business_type.business_type_id')
    name: str
    email: str
    website: str
    status: bool = Field(default=True)
    business_type_relation: 'BusinessType' = Relationship(back_populates='businesses')
    products: List['BusinessProduct'] = Relationship(back_populates='business_relation')
    managers: List['BusinessManger'] = Relationship(back_populates='business_relation')
    orders: List['Order'] = Relationship(back_populates='business_relation')


class BusinessType(SQLModel, table=True):
    __tablename__ = 'business_type'
    business_type_id: int = Field(primary_key=True)
    business_type: str
    status: bool = Field(default=True)
    businesses: List['Business'] = Relationship(back_populates='business_type_relation')


class BusinessManger(SQLModel, table=True):
    __tablename__ = 'business_manager'
    business_manager_id: int = Field(primary_key=True)
    business_id: int = Field(foreign_key='business.business_id')
    user_id: int = Field(foreign_key='users.user_id')
    business_relation: 'Business' = Relationship(back_populates='managers')


#  Carts Models

class Cart(SQLModel, table=True):
    __tablename__ = 'cart'
    cart_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key='users.user_id')
    user_relation: 'User' = Relationship(back_populates='cart')
    cart_items: List['CartItem'] = Relationship(back_populates='cart_relation')




class CartItem(SQLModel, table=True):
    __tablename__ = 'cart_item'
    cart_item_id: int = Field(primary_key=True)
    cart_id: int = Field(foreign_key='cart.cart_id')
    business_product_id: int = Field(foreign_key='business_product.business_product_id')
    processing_option_id: int = Field(foreign_key='processing_option.processing_option_id')
    quantity: float
    unit_price: float
    cart_relation: 'Cart' = Relationship(back_populates='cart_items')
    business_product_relation: List['BusinessProduct'] = Relationship(back_populates="cart_obj_relation")


# Order Models

class Order(SQLModel, table=True):
    __tablename__ = 'order'
    order_id: int = Field(primary_key=True)
    order_numer: int = Field(unique=True)
    user_id: int = Field(foreign_key='users.user_id')
    business_id: int = Field(foreign_key='business.business_id')
    delivery_address_id: int = Field(foreign_key='delivery_address.address_id')
    delivery_charges: float
    order_total: float
    discount: float
    total_amount: float
    instructions: str
    user_relation: 'User' = Relationship(back_populates='orders')
    business_relation: 'Business' = Relationship(back_populates='orders')
    delivery_address_relation: 'DeliveryAddress' = Relationship(back_populates='orders')
    order_items: List['OrderItem'] = Relationship(back_populates='order_relation')
    order_tracking: List['OrderTracking'] = Relationship(back_populates='order_relation')


class OrderItem(SQLModel, table=True):
    __tablename__ = 'order_item'
    order_item_id: int = Field(primary_key=True)
    order_id: int = Field(foreign_key='order.order_id')
    business_product_id: int = Field(foreign_key='business_product.business_product_id')
    processing_option_id: int = Field(foreign_key='processing_option.processing_option_id')
    quantity: float
    unit_price: float
    order_relation: 'Order' = Relationship(back_populates='order_items')


class OrderTracking(SQLModel, table=True):
    __tablename__ = 'order_tracking'
    order_tracking_id: int = Field(primary_key=True)
    order_id: int = Field(foreign_key='order.order_id')
    order_status_id: int = Field(foreign_key='order_status.order_status_id')
    remarks: str
    order_relation: 'Order' = Relationship(back_populates='order_tracking')
    order_status_relation: 'OrderStatus' = Relationship(back_populates='order_tracking_relation')


class OrderStatus(SQLModel, table=True):
    __tablename__ = 'order_status'
    order_status_id: int = Field(primary_key=True)
    order_status: bool
    order_tracking_relation: 'OrderTracking' = Relationship(back_populates='order_status_relation')


# Product Models

class ProductCategory(SQLModel, table=True):
    __tablename__ = 'product_category'
    product_category_id: int = Field(primary_key=True)
    product_category_name: str
    status: bool = Field(default=True)
    products: List['Product'] = Relationship(back_populates='product_category_relation')


class ProductImage(SQLModel, table=True):
    __tablename__ = 'product_image'
    product_image_id: int = Field(primary_key=True)
    file_id: str
    product_id: int = Field(foreign_key='product.product_id')
    status: bool = Field(default=True)
    product_relation: 'Product' = Relationship(back_populates='product_images')


class Product(SQLModel, table=True):
    __tablename__ = 'product'
    product_id: int = Field(primary_key=True)
    product_category_id: int = Field(foreign_key='product_category.product_category_id')
    name: str
    description: str
    status: bool = Field(default=True)
    business_products: List['BusinessProduct'] = Relationship(back_populates='product_relation')
    product_category_relation: 'ProductCategory' = Relationship(back_populates='products')
    product_images: List['ProductImage'] = Relationship(back_populates='product_relation')


class ProductProcessing(SQLModel, table=True,index=True):
    __tablename__ = 'product_processing'
    product_processing_id: int = Field(primary_key=True)
    product_processing: str
    product_processings:'ProcessingOption' = Relationship(back_populates="processing_option_relation")

    status: bool


class Photos(SQLModel, table=True):
    __tablename__ = 'photos'
    id: int = Field(primary_key=True)
    photo_name: str
    url: str
