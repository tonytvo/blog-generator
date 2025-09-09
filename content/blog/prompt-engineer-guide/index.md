---
title: prompt engineering guide
date: "2025-05-12T22:12:03.284Z"
description: "prompt engineering guide"
tags: ["ai", "investing", "software"]
---

# prompt examples

- **detail outlined books, articles, etc...**
  - expand in much more details with bold high-light quotes/phrases the above sections "## **9. Continual Learning and Testing in Production**

* **Continual Learning**

  * Retraining strategies.
  * When and how to update models.
* **Testing in Production**

  * Shadow deployments, A/B testing, and canary releases.
  * Multi-armed bandit approaches for online experimentation."
  - second pass:
    - expand in much more details, with bold high-light quotes/phrases, in depth and more examples for "" please

- **community research**

```
you're an expert in realestate investing, give me detailed outline on the CFB Currie neighborhood in Calgary with the following questions:
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


# Quotes


# References
- https://www.promptingguide.ai/
- https://www.amazon.ca/Art-Prompt-Engineering-ChatGPT-Plugins-ebook/dp/B0BSN3PTX8
- https://www.amazon.ca/Prompt-Engineering-LLMs-Model-Based-Applications/dp/1098156153/


Here is a detailed outline of *Designing Machine Learning Systems: An Iterative Process* by Chip Huyen based on the extracted table of contents and book description.

---

# **Outline of Designing Machine Learning Systems: An Iterative Process**

### *By Chip Huyen*

## **Preface**

* Overview of the book’s objectives and intended audience.
* Emphasis on taking a holistic approach to ML system design.
* Discussion of common industry challenges in deploying ML.
* Explanation of how this book builds on practical experience.

---

## **1. Overview of Machine Learning Systems**

* **When to Use Machine Learning**

  * Understanding ML’s role in solving business problems.
  * Criteria for deciding whether ML is the right solution.
* **Machine Learning Use Cases**

  * Industry applications of ML across different sectors.
* **Understanding Machine Learning Systems**

  * Key differences between ML in research vs. production.
  * Comparison between ML systems and traditional software.

---

## **2. Introduction to Machine Learning Systems Design**

* **Business and ML Objectives**

  * Aligning ML projects with business needs.
* **Requirements for ML Systems**

  * **Reliability** – Ensuring robustness.
  * **Scalability** – Handling growing workloads.
  * **Maintainability** – Facilitating updates and debugging.
  * **Adaptability** – Keeping up with changing data.
* **Iterative Process**

  * Importance of an iterative approach in ML.
* **Framing ML Problems**

  * Different types of ML tasks.
  * Choosing objective functions.
  * The balance between human intuition and data-driven decision-making.

---

## **3. Data Engineering Fundamentals**

* **Data Sources**

  * Where data comes from and how to handle it.
* **Data Formats**

  * Structured vs. unstructured data.
  * Row-major vs. column-major storage.
* **Data Models**

  * Relational databases vs. NoSQL.
* **Data Storage and Processing**

  * Transactional vs. analytical processing.
  * ETL pipelines (Extract, Transform, Load).
  * Batch vs. streaming data processing.

---

## **4. Training Data**

* **Sampling Methods**

  * Simple random, stratified, and weighted sampling.
* **Labeling Strategies**

  * Human-annotated vs. naturally occurring labels.
  * Dealing with label scarcity.
* **Class Imbalance Handling**

  * Techniques to mitigate skewed datasets.
* **Data Augmentation**

  * Transformations and synthetic data generation.

---

## **5. Feature Engineering**

* **Learned vs. Engineered Features**
* **Common Feature Engineering Operations**

  * Handling missing values.
  * Scaling and normalization.
  * Encoding categorical variables.
* **Data Leakage Prevention**

  * Common causes and detection techniques.
* **Feature Importance and Generalization**

  * Understanding feature contribution.

---

## **6. Model Development and Offline Evaluation**

* **Model Training & Development**
* **Evaluating ML Models**

  * Offline evaluation metrics and techniques.
* **Ensemble Methods**

  * Combining multiple models for better performance.
* **Experiment Tracking & Versioning**
* **Distributed Training**

  * Scaling ML model training.
* **AutoML**

  * Automating model selection and hyperparameter tuning.

---

## **7. Model Deployment and Prediction Services**

* **Machine Learning Deployment Myths**

  * Addressing common misconceptions.
* **Batch vs. Online Prediction**

  * Transitioning between different inference methods.
* **Model Compression Techniques**

  * Low-rank factorization, pruning, and quantization.
* **ML in Cloud and Edge Computing**

  * Deploying models in various environments.

---

## **8. Data Distribution Shifts and Monitoring**

* **Causes of ML System Failures**

  * Software vs. ML-specific failures.
* **Detecting & Addressing Data Distribution Shifts**

  * Strategies to mitigate concept drift.
* **Monitoring & Observability**

  * Implementing an effective ML monitoring system.

---

## **9. Continual Learning and Testing in Production**

* **Continual Learning**

  * Retraining strategies.
  * When and how to update models.
* **Testing in Production**

  * Shadow deployments, A/B testing, and canary releases.
  * Multi-armed bandit approaches for online experimentation.

---

## **10. Infrastructure and Tooling for MLOps**

* **Storage and Compute Considerations**

  * Cloud vs. on-premise infrastructure.
* **Development Environments**

  * Standardizing dev environments for ML teams.
* **Resource Management**

  * Job schedulers, workflow orchestration, and automation tools.
* **Building an ML Platform**

  * Model and feature stores.
  * The trade-offs of build vs. buy decisions.

---

## **11. The Human Side of Machine Learning**

* **User Experience**

  * Designing ML models with usability in mind.
* **Team Structure**

  * Organizing ML teams for effectiveness.
* **Responsible AI**

  * Ethical considerations and case studies.
  * Frameworks for fairness and accountability.

---

## **Epilogue**

* Final thoughts on the future of ML systems.
* Call to action for ML practitioners to focus on iterative improvement.

---

## **Appendix & References**

* Additional technical details.
* Key references and further reading.

---

This book serves as a comprehensive resource for ML engineers, data scientists, and software developers working on designing and deploying production-ready ML systems. It emphasizes the iterative process and real-world challenges of ML system design.
