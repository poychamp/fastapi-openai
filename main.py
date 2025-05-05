from fastapi import FastAPI
from utils import openai_client
from typing import Any, Dict

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print ("startup_event")

@app.on_event("shutdown")
async def shutdown_event():
    print ("shutdown_event")

@app.get("/")
async def index():
    system_prompt = "this is a system prompt"
    user_prompt = "give me an example user prompt"

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        stream=False,
    )

    return {
        "content": completion.choices[0].message.content
    }

@app.post("/")
async def store(payload: Dict[str, Any]):
    system_prompt = payload.get("system_prompt")
    user_prompt = payload.get("user_prompt")

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        stream=False,
    )

    return {
        "content": completion.choices[0].message.content
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8030, reload=True)
