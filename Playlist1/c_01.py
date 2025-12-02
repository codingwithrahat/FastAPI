from fastapi import FastAPI          #call FastAPI class from fastapi library

app = FastAPI()                      #create an object

@app.get("/")                        # root url
def hello():
    return {"Mssg" : "Hello"}
