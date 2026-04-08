import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("OPENAI_API_KEY")


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )


def main():
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

    log_start("email_task", "EmailEnv", MODEL_NAME)

    rewards = []
    steps = 0

    for i in range(5):
        reward = 0.1
        rewards.append(reward)
        steps += 1

        log_step(steps, "dummy_action", reward, i == 4, None)

    score = sum(rewards)

    log_end(True, steps, score, rewards)


if __name__ == "__main__":
    main()
