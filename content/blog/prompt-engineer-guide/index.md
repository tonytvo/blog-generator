---
title: prompt engineering guide
date: "2025-05-12T22:12:03.284Z"
description: "prompt engineering guide"
tags: ["ai", "investing", "software"]
---

# prompt examples

- **detail outlined books, articles, etc...**
  - expand in much more details with bold high-light quotes/phrases in depth and more examples for the above sections "## 6️⃣ Flaws in Session Management

Session tokens must be:

* Unpredictable
* Unique
* Properly expired
* Bound to correct user

Common flaws:

* Session fixation
* Predictable tokens
* Token leakage in URLs
* Missing HTTPOnly flag
* Missing Secure flag

Core principle:

> Session management is equivalent to authentication."
  - second pass:
    - expand in much more details, with bold high-light quotes/phrases, in depth and more examples for "" please

- **community research**

```text
you're an expert in realestate investing, give me detailed outline on the Hotchkiss neighborhood in Calgary with the following questions:
- what are nearby amenities, attractions?
- when was the houses were commonly built?
- what are the common building type?
- what are the zoning regulations? does zoning regulations allows more units per lot?
- what is the population? what is the population growth?
- what is the average income in the area?
- what is the crime rate?
- what are the rentals supply/demand in the communities?
- what are the average rents?
- is it A, B, C, D neighborhood?
- what are the long-term potential appreciation compared to current returns and cashflow?
- what is average house prices?
- what real estate investment strategies could work for this neighborhood?
```

- **complete Dept Snapshot**
  - Here’s all my debt: [type, balance, interest rate]. Organize by urgency, interest, and balance to create a clear payoff roadmap.
  - Here’s my monthly income and all expenses: [list]. Identify at least 3 areas to cut or optimize without lowering quality of life
  - Based on the debt list, create a monthly payment plan using snowball or avalanche method, including exact amounts and milestones.
  - Create a visual debt reduction tracker I can fill weekly. Include milestones, reward checkpoints, and motivational prompts for consistent progress.
  - Build a monthly checklist to update debts, review progress, adjust payments, and reallocate extra funds toward faster debt payoff.

- **streaming setup**
  - Act as a media organizer. Create a full system where I can access free, legal movie libraries online
  - Find the top 10 open-source platforms that stream free films & series — categorize them by quality.
  - Design a step-by-step guide to connect these platforms into one hub for easy access.
  - Suggest browser extensions or apps to centralize all free movie sources.
  - Make my setup ad-free using only safe & legal methods.
  - Generate a daily list of trending free movies I can watch tonight.
  - Act as a personal movie concierge — recommend titles based on my past viewing taste.

- **consolidate all of provided information**
  - Please consolidate all the information you have provided in our discussion "" into one structured text. Eliminate redundancy and organize it logically by topic

- **TDD development**

We are doing test driven development. For each task, do the following:

1. Add a test to the test file specified by the user.
2. Run the tests and ensure it fails. If it doesn't stop.
3. Add the implementation to the implementation file specified by the user.
4. Run the tests and ensure it passes. If it doesn't attempt to fix it by changing only the implementation.
5. Commit it, starting the commit message with 🤖 do denote the commit was done by you.
6. Stop and wait for the next task.

If the task involves refactoring, take small steps figure out a sequence of small moves that minimize the amount of time the code is broken. Treat each small step as a task, run the tests, and commit after each one.

If the user doesn't specify test and implementation files, stop and ask the user before continuing. DO NOT USE TOOLS TO TRY TO FIND THE FILES.

# Quotes

# References

- <https://www.promptingguide.ai/>
- <https://www.amazon.ca/Art-Prompt-Engineering-ChatGPT-Plugins-ebook/dp/B0BSN3PTX8>
- <https://www.amazon.ca/Prompt-Engineering-LLMs-Model-Based-Applications/dp/1098156153/>
