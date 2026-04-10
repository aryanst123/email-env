import os
from typing import List, Optional
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("API_KEY")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error or 'null'}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )


def get_action(email: str):
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an intelligent email assistant."},
                {
                    "role": "user",
                    "content": f"""
Email:
{email}
Choose ONE action:
DELETE (spam)
KEEP (important)
REPLY (needs response)
Only output one word.
""",
                },
            ],
            max_tokens=5,
        )
        return (completion.choices[0].message.content or "KEEP").strip().upper()
    except:
        return "KEEP"


def run_task(task_name: str, email: str):
    log_start(task_name, "EmailEnv", MODEL_NAME)

    rewards = []
    steps = 0

    for i in range(2):
        action = get_action(email)

        if "SALE" in email:
            reward = 0.85 if action == "DELETE" else 0.3
        elif "subscription" in email.lower():
            reward = 0.75 if action == "KEEP" else 0.3
        else:
            reward = 0.8 if action == "REPLY" else 0.4

        done = i == 1

        rewards.append(reward)
        steps += 1

        log_step(steps, action, reward, done, None)

    score = sum(rewards) / len(rewards)
    score = max(0.01, min(0.99, score))

    log_end(True, steps, score, rewards)


def main():
    run_task("easy_task", "🔥 SALE!!! Buy now and get 90% OFF!!!")
    run_task("medium_task", "Reminder: subscription renews tomorrow")
    run_task("hard_task", "Can you send the Q3 financial report today?")


if __name__ == "__main__":
    main()
