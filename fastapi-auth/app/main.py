from fastapi import FastAPI 

app = FastAPI()

@app.get("/textcheck")
def readtext():
    return "Hello World"   



