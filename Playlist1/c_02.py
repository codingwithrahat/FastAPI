from fastapi import FastAPI

app = FastAPI()



@app.get("/rahat")                   #/rahat path
def rahat():
    return {"Mssg" : "rahat"}  

@app.get("/")                        # 1st root url
def hello():
    return {"Mssg" : "Hello"}

@app.get("/")                        # 2nd root url
def world():
    return {"Mssg" : "World"}        #this will not work , cz first root url will be execute


@app.get("/rahat/hossan")                   #/rahat/hossan path
def rahathossan():
    return {"Mssg" : "rahat hossan"} 





