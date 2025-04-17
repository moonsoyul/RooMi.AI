from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/get_shapegrammar")
async def get_shapegrammar():
    try:
        with open("shapegrammar.json", "r") as file:
            shape_grammar = json.load(file)
            print("📦 JSON 로딩 성공! 내용 일부:", str(shape_grammar)[:200], "...")
        return JSONResponse(content=shape_grammar)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
