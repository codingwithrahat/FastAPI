from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl     #BaseModel/HttpUrl for request body validation

app = FastAPI()


#define request body schema
class course(BaseModel):
    name : str
    ins : str
    duration : float
    website : HttpUrl 

#post method
# POST endpoint that accepts a Course object and returns the received data
@app.post("/post")
def create_post(post : course):
    return {"data" : post}








