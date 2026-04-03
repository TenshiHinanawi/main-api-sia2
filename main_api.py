from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "online", "message": "API is running"}

@app.post("/process")
async def process(request: Request):
    body = await request.json()
    print(body)
    return {"received": body, "status": "success"}