from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from db import is_user_exist

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/login")
async def login(request: Request):
    try:
        data = await request.json()
        email = data["email"]
        password = data["password"]
        token = await is_user_exist(email, password)

        if token:
            return {"status": "success", "token": token}
        else:
            return {"status": "failed"}
    except Exception as e:
        print(e)
        return {"status": "failed"}
