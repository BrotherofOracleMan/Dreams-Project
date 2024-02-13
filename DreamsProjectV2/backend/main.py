
import models
from datetime import datetime, date
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import Dream as ModelDream
from schema import Dream as SchemaDream, BeginAndLastDate
from sqlalchemy import and_
from sqlalchemy.orm.session import Session

app = FastAPI()


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_single_record_by_dream_name(dream_title: str, db):
    return db.query(ModelDream).filter(ModelDream.dream_title == dream_title).first() is not None


def get_single_record_by_dream_id(db, dream_id: int):
    return db.query(ModelDream).filter(ModelDream.id == dream_id).first() is not None


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
    # Do a validation to check if both the dream_title and begin date and last date are not empty
    # if not dream_title or not dream.dict():
    #    raise HTTPException(status_code=400, detail="Request body or Query parameter 'dream' is missing or empty")

    # For only query parameters
    print(dream)
    print(date_request_info)

    if not dream and not date_request_info:
        if dream_title and begin_date and last_date:
            # checks if dream title exists
            return get_dreams_by_dream_title_and_date(db, dream_title, begin_date, last_date)
        elif begin_date and last_date:
            # look for dreams between the beginning date and end date
            return get_dreams_by_date_range(db, begin_date, last_date)
        else:
            raise HTTPException(status_code=422, detail="Using Query Parameters failed")
    elif dream or date_request_info:
        response_dict ={}
        if dream:
            response_dict["dream_title"] = dream.dream_title
        if date_request_info:
            response_dict["begin_date"] = date_request_info.begin_date
            response_dict["end_date"] = date_request_info.end_date

        if all(value is not None for field, value in response_dict.items()):
            return get_dreams_by_dream_title_and_date(db,
                                                      response_dict["dream_title"],
                                                      response_dict["begin_date"],
                                                      response_dict["end_date"]
                                                      )
        elif response_dict["begin_date"] and response_dict["end_date"]:
            return get_dreams_by_date_range(db,
                                            response_dict["begin_date"],
                                            response_dict["end_date"]
                                            )
        else:
            return HTTPException(status_code=422, detail="Incomplete Request Body")

    raise HTTPException(status_code=400, detail="Query parameters is/are missing")


# ToDo:create an API for updating a Dream from the DataBase
@app.put("/dreams")
async def update_dream():
    return {"message": "Updated dream Call"}


@app.post("/dreams")
async def create_dream(dream: SchemaDream, db: Session = Depends(get_db)):
    custom_headers = {
        "Content-Type": "application/json",
        "Content-Langauge": "en",
    }
    try:
        # first check if the dream exists within the DB
        # need to add field validation
        if get_single_record_by_dream_id(db, dream.id) or get_single_record_by_dream_name(dream.dream_title, db):
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
