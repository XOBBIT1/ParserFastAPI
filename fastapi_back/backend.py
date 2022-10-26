import uvicorn
from fastapi import FastAPI
from py_mongo.routers.clothe import clothe

app = FastAPI()
app.include_router(clothe)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("fastapi_back.backend:app", port=8000, host="127.0.0.1", reload=True)
