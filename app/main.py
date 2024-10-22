from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app import model
from .database import engine,get_db
from .post_route import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str,db: Session = Depends(get_db)):
    return {"message": f"Hello {name}"}