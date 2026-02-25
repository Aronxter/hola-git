from fastapi import FastAPI, HTTPException, status, staticfiles

app = FastAPI()

@app.get("/")
async def nunu():
    return {"message": "el nunu"}