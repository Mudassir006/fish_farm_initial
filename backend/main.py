import os
import shutil
from typing import List

import jwt
from fastapi import FastAPI, Depends, Form, File, HTTPException
from fastapi import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from keycloak import KeycloakOpenID
from sqlmodel import select
from starlette import status

import crud
import database
import models
import schema
from database import Session, get_session
from exceptions import not_found_exception

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    realm_name="fishfarmpk",
    client_id="test-1",
)

app = FastAPI()
database.main()
app.mount('/static', StaticFiles(directory='static'), name='static')

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)



ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def decode_token(token: str):
    try:
        payload = jwt.decode(jwt=token, options={"verify_signature": False})
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


# print(keycloak_openid.userinfo(token['access_token']))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/all_cities')
async def all_city(session: Session = Depends(get_session)):
    return session.query(models.City).all()


@app.get('/all_countries')
async def all_countries(session: Session = Depends(get_session)):
    return session.query(models.Country).all()


@app.get('/all_regions')
async def all_region(session: Session = Depends(get_session)):
    return session.query(models.Region).all()


@app.get('/all_products', response_model=List[schema.Product])
async def all_products(session: Session = Depends(get_session)):
    r = session.exec(select(models.Product).offset(0).limit(100)).all()
    return r


@app.get('/all_blogs', response_model=List[schema.Blog])
async def all_blogs(session: Session = Depends(get_session)):
    r = session.exec(select(models.Blog).offset(0).limit(100)).all()
    return r


@app.get('/all_orders')
async def all_orders(session: Session = Depends(get_session)):
    return session.query(models.Order).all()


@app.get('/all_business_products', response_model=List[schema.BusinessProduct1])
async def all_business_products(session: Session = Depends(get_session)):
    r = session.exec(select(models.BusinessProduct).offset(0).limit(100)).all()
    return r


@app.get('/all_business')
async def all_business(session: Session = Depends(get_session)):
    return session.query(models.Business).all()


@app.get('/all_cart_items', response_model=List[schema.Cart])
async def all_cart_items(session: Session = Depends(get_session)):
    r = session.exec(select(models.Cart).offset(0).limit(100)).all()
    return r


# ................................................Post Methods.............................#


@app.post("/create_blog/")
async def create_blog(author_id: int = Form(...), title: str = Form(...), blog: str = Form(...),

                      slug: str = Form(...), lang: str = Form(...),
                      file: UploadFile = File(...), session: database.Session = Depends(get_session)):
    # Save image locally

    upload_dir = os.path.join(os.getcwd(), "../frontend/public")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)

    db_image = models.Photos(photo_name=file.filename, url=f'/{file.filename}')
    session.add(db_image)
    session.commit()
    session.refresh(db_image)

    # Create entry in database for the blog
    image_url = f"/{file.filename}"

    blog = models.Blog(author_id=author_id, title=title, blog=blog, lang=lang, slug=slug,
                       image_url=image_url)
    session.add(blog)
    session.commit()

    return {"File Name": file.filename}


@app.post('/create_user')
async def create_user(user: schema.User1, session: Session = Depends(get_session)):
    new = crud.Create_user(user, session)
    return {'ser': new}


@app.post('/delivery_address')
async def delivery_address(address: schema.DeliveryAddress, session: Session = Depends(get_session)):
    add = crud.delivery_address(address, session)
    return {"delivery": add}


@app.post('/business_address')
async def business_address(address: schema.BusinessAddress, session: Session = Depends(get_session)):
    add = crud.business_address(address, session)
    return {"delivery": add}


@app.post('/create_city')
async def create_city(city: schema.City, session: Session = Depends(get_session)):
    add_city = crud.city(city, session)
    return {'city': add_city}


@app.post('/create_region')
async def create_region(reg: schema.Region, session: Session = Depends(get_session)):
    add_region = crud.region(reg, session)

    return {"Region": add_region}


@app.post('/create_country')
async def create_country(country: schema.Country, session: Session = Depends(get_session)):
    add_country = crud.country(country, session)

    return {"Country": add_country}


@app.post('/add_business')
async def add_business(business: schema.Business, session: Session = Depends(get_session)):
    add = crud.business(business, session)

    return {"Details": add}


@app.post('/add_business_type')
async def add_business_type(business_type: schema.BusinessType,
                            session: Session = Depends(get_session)):
    add_type = crud.business_type(business_type, session)

    return {"Business_type": add_type}


@app.post('/add_business_manager')
async def business_manager(manager: schema.BusinessManager, session: Session = Depends(get_session)):
    c = crud.business_manager(manager, session)

    return {"manager": c}


@app.post('/add_product_category')
async def product_category(pc: schema.ProductCategory, session: Session = Depends(get_session)):
    cat = crud.product_category(pc, session)

    return {"Product Category": cat}


@app.post('/add_product_image')
async def add_product_image(session: database.Session = Depends(get_session), product_id: int = Form(...),
                            status: bool = Form(...), file: UploadFile = File(...)):
    upload_dir = os.path.join(os.getcwd(), "../frontend/public")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)

    db_image = models.Photos(photo_name=file.filename, url=f"/{file.filename}")
    session.add(db_image)
    session.commit()

    # Create entry in database for the blog
    file_url = f"/{file.filename}"
    pic = models.ProductImage(status=status, file_id=file_url, product_id=product_id)

    session.add(pic)
    session.commit()
    session.refresh(pic)

    return pic


@app.post('/add_product')
async def add_product(prod: schema.Product, session: Session = Depends(get_session)):
    p = crud.product(prod, session)

    return {"Product": p}


@app.post('/product_processing')
async def product_processing(prp: schema.ProductProcessing, session: Session = Depends(get_session)):
    pip = crud.product_processing(prp, session)

    return {"processing": pip}


@app.post('/add_business_product')
async def add_business_product(bp: schema.BusinessProduct, session: Session = Depends(get_session)):
    abp = crud.business_product(bp, session)

    return {"Business Product": abp}


@app.post('/add_source')
async def add_source(sour: schema.ProductSource, session: Session = Depends(get_session)):
    s = crud.product_source(sour, session)

    return {"Source": s}


@app.post('/add_unit')
async def add_unit(au: schema.MeasuringUnit, session: Session = Depends(get_session)):
    add = crud.measuring_unit(au, session)

    return {"Unit": add}


@app.post('/processing_option')
async def processing_option(po: schema.ProcessingOption1, session: Session = Depends(get_session)):
    pro = crud.processing_option(po, session)

    return {"Option": pro}


@app.post('/cart')
async def cart(cart: schema.Cart1, session: Session = Depends(get_session), ):
    c = crud.cart(cart, session)

    return {"Cart": c}


@app.post('/cart_item')
async def cart_item(ci: schema.CartItem1, token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    decoded_token = decode_token(token)

    user_id = decoded_token.get("sub")
    user_name = decoded_token.get("name")
    print(user_id, user_name, decoded_token.get('email'))
    print(decoded_token.get('preferred_username'))

    caart = crud.cart_item(ci, session)

    return {"message": caart}


@app.post('/add_order')
async def add_order(ao: schema.Order, session: Session = Depends(get_session)):
    order = crud.order(ao, session)

    return {"Order": order}


@app.post('/order_item')
async def order_item(oi: schema.OrderItem, session: Session = Depends(get_session)):
    item = crud.order_item(oi, session)

    return {"Item": item}


@app.post('/order_tracking')
async def order_tracking(ot: schema.OrderTracking, session: Session = Depends(get_session)):
    track = crud.order_tracking(ot, session)

    return {"Track": track}


@app.post('/order_status')
async def order_status(os: schema.OrderStatus, session: Session = Depends(get_session)):
    stat = crud.order_status(os, session)

    return {"Status": stat}


# ................................Get Methods..............................#


@app.get("/blog/name/{name}", response_model=list[schema.Blog])
def search_blog(name: str, db: Session = Depends(get_session)):
    db_dept = crud.search_blogs(db, name)
    if db_dept is None:
        raise not_found_exception
    return db_dept


@app.get("/city/name/{name}", response_model=list[schema.City])
def search_city(name: str, db: Session = Depends(get_session)):
    db_dept = crud.search_city(db, name)
    if db_dept is None:
        raise not_found_exception
    return db_dept


@app.get("/country/name/{name}", response_model=list[schema.Country])
def search_country(name: str, db: Session = Depends(get_session)):
    db_dept = crud.search_country(db, name)
    if db_dept is None:
        raise not_found_exception
    return db_dept


@app.get("/region/name/{name}", response_model=list[schema.Region])
def search(name: str, db: Session = Depends(get_session)):
    db_dept = crud.search_region(db, name)
    if db_dept is None:
        raise not_found_exception
    return db_dept


@app.get("/blog/id/{id}", response_model=schema.Blog)
def get_blog(id: int, session: Session = Depends(get_session)):
    blog = crud.read_blog(session, id)
    if blog is None:
        raise not_found_exception
    return blog


@app.get("/user/id/{id}", response_model=schema.User)
def get_user(id: int, session: Session = Depends(get_session)):
    user = crud.read_user(session, id)
    if user is None:
        raise not_found_exception
    return user


@app.get("/author/id/{id}", response_model=schema.Author)
def get_author(id: int, session: Session = Depends(get_session)):
    author = crud.read_author(session, id)
    if author is None:
        raise not_found_exception
    return author


@app.get("/delivery_address/id/{id}", response_model=models.DeliveryAddress)
def get_d_address(id: int, session: Session = Depends(get_session)):
    x = crud.read_d_address(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/business_address/id/{id}", response_model=schema.BusinessAddress)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_b_address(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/city/id/{id}", response_model=schema.City)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_city(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/region/id/{id}", response_model=schema.Region)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_region(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/country/id/{id}", response_model=schema.Country)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_country(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/business/id/{id}", response_model=schema.Business)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_business(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/business_type/id/{id}", response_model=schema.BusinessType)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_business_type(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/manager/id/{id}", response_model=schema.BusinessManager)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_business_manager(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/product_category/id/{id}", response_model=schema.ProductCategory)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_product_category(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/product_image/id/{id}", response_model=schema.ProductImage)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_product_image(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/product/id/{id}", response_model=schema.Product)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_product(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/product_processing/id/{id}", response_model=schema.ProductProcessing)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_product_processing(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/business_product/id/{id}", response_model=schema.BusinessProduct)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_business_product(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/source/id/{id}", response_model=schema.ProductSource)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_source(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/unit/id/{id}", response_model=schema.MeasuringUnit)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_unit(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/processing_option/id/{id}", response_model=schema.ProcessingOption)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_processing_option(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/cart/id/{id}", response_model=schema.Cart )
def get_user(id: int, session: Session = Depends(get_session),token: str = Depends(oauth2_scheme)):
    decoded_token = decode_token(token)
    print(decoded_token.get('name'))
    x = crud.read_cart(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/cart_item/id/{id}", response_model=schema.CartItem)
def get_user(id: int, session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    decoded_token = decode_token(token)
    print(decoded_token.get('name'))
    x = crud.read_cart_item(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/order/id/{id}", response_model=schema.Order1)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_order(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/order_item/id/{id}", response_model=schema.OrderItem)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_order_item(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/order_tracking/id/{id}", response_model=schema.OrderTracking)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_order_tracking(session, id)
    if x is None:
        raise not_found_exception
    return x


@app.get("/order_status/id/{id}", response_model=schema.OrderStatus)
def get_user(id: int, session: Session = Depends(get_session)):
    x = crud.read_order_status(session, id)
    if x is None:
        raise not_found_exception
    return x


# .............................................Delete Methods................................#

@app.delete("/delete_user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_session)):
    crud.delete_user(db, id)


@app.delete("/delete_author/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id: int, db: Session = Depends(get_session)):
    crud.delete_author(db, id)


@app.delete("/delete_blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_session)):
    crud.delete_blog(db, id)


@app.delete("/delete_d_address/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_daddress(id: int, db: Session = Depends(get_session)):
    crud.delete_d_address(db, id)


@app.delete("/delete_b_address/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_b_address(id: int, db: Session = Depends(get_session)):
    crud.delete_b_address(db, id)


@app.delete("/delete_city/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_city(id: int, db: Session = Depends(get_session)):
    crud.delete_city(db, id)


@app.delete("/delete_region/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_region(id: int, db: Session = Depends(get_session)):
    crud.delete_region(db, id)


@app.delete("/delete_country/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(id: int, db: Session = Depends(get_session)):
    crud.delete_country(db, id)


@app.delete("/delete_business/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_business(id: int, db: Session = Depends(get_session)):
    crud.delete_business(db, id)


@app.delete("/delete_btype/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_btype(id: int, db: Session = Depends(get_session)):
    crud.delete_btype(db, id)


@app.delete("/delete_bmanager/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bmanager(id: int, db: Session = Depends(get_session)):
    crud.delete_bmanager(db, id)


@app.delete("/delete_pcategory/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pcategory(id: int, db: Session = Depends(get_session)):
    crud.delete_pcategory(db, id)


@app.delete("/delete_pimage/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pimage(id: int, db: Session = Depends(get_session)):
    crud.delete_pimage(db, id)


@app.delete("/delete_product/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_session)):
    crud.delete_product(db, id)


@app.delete("/delete_bproduct/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bproduct(id: int, db: Session = Depends(get_session)):
    crud.delete_bproduct(db, id)


@app.delete("/delete_source/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_source(id: int, db: Session = Depends(get_session)):
    crud.delete_source(db, id)


@app.delete("/delete_unit/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_unit(id: int, db: Session = Depends(get_session)):
    crud.delete_unit(db, id)


@app.delete("/delete_poption/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_poption(id: int, db: Session = Depends(get_session)):
    crud.delete_poption(db, id)


@app.delete("/delete_cart/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cart(id: int, db: Session = Depends(get_session)):
    crud.delete_cart(db, id)


@app.delete("/delete_citem/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_citem(id: int, db: Session = Depends(get_session)):
    crud.delete_citem(db, id)


@app.delete("/delete_order/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id: int, db: Session = Depends(get_session)):
    crud.delete_order(db, id)


@app.delete("/delete_oitem/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_oitem(id: int, db: Session = Depends(get_session)):
    crud.delete_oitem(db, id)


@app.delete("/delete_otracking/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_otracking(id: int, db: Session = Depends(get_session)):
    crud.delete_otracking(db, id)


@app.patch('/update_user/{id}')
async def update_user(id: int, obj: schema.UpdateUser, session: Session = Depends(get_session)):
    new_user = crud.update_user(obj, session, id)

    return {"Updated User": new_user}


@app.patch('/update_author/{id}')
async def update_author(id: int, obj: schema.UpdateAuthor, session: Session = Depends(get_session)):
    new_user = crud.update_author(obj, session, id)

    return {"Updated Author": new_user}


@app.patch('/update_blog/{id}')
async def update_blog(id: int, obj: schema.UpdateBlog, session: Session = Depends(get_session)):
    new_user = crud.update_blog(obj, session, id)

    return {"Updated Blog": new_user}


@app.patch('/update_delivey_address/{id}')
async def update_delivery_address(id: int, obj: schema.UpdateDaddress, session: Session = Depends(get_session)):
    new_user = crud.update_d_address(obj, session, id)

    return {"Updated Delivey Address": new_user}


@app.patch('/update_business_address/{id}')
async def update_business_address(id: int, obj: schema.UpdateBaddress, session: Session = Depends(get_session)):
    new_user = crud.update_b_address(obj, session, id)

    return {"Updated Business Address": new_user}


@app.patch('/update_city/{id}')
async def update_city(id: int, obj: schema.UpdateCity, session: Session = Depends(get_session)):
    new_user = crud.update_city(obj, session, id)

    return {"Updated City": new_user}


@app.patch('/update_country/{id}')
async def update_country(id: int, obj: schema.UpdateCountry, session: Session = Depends(get_session)):
    new_user = crud.update_country(obj, session, id)

    return {"Updated Country": new_user}


@app.patch('/update_region/{id}')
async def update_region(id: int, obj: schema.UpdateRegion, session: Session = Depends(get_session)):
    new_user = crud.update_region(obj, session, id)

    return {"Updated Region": new_user}


@app.patch('/update_business/{id}')
async def update_business(id: int, obj: schema.UpdateBusiness, session: Session = Depends(get_session)):
    new_user = crud.update_business(obj, session, id)

    return {"Updated Business": new_user}


@app.patch('/update_btype/{id}')
async def update_business_types(id: int, obj: schema.UpdateBtype, session: Session = Depends(get_session)):
    new_user = crud.update_btype(obj, session, id)

    return {"Updated Type": new_user}


@app.patch('/update_category/{id}')
async def update_category(id: int, obj: schema.UpdatePcategory, session: Session = Depends(get_session)):
    new_user = crud.update_p_category(obj, session, id)

    return {"Updated Category": new_user}


@app.patch('/update_image/{id}')
async def update_product_image(id: int, obj: schema.UpdatePimage, session: Session = Depends(get_session)):
    new_user = crud.update_pimage(obj, session, id)

    return {"Updated Product Image": new_user}


@app.patch('/update_product/{id}')
async def update_product(id: int, obj: schema.UpdateProduct, session: Session = Depends(get_session)):
    new_user = crud.update_product(obj, session, id)

    return {"Updated Product": new_user}


@app.patch('/update_processing/{id}')
async def update_processing(id: int, obj: schema.UpdatePprocessing, session: Session = Depends(get_session)):
    new_user = crud.update_processing(obj, session, id)

    return {"Updated Product Processing": new_user}


@app.patch('/update_business_product/{id}')
async def update_business_product(id: int, obj: schema.UpdateBproduct, session: Session = Depends(get_session)):
    new_user = crud.update_bproduct(obj, session, id)

    return {"Updated Business Product": new_user}


@app.patch('/update_source/{id}')
async def update_source(id: int, obj: schema.UpdateSource, session: Session = Depends(get_session)):
    new_user = crud.update_source(obj, session, id)

    return {"Updated Source": new_user}


@app.patch('/update_unit/{id}')
async def update_unit(id: int, obj: schema.Updateunit, session: Session = Depends(get_session)):
    new_user = crud.update_unit(obj, session, id)

    return {"Updated Unit": new_user}


@app.patch('/update_cart_item/{id}')
async def update_cart_item(id: int, obj: schema.UpdateCartItem, session: Session = Depends(get_session)):
    new_user = crud.update_cart_item(obj, session, id)

    return {"Updated CartItem": new_user}


@app.patch('/update_order/{id}')
async def update_order(id: int, obj: schema.UpdateOrder, session: Session = Depends(get_session)):
    new_user = crud.update_order(obj, session, id)

    return {"Updated Order": new_user}


@app.patch('/update_tracking/{id}')
async def update_tracking(id: int, obj: schema.UpdateOItracking, session: Session = Depends(get_session)):
    new_user = crud.update_tracking(obj, session, id)

    return {"Updated User": new_user}


@app.patch('/update_order_status/{id}')
async def update_status(id: int, obj: schema.UpdateOStatus, session: Session = Depends(get_session)):
    new_user = crud.order_status(obj, session ,id)

    return {"Updated Status": new_user}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, session: database.Session = Depends(get_session)):
    upload_dir = os.path.join(os.getcwd(), "../frontend/images")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    # copy the file contents
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data = models.Photos(photo_name=file.filename, url=f'frontend/images/{file.filename}')
    session.add(data)
    session.commit()
    session.refresh(data)

    return {"filename": file.filename}


@app.get('/read_images')
async def read_all_images(session: database.Session = Depends(get_session)):
    return session.query(models.Photos).all()


@app.post("/create_author/")
async def create_author(user_id: int = Form(...), title: str = Form(...), name: str = Form(...),
                        name_urdu: str = Form(...), title_urdu: str = Form(...),
                        file: UploadFile = File(...), session: database.Session = Depends(get_session)):
    # Save image locally

    upload_dir = os.path.join(os.getcwd(), "../frontend/public")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)

    db_image = models.Photos(photo_name=file.filename, url=f'/{file.filename}')
    session.add(db_image)
    session.commit()
    session.refresh(db_image)

    # Create entry in database for the blog
    image_url = f"/{file.filename}"

    blog = models.Author(user_id=user_id, title=title, name=name, title_urdu=title_urdu, name_urdu=name_urdu,
                         photo_url=image_url)
    session.add(blog)
    session.commit()

    return {"File Name": file.filename}
