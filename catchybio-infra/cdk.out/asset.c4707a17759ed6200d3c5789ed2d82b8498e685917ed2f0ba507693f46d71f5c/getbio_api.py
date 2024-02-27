from fastapi import FastAPI, HTTPException
from getbio import generate_bio
# from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# handler = Mangum(app)

@app.get("/generate_bio")
async def generate_bio_api(raw_bio):
    snippet = generate_bio(raw_bio)
    return {"snippet": snippet}