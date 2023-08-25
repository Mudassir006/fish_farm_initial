from fastapi import HTTPException
from sqlmodel import select

import models
import schema
from database import Session
from exceptions import not_found_exception


def Creat_blog(blog: schema.Blog, session: Session):
    new_blog = models.Blog(title=blog.title, slug=blog.slug, blog=blog.blog, lang=blog.lang, author_id=blog.author_id)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)

    return new_blog


def Create_user(user: schema.User, session: Session):
    n_user = models.User(email=user.email, full_name=user.full_name, gender=user.gender, password=user.password,
                         role=user.role)
    session.add(n_user)
    session.commit()
    session.refresh(n_user)

    return n_user


def create_autor(author: schema.Author, session: Session):
    n_author = models.Author(name=author.name, title=author.title, title_urdu=author.title_urdu,
                             name_urdu=author.name_urdu, photo_url=author.photo_url, user_id=author.user_id)

    session.add(n_author)
    session.commit()
    session.refresh(n_author)

    return n_author


def delivery_address(address: schema.DeliveryAddress, session: Session):
    d_address = models.DeliveryAddress(address=address.address, phone=address.phone, coordinates=address.coordinates,
                                       city_id=address.city_id, user_id=address.user_id)

    session.add(d_address)
    session.commit()
    session.refresh(d_address)

    return d_address


def business_address(address: schema.BusinessAddress, session: Session):
    b_address = models.DeliveryAddress(address=address.address, phone=address.phone, coordinates=address.coordinates,
                                       city_id=address.city_id, user_id=address.user_id)

    session.add(b_address)
    session.commit()
    session.refresh(b_address)

    return b_address


def city(city: schema.City, session: Session):
    cityy = models.City(name=city.name, abbrevation=city.abbrevation, status=city.status, region_id=city.region_id)

    session.add(cityy)
    session.commit()
    session.refresh(cityy)
    return cityy


def region(region: schema.Region, session: Session):
    regi = models.Region(name=region.name, status=region.status, country_id=region.country_id)

    session.add(regi)
    session.commit()
    session.refresh(regi)

    return regi


def country(c: schema.Country, session: Session):
    count = models.Country(name=c.name, status=c.status, country_code=c.country_code,
                           aplha2_code=c.aplha2_code)

    session.add(count)
    session.commit()
    session.refresh(count)

    return count


def business(business: schema.Business, session: Session):
    bus = models.Business(name=business.name, email=business.email, website=business.website, status=business.status,
                          business_type_id=business.business_type_id)

    session.add(bus)
    session.commit()
    session.refresh(bus)


def business_type(bus_type: schema.BusinessType, session: Session):
    b_type = models.BusinessType(business_type=bus_type.business_type, status=bus_type.status)

    session.add(b_type)
    session.commit()
    session.refresh(b_type)

    return b_type


def business_manager(manager: schema.BusinessManager, session: Session):
    b_m = models.BusinessManger(business_id=manager.business_id, user_id=manager.user_id)
    session.add(b_m)
    session.commit()
    session.refresh(b_m)

    return b_m


def product_category(pc: schema.ProductCategory, session: Session):
    pec = models.ProductCategory(product_category_name=pc.product_category_name, status=pc.status)

    session.add(pec)
    session.commit()
    session.refresh(pec)

    return pec


def product_image(pi: schema.ProductImage, session: Session):
    pic = models.ProductImage(status=pi.status, file_id=pi.file_id, product_id=pi.product_id)

    session.add(pic)
    session.commit()
    session.refresh(pic)

    return pic


def product(p: schema.Product, session: Session):
    pro = models.Product(name=p.name, status=p.status, product_category_id=p.product_category_id)

    session.add(pro)
    session.commit()
    session.refresh(pro)

    return pro


def product_processing(prp: schema.ProductProcessing, session: Session):
    pip = models.ProductProcessing(product_processing=prp.product_processing, status=prp.status)

    session.add(pip)
    session.commit()
    session.refresh(pip)

    return pip


def business_product(bp: schema.BusinessProduct, session: Session):
    brp = models.BusinessProduct(minimum_order=bp.minimum_order, maximum_order=bp.maximum_order, in_stock=bp.in_stock,
                                 unit_price=bp.unit_price, business_id=bp.business_id, product_id=bp.product_id,
                                 product_source_id=bp.product_source_id, measuring_unit_id=bp.measuring_unit_id)

    session.add(brp)
    session.commit()
    session.refresh(brp)

    return brp


def product_source(ps: schema.ProductSource, session: Session):
    pos = models.ProductSource(source=ps.source)

    session.add(pos)
    session.commit()
    session.refresh(pos)


def measuring_unit(mu: schema.MeasuringUnit, s: Session):
    mis = models.MeasuringUnit(name=mu.name, status=mu.status)

    s.add(mis)
    s.commit()
    s.refresh(mis)

    return mis


def processing_option(po: schema.ProcessingOption, s: Session):
    pop = models.ProcessingOption(status=po.status, product_processing_id=po.product_processing_id,
                                  business_product_id=po.business_product_id)

    s.add(pop)
    s.commit()
    s.refresh(pop)

    return pop


def cart(cart: schema.Cart, s: Session):
    caart = models.Cart(user_id=cart.user_id)

    s.add(caart)
    s.commit()
    s.refresh(caart)

    return caart


def cart_item(cat: schema.CartItem, s: Session):
    catim = models.CartItem(quantity=cat.quantity, unit_price=cat.unit_price, cart_id=cat.cart_id,
                            business_product_id=cat.business_product_id, processing_option_id=cat.processing_option_id)
    s.add(catim)
    s.commit()
    s.refresh(catim)

    return catim


def order(order: schema.Order, s: Session):
    ord = models.Order(order_numer=order.order_numer, delivery_charges=order.delivery_charges, discount=order.discount,
                       order_total=order.order_total, instructions=order.instructions, user_id=order.user_id,
                       business_id=order.business_id, delivery_address_id=order.delivery_address_id,
                       total_amount=order.total_amount)

    s.add(ord)
    s.commit()
    s.refresh(ord)

    return ord


def order_item(oitem: schema.OrderItem, s: Session):
    item = models.OrderItem(quantity=oitem.quantity, unit_price=oitem.unit_price,
                            business_product_id=oitem.business_product_id, order_id=oitem.order_id,
                            processing_option_id=oitem.processing_option_id)

    s.add(item)
    s.commit()
    s.refresh(item)

    return item


def order_tracking(ot: schema.OrderTracking, s: Session):
    track = models.OrderTracking(remarks=ot.remarks, order_id=ot.order_id, order_status_id=ot.order_status_id)

    s.add(track)
    s.commit()
    s.refresh(track)

    return track


def order_status(os: schema.OrderStatus, s: Session):
    stat = models.OrderStatus(order_status=os.order_status)

    s.add(stat)
    s.commit()
    s.add(stat)

    return stat


# ...............................Read Methods...............................#

def read_blog(session: Session, id: int):
    return session.query(models.Blog).filter(models.Blog.blog_id == id).first()


def read_user(session: Session, id: int):
    return session.query(models.User).filter(models.User.user_id == id).first()


def read_author(session: Session, id: int):
    return session.query(models.Author).filter(models.Author.author_id == id).first()


def read_d_address(session: Session, id: int):
    return session.query(models.DeliveryAddress).filter(models.DeliveryAddress.address_id == id).first()


def read_b_address(session: Session, id: int):
    return session.query(models.BusinessAddress).filter(models.BusinessAddress.address_id == id).first()


def read_city(session: Session, id: int):
    return session.query(models.City).filter(models.City.city_id == id).first()


def read_region(session: Session, id: int):
    return session.query(models.Region).filter(models.Region.region_id == id).first()


def read_country(session: Session, id: int):
    return session.query(models.Country).filter(models.Country.country_id == id).first()


def read_business(session: Session, id: int):
    return session.query(models.Business).filter(models.Business.business_id == id).first()


def read_business_type(session: Session, id: int):
    return session.query(models.BusinessType).filter(models.BusinessType.business_type_id == id).first()


def read_business_manager(session: Session, id: int):
    return session.query(models.BusinessManger).filter(models.BusinessManger.business_manager_id == id).first()


def read_product_category(session: Session, id: int):
    return session.query(models.ProductCategory).filter(models.ProductCategory.product_category_id == id).first()


def read_product_image(session: Session, id: int):
    return session.query(models.ProductImage).filter(models.ProductImage.product_image_id == id).first()


def read_product(session: Session, id: int):
    return session.query(models.Product).filter(models.Product.product_id == id).first()


def read_product_processing(session: Session, id: int):
    return session.query(models.ProductProcessing).filter(models.ProductProcessing.product_processing_id == id).first()


def read_business_product(session: Session, id: int):
    return session.query(models.BusinessProduct).filter(models.BusinessProduct.business_product_id == id).first()


def read_source(session: Session, id: int):
    return session.query(models.ProductSource).filter(models.ProductSource.product_source_id == id).first()


def read_unit(session: Session, id: int):
    return session.query(models.MeasuringUnit).filter(models.MeasuringUnit.measuring_unit_id == id).first()


def read_processing_option(session: Session, id: int):
    return session.query(models.ProcessingOption).filter(models.ProductProcessing.product_processing_id == id).first()


def read_cart(session: Session, id: int):
    return session.query(models.Cart).filter(models.Cart.cart_id == id).first()


def read_cart_item(session: Session, id: int):
    return session.query(models.CartItem).filter(models.CartItem.cart_item_id == id).first()


def read_order(session: Session, id: int):
    return session.query(models.Order).filter(models.Order.order_id == id).first()


def read_order_item(session: Session, id: int):
    return session.query(models.OrderItem).filter(models.OrderItem.order_item_id == id).first()


def read_order_tracking(session: Session, id: int):
    return session.query(models.OrderTracking).filter(models.OrderTracking.order_tracking_id == id).first()


def read_order_status(session: Session, id: int):
    return session.query(models.OrderStatus).filter(models.OrderStatus.order_status_id == id).first()


# ................................................................Delete Methods....................................#


def delete_user(db: Session, id: int):
    del_obj = db.query(models.User).filter(models.User.user_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_author(db: Session, id: int):
    del_obj = db.query(models.Author).filter(models.Author.author_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_blog(db: Session, id: int):
    del_obj = db.query(models.Blog).filter(models.Blog.blog_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_d_address(db: Session, id: int):
    del_obj = db.query(models.DeliveryAddress).filter(models.DeliveryAddress.address_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_b_address(db: Session, id: int):
    del_obj = db.query(models.Business).filter(models.BusinessAddress.address_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_city(db: Session, id: int):
    del_obj = db.query(models.City).filter(models.City.city_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_region(db: Session, id: int):
    del_obj = db.query(models.Region).filter(models.Region.region_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_country(db: Session, id: int):
    del_obj = db.query(models.Country).filter(models.Country.country_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_business(db: Session, id: int):
    del_obj = db.query(models.Business).filter(models.Business.business_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_btype(db: Session, id: int):
    del_obj = db.query(models.BusinessType).filter(models.BusinessType.business_type_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_bmanager(db: Session, id: int):
    del_obj = db.query(models.BusinessManger).filter(models.BusinessManger.business_manager_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_pcategory(db: Session, id: int):
    del_obj = db.query(models.ProductCategory).filter(models.ProductCategory.product_category_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_source(db: Session, id: int):
    del_obj = db.query(models.ProductSource).filter(models.ProductSource.product_source_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_pimage(db: Session, id: int):
    del_obj = db.query(models.ProductImage).filter(models.ProductImage.product_image_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_product(db: Session, id: int):
    del_obj = db.query(models.Product).filter(models.Product.product_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_bproduct(db: Session, id: int):
    del_obj = db.query(models.BusinessProduct).filter(models.BusinessProduct.business_product_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_unit(db: Session, id: int):
    del_obj = db.query(models.MeasuringUnit).filter(models.MeasuringUnit.measuring_unit_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_poption(db: Session, id: int):
    del_obj = db.query(models.ProcessingOption).filter(models.ProcessingOption.processing_option_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_cart(db: Session, id: int):
    del_obj = db.query(models.Cart).filter(models.Cart.cart_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_citem(db: Session, id: int):
    del_obj = db.query(models.CartItem).filter(models.CartItem.cart_item_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_order(db: Session, id: int):
    del_obj = db.query(models.Order).filter(models.Order.order_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_oitem(db: Session, id: int):
    del_obj = db.query(models.OrderItem).filter(models.OrderItem.order_item_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


def delete_otracking(db: Session, id: int):
    del_obj = db.query(models.OrderTracking).filter(models.OrderTracking.order_tracking_id == id).first()
    if del_obj is None:
        raise not_found_exception
    db.delete(del_obj)
    db.commit()


# ......................Search Somethings.........................#


def search_blogs(db: Session, name: str):
    query = select(models.Blog).where(models.Blog.title.ilike("%{}%".format(name)))
    return db.exec(query).all()


def search_region(db: Session, name: str):
    query = select(models.Region).where(models.Region.name.ilike("%{}%".format(name)))
    return db.exec(query).all()


def search_city(db: Session, name: str):
    query = select(models.City).where(models.City.name.ilike("%{}%".format(name)))
    return db.exec(query).all()


def search_country(db: Session, name: str):
    query = select(models.Country).where(models.Country.name.ilike("%{}%".format(name)))
    return db.exec(query).all()


# ...............................Update_method.....................#


def update_user(obj: schema.UpdateUser, session: Session, id):
    new_user = session.get(models.User, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_author(obj: schema.UpdateAuthor, session: Session, id):
    new_author = session.get(models.Author, id)
    if not new_author:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_author, key, value)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


def update_blog(obj: schema.UpdateBlog, session: Session, id):
    new_blog = session.get(models.Blog, id)
    if not new_blog:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_blog, key, value)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)
    return new_blog


def update_d_address(obj: schema.UpdateDaddress, session: Session, id):
    new_d_address = session.get(models.DeliveryAddress, id)
    if not new_d_address:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_d_address, key, value)
    session.add(new_d_address)
    session.commit()
    session.refresh(new_d_address)
    return new_d_address


def update_b_address(obj: schema.UpdateBaddress, session: Session, id):
    new_b_address = session.get(models.BusinessAddress, id)
    if not new_b_address:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_b_address, key, value)
    session.add(new_b_address)
    session.commit()
    session.refresh(new_b_address)
    return new_b_address


def update_city(obj: schema.UpdateCity, session: Session, id):
    new_city = session.get(models.City, id)
    if not new_city:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_city, key, value)
    session.add(new_city)
    session.commit()
    session.refresh(new_city)
    return new_city


def update_region(obj: schema.UpdateRegion, session: Session, id):
    new_region = session.get(models.Region, id)
    if not new_region:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_region, key, value)
    session.add(new_region)
    session.commit()
    session.refresh(new_region)
    return new_region


def update_country(obj: schema.UpdateCountry, session: Session, id):
    new_country = session.get(models.Country, id)
    if not new_country:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_country, key, value)
    session.add(new_country)
    session.commit()
    session.refresh(new_country)
    return new_country


def update_business(obj: schema.UpdateBusiness, session: Session, id):
    new_business = session.get(models.Business, id)
    if not new_business:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_business, key, value)
    session.add(new_business)
    session.commit()
    session.refresh(new_business)
    return new_business


def update_btype(obj: schema.UpdateBtype, session: Session, id):
    new_user = session.get(models.BusinessType, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_p_category(obj: schema.UpdatePcategory, session: Session, id):
    new_user = session.get(models.ProductCategory, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_pimage(obj: schema.UpdatePimage, session: Session, id):
    new_user = session.get(models.ProductImage, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_product(obj: schema.UpdateProduct, session: Session, id):
    new_user = session.get(models.Product, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_processing(obj: schema.UpdatePprocessing, session: Session, id):
    new_user = session.get(models.ProductProcessing, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_bproduct(obj: schema.UpdateBproduct, session: Session, id):
    new_user = session.get(models.BusinessProduct, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_source(obj: schema.UpdateSource, session: Session, id):
    new_user = session.get(models.ProductSource, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_unit(obj: schema.Updateunit, session: Session, id):
    new_user = session.get(models.MeasuringUnit, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_cart_item(obj: schema.UpdateCartItem, session: Session, id):
    new_user = session.get(models.CartItem, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_order(obj: schema.UpdateOrder, session: Session, id):
    new_user = session.get(models.Order, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_oitem(obj: schema.UpdateOItem, session: Session, id):
    new_user = session.get(models.OrderItem, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_tracking(obj: schema.UpdateOItracking, session: Session, id):
    new_user = session.get(models.OrderTracking, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_ostatus(obj: schema.UpdateOStatus, session: Session, id):
    new_user = session.get(models.OrderStatus, id)
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = obj.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(new_user, key, value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
