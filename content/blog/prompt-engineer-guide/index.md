---
title: prompt engineering guide
date: "2025-05-12T22:12:03.284Z"
description: "prompt engineering guide"
tags: ["ai", "investing", "software"]
---

# prompt examples

- **detail outlined books, articles, etc...**
  - expand in much more details with bold high-light quotes/phrases the above sections "### **Chapter 5 — Presentation Stage**

* Visualizing and aggregating telemetry.

  * Dashboards via Grafana, Kibana
  * Aggregation functions and statistical validity
  * Linking raw data to decision support"
  - second pass:
    - expand in much more details, with bold high-light quotes/phrases, in depth and more examples for "### **Chapter 2 — Emitting Stage: Creating and Submitting Telemetry**" please

- **community research**

```
you're an expert in realestate investing, give me detailed outline on the Westlake neighborhood in Red Deer with the following questions:
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


Here’s a **detailed outline** of *Software Telemetry* by **Jamie Riedesel** (Manning, 2021) — a comprehensive guide to building, operating, and improving end-to-end telemetry systems for modern software infrastructure.

---

## 📘 **Book Overview**

**Purpose:**
Teach how to **design, operate, and evolve telemetry systems** that support decision-making across operations, development, and compliance.
It covers the **three stages** of telemetry pipelines—**Emitting, Shipping, and Presentation**—and extends to **multitenancy, optimization, security, and regulatory compliance**.

**Audience:**
Software engineers, SREs, DevOps, systems engineers, and security/compliance professionals maintaining or redesigning telemetry systems.

**Core Themes:**

* Logs, Metrics, and Traces — the **three pillars of observability**
* End-to-end telemetry architecture
* Legal and data-handling practices (GDPR, toxic data)
* Real-world telemetry pipelines (Fluentd, Logstash, Prometheus, OpenTelemetry, ELK, etc.)
* Practical, vendor-neutral, system-oriented techniques

---

## 🧩 **Structure of the Book**

### **Preface & About This Book**

* Motivation: lack of unified resources on telemetry ecosystems.
* Goals: improve cost management, compliance, and observability.
* Coverage includes **containers, FaaS, and hybrid infrastructures** .
* Methodology: uses **Python** and **Ruby** for examples, config formats from **Logstash**, and checklists for system review.

---

## 🧱 **PART 1 — Telemetry System Architecture**

Focus: conceptual framework of all telemetry systems.

### **Chapter 1 — Introduction**

* Defines **four styles of telemetry**:

  1. Centralized Logging
  2. Metrics
  3. Distributed Tracing
  4. SIEM (Security Information and Event Management)
* Describes how telemetry is used by:

  * DevOps & SRE teams
  * Security & compliance
  * Customer support
  * Business intelligence
* Common challenges: underinvestment, standardization, data leaks, and legal disruptions .

---

### **Chapter 2 — Emitting Stage: Creating and Submitting Telemetry**

* Sources: production code, hardware, and as-a-Service systems.
* Methods:

  * Log files, system logs, stdout streams
  * SNMP from devices (e.g., Cisco firewalls)
  * SaaS and IaaS event streams
* Key concept: **markup** and **formatting** for efficient emission.

---

### **Chapters 3–4 — Shipping Stage**

* **Chapter 3:** Transporting telemetry from emitters to storage.

  * Direct vs queued shipping
  * Shipping between SaaS systems
  * Tipping points for architecture change
* **Chapter 4:** Unifying formats and encoding telemetry.

  * Converting between Syslog, JSON, and object encodings
  * **Cardinality design** for metrics scalability

---

### **Chapter 5 — Presentation Stage**

* Visualizing and aggregating telemetry.

  * Dashboards via Grafana, Kibana
  * Aggregation functions and statistical validity
  * Linking raw data to decision support

---

### **Chapter 6 — Marking Up and Enriching Telemetry**

* Adds **context** (enrichment) and **structure** (markup).
* Covers type conversions, metadata tagging, correlation IDs.

---

### **Chapter 7 — Handling Multitenancy**

* Managing visibility boundaries across teams or clients.
* Techniques for cost control, tenant isolation, and role-based access.

---

## 🌐 **PART 2 — Use Cases Revisited: Applying Architecture Concepts**

Eleven real-world examples showing how telemetry systems evolve by organization type .

### **Chapter 8 — Growing Cloud-Based Startup**

* From single-dashboard telemetry (AWS/GCP) to internal systems.
* Transition to in-house collection pipelines (Fluentd, ELK).

### **Chapter 9 — Non-Software Business**

* Telemetry in IT departments using SaaS tools.
* Expanding scope when internal development begins.

### **Chapter 10 — Long-Established Business IT (Legacy/Mainframe)**

* Integrating mainframe telemetry into modern observability stacks.
* Practical handling of hybrid systems.

---

## ⚙️ **PART 3 — Techniques for Handling Telemetry**

Operational excellence and problem-solving toolkit .

### **Chapter 11 — Optimizing for Regular Expressions at Scale**

* Regex performance tuning in telemetry pipelines.
* Reducing CPU/memory overhead of pattern matching.

### **Chapter 12 — Standardized Logging and Event Formats**

* Building structured loggers (JSON, YAML).
* Creating schema-consistent events for observability tools.

### **Chapter 13 — Non-File Emitting Techniques**

* Telemetry in containers and serverless (FaaS) systems.
* Network-based emission protocols (UDP/TCP, OpenTelemetry).

### **Chapter 14 — Managing Cardinality in Telemetry**

* Understanding and limiting high-cardinality data in metrics.
* Aggregation, sampling, and label-management strategies.

### **Chapter 15 — Ensuring Telemetry Integrity**

* Making telemetry **tamper-resistant** and auditable.
* Write-only emission methods, access logging, and secure queues .

### **Chapter 16 — Redacting and Reprocessing Telemetry**

* Handling **toxic data** (PII, GDPR).
* Real-time and batch redaction pipelines.
* Re-ingestion for platform migrations.

### **Chapter 17 — Building Policies for Retention and Aggregation**

* Creating **retention policies** for logs, metrics, and traces.
* Sampling and aggregation for long-term efficiency .

### **Chapter 18 — Surviving Legal Processes**

* **eDiscovery, record retention, and compliance workflows.**
* Working with legal teams to manage telemetry evidence .

---

## 📚 **Appendices**

* **A:** Seven major telemetry storage systems (Elasticsearch, Prometheus, Cassandra, etc.).
* **B:** Consolidated checklist of recommendations.
* **C:** Exercise answers and further guidance .

---

## 🧠 **Key Takeaways**

1. **Telemetry = feedback loop for decision-making** — not just monitoring.
2. The **three-stage pipeline (Emitting → Shipping → Presentation)** underpins every system.
3. **Multitenancy, security, and compliance** are as vital as performance.
4. **Toxic data handling** and **legal preparedness** are non-optional in modern orgs.
5. Focus on **architecture and maintainability**, not tools or frameworks.

---

Would you like me to create a **visual architecture diagram** summarizing the three telemetry stages (Emitting, Shipping, Presentation) and their typical toolchains (e.g., Fluentd → Elasticsearch → Kibana → SIEM/Tracing)?
