from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/create_new_test")
async def create_new_test():
    return {"message": "OK"}


@app.get("/test_list")
async def test_list():
    return {"message": "test_list"}


@app.get("/test_detail")
async def test_list():
    return {"message": "test_list"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="localhost")