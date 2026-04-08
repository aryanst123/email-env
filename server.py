from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI()

STATE = {"step": 0}


class Action(BaseModel):
    action_type: str
    email_id: int = 0
    content: Optional[str] = None


@app.post("/reset")
def reset():
    global STATE
    STATE = {"step": 0}

    # small delay to avoid cold start race
    time.sleep(1)

    return {
        "observation": {
            "emails": [
                {"id": 1, "subject": "SALE!!!"},
                {"id": 2, "subject": "Meeting Tomorrow"},
            ],
            "step": 0,
        }
    }


@app.post("/step")
def step(action: Action):
    STATE["step"] += 1

    reward = 0.1
    done = STATE["step"] >= 5

    return {
        "observation": {
            "emails": [
                {"id": 1, "subject": "SALE!!!"},
                {"id": 2, "subject": "Meeting Tomorrow"},
            ],
            "step": STATE["step"],
        },
        "reward": reward,
        "done": done,
        "info": {},
    }


@app.get("/state")
def state():
    return STATE
