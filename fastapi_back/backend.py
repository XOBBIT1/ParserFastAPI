import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("fastapi_back.backend:app", port=8000, host="127.0.0.1", reload=True)
