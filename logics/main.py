from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.logics import generate_function_name

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class CodeData(BaseModel):
    code: str

@app.post("/submit-code/")
async def submit_code(data: CodeData):
    try:
        result = generate_function_name(data.code)
        return {'received_code': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
