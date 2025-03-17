from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from database import Base, SessionLocal, engine

import models
from schemas import NameCreate

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)
db = SessionLocal()

#  Display Data
@app.get("/",response_model=list[NameCreate])
def all_names():
    all_names = db.query(models.User).all()
    return all_names


@app.get("/views", response_class=HTMLResponse)
async def index(request: Request):
    all_names_data = all_names()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "records":all_names_data
        }
    )


# # Add Data
# @app.post("/adduser",response_model=NameCreate)
# def add_names(user:NameCreate):
#     db.append(user)
#     return {"id":user.id,"name":user.name}
#     new_name = models.User(
#         id= user.id,
#         name= user.name
#     )
#     db.add(new_name)
#     db.commit()   
#     db.refresh(new_name)

#     return new_name


# @app.get("/views/add", response_class=HTMLResponse)
# async def add(request: Request):
#     return templates.TemplateResponse("add.html", {"request": request})





# @app.get("/hello")
# async def hello():
#     return {"message": "HELLO"}


# # GET request with path parameter
# @app.get("/name/{name_id}")
# def get_name(name_id: int):
#     return {"message": f"User ID received: {name_id}"}
