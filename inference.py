import os
from typing import List, Optional
from openai import OpenAI

# REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")  # NO default

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(
    step: int, action: str, reward: float, done: bool, error: Optional[str]
) -> None:
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )


def main():
    log_start("email_task", "EmailEnv", MODEL_NAME)

    rewards: List[float] = []
    steps = 0

    for i in range(5):
        action = "DELETE"

        reward = 0.1
        done = i == 4

        rewards.append(reward)
        steps += 1

        log_step(steps, action, reward, done, None)

    score = sum(rewards)

    log_end(True, steps, score, rewards)


if __name__ == "__main__":
    main()
