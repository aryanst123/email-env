from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Action(BaseModel):
    action_type: str
    content: Optional[str] = None


# ---------------- TASK 1 (EASY) ----------------
@app.post("/reset_spam")
def reset_spam():
    return {
        "observation": {
            "task_id": 1,
            "task_type": "spam_detection",
            "instruction": "Identify and delete obvious spam email",
            "email": "🔥 SALE!!! Buy now and get 90% OFF!!!",
            "step": 0
        }
    }


@app.post("/step_spam")
def step_spam(action: Action):
    a = action.action_type.upper()

    if a == "DELETE":
        reward = 0.85
    elif a == "KEEP":
        reward = 0.3
    else:
        reward = 0.2

    return {
        "observation": {"task_id": 1, "task_type": "spam_detection", "step": 1},
        "reward": reward,
        "done": True,
        "info": {"difficulty": "easy"}
    }


# ---------------- TASK 2 (MEDIUM) ----------------
@app.post("/reset_important")
def reset_important():
    return {
        "observation": {
            "task_id": 2,
            "task_type": "important_email",
            "instruction": "Decide if email is important",
            "email": "Reminder: Your subscription will renew tomorrow.",
            "step": 0
        }
    }


@app.post("/step_important")
def step_important(action: Action):
    a = action.action_type.upper()

    if a == "KEEP":
        reward = 0.75
    elif a == "DELETE":
        reward = 0.25
    else:
        reward = 0.4

    return {
        "observation": {"task_id": 2, "task_type": "important_email", "step": 1},
        "reward": reward,
        "done": True,
        "info": {"difficulty": "medium"}
    }


# ---------------- TASK 3 (HARD) ----------------
@app.post("/reset_reply")
def reset_reply():
    return {
        "observation": {
            "task_id": 3,
            "task_type": "reply_generation",
            "instruction": "Decide if reply is needed",
            "email": "Hi, can you send the Q3 financial report before EOD?",
            "step": 0
        }
    }


@app.post("/step_reply")
def step_reply(action: Action):
    a = action.action_type.upper()

    if a == "REPLY":
        reward = 0.8
    elif a == "KEEP":
        reward = 0.5
    else:
        reward = 0.2

    return {
        "observation": {"task_id": 3, "task_type": "reply_generation", "step": 1},
        "reward": reward,
        "done": True,
        "info": {"difficulty": "hard"}
    }


# DEFAULT ROUTES
@app.post("/reset")
def reset():
    return reset_spam()


@app.post("/step")
def step(action: Action):
    return step_spam(action)


@app.get("/state")
def state():
    return {"status": "ok"}


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
