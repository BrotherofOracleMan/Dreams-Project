import models
from datetime import datetime, date
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import Dream as ModelDream
from schema import Dream as SchemaDream, BeginAndLastDate, ItemUpdate
from sqlalchemy import and_
from sqlalchemy.orm.session import Session

app = FastAPI()


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_single_record_by_dream_name(db, dream_title: str):
    return db.query(ModelDream).filter(ModelDream.dream_title == dream_title).first() is not None


def check_single_record_by_dream_id(db, dream_id: int):
    return db.query(ModelDream).filter(ModelDream.id == dream_id).first() is not None


def get_single_record_by_dream_name(db, dream_title: str):
    return db.query(ModelDream).filter(ModelDream.dream_title == dream_title).first()


def get_single_record_by_dream_id(db, dream_id: int):
    return db.query(ModelDream).filter(ModelDream.id == dream_id).first()


def get_dreams_by_date_range(db, start_date: date, end_date: date):
    return db.query(ModelDream).filter(ModelDream.created >= start_date, ModelDream.created <= end_date).all()


def get_dreams_by_dream_title_and_date(db, dream_title: str, start_date: date, end_date: date):
    return db.query(ModelDream).filter(and_(
        ModelDream.dream_title == dream_title,
        ModelDream.created >= start_date,
        ModelDream.created <= end_date
    )
    ).all()


@app.get("/")
async def read_root():
    return {"message": "root index of API"}


@app.get("/dreams")
async def get_dream(dream: SchemaDream = None,
                    date_request_info: BeginAndLastDate = None,
                    dream_title: str = None,
                    begin_date: date = None,
                    last_date: date = None,
                    db: Session = Depends(get_db)):
    if not dream_title and not dream.dict():
        raise HTTPException(status_code=400, detail="Request body or Query parameter 'dream' is missing or empty")

    response_dict = {}
    if not dream and not date_request_info:
        if dream_title and begin_date and last_date:
            return get_dreams_by_dream_title_and_date(db, dream_title, begin_date, last_date)
        elif begin_date and last_date:
            return get_dreams_by_date_range(db, begin_date, last_date)
        else:
            raise HTTPException(status_code=422, detail="Using Query Parameters failed")
    elif dream or date_request_info:
        if dream:
            response_dict["dream_title"] = dream.dream_title
        if date_request_info:
            response_dict["begin_date"] = date_request_info.begin_date
            response_dict["last_date"] = date_request_info.last_date

        if "dream_title" in response_dict.keys() and all(value is not None for field, value in response_dict.items()):
            return get_dreams_by_dream_title_and_date(db,
                                                      response_dict["dream_title"],
                                                      response_dict["begin_date"],
                                                      response_dict["last_date"]
                                                      )

        elif response_dict["begin_date"] and response_dict["last_date"]:
            return get_dreams_by_date_range(db,
                                            response_dict["begin_date"],
                                            response_dict["last_date"]
                                            )
        else:
            return HTTPException(status_code=422, detail="Incomplete Request Body")

    raise HTTPException(status_code=400, detail="Query parameters or JSON Body is not correct")


# ToDo:create an API for updating a Dream from the DataBase
@app.put("/dreams")
async def update_dream(dream_id: int,
                       update_item: ItemUpdate,
                       db: Session = Depends(get_db)
                       ):
    custom_headers = {
        "Content-Type": "application/json",
        "Content-Langauge": "en",
    }
    existing_item = get_single_record_by_dream_id(db, dream_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for field, value in update_item.dict().items():
        if value is not None:
            setattr(existing_item, field, value)

    db.commit()
    db.refresh(existing_item)
    response_json = jsonable_encoder({
        "Message": "Successful Update. See Updated Value below",
        "Updated Value": existing_item
    })

    return JSONResponse(
        content=response_json,
        headers=custom_headers,
        status_code=status.HTTP_200_OK
    )


@app.post("/dreams")
async def create_dream(dream: SchemaDream, db: Session = Depends(get_db)):
    custom_headers = {
        "Content-Type": "application/json",
        "Content-Langauge": "en",
    }
    try:
        # first check if the dream exists within the DB
        # need to add field validation
        if check_single_record_by_dream_id(db, dream.id) or check_single_record_by_dream_name(dream.dream_title, db):
            raise HTTPException(status_code=409, detail="Dream already exists")
        dream_dict = {**dream.dict(), 'last_updated': datetime.now(), 'created': datetime.now()}
        add_dream = ModelDream(**dream_dict)
        db.add(add_dream)
        db.commit()
        db.refresh(add_dream)
        json_data = jsonable_encoder(add_dream)
        return JSONResponse(content=json_data,
                            headers=custom_headers,
                            status_code=status.HTTP_201_CREATED
                            )
    except HTTPException:
        return JSONResponse(
            content={"message": "Dream already exists"},
            headers=custom_headers,
            status_code=409
        )
