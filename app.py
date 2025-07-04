# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import generate_rewritten_ad

app = FastAPI()

class AdRewriteRequest(BaseModel):
    ad_text: str
    tone: str
    platform: str

@app.post("/run-agent")
async def run_agent(request: AdRewriteRequest):
    try:
        rewritten_text, justification = generate_rewritten_ad(
            request.ad_text, request.tone, request.platform
        )
        return {
            "rewritten_text": rewritten_text,
            "justification": justification
        }
    except Exception as e:
        print(f"🔥 Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
