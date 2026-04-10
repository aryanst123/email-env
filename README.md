# Email Environment (OpenEnv)

## Overview

This project simulates a real-world email inbox management system using the OpenEnv framework. The agent must analyze incoming emails and decide whether to delete, keep, or reply.

---

## Problem Statement

Email triaging is a common real-world task where users must:

* filter spam
* prioritize important messages
* respond to actionable emails

This environment models that workflow.

---

## Actions

The agent can take 3 actions:

* DELETE → remove spam emails
* KEEP → retain important emails
* REPLY → respond to emails that require action

---

## Tasks

### 1. Spam Detection (Easy)

* Identify clearly promotional emails
* Objective: delete spam

### 2. Important Email Classification (Medium)

* Emails are slightly ambiguous
* Objective: decide if email is important

### 3. Reply Decision (Hard)

* Requires understanding intent
* Objective: decide if reply is needed

---

## Reward Design

* Correct action → high reward (~0.75–0.85)
* Partial correctness → medium reward (~0.4–0.6)
* Incorrect action → low reward (~0.2–0.3)

Rewards are designed to provide meaningful feedback rather than binary success/failure.

---

## LLM Usage

The agent uses an LLM to:

* understand email content
* decide appropriate action

Environment variables used:

* API_BASE_URL
* API_KEY
* MODEL_NAME

---

## Deployment

The environment is deployed on Hugging Face Spaces using:

* FastAPI backend
* Docker container

---

## Key Features

* Real-world inspired task
* Multi-level difficulty
* Deterministic reward system
* LLM-driven decisions
* OpenEnv compliant

---

## Future Improvements

* Multi-step email conversations
* Context-aware reply generation
* Advanced scoring for responses
