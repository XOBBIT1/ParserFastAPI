import uvicorn
from fastapi import FastAPI
from mg_db.routers.clothe import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("fastapi_back.backend:app", port=8000, host="127.0.0.1", reload=True)
