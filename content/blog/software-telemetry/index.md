---
title: Software Telemetry by Jamie Riedesel summary
date: "2025-10-10T22:12:03.284Z"
description: "Software Telemetry by Jamie Riedesel summary"
tags: ["softwaredevelopment"]
---

Excellent — let’s expand **Part 1 – Telemetry System Architecture (Chapter 1: Introduction)** from *Software Telemetry* by **Jamie Riedesel** in rich, detailed form with **bolded key phrases**, contextual explanations, and practical insights, as you requested.

---

# 🧱 **Telemetry System Architecture**

## 🎯 **Focus:**

This part of the book establishes the **conceptual foundation** of all telemetry systems — explaining how **telemetry underpins decision-making** in software systems by converting raw operational data into **actionable insight**.

Riedesel emphasizes that **telemetry is not just monitoring**:

> **“Telemetry is the art and science of collecting, transporting, and interpreting operational data so humans and machines can make better decisions.”**

It spans everything from **low-level system metrics** (CPU, memory, disk I/O) to **business outcomes** (user conversion rates, revenue per second), forming the **nervous system** of modern software.

---

## 📘 **Introduction**

### 🧩 1. What Is Telemetry?

* **Telemetry** originates from aerospace and industrial systems, meaning **“measurement at a distance.”**
* In software, it refers to **automated, continuous collection of operational data** about code, infrastructure, and user interactions.
* The goal: enable teams to **observe, diagnose, and improve systems** without manual intervention or guesswork.

Riedesel writes:

> **“Every decision your organization makes about software operations is either supported or hindered by the quality of your telemetry.”**

---

### ⚙️ 2. The Four Styles of Telemetry

Riedesel identifies **four major styles**, each addressing a distinct layer of system observability:

1. #### **Centralized Logging**

   * The most familiar form — **aggregating logs from many systems** into a central store (e.g., Elasticsearch, Splunk, CloudWatch Logs).

   * Provides **contextual event history**, essential for debugging and auditing.

   * Best suited for **qualitative analysis** — “What happened?” or “Why did this fail?”

   * Key challenge: **log volume explosion** and **unstructured formats** leading to storage and parsing overhead.

   > **“Logs tell stories — but if everyone writes in a different language, your telemetry system becomes a Tower of Babel.”**

2. #### **Metrics**

   * Numeric, time-series data about system performance: **request latency, error rates, CPU usage, queue lengths, etc.**
   * Enables **quantitative analysis** — “How fast?”, “How much?”, “How often?”
   * Supports **alerting** and **capacity planning**, and feeds into tools like **Prometheus**, **Datadog**, or **InfluxDB**.
   * The emphasis is on **low cardinality and statistical clarity**, since metrics are designed for aggregation and trend detection.
   * Riedesel:

     > **“Metrics show health at a glance — they’re your system’s vital signs.”**

3. #### **Distributed Tracing**

   * Focused on **understanding request flow across services**, particularly in microservice architectures.
   * A trace represents the **end-to-end journey of a single transaction**, often through dozens of services.
   * Provides **causal context** and exposes latency bottlenecks or dependency failures.
   * Common tools: **Jaeger**, **Zipkin**, **Honeycomb**, **OpenTelemetry Tracing**.
   * Key insight:

     > **“Traces are the connective tissue that link logs and metrics into a coherent picture of user experience.”**

4. #### **SIEM (Security Information and Event Management)**

   * Originally from the **security operations world**, but increasingly integrated into software observability.
   * Collects, correlates, and analyzes security events — logins, privilege escalations, file access, API misuse, etc.
   * Used to **detect intrusions**, **comply with audits**, and **respond to incidents**.
   * The author highlights that SIEM often operates **parallel** to engineering telemetry, but ideally should **share the same data sources**.
   * Key warning:

     > **“When security and operations collect telemetry separately, you pay twice and see half.”**

---

### 👥 3. Who Uses Telemetry — and Why

Riedesel underscores that **telemetry systems serve multiple stakeholders** beyond developers:

| Stakeholder                    | Purpose                                                                                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DevOps & SRE Teams**         | To maintain **reliability, uptime, and incident response**. They need **real-time metrics, alerts, and traces** to identify and remediate outages quickly. |
| **Security & Compliance**      | To monitor for **suspicious activity, audit trails, and regulatory evidence**. Telemetry must support **immutability, access control, and data lineage.**  |
| **Customer Support**           | Uses telemetry to **reproduce customer issues**, validate bug reports, and monitor **service-level agreements (SLAs)**.                                    |
| **Business Intelligence (BI)** | Leverages telemetry to **correlate system behavior with business outcomes**, such as user engagement or transaction volume.                                |

The book’s central idea:

> **“A well-designed telemetry system speaks all these dialects fluently.”**

This means the same underlying pipeline can feed **Grafana dashboards**, **security alerts**, and **business KPIs** — if structured correctly.

---

### ⚠️ 4. Common Challenges

The introduction closes by confronting **why telemetry often fails in real-world organizations**, even though it’s so essential.

1. **Underinvestment and Neglect**

   * Telemetry is **“invisible until it breaks”**, leading to chronic underfunding.
   * Riedesel warns:

     > **“Organizations treat telemetry as plumbing, not infrastructure — until the leak floods the house.”**
   * Result: reactive firefighting, missing context during incidents, poor data quality.

2. **Lack of Standardization**

   * Inconsistent event formats, naming conventions, or timestamp handling cause fragmentation.
   * Teams build parallel telemetry stacks that **cannot interoperate**, increasing cost and cognitive load.
   * Remedy: adopt **common schemas** and **shared context identifiers** (like correlation IDs or trace IDs).

3. **Data Leaks and Toxic Telemetry**

   * Many systems inadvertently log **sensitive data** (PII, credentials, financial information).
   * This creates **security, privacy, and compliance liabilities**.
   * Later chapters discuss **redaction pipelines** and **telemetry classification frameworks**.
   * Quote:

     > **“Telemetry can betray you if it captures what it shouldn’t — and keeps it longer than it should.”**

4. **Legal and Regulatory Disruptions**

   * With GDPR, CCPA, and similar laws, telemetry systems are now subject to **the same scrutiny as customer databases**.
   * Retention policies, data residency, and right-to-erasure requests directly affect design choices.
   * Example: an innocuous log containing IP addresses can be considered **personal data** under GDPR.

---

### 🧠 5. Chapter Summary — Core Mindset

The introduction sets the mental model for the rest of the book:

* Think of telemetry as a **living ecosystem**, not a static product.
* Design pipelines that are **observable, auditable, and evolvable**.
* Treat telemetry as a **first-class citizen** of your system’s architecture — on par with APIs, databases, and CI/CD pipelines.

> **“Telemetry is both mirror and microscope — it reflects what your system does and reveals what you didn’t know.”**


---

## ⚙️ **Emitting Stage: Creating and Submitting Telemetry**

### 🎯 **Purpose of the Emitting Stage**

Riedesel opens this chapter by defining **“emission”** as the **birthplace of all telemetry data** — the point where **systems, code, or services** first produce raw information about what’s happening.

> **“Emission is where the data begins its life. If this stage is noisy, inconsistent, or incomplete, everything downstream inherits that flaw.”**

This is the **foundation layer** of the entire telemetry pipeline. Every log line, metric point, or event captured later originates from **emitters** — whether that’s a web server, a sensor, a cloud service, or an API gateway.

Riedesel emphasizes that:

> **“A telemetry system is only as trustworthy as its emitters.”**

Even the best visualization and analysis tools cannot fix **badly structured, uncorrelated, or incomplete emissions**.

---

### 🧩 **1. Major Sources of Telemetry**

The author divides telemetry sources into **three main families**, each with its own emission model, reliability concerns, and legal considerations.

#### (a) **Production Code**

* The most **common and controllable source** of telemetry.
* Developers insert **logging, tracing, and metrics instrumentation** directly into application code.
* Examples:

  * `logger.info("User login successful", user_id=...)`
  * `statsd.increment("checkout.completed")`
  * `trace.start_span("database.query")`
* Purpose: capture **application-level insights** (business events, user actions, error conditions).
* Emphasis: use **structured, semantic logs** instead of ad-hoc text.

Riedesel’s warning:

> **“If your logs require grep, you’ve already lost half the battle.”**

Structured emission (e.g., JSON logs) allows automation, parsing, and analytics — while unstructured logs create brittle regex filters later in the pipeline.

#### (b) **Hardware Devices**

* Network devices, routers, switches, and IoT sensors emit telemetry via **standardized protocols**.
* The most common example: **SNMP (Simple Network Management Protocol)**.

  * Used by **Cisco, Juniper, HP**, and most network vendors.
  * Emits status information like port errors, bandwidth usage, temperature, and voltage.
* Hardware telemetry is often **event-driven** or **poll-based** — meaning the monitoring system queries for data at intervals.
* Problems arise when **SNMP traps** flood systems during outages — “the storm of events when things fail.”

Quote:

> **“Hardware telemetry speaks the oldest dialect — terse, numeric, and cryptic — but it still tells critical truths about the health of the foundation.”**

#### (c) **SaaS and IaaS Systems**

* In the cloud era, much telemetry originates from **external services** you don’t fully control.
* Examples:

  * AWS CloudWatch events
  * GCP Stackdriver logs
  * Azure Monitor metrics
  * Stripe, Twilio, or GitHub webhook events
* These systems often emit telemetry via **HTTP event streams, JSON APIs, or audit logs**.
* Integration challenge: **normalize foreign schemas** and **timestamps** to fit your unified telemetry model.

Riedesel notes:

> **“Your telemetry doesn’t stop at your servers anymore. Every SaaS product your business depends on is now part of your observability surface.”**

This means telemetry design must consider **external integrations, rate limits, and API schema drift**.

---

### 🔄 **2. Methods of Emission**

After identifying sources, Riedesel describes **common emission methods**, mapping each to real-world use cases.

#### **(1) Log Files**

* Traditional method: applications write events to files on disk (`/var/log/...`).
* Advantages: easy to implement, human-readable, durable.
* Disadvantages: difficult for **containerized or ephemeral systems**, since log files vanish when the container dies.
* Modern guidance:

  > **“Logs should go to streams, not disks — because disks are pets, streams are cattle.”**

Hence, newer architectures redirect logs to **stdout/stderr**, enabling collection by sidecar agents (Fluentd, Logstash, etc.).

#### **(2) System Logs**

* OS-level telemetry like **syslog**, **journalctl**, or **event logs**.
* These often capture **kernel, network, authentication, and daemon messages**.
* They provide context that application logs alone can’t (e.g., hardware errors, restarts).
* The book encourages integrating these with application telemetry for **complete incident timelines**.

> **“System logs are your black box recorder — they capture what your app didn’t notice.”**

#### **(3) Standard Output Streams**

* Common in **cloud-native** environments such as Kubernetes or AWS Lambda.
* Instead of writing to disk, applications write logs to **stdout**.
* Log collectors (sidecars, daemons, or host agents) then stream this output to central systems.
* This avoids file permission issues, supports auto-scaling, and simplifies container lifecycle management.
* Example: Docker captures stdout and sends it to the logging driver (Fluentd, Loki, etc.).

Riedesel emphasizes:

> **“Emitters in a stateless world must speak over ephemeral channels.”**

#### **(4) SNMP and Device Telemetry**

* As mentioned, SNMP traps and polls remain the backbone for physical device telemetry.
* SNMPv3 introduced encryption and authentication, addressing prior risks of **plain-text community strings**.
* Still, hardware telemetry must be **rate-limited** and **filtered**, since storms of events can overwhelm ingest pipelines.

#### **(5) SaaS and IaaS Event Streams**

* Modern SaaS platforms expose **event hooks**, **audit APIs**, or **change streams**.
* Examples:

  * **AWS CloudTrail** → records API activity.
  * **GitHub Audit Log** → developer behavior telemetry.
  * **Okta or GSuite logs** → identity and access telemetry.
* Integration pattern:

  * Use **webhooks** or **scheduled API polling**.
  * Ingest via an **event collector microservice** or message queue.
  * Apply **schema normalization** before storage.

Riedesel highlights:

> **“Every vendor speaks a different dialect of JSON — your telemetry platform must be multilingual.”**

---

### 🧠 **3. Key Concept: “Markup” and “Formatting”**

This section is one of the chapter’s most critical and nuanced discussions. Riedesel introduces **markup** and **formatting** as the **hidden architecture** of successful telemetry emission.

> **“How you format your telemetry determines how expensive it will be to process, store, and understand — forever.”**

#### **(a) Markup = Structural Context**

* Markup refers to **embedding structure or metadata** into telemetry events.
* Examples:

  * Adding fields like `service_name`, `environment`, `region`, `trace_id`, `severity`, `user_id`.
  * Encoding events in **JSON**, **Protocol Buffers**, or **structured key-value pairs**.
* Purpose:

  * Enables **machine parsing**.
  * Preserves **contextual meaning** (who, what, where, when).
  * Allows correlation across systems (e.g., linking user activity to backend traces).

> **“Good markup is like a passport — it lets your telemetry cross system borders without losing its identity.”**

#### **(b) Formatting = Syntax Consistency**

* Formatting defines **how** the structured data is represented — e.g., JSON vs. plain text vs. key-value pairs.
* Consistent formatting allows:

  * Simplified ingestion pipelines.
  * Easier versioning and backward compatibility.
  * Predictable storage and indexing.
* The book recommends **human-readable structured formats** (JSON, YAML) over binary formats, unless efficiency is critical.
* Quote:

  > **“Human-readable formats cost storage; binary formats cost debugging.”**

#### **(c) Avoiding Anti-Patterns**

* Common mistakes at the emission stage:

  1. **Over-logging** – flooding telemetry with redundant or verbose data.
  2. **Inconsistent keys** – e.g., using `userId`, `userid`, `User_ID` across services.
  3. **Hidden context** – burying critical identifiers inside message text instead of structured fields.
  4. **Unescaped data** – leaking raw input that breaks JSON or XML parsers.
  5. **Time drift** – relying on system clocks without synchronization.

Riedesel cautions:

> **“You can’t fix bad markup downstream. You can only regret it.”**

Hence, emission is where **discipline and schema governance** begin.

---

### 🔐 **4. Reliability and Security at the Emission Point**

Telemetry can be **compromised or lost** even before it leaves the emitter.

* **Buffering and Backpressure**
  Emitters must handle temporary network failures gracefully — through **local queues or ring buffers**.

  > **“If emitters block on telemetry, you’re monitoring less to protect uptime — that’s a false economy.”**

* **Security and Least Privilege**
  Emitters should **authenticate with telemetry collectors** using API keys, service accounts, or signed payloads.

  > **“Telemetry should not become an attack vector; every log line is a potential leak.”**

* **Data Minimization**
  Avoid logging secrets, tokens, or sensitive identifiers.
  Adopt a **telemetry classification policy** (public, internal, confidential).

---

### 🧩 **Summary — Emission as Architecture**

Riedesel closes with a powerful framing:

> **“The emitting stage is where you decide what your organization will ever know about its systems.”**

That decision includes:

* **Which events exist or vanish forever**
* **How those events will be interpreted downstream**
* **How costly it will be to scale or audit later**

She concludes:

> **“Telemetry begins at the point of emission — and that’s where reliability, legality, and observability are either born or lost.”**

---

✅ **Summary Checklist: Emitting Best Practices**

| Principle               | Description                                                       |
| ----------------------- | ----------------------------------------------------------------- |
| **Structured Emission** | Use JSON or key-value logs instead of plain text.                 |
| **Consistent Markup**   | Include standard fields (timestamp, service, trace_id, severity). |
| **Stateless Output**    | Write to stdout for containerized environments.                   |
| **Rate Limiting**       | Prevent emission storms (e.g., retry floods, SNMP traps).         |
| **Secure Transmission** | Encrypt data, sign payloads, avoid sensitive content.             |
| **Error Tolerance**     | Queue locally when network or collector unavailable.              |

---

## ⚙️ **Transporting Telemetry from Emitters to Storage**

### 🎯 **Purpose of the Shipping Stage**

After telemetry is **emitted** (created), it must be **transported safely, efficiently, and predictably** to a central storage or processing system.

Jamie Riedesel frames this stage as the **circulatory system** of software telemetry:

> **“If emitters are the organs that produce telemetry, the shipping layer is the bloodstream — carrying vital information to where it can be understood.”**

She warns:

> **“Telemetry shipping failures are invisible disasters — the system looks healthy, but you’ve gone blind.”**

This stage decides whether **data is lost, delayed, duplicated, or corrupted** before reaching its destination.

---

### 🧩 **1. Direct vs. Queued Shipping**

Telemetry can be delivered in two architectural patterns: **direct** or **queued**. Each comes with trade-offs in **latency, reliability, cost, and operational complexity**.

#### (a) **Direct Shipping**

* Emitters **send telemetry straight to the destination system** (e.g., Elasticsearch, Prometheus, Splunk, or a cloud collector).
* Common in **small systems** or **serverless functions** where simplicity matters more than resilience.
* Example:

  * An NGINX log stream sent directly to **Elasticsearch**.
  * A microservice posting metrics directly to **Prometheus PushGateway**.

**Advantages:**

* Simpler pipeline (fewer moving parts).
* Lower latency (no intermediate queue).
* Easier debugging (fewer hops).

**Disadvantages:**

* **Backpressure risk:** if the destination is overloaded, emitters may block or drop data.
* **Tight coupling:** changes in the storage schema or endpoint can break emitters.
* **No replay:** lost data is unrecoverable.

Riedesel warns:

> **“Direct shipping is like driving without a seatbelt — fine until the crash.”**

It’s acceptable for prototypes or low-volume systems, but not for **production-grade telemetry**.

---

#### (b) **Queued Shipping**

* Telemetry is sent first to a **buffering or queuing layer** (e.g., **Kafka**, **RabbitMQ**, **AWS Kinesis**, **Google Pub/Sub**, or **Fluentd**).
* This intermediate layer **decouples emitters from consumers**, providing resilience, ordering, and backpressure handling.

**Flow Example:**

```
Emitters → Fluent Bit → Kafka → Logstash → Elasticsearch
```

**Advantages:**

* **Durability:** queues can store messages until downstream systems recover.
* **Scalability:** emitters can continue sending even during heavy load.
* **Flexibility:** multiple consumers can process the same stream differently (e.g., metrics vs. security analysis).
* **Replay capability:** past telemetry can be reprocessed for incident investigation or schema changes.

**Disadvantages:**

* Added complexity (more components to operate).
* Higher latency (milliseconds to seconds).
* Potential for data duplication or out-of-order messages.

Riedesel emphasizes:

> **“Queues turn telemetry from a fragile stream into a resilient river — but you must control the flood.”**

---

### 🚦 **2. Backpressure and Flow Control**

A crucial design theme in this chapter is **backpressure** — what happens when telemetry is produced faster than it can be stored or analyzed.

* Emitters can **block**, **drop**, or **buffer** data.
* Intermediate queues can **fill up** and cause **network congestion**.
* Overloaded collectors can **throttle** incoming streams.

Riedesel’s principle:

> **“Telemetry that blocks application progress becomes a self-inflicted denial of service.”**

**Best Practices:**

1. Use **asynchronous emission** wherever possible.
2. Implement **bounded buffers** to avoid unbounded memory growth.
3. Employ **drop policies** for non-critical telemetry under load.
4. Monitor queue depth as a **first-class metric** — it’s the heartbeat of your telemetry system.

---

### ☁️ **3. Shipping Between SaaS Systems**

Modern organizations operate across multiple SaaS environments — AWS, Datadog, GitHub, Cloudflare, Okta, etc.

These systems each emit **telemetry-as-a-service**, but **interconnecting them** is complex.

Riedesel observes:

> **“In the cloud era, telemetry has gone federated — no single system owns the truth anymore.”**

#### **Challenges:**

* **Diverse formats:** JSON schemas differ between vendors.
* **Rate limits:** APIs often throttle requests.
* **Data latency:** events may arrive hours after emission.
* **Security & credentials:** API keys, webhooks, and IAM roles all need secure rotation.

#### **Integration Patterns:**

1. **Webhook relays:** immediate push of telemetry to your collector (e.g., Stripe → HTTP endpoint).
2. **Scheduled API pulls:** periodic retrieval (e.g., GitHub audit logs via REST).
3. **Cloud-native bridges:** AWS EventBridge, GCP Pub/Sub connectors.

#### **Best Practice:**

> **“Don’t build your own SaaS bridge when the vendor already offers an export stream — consume, don’t scrape.”**

Use **vendor-supported streaming APIs** or **ETL services** (like Snowflake connectors, Datadog forwarders) to maintain reliability and schema consistency.

---

### 🧭 **4. Tipping Points for Architecture Change**

As telemetry grows, systems reach **scaling inflection points** that force architectural evolution.

Riedesel frames these **tipping points** as natural transitions every organization eventually faces:

| Stage                   | Symptoms                                | Needed Shift                                                              |
| ----------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| **Local Logging**       | Manual file collection, missing events  | Adopt centralized logging via syslog or Fluentd                           |
| **Direct Shipping**     | Collector overload, data loss           | Introduce buffering (Kafka, Kinesis)                                      |
| **Buffered Shipping**   | Queue lag, cost explosion               | Introduce **data retention policies** and **aggregation**                 |
| **Federated Telemetry** | Multiple SaaS systems, siloed analytics | Deploy **unified schema governance** and **cross-domain correlation IDs** |

She warns:

> **“Every telemetry system outgrows its first architecture — the tragedy is not noticing it until data is gone.”**

---

## 🧱 **Unifying Formats and Encoding Telemetry**

### 🎯 **Purpose**

Once telemetry reaches the collector, it must be **normalized, encoded, and made uniform** so it can be indexed, visualized, and correlated across systems.

Riedesel introduces this chapter with a central idea:

> **“Telemetry that cannot be unified cannot be trusted.”**

Even if data is collected flawlessly, **inconsistent encoding or schema mismatch** makes it impossible to query effectively or perform cross-system analytics.

---

### 🔄 **1. The Problem of Format Fragmentation**

Every emitter speaks its own dialect:

* One app writes **plain text logs**
* Another emits **JSON**
* A third sends **Syslog-formatted lines**
* A SaaS product sends **nested JSON objects**

Result:

> **“Without translation, your telemetry warehouse becomes a Babel tower of half-truths.”**

Thus, the **unifying stage** converts all formats into a **normalized schema** for storage.

---

### ⚙️ **2. Converting Between Syslog, JSON, and Object Encodings**

Riedesel presents practical examples of how telemetry data transforms across formats:

#### (a) **Syslog → JSON**

* Syslog is a legacy standard for event messages in networked systems.
* Contains a **priority**, **timestamp**, **hostname**, **process name**, and **message**.
* However, the “message” part is often unstructured text.

To make it machine-readable, we wrap it in JSON or extract key fields:

```text
<34>1 2024-01-01T12:00:00Z web01 nginx[123]: request_path=/home status=200
```

➡️

```json
{
  "timestamp": "2024-01-01T12:00:00Z",
  "host": "web01",
  "app": "nginx",
  "request_path": "/home",
  "status": 200
}
```

> **“Translating Syslog to structured JSON is the single most powerful upgrade a telemetry pipeline can make.”**

#### (b) **JSON → Object Encodings**

* JSON is widely supported but inefficient for **high-volume metrics**.
* Alternatives: **Protocol Buffers**, **Avro**, or **MessagePack** — more compact and schema-driven.
* These enable **binary serialization**, saving bandwidth and storage at scale.

Riedesel cautions:

> **“Choose binary formats for machines, not for humans — you can’t grep a protobuf.”**

She suggests a **hybrid approach**:

* Use JSON for ingestion and debugging.
* Convert to binary encodings for long-term archival or analytics.

---

### 🧩 **3. Schema Governance and Field Consistency**

Beyond syntax, **semantic alignment** is essential:

* Standardize field names: always use `service`, not `svc_name` or `app_name`.
* Enforce timestamp formats (e.g., **ISO 8601 in UTC**).
* Maintain **type discipline** — don’t let `user_id` be a string in one service and an integer in another.

> **“A telemetry schema is a contract between your systems and your sanity.”**

To enforce this, organizations adopt:

* **OpenTelemetry semantic conventions**
* **JSON schema validation pipelines**
* **CI/CD schema linting tools**

---

### 📊 **4. Designing for Cardinality Scalability**

Perhaps the most important section in this chapter deals with **cardinality** — the number of unique combinations of metric labels.

#### **What is Cardinality?**

* A metric with labels (e.g., `requests_total{region="us-east", user_id="12345"}`) has high cardinality if **too many unique label values exist**.
* Each unique combination creates a **new time-series** in systems like Prometheus.

Riedesel explains:

> **“Cardinality is the hidden tax of telemetry — you pay it in memory, CPU, and time.”**

#### **Symptoms of Cardinality Explosion**

* Prometheus OOMs or slows down.
* Dashboards become sluggish.
* Query engines timeout.
* Costs skyrocket for hosted monitoring.

#### **Best Practices**

1. **Avoid user-specific labels** (e.g., `user_id`, `session_id`).
2. **Bucketize values** (e.g., latency buckets instead of per-request times).
3. **Aggregate early** (e.g., sum per-region, not per-instance).
4. **Implement cardinality budgets** — define acceptable series counts per service.

> **“Every new label combination should earn its keep — if you can’t justify it, remove it.”**

She also stresses **instrumentation discipline**:

* Developers should understand that adding a single new label can multiply storage costs.
* Create **shared review processes** for new metrics.

#### **Rule of Thumb:**

> **“A telemetry system dies not from too little data, but from too much uniqueness.”**

---

### 📦 **5. End-to-End Encoding Pipeline Example**

Riedesel outlines a realistic data path combining both chapters’ ideas:

```
Emitters (Apps, Devices, SaaS)
   ↓
Fluent Bit Agents
   ↓
Kafka Topics (JSON)
   ↓
Logstash Processors
   ↓
Elasticsearch (normalized JSON)
   ↓
Data Warehouse / SIEM (binary compressed objects)
```

Each step either **translates** (e.g., Syslog → JSON) or **reformats** (JSON → Protobuf), balancing **human readability** with **machine efficiency**.

---

### 🧠 **Summary — “Unification Is Understanding”**

> **“You can’t correlate what you can’t normalize.”**

In Riedesel’s framework, **unifying formats and controlling cardinality** are what transform telemetry from *data* into *knowledge*.

Without schema governance, telemetry becomes noise.
Without cardinality discipline, it becomes cost.

The ultimate design goal:

> **“Emit structured data, ship it safely, unify it consistently, and scale it responsibly — that’s the architecture of trustworthy telemetry.”**

---

✅ **Summary Checklist: Shipping + Encoding Best Practices**

| Principle                         | Description                                                              |
| --------------------------------- | ------------------------------------------------------------------------ |
| **Use Queues**                    | Always buffer between emitters and storage to handle spikes and outages. |
| **Monitor Queue Depth**           | Treat backlog as a leading indicator of telemetry health.                |
| **Normalize Formats Early**       | Convert Syslog/plaintext to structured JSON at ingestion.                |
| **Govern Schemas**                | Enforce consistent field names and data types.                           |
| **Control Cardinality**           | Eliminate unnecessary metric labels and aggregate early.                 |
| **Plan Architecture Transitions** | Watch for tipping points as data volume or team count grows.             |

---


## 📊 **Presentation Stage: Visualizing and Aggregating Telemetry**

### 🎯 **Purpose of the Presentation Stage**

In previous chapters, Riedesel covered the **emission** (creation) and **shipping** (transport) of telemetry data. Now, she focuses on what she calls **“the final mile”** — the stage where data **meets human cognition**.

> **“The presentation stage is where telemetry leaves the machine world and enters the human world.”**

At this point, the system’s success depends not just on performance or schema — but on **how clearly people can interpret what’s shown**.

The author makes an essential distinction:

> **“Raw telemetry tells you what happened. Presentation tells you what it means.”**

This chapter is not just about pretty dashboards — it’s about **transforming telemetry into decision support systems** for engineers, analysts, executives, and compliance teams.

---

### 🧩 **1. From Data to Understanding: The Role of Presentation**

Riedesel opens with a core principle:

> **“A telemetry system that doesn’t present well is a silent system — it’s talking, but no one understands it.”**

Even if your collection and storage layers are perfect, poor presentation creates:

* **Information overload**
* **False confidence in averages**
* **Ignored warnings**
* **Unquestioned dashboards that mislead**

Thus, the presentation stage is about designing **“clarity pipelines”**, not just dashboards.

#### Key Goals:

1. **Visualize** — Turn complex datasets into intuitive, interactive visual models.
2. **Aggregate** — Summarize raw data to reveal trends, patterns, and anomalies.
3. **Link** — Connect telemetry signals to **decisions and actions**.

---

### 🖥️ **2. Visualizing Telemetry: Dashboards and Human Factors**

Telemetry visualization tools like **Grafana, Kibana, Datadog, Splunk, and New Relic** are central to this stage.
Riedesel argues that **dashboards are the “storytellers” of telemetry**, but only if designed deliberately.

> **“Good dashboards explain, not impress.”**

#### **(a) Grafana and Kibana as Exemplars**

* **Grafana** excels at **numerical and time-series visualization**, built on metrics like Prometheus or InfluxDB.

  * Ideal for **SRE and operations dashboards** (e.g., latency, CPU, error rates).
  * Provides strong alerting and panel templating.

* **Kibana**, part of the **ELK (Elasticsearch, Logstash, Kibana)** stack, is optimized for **exploratory log analytics** and **ad hoc querying**.

  * Ideal for debugging and tracing.
  * Enables slicing by text, metadata, or fields (e.g., `status_code:500 AND region:us-west`).

**Integration pattern example:**

```
Fluentd → Elasticsearch → Kibana
Prometheus → Grafana
Jaeger → Grafana/Tempo (for traces)
```

Each tool sits on top of the telemetry stack, turning **streams of data into human-friendly visuals**.

---

#### **(b) Dashboard Design Principles**

Riedesel draws on cognitive ergonomics — how humans perceive information under stress — especially during **incident response**.

> **“Dashboards are not for beauty contests; they’re for firefights.”**

**Principles:**

1. **Clarity over completeness.** Avoid overloading with too many panels or metrics.
2. **Layered storytelling.** Start with high-level status, then drill into details.
3. **Color with purpose.** Red = urgency, green = normal, gray = unknown. Avoid rainbow palettes that dilute meaning.
4. **Context first.** Always show **time window**, **environment**, and **version** metadata.
5. **Annotations and correlation.** Overlay deploy events, config changes, or feature flags on metric graphs.

> **“If your dashboard can’t tell you when the last deploy happened, it’s missing the most important annotation of all.”**

---

### 📈 **3. Aggregation: Making Sense of Volume**

After visualization comes **aggregation** — the mathematical condensation of billions of telemetry points into meaningful summaries.

Riedesel stresses:

> **“Aggregation is the act of asking better questions of your data.”**

Without aggregation, telemetry is just noise — a firehose of irrelevant detail.

#### **(a) Types of Aggregation Functions**

Different telemetry types require different summarization strategies:

| Telemetry Type | Common Aggregations                        | Example                        |
| -------------- | ------------------------------------------ | ------------------------------ |
| **Metrics**    | Average, percentile, rate, sum, count      | `avg(request_latency)`         |
| **Logs**       | Count by severity, group by message        | `count(*) WHERE level='error'` |
| **Traces**     | Average span duration, top N slowest paths | `p95(span.duration)`           |

Riedesel distinguishes between **descriptive** and **diagnostic** aggregations:

* *Descriptive:* what’s happening now (e.g., average latency).
* *Diagnostic:* why it’s happening (e.g., correlation between latency and region).

> **“Every aggregation hides detail — make sure you’re hiding the right details.”**

---

#### **(b) Temporal Aggregation**

Telemetry data is inherently **time-based**, so **temporal aggregation** is critical:

* **Minute/hour/day windows** reveal trends and patterns.
* **Moving averages** smooth volatility but can hide spikes.
* **Percentiles** (p50, p90, p99) expose outliers and tail latency.

Riedesel warns:

> **“Averages are comfort food — easy to digest, but nutritionally empty.”**

**Example:**
If your 99th percentile latency is 5 seconds while the average is 200ms, you’re misleading yourself with the average.
Use **histograms** or **quantile-based aggregation** for operational truth.

---

#### **(c) Dimensional Aggregation and Cardinality Awareness**

When aggregating, it’s easy to accidentally reintroduce **cardinality explosion** (see Chapter 4).

For example:

```promql
sum(rate(http_requests_total[5m])) by (region, service)
```

is good — but adding `by (region, service, user_id)` will **multiply series exponentially**.

> **“Aggregation is a compression algorithm — not a multiplication algorithm.”**

Always aggregate along **business-relevant dimensions**, not arbitrary identifiers.

---

### 📊 **4. Statistical Validity in Telemetry**

One of the book’s most insightful sections discusses **the dangers of misusing telemetry statistics**.

Riedesel writes:

> **“Dashboards lie — not because they want to, but because we ask the wrong questions.”**

#### **(a) Sampling Bias**

Telemetry often represents only what’s **instrumented**, not what’s **experienced**.
For instance, a log-based metric may exclude events from services that failed silently.

> **“Telemetry shows the observable universe — not the entire one.”**

Mitigation:

* Ensure uniform instrumentation across services.
* Use synthetic monitoring to fill visibility gaps.

#### **(b) Aggregation Distortion**

Improper aggregation can distort truth:

* Averaging across dissimilar metrics (e.g., combining batch and interactive workloads).
* Merging time zones or misaligned intervals.
* Using **non-weighted averages** for metrics like cost or duration.

> **“Statistics without context are worse than no statistics at all.”**

#### **(c) False Correlations**

With large telemetry datasets, it’s easy to “discover” meaningless patterns.
Example: CPU spikes correlating with user logins — but actually caused by a background cache warmup.

Riedesel warns:

> **“The more telemetry you have, the more coincidences you’ll mistake for causes.”**

Mitigation: Always **verify correlation through causality tests** — link metrics to traces and logs.

---

### 🧠 **5. Linking Raw Data to Decision Support**

This section marks the philosophical heart of the chapter — transforming telemetry from operational feedback into **organizational intelligence**.

> **“Telemetry is not the goal. Decision-making is.”**

#### **(a) Multi-Layered Feedback Loops**

Riedesel describes telemetry as the backbone of **multiple feedback loops**:

* **Real-time:** alerting, anomaly detection, incident response.
* **Tactical:** post-incident analysis, sprint retrospectives.
* **Strategic:** capacity planning, feature adoption, cost optimization.

She compares it to **business nervous systems**:

> **“Telemetry tells you when to flinch, when to heal, and when to grow.”**

#### **(b) Bridging Engineering and Business**

Telemetry presentation must serve both **technical and non-technical stakeholders**:

* Engineers: need detailed traces and metrics for debugging.
* Executives: need KPI dashboards showing uptime, cost, and user satisfaction.
* Compliance officers: need verifiable logs of access and retention.

The same data supports all these roles through **different aggregation and visualization layers**.

> **“If your telemetry only serves engineers, it’s observability. When it serves decisions, it’s intelligence.”**

#### **(c) From Dashboards to Automation**

The most advanced organizations go beyond manual dashboards into **automated telemetry-driven decision systems**:

* **Autoscaling policies** driven by metrics.
* **Canary deployment rollbacks** based on telemetry thresholds.
* **Security incident responses** triggered by SIEM telemetry.

This is telemetry maturing into **“autonomic feedback”** — the system self-correcting based on what it sees.

> **“Mature telemetry systems don’t just inform humans — they empower systems to react faster than humans can.”**

---

### 🔐 **6. The Cost of Presentation**

Riedesel closes with a sober reminder: visualization layers are **expensive and fragile** if mismanaged.

* **Query costs** grow exponentially as users run interactive dashboards.
* **Retention policies** must filter what’s visualized vs. what’s archived.
* **Security**: dashboards often expose sensitive fields (user IDs, IPs, PII).

Hence:

> **“Every pixel you show has a cost — in compute, in clarity, and in confidentiality.”**

She encourages building **tiered access dashboards**:

* Ops dashboards → detailed, low-level metrics.
* Management dashboards → aggregated KPIs only.
* Security dashboards → anonymized and access-controlled.

---

### ✅ **Summary — Presentation as Decision Infrastructure**

> **“The value of telemetry is realized not when it’s collected, but when it’s understood.”**

Riedesel’s closing insight reframes telemetry systems as **decision infrastructure** — the bridge between **observation and action**.

**Summary Principles:**

1. **Design dashboards for cognition, not decoration.**
2. **Aggregate carefully — never hide pain behind averages.**
3. **Validate statistical soundness** — telemetry lies if misunderstood.
4. **Align presentation with decisions** — every graph should answer “so what?”.
5. **Protect and optimize visual data** — clarity, privacy, and cost all matter.

> **“A telemetry system’s purpose is to make invisible problems visible — and visible truths actionable.”**

---

✅ **Summary Checklist: Presentation Stage Best Practices**

| Category                  | Best Practice                                       | Key Insight                                                 |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| **Visualization**         | Use Grafana/Kibana with consistent design patterns  | *“Dashboards explain, not impress.”*                        |
| **Aggregation**           | Favor percentiles and context-based grouping        | *“Averages comfort, percentiles reveal.”*                   |
| **Statistical Integrity** | Avoid bias, validate sampling, and ensure causality | *“Telemetry shows what’s observable, not everything.”*      |
| **Decision Alignment**    | Tailor dashboards to user roles and goals           | *“When telemetry informs action, it fulfills its purpose.”* |
| **Governance & Security** | Control dashboard access, anonymize sensitive data  | *“Every pixel you show has a cost.”*                        |

---

## 🧩 **Marking Up and Enriching Telemetry**

### 🎯 **Purpose of This Chapter**

After understanding how telemetry is **emitted**, **shipped**, and **presented**, Riedesel now focuses on the **middle intelligence layer** — where raw data gains meaning, traceability, and relational depth.

She opens with one of the most important quotes in the entire book:

> **“Telemetry without context is trivia. Telemetry with context is knowledge.”**

This chapter is about creating that context — transforming a jumble of events, metrics, and traces into a **cohesive story** of what’s really happening in your system.

Riedesel emphasizes that **markup** and **enrichment** are what enable **cross-system correlation**, **root-cause analysis**, and **observability at scale**.

> **“You don’t debug single events — you debug stories told by correlated events.”**

---

### 🧠 **1. The Difference Between Markup and Enrichment**

Riedesel carefully distinguishes between two intertwined but distinct concepts:

#### **(a) Markup = Structure**

Markup adds **syntactic clarity** — making each telemetry event **machine-readable, schema-consistent, and self-describing**.

> **“Markup is about structure — turning a blob of text into an object with meaning.”**

Markup examples:

```json
{
  "timestamp": "2025-10-10T17:00:00Z",
  "service": "checkout-api",
  "severity": "error",
  "message": "Payment gateway timeout",
  "trace_id": "abcd1234efgh5678",
  "region": "us-west-2"
}
```

Every field is **explicit**, typed, and standardized — enabling systems like Elasticsearch, Prometheus, or Grafana to **index, correlate, and aggregate** effectively.

Riedesel notes:

> **“Good markup is the grammar of telemetry. It’s how machines learn to read what humans already understand.”**

---

#### **(b) Enrichment = Context**

Enrichment, by contrast, adds **semantic information** — metadata that **wasn’t originally part of the emitted event**, but helps **explain it**.

> **“Enrichment doesn’t change the fact — it changes how useful that fact becomes.”**

Examples:

* Adding the **deployment version** or **Git commit SHA** to logs.
* Adding **region**, **availability zone**, or **tenant ID**.
* Appending **user tier**, **plan type**, or **business unit** for analytics.
* Linking **trace IDs** to correlate across services.

Enrichment transforms raw telemetry into **narrative telemetry** — where each data point knows **who**, **what**, **where**, and **why**.

> **“Telemetry enrichment is how you teach your systems to think like an investigator.”**

---

### ⚙️ **2. The Mechanics of Markup**

Riedesel dives into the technical mechanics of how markup works in telemetry pipelines.

#### **(a) Structural Consistency**

Every telemetry event should follow a consistent schema:

* **Required fields** (timestamp, service, severity)
* **Optional metadata** (trace_id, environment, user_id)
* **Consistent naming** (`user_id`, not `userid` or `UserID`)
* **Consistent data types** (`int` for counts, `string` for messages)

> **“Markup is not about adding fields; it’s about agreeing what the fields mean.”**

She recommends adopting **industry-wide conventions**, such as those defined by:

* **OpenTelemetry semantic conventions**
* **Elastic Common Schema (ECS)**
* **CloudEvents specification**

These frameworks allow **interoperability across vendors and platforms** — essential in hybrid and multi-cloud ecosystems.

---

#### **(b) Example: Turning Freeform Logs into Structured Telemetry**

Raw log:

```
[ERROR] 2025-10-10 16:42:05 - Order 12345 failed - timeout talking to payment API
```

Structured telemetry:

```json
{
  "timestamp": "2025-10-10T16:42:05Z",
  "level": "error",
  "order_id": 12345,
  "error": "payment_timeout",
  "service": "checkout-api",
  "env": "prod",
  "region": "us-central1"
}
```

> **“Structure is compression through meaning — every field saves time downstream.”**

Structured markup eliminates the need for regex parsing, allows faster search, and enables aggregation across attributes like service or region.

---

### 🧬 **3. The Art of Enrichment: Adding Context Intelligently**

Riedesel emphasizes that **not all enrichment is good enrichment**.

Adding context must be **intentional**, **relevant**, and **cost-aware**.

> **“Every field you add is a new dimension to store, index, and query — treat enrichment like seasoning, not stuffing.”**

#### **(a) Sources of Enrichment**

Enrichment data usually comes from **metadata services**, **infrastructure layers**, or **lookup tables**:

| Source                       | Example Enrichment          | Use                              |
| ---------------------------- | --------------------------- | -------------------------------- |
| **Deployment metadata**      | app version, build hash     | Track regressions after releases |
| **Cloud metadata**           | region, zone, instance type | Correlate outages by region      |
| **Business metadata**        | tenant ID, plan type        | Analyze impact by customer tier  |
| **CI/CD systems**            | pipeline ID, branch name    | Trace issues to deployments      |
| **Infrastructure inventory** | host tags, owner team       | Accountability and escalation    |

> **“Enrichment connects telemetry to the human structures that care about it.”**

---

#### **(b) Real-Time vs. Offline Enrichment**

There are **two main timing models** for enrichment:

1. **Real-Time Enrichment** — applied **in-stream**, as telemetry flows through agents like **Fluentd**, **Logstash**, or **Vector**.
   Example:

   * A Fluentd filter injects `region` and `environment` tags from EC2 metadata API.
   * Useful for contextual tagging of **live telemetry** for monitoring and alerting.

2. **Offline Enrichment** — applied **post-ingestion**, typically through **ETL or batch jobs** in a data warehouse.
   Example:

   * Adding customer profile info from CRM or billing database.
   * Useful for **forensic analysis, compliance, and business intelligence**.

> **“Real-time enrichment explains the ‘how.’ Offline enrichment explains the ‘why.’”**

The most mature telemetry systems use both.

---

#### **(c) Correlation IDs — The Backbone of Observability**

Riedesel calls **correlation IDs** the **“glue of distributed understanding.”**

In complex microservice systems, a single user action (like submitting an order) may generate telemetry across:

* API Gateway
* Order Service
* Payment Processor
* Notification Queue

Each service emits logs and metrics — but without correlation, they look unrelated.

By adding a **shared correlation ID** (e.g., `trace_id`), you can reconstruct the entire request path.

> **“Correlation IDs turn chaos into choreography.”**

**Implementation patterns:**

* Use **UUIDv4** or **ULID** as unique identifiers.
* Propagate IDs through **HTTP headers** (e.g., `X-Request-ID` or `traceparent` in W3C Trace Context).
* Add the ID to **all logs, metrics, and traces** within that request scope.

**Result:**
You can query in Kibana or Grafana for a single correlation ID and see the entire cross-service narrative.

---

### 🔢 **4. Type Conversions and Data Normalization**

Once telemetry is enriched, it’s critical that all fields maintain **consistent data types and formats**.

Riedesel warns:

> **“A number stored as a string is telemetry’s version of a landmine — it looks safe until you step on it.”**

#### Common Issues:

* **Strings vs. integers:** `"200"` vs `200`
* **Boolean inconsistencies:** `"true"` vs `true`
* **Timestamp chaos:** mixed time zones or unstandardized formats
* **Case sensitivity:** `"ERROR"`, `"Error"`, `"error"`

These inconsistencies break aggregations, filters, and visualizations.

**Best Practices:**

1. Always use **ISO 8601 UTC** for timestamps.
2. Standardize units (e.g., milliseconds, bytes).
3. Normalize boolean and severity levels (`info`, `warn`, `error`).
4. Apply **schema validation** before ingestion (JSON Schema, Avro).

> **“Normalization is the hygiene of telemetry — invisible when done right, revolting when ignored.”**

---

### 🧩 **5. Advanced Enrichment: Derived and Synthetic Fields**

Beyond metadata, you can add **derived fields** — calculated or inferred values that enhance analysis.

Examples:

* Compute **latency buckets** from timestamps (`duration_ms`).
* Add **error_category** (network vs. database vs. user).
* Add **geo-location** from IP address.
* Add **business impact** (“premium customer”, “high-value transaction”).

These are called **synthetic enrichments** — not present in the raw data, but inferred from it.

Riedesel’s insight:

> **“Enrichment is not just decoration — it’s transformation. You’re building new meaning from old data.”**

However, she warns:

> **“Every synthetic field adds processing cost — only enrich what improves your ability to decide.”**

---

### 🧠 **6. Governance and Safety in Enrichment**

While enrichment adds power, it also increases **risk** — of leaks, privacy violations, and cost bloat.

Riedesel highlights **three safety principles**:

#### (a) **Data Minimization**

Only enrich with data that is:

* Necessary for observability or analysis.
* Non-sensitive or anonymized.
* Cleared for use under privacy policy.

> **“Telemetry enrichment is seductive — it tempts you to add what you don’t need.”**

#### (b) **Field Classification**

Establish **data classification** for telemetry fields:

* **Public** (non-sensitive)
* **Internal** (organizational only)
* **Confidential** (user data, PII)

Use this classification to enforce redaction and access control downstream.

#### (c) **Immutable Enrichment**

Once telemetry is emitted and enriched, **don’t retroactively modify it in-place**.
Instead, reprocess it through a separate pipeline.

> **“Telemetry is evidence — never tamper with evidence.”**

---

### 🧭 **7. Practical Pipeline Example**

Riedesel gives a sample end-to-end enrichment architecture:

```
Applications (emit JSON logs)
   ↓
Fluent Bit / Fluentd agent
   ↓
→ Enrichment filter (adds region, env, trace_id)
   ↓
→ Logstash (schema validation, type conversion)
   ↓
→ Kafka topic (structured events)
   ↓
→ Elasticsearch / Data Lake
   ↓
→ Offline enrichment (business metadata join)
   ↓
→ Kibana / Grafana dashboards
```

Each stage adds **context, safety, and structure**, producing **telemetry that is both technically and semantically consistent**.

> **“Enrichment is the bridge between the system that emits and the people who must understand.”**

---

### 🔍 **Summary — Context Is the Multiplier**

Riedesel concludes with a central thesis:

> **“Enrichment doesn’t make telemetry bigger — it makes it smarter.”**

The more meaning you attach to your data **without compromising cost, performance, or privacy**, the more **actionable and self-explanatory** your system becomes.

---

✅ **Summary Checklist: Markup & Enrichment Best Practices**

| Category                 | Practice                                                          | Key Insight                                                     |
| ------------------------ | ----------------------------------------------------------------- | --------------------------------------------------------------- |
| **Markup**               | Use structured formats (JSON, Avro, OpenTelemetry schema)         | *“Structure is the grammar of telemetry.”*                      |
| **Metadata**             | Add consistent tags: service, env, region, version                | *“Markup makes data readable; enrichment makes it useful.”*     |
| **Correlation**          | Propagate trace IDs or request IDs across services                | *“Correlation IDs turn chaos into choreography.”*               |
| **Type Safety**          | Normalize data types and timestamps                               | *“Normalization is telemetry hygiene.”*                         |
| **Selective Enrichment** | Add only meaningful, low-risk context                             | *“Treat enrichment like seasoning — a little goes a long way.”* |
| **Governance**           | Classify fields, redact sensitive data, prevent retroactive edits | *“Telemetry is evidence — never tamper with evidence.”*         |

---


Excellent — below is a **comprehensive, in-depth expansion** of **Part 2 — Use Cases Revisited** and **Chapter 8 — “Growing Cloud-Based Startup”** from *Software Telemetry* by **Jamie Riedesel**, written in your preferred **bold-highlighted, technically grounded, and architectural narrative style.**

This section marks the **practical midpoint** of the book — where theory meets reality.
Riedesel transitions from **architecture blueprints** to **real-world evolution stories**, showing how telemetry systems **grow, break, and mature** in different organizational contexts.

---

# 🌐 **Use Cases: Applying Architecture Concepts**

## 🎯 **Purpose of Part 2**

Riedesel takes the reader through **eleven progressively complex organizational case studies**, each demonstrating how **telemetry architecture evolves with scale, culture, and maturity**.

> **“Every organization already has telemetry — the question is whether it’s intentional or accidental.”**

This part answers:

* How do telemetry systems **start small and scale up**?
* When do they **outgrow vendor dashboards** and build custom pipelines?
* What are the **failure patterns** at each stage of telemetry maturity?
* How do compliance, cost, and chaos shape architectural choices?

---

## 🧱 **Telemetry Maturity Spectrum**

Before diving into case studies, Riedesel introduces a **maturity model**:

| Stage           | Description                                   | Key Risk                     |
| --------------- | --------------------------------------------- | ---------------------------- |
| **Ad Hoc**      | Each engineer logs and monitors independently | Data fragmentation           |
| **Centralized** | Shared dashboards and metrics                 | Scaling bottlenecks          |
| **Automated**   | Pipeline-based ingestion and standard schemas | Complexity growth            |
| **Regulated**   | Telemetry treated as compliance evidence      | Cost and governance pressure |

She writes:

> **“Telemetry maturity doesn’t correlate with company size — it correlates with pain tolerance.”**

Even small teams can build sophisticated systems if they experience operational pain early.
Conversely, large enterprises can remain stuck in fragmented chaos if telemetry isn’t prioritized strategically.

---

## 🚀 **Growing Cloud-Based Startup**

### 🧩 **Overview**

This chapter follows the journey of a **typical cloud-native startup** — a small but fast-growing SaaS company running entirely on **AWS, GCP, or Azure**.

Riedesel uses this archetype to explore how **telemetry evolves organically** from a handful of dashboards into a **purpose-built internal telemetry platform.**

> **“In startups, telemetry begins as a luxury and ends as a lifeline.”**

---

### ☁️ **1. Phase 1 — The “Single Dashboard Era” (Telemetry by Vendor Defaults)**

At the beginning, the startup’s entire monitoring and observability strategy relies on **whatever their cloud provider gives them out of the box.**

#### **Common Setup:**

* AWS CloudWatch / GCP Stackdriver / Azure Monitor
* Application logs written to stdout or Cloud Logging
* Occasional use of vendor dashboards for uptime and CPU metrics
* Alerts configured in email or Slack based on simple thresholds

#### **Example:**

> “If CPU > 80% for 5 minutes → send Slack alert to #ops-channel”

Riedesel describes this phase as **“telemetry by convenience”**:

> **“You’re using telemetry not because you designed for it, but because the cloud makes it impossible not to.”**

**Benefits:**

* Zero infrastructure overhead
* Tight integration with cloud resources
* Easy visualization (managed dashboards)

**Limitations:**

* Fragmented between services (Lambda logs in one place, RDS logs in another)
* Poor correlation between components
* No standardized schema or cross-application traceability
* Limited retention and export capability
* Vendor lock-in

> **“At this stage, telemetry exists — but understanding doesn’t.”**

The startup may think it’s observant, but in reality, it’s **staring at disconnected instruments**.

---

### 🧰 **2. Phase 2 — The “Glue and Scripting Era” (Telemetry Chaos Automation)**

As the startup grows (perhaps from 5 to 25 engineers, or from 1 to 10 services), **manual debugging through logs and dashboards becomes unscalable.**

Engineers begin writing **custom scripts, cron jobs, and glue logic** to stitch together data from multiple cloud services.

**Typical signs of this phase:**

* Bash or Python scripts pulling data from CloudWatch APIs
* Ad hoc dashboards combining CloudWatch + Prometheus data
* CSV exports of logs for local analysis
* Alerts manually tuned by individual teams
* “Shadow telemetry” — each team manages its own subset of metrics and logs

Riedesel calls this:

> **“The era of telemetry folklore — everyone has a personal script that nobody else understands.”**

#### Example Failure Pattern:

* A production outage occurs.
* Half the logs are in AWS CloudWatch, half in a Lambda console.
* One engineer remembers they once built a Python script that fetches S3 error logs — but it’s not in Git.

> **“At this point, your telemetry is more like detective work than engineering.”**

The startup is now painfully aware of **visibility debt** — every debugging session costs hours of grep, scroll, and guesswork.

---

### 🏗️ **3. Phase 3 — The “Internal Pipeline Awakening”**

After the first few painful outages, leadership finally recognizes that **telemetry is infrastructure, not tooling.**

The startup begins building its first **internal telemetry pipeline.**

Riedesel explains:

> **“This is the turning point where startups evolve from consuming telemetry to producing telemetry.”**

#### **Architecture Transition:**

From this:

```
App Logs → CloudWatch
Metrics → Prometheus (per service)
Alerts → Email
```

To this:

```
App Logs → Fluent Bit → Kafka → Elasticsearch
Metrics → Prometheus → Grafana
Traces → OpenTelemetry → Jaeger
```

This transition involves three key milestones:

---

#### **(a) Adopting Fluentd / Fluent Bit (Collection Layer)**

* Replace raw CloudWatch logs with structured pipelines.
* Fluent Bit acts as the **first-tier shipper**, aggregating logs locally before sending to Elasticsearch.
* Reduces cost, latency, and dependency on vendor APIs.

> **“Fluent Bit turns your telemetry from a pile of text into a living stream.”**

Key benefits:

* Control over log structure and enrichment
* On-prem or hybrid pipeline compatibility
* Standardization across containers and services

---

#### **(b) Building an ELK Stack (Central Storage and Search Layer)**

* Elasticsearch for indexing
* Logstash for enrichment and filtering
* Kibana for visualization

Riedesel notes:

> **“The ELK stack is the startup’s rite of passage — your first real telemetry system.”**

This allows the team to:

* Centralize application logs, security events, and metrics
* Search by correlation ID across services
* Build shared dashboards with rich filters

However, challenges soon appear:

* Elasticsearch scaling and memory pressure
* Disk storage costs for log retention
* Complex maintenance and upgrades

> **“You’ve gained power — but you’ve also inherited a platform.”**

---

#### **(c) Embracing OpenTelemetry**

As systems scale further (especially in microservice architectures), the startup begins to instrument services using **OpenTelemetry** — for unified tracing, metrics, and logging.

**Why it matters:**

* Avoids vendor lock-in
* Enables **correlation across services**
* Provides **language SDKs** for consistent instrumentation
* Integrates seamlessly with Grafana Tempo, Jaeger, or Honeycomb

> **“OpenTelemetry is how startups graduate from observability to understanding.”**

By this point, telemetry is no longer an afterthought — it’s part of **the CI/CD lifecycle**.

---

### ⚖️ **4. Challenges During the Transition**

Even though this shift is powerful, Riedesel stresses that it introduces new operational and cultural challenges.

#### **(a) Cost Shock**

* Ingestion and indexing costs surge as log volume grows.
* Teams start filtering and sampling telemetry to control expenses.

> **“Telemetry costs will sneak up on you — one debug log at a time.”**

Mitigation strategies:

* Define **retention tiers** (e.g., 7 days for detailed logs, 90 days for summaries).
* Adopt **structured logging** early to avoid noise.
* Move rarely queried telemetry to cheaper storage (S3, Glacier).

---

#### **(b) Ownership and Access Control**

* Who owns the telemetry stack? DevOps? SRE? Platform team?
* Access sprawl occurs when every engineer can query production logs.

> **“Without ownership, telemetry becomes everyone’s responsibility — and no one’s priority.”**

The startup must establish:

* A **central telemetry owner or platform team**
* **RBAC (role-based access control)** for logs and dashboards
* Guidelines for **privacy and PII redaction**

---

#### **(c) Schema and Enrichment Discipline**

With multiple teams emitting data, consistency erodes quickly:

* One service logs `"userId"`, another `"user_id"`.
* Some timestamps are local, others UTC.

> **“In startups, telemetry entropy grows faster than traffic.”**

The solution: implement **schema governance** — define common fields and tag standards (service, region, environment, trace_id).

---

### 🧭 **5. The Maturity Inflection Point**

At around 50–100 employees or ~20 microservices, the startup reaches an **inflection point**.

Riedesel describes it vividly:

> **“You’re no longer a startup with dashboards — you’re an infrastructure company that happens to build a product.”**

Telemetry now serves multiple purposes:

* **Operations** (SRE dashboards, on-call rotation)
* **Security** (SIEM integration, access audit logs)
* **Business Intelligence** (usage metrics, feature adoption)

This diversity forces the startup to **segregate telemetry by audience**:

* Technical telemetry → ELK / Prometheus / Jaeger
* Security telemetry → SIEM
* Product telemetry → Data warehouse / Snowflake

> **“When you start building dashboards for executives, your telemetry system has officially grown up.”**

---

### 🔁 **6. Continuous Improvement: From Pipelines to Platforms**

At this stage, the startup may hire a **Platform Engineer or Telemetry Lead** to scale and optimize the system.

The telemetry stack evolves into a **self-service platform**:

* Developers define **structured log formats** via libraries.
* Pipelines are managed through **infrastructure as code (Terraform, Helm)**.
* Dashboards and alerts are **templated** to ensure consistency.

Riedesel calls this transition:

> **“The move from artisanal telemetry to industrial telemetry.”**

The platform mindset transforms telemetry from **reactive monitoring** to **proactive insight generation**.

---

### 🧠 **Summary — Lessons from the Cloud Startup Journey**

Riedesel closes with several key takeaways that apply broadly across modern software organizations:

| Lesson                                | Description                                                      |
| ------------------------------------- | ---------------------------------------------------------------- |
| **Start simple, but plan to evolve.** | Vendor telemetry is fine at first — until it limits insight.     |
| **Standardize early.**                | Schema discipline saves you from chaos later.                    |
| **Invest before pain.**               | Building pipelines before crises reduces MTTR and cost.          |
| **Telemetry is infrastructure.**      | It requires ownership, governance, and lifecycle management.     |
| **Grow from consumers to producers.** | Don’t just use telemetry tools — build your own system of truth. |

Final insight:

> **“The startup’s telemetry journey mirrors its business journey — from chaos to clarity, from reactive to predictive.”**

---

✅ **Summary Checklist: Growing Cloud-Based Startup Telemetry**

| Stage                       | Description                              | Tools/Practices         | Core Principle                |
| --------------------------- | ---------------------------------------- | ----------------------- | ----------------------------- |
| **Vendor Default**          | Relying on AWS/GCP dashboards            | CloudWatch, Stackdriver | *Telemetry by convenience*    |
| **Glue Scripts**            | Manual API fetches and ad hoc dashboards | Bash, Python scripts    | *Folklore over design*        |
| **Pipeline Foundation**     | Building structured collection           | Fluentd, Kafka, ELK     | *Own your data path*          |
| **Observability Expansion** | Unified tracing and metrics              | OpenTelemetry, Jaeger   | *Correlate everything*        |
| **Platform Maturity**       | Telemetry as a product                   | IaC, governance, RBAC   | *Telemetry as infrastructure* |

---

Perfect — below is a **comprehensive, expanded, and deeply contextualized outline** of **Chapter 9 — “Non-Software Business”** from *Software Telemetry* by **Jamie Riedesel**, written in the same **bold-highlighted, architecture-aware, and narrative-rich** style as before.

This chapter contrasts sharply with the previous one. If Chapter 8 showed a **born-in-the-cloud startup** evolving telemetry through necessity and growth, Chapter 9 focuses on organizations where **software is not the product** — but **still runs the business**.

---

## 🏢 **Non-Software Business**

### 🎯 **Purpose and Context**

Riedesel begins by acknowledging a hard truth:

> **“Every company is a software company — most just don’t know it yet.”**

This chapter examines how **traditional, non-software organizations** (manufacturers, retailers, logistics firms, hospitals, universities, government agencies, etc.) **adopt telemetry indirectly** — first through **IT operations** and later through **digital initiatives** that slowly transform them into software-centric enterprises.

Unlike startups, these companies:

* Don’t have a DevOps culture by default.
* Depend heavily on **off-the-shelf SaaS systems** (ERP, CRM, HR, POS, etc.).
* View telemetry initially as **a compliance or uptime function**, not a product enabler.
* Often suffer from **organizational silos** where operations, development, and business units own different data streams.

Riedesel frames this environment as one of **“telemetry by outsourcing.”**

> **“In non-software businesses, telemetry starts not in the code but in the contracts.”**

---

### 🖥️ **1. Telemetry Begins in the IT Department**

#### **(a) Inherited Visibility from Vendors**

Most non-software organizations rely on a patchwork of SaaS and on-premises systems:

* **Microsoft 365** or **Google Workspace** for collaboration
* **Salesforce**, **SAP**, or **Oracle ERP** for operations
* **ServiceNow**, **PagerDuty**, or **SolarWinds** for IT management
* **VMware**, **Cisco**, or **Fortinet** appliances in the datacenter

Each of these systems emits telemetry — but through its **own proprietary portal** or **API**.

Riedesel writes:

> **“Your first telemetry dashboards arrive through vendor logins, not engineering effort.”**

This results in **fragmented visibility**:

* Network logs are in one portal.
* Application health in another.
* Security events in a third.

> **“The telemetry exists, but it’s trapped in a dozen walled gardens.”**

---

#### **(b) SaaS-Driven Telemetry as a Service**

Because internal IT teams rarely build custom pipelines, they depend on **SaaS-provided observability dashboards**.
Examples:

* Microsoft’s **Azure Monitor** or **Defender for Cloud**
* Google’s **Admin Console** and **Security Center**
* Salesforce’s **event monitoring API**

Benefits:

* No maintenance overhead.
* Regulatory-compliant by design.
* Built-in visualizations for security and usage analytics.

Limitations:

* **Little cross-system correlation.**
* **Opaque metrics definitions.**
* **Vendor lock-in** for historical data.

Riedesel observes:

> **“You don’t own your telemetry — you rent visibility by the month.”**

---

#### **(c) The Shadow Telemetry Problem**

Because official telemetry channels are locked behind IT admin privileges, **departments build their own shadow monitoring** using Excel exports, PowerBI reports, or ad-hoc scripts.

Example:

* Finance exports CSVs from SAP monthly to audit transaction errors.
* HR extracts access logs from the identity provider for compliance.
* Operations teams rely on spreadsheet pivot tables as “dashboards.”

> **“Shadow telemetry is where observability meets office politics.”**

This leads to duplicated effort, inconsistent KPIs, and data latency measured in weeks.

---

### 🌱 **2. The First Expansion — When Telemetry Meets Digital Transformation**

As these organizations pursue modernization — migrating workloads to the cloud or building customer-facing portals — telemetry must **expand beyond IT.**

#### **(a) The Trigger Moment: Internal Development Begins**

Riedesel pinpoints the key turning point:

> **“The day your company writes its first line of production code, your telemetry universe changes forever.”**

That first in-house application — maybe a customer portal, mobile app, or API integration — demands **real observability**:

* Developers need logs and metrics they can query.
* Security needs audit trails for compliance (SOX, HIPAA, GDPR).
* Operations needs uptime and SLA reporting.

Suddenly, **the old IT dashboards are insufficient**.
Telemetry must now bridge **SaaS**, **custom code**, and **cloud infrastructure**.

---

#### **(b) Building a Telemetry Bridge between Worlds**

The organization typically introduces **middleware telemetry** — a bridge connecting legacy IT monitoring with new application telemetry.

Example flow:

```
Existing SaaS systems (ServiceNow, SAP)
       ↓
Integration Bus (Kafka / MuleSoft / Azure Event Hub)
       ↓
Central Log Collector (Fluentd / Logstash)
       ↓
Storage (Elasticsearch / Splunk)
       ↓
Visualization (Kibana / PowerBI)
```

> **“The goal is not to replace vendor telemetry, but to normalize it.”**

This phase introduces:

* **ETL pipelines** for SaaS audit logs.
* **Structured logging** for internal apps.
* **Cross-domain dashboards** combining IT, business, and development data.

Now the company begins to see **systemic patterns** — how outages in a CRM ripple into sales KPIs, or how API latency impacts customer experience.

---

#### **(c) Cultural Friction and Data Politics**

Telemetry expansion collides with organizational culture.
The IT department historically guards access to logs for **security reasons**, while development teams demand **self-service observability**.

Riedesel calls this:

> **“The turf war between operations confidentiality and developer velocity.”**

Common debates:

* Should developers have access to production logs?
* Can business analysts see system performance dashboards?
* Who pays for the new ELK cluster or Splunk license?

Without clear governance, telemetry projects stall under bureaucracy.

**Best Practice:**

* Establish a **Telemetry Working Group** including IT, Security, and Dev leads.
* Define access tiers (read-only vs. admin).
* Treat telemetry as a **shared business service**, not a department tool.

> **“When everyone owns a slice of visibility, the whole company starts to see.”**

---

### ⚙️ **3. Evolving from Reactive Monitoring to Proactive Telemetry**

Initially, non-software companies only use telemetry for **reactive IT incident management**:

* Detect outages.
* Reset servers.
* Notify vendors.

Over time, they realize telemetry can **predict and prevent issues** — a shift from **monitoring to observability**.

#### **(a) From Alerts to Analytics**

* Move from simple up/down alerts to **trend dashboards**.
* Analyze ticket data from ServiceNow for recurring incidents.
* Use metrics to justify automation investments.

> **“Data stops being noise when it starts informing budgets.”**

#### **(b) Telemetry as Business Evidence**

Once telemetry enters PowerBI or Tableau, executives begin using it to measure:

* SLA adherence with external vendors.
* Cost allocation by system or department.
* Compliance audit readiness.

Riedesel notes:

> **“In traditional enterprises, telemetry’s first killer app isn’t uptime — it’s accountability.”**

---

### 🧩 **4. Integrating Internal Apps and Legacy Systems**

When in-house development grows, the IT landscape becomes **hybrid**: legacy systems + new cloud applications.

#### **(a) The Dual-Stack Reality**

* Mainframes or Oracle DBs coexist with AWS Lambda or Kubernetes clusters.
* On-prem SIEM tools (ArcSight, QRadar) coexist with cloud log pipelines (CloudWatch, Stackdriver).

> **“Telemetry has to speak both COBOL and Kubernetes.”**

**Technical solutions:**

* Use **collectors like Fluentd, Logstash, or Telegraf** to bridge both worlds.
* Standardize formats via **JSON schemas or ECS (Elastic Common Schema)**.
* Correlate across time using **synchronized NTP and UTC timestamps**.

---

#### **(b) Introducing OpenTelemetry for New Apps**

* Developers instrument new microservices with OpenTelemetry SDKs.
* Export traces to Jaeger or Tempo.
* Gradually integrate with IT’s centralized log management.

> **“The new telemetry doesn’t replace the old — it wraps around it.”**

This co-existence phase can last years but forms the foundation of **enterprise observability**.

---

### 🔐 **5. Compliance, Security, and Audit Pressure**

For non-software businesses, one of the main reasons telemetry matures is **regulation**.

Examples:

* **SOX** (financial integrity)
* **HIPAA** (healthcare privacy)
* **PCI-DSS** (payment security)
* **GDPR / CCPA** (personal data protection)

Riedesel explains:

> **“In regulated industries, telemetry isn’t optional — it’s evidence.”**

Key requirements:

* Immutable log storage (write-once, read-many).
* Retention policies (1–7 years).
* Audit trails for access and configuration changes.

Tools: Splunk, Elastic Security, AWS Audit Manager, Azure Sentinel.

This pressure often justifies telemetry investment that IT budgets alone could not.

> **“Compliance buys what performance cannot.”**

---

### 📈 **6. Emergence of Cross-Functional Telemetry Teams**

Once telemetry spans IT and software teams, organizations create a **central observability function** or **Telemetry Center of Excellence (CoE)**.

Responsibilities:

* Define telemetry standards and schemas.
* Manage ingestion pipelines and retention policies.
* Offer dashboards as shared internal services.
* Train departments on interpreting data.

> **“In mature enterprises, telemetry becomes the language between departments.”**

This evolution mirrors the startup’s “Platform Engineering” model but with **corporate constraints** (change management, budgets, procurement cycles).

---

### 💡 **7. Example Scenario: Retail Company Modernizing Telemetry**

**Phase 1:** IT monitors POS terminals and network uptime via SolarWinds.
**Phase 2:** Company launches an online store — adds AWS CloudWatch and ELK Stack.
**Phase 3:** Security introduces Splunk for compliance.
**Phase 4:** Business analysts consume telemetry data in PowerBI.
**Phase 5:** Unified telemetry pipeline connects POS, website, and cloud services using Fluent Bit → Kafka → Elastic.

Result:

* Real-time sales analytics tied to infrastructure performance.
* Single correlation ID from checkout API to payment processor.
* Reduced incident resolution time by 60%.

> **“When a retailer knows which server sold the shoes, telemetry has gone full circle.”**

---

### 🧠 **8. Chapter Summary — Telemetry as the Backbone of Digital Transformation**

Riedesel closes the chapter with a fundamental insight:

> **“The day you start building software, your IT telemetry becomes your application telemetry.”**

In other words, the border between **infrastructure monitoring** and **business observability** disappears.

**Core Lessons:**

| Theme                                 | Key Takeaway                                               |
| ------------------------------------- | ---------------------------------------------------------- |
| **Start with what vendors give you.** | SaaS telemetry is a foundation, not a trap.                |
| **Normalize across systems.**         | Use integration buses and standard schemas.                |
| **Create shared ownership.**          | Avoid turf wars between IT and dev teams.                  |
| **Leverage compliance funding.**      | Regulations can drive modernization.                       |
| **Plan for convergence.**             | Infrastructure and application telemetry eventually merge. |

Final quote:

> **“Telemetry is the bridge between the old world that ran on hardware and the new one that runs on software.”**

---

✅ **Summary Checklist: Non-Software Business Telemetry Evolution**

| Phase                    | Characteristics              | Tools                   | Strategic Goal                     |
| ------------------------ | ---------------------------- | ----------------------- | ---------------------------------- |
| **Vendor Default**       | Siloed SaaS dashboards       | CloudWatch, ServiceNow  | Basic uptime visibility            |
| **Shadow Telemetry**     | Manual exports, spreadsheets | CSV, PowerBI            | Departmental accountability        |
| **Integration Bridge**   | Central ingestion pipeline   | Fluentd, Kafka, Elastic | Unified visibility                 |
| **Hybrid Observability** | Cloud + legacy integration   | OpenTelemetry, SIEM     | Cross-system correlation           |
| **Regulated Maturity**   | Audit-grade telemetry        | Splunk, Sentinel        | Compliance & security intelligence |

---


## 🏦 **Long-Established Business IT (Legacy/Mainframe)**

### 🎯 **Purpose and Context**

Riedesel opens with a blunt observation:

> **“The older your systems, the more they matter — and the less they tell you.”**

This chapter focuses on organizations that **predate the internet age**, yet remain critical to global economies — **banks, airlines, insurance companies, telecoms, and governments** — all running complex mainframe-based systems that:

* Process billions of dollars daily,
* Depend on decades-old COBOL or PL/I code,
* Interface with modern APIs and web front-ends,
* And yet provide almost **no modern telemetry**.

Riedesel calls this domain the **“dark matter of enterprise telemetry”** — vast, powerful, but mostly invisible.

> **“Your digital transformation is only as observant as your oldest system.”**

---

### 🧩 **1. The Legacy Reality — Telemetry by Neglect**

#### **(a) Decades of Accidental Complexity**

Legacy IT systems were never designed for **observability**; they were designed for **reliability** and **control**.
Telemetry, if it existed, was typically:

* Printed to batch job reports,
* Written to flat files or tape archives,
* Aggregated weekly or monthly for accountants — not engineers.

Riedesel explains:

> **“These systems didn’t emit telemetry — they emitted paperwork.”**

Even today, many COBOL applications still log to **EBCDIC text files**, which require manual extraction and conversion to ASCII before analysis.

**Key problem:** There’s no `stdout`, no JSON, no metrics endpoint — just job logs buried in proprietary formats.

---

#### **(b) Islands of Monitoring**

Over the decades, enterprises added layers of specialized tools:

* **IBM Tivoli Monitoring (ITM)**
* **CA Sysview / MainView**
* **BMC Control-M**
* **HP OpenView**
* **SolarWinds for network devices**

Each tool captures its own view — CPU usage, job execution, queue depth, or storage consumption.
But there’s **no unified telemetry plane**.

> **“In mainframe environments, visibility is not missing — it’s trapped.”**

Each system sees part of the elephant; none see the whole.

---

### ⚙️ **2. Integrating Mainframe Telemetry into Modern Observability**

Riedesel’s core principle for modernization is pragmatic:

> **“You can’t rewrite the mainframe — but you can teach it to talk.”**

The challenge isn’t replacement — it’s **integration**.

---

#### **(a) The Layered Bridge Architecture**

She introduces a **three-layer model** for bringing legacy telemetry into modern systems:

```
[Mainframe / Legacy Apps]
     ↓
[Extraction Layer]
     ↓
[Normalization Layer]
     ↓
[Modern Observability Stack]
```

Let’s break these down.

---

##### **1️⃣ Extraction Layer — Getting Data Out Without Breaking Things**

The first step is to **capture telemetry safely** without modifying fragile legacy code.

Techniques include:

* **Job log scraping:** Automate extraction of JES2/JES3 logs after batch job completion.
* **System SMF (System Management Facility) feeds:** Collect CPU, I/O, and performance metrics directly from z/OS.
* **Network flow mirroring:** Capture IPFIX/NetFlow data for mainframe network interfaces.
* **Middleware event intercepts:** Use MQSeries or CICS transaction monitors to emit structured events.

> **“The goal of extraction is non-invasive visibility — listen without touching.”**

In many enterprises, **CICS exit points** are the only safe place to hook in telemetry.
Riedesel warns:

> **“Mainframes are like antique aircraft — you can instrument them, but you can’t drill new holes.”**

---

##### **2️⃣ Normalization Layer — Translating the Old Dialects**

Once extracted, legacy telemetry must be **converted into modern, machine-readable formats**.
Common transformations:

* EBCDIC → UTF-8
* CSV flat files → JSON
* Fixed-width COBOL records → Structured fields with metadata
* Timestamps → ISO 8601 UTC

This process may involve:

* **ETL (Extract-Transform-Load) pipelines** using **Informatica, Apache NiFi, or Logstash**
* **Custom parsers** for batch job reports
* **Schema mapping** between mainframe event codes and modern event types

> **“Every log line is an artifact of history — normalization is your archaeology.”**

Riedesel stresses using a **repeatable, automated ETL process** to ensure consistency, reproducibility, and auditability.

---

##### **3️⃣ Modern Observability Stack — Correlation and Visualization**

After normalization, telemetry enters the same ecosystem as newer systems:

* **Elasticsearch** or **Splunk** for indexing.
* **Grafana / Kibana** for visualization.
* **Prometheus exporters** for derived metrics.
* **OpenTelemetry collector** for unified ingestion.

> **“When a mainframe event shows up on your Grafana dashboard next to your Kubernetes pod, that’s digital transformation in action.”**

This allows unified dashboards that show, for instance:

* A mainframe job failure causing API response delays in a cloud microservice.
* A network congestion event in a router affecting both z/OS and AWS EC2.

---

#### **(b) Middleware as the Translator**

Riedesel highlights the role of **middleware** — the “linguistic bridge” between old and new.

**IBM MQ (Message Queue)**, **Kafka Connectors**, and **REST wrappers** can expose legacy events to modern consumers.

Example:

* CICS transactions publish messages to an MQ queue.
* A Kafka connector consumes those messages, enriches with metadata, and streams to Elasticsearch.

> **“Middleware doesn’t replace the mainframe — it makes it legible.”**

In this model, legacy systems **emit events indirectly**, through middleware rather than code changes.
This preserves uptime and avoids regulatory risk.

---

### 🧠 **3. Practical Handling of Hybrid Systems**

Modern enterprises rarely have a clean division between “legacy” and “cloud.”
Instead, they operate **hybrid architectures**, where mainframes, VMs, containers, and serverless functions all coexist.

Riedesel offers several strategies for making telemetry coherent across these environments.

---

#### **(a) Time Synchronization and Correlation**

> **“You can’t correlate what doesn’t share time.”**

Legacy systems often operate on **local time zones**, sometimes with **non-UTC offsets**, and occasionally drift out of sync.
To unify telemetry:

* Enforce **NTP synchronization** across all systems.
* Convert all timestamps to **UTC in ISO 8601**.
* Add metadata fields like `source_system` and `timezone` for context.

This ensures traceability when incidents span multiple domains (e.g., mainframe batch jobs triggering API delays in the cloud).

---

#### **(b) Unifying Identifiers**

Hybrid observability requires **cross-system correlation**:

* Introduce **transaction or correlation IDs** into MQ messages or REST bridges.
* Link them to downstream events in distributed systems.

> **“Correlation IDs are the Rosetta Stone of hybrid telemetry.”**

When every layer (mainframe → middleware → microservice → database) carries a shared ID, the organization gains **end-to-end visibility** across time, technology, and ownership boundaries.

---

#### **(c) Abstracting Legacy Noise**

Riedesel warns that legacy telemetry can overwhelm modern systems due to verbosity or irrelevant detail.

> **“Mainframes produce more metrics than insight — filter ruthlessly.”**

Best Practices:

* Drop redundant heartbeat or “success” messages.
* Summarize repetitive job logs into aggregated counters.
* Compress large event archives before ingestion.
* Implement sampling for low-severity logs.

The key is to **preserve signal, not bulk**.

---

#### **(d) Maintaining Data Fidelity for Compliance**

Because legacy systems often run **regulated workloads** (financial or healthcare), telemetry must be **forensically reliable**.

Requirements:

* Write-once (immutable) storage for audit trails.
* Tamper-proof checksums for transferred data.
* Chain-of-custody metadata during ETL.

> **“In legacy telemetry, trust is more valuable than real-time.”**

Even if ingestion is delayed, integrity must never be compromised.

---

### 🏗️ **4. Case Example — Modernizing a Financial Institution’s Mainframe Telemetry**

Riedesel provides an anonymized composite example of a **large global bank**.

#### **Initial State:**

* Core banking on IBM z/OS mainframes (COBOL + DB2).
* Job logs stored locally on tape and batch reports emailed weekly.
* Network telemetry from F5 and Cisco monitored separately.
* Cloud microservices (AWS) handling mobile banking APIs.

#### **Problems:**

* Incident resolution took hours due to siloed data.
* Security audits failed due to incomplete log retention.
* No traceability between API outages and backend job delays.

#### **Modernization Steps:**

1. **Deploy SMF and RMF collectors** on z/OS to export performance data.
2. **Stream MQ message logs** through Kafka into Elasticsearch.
3. **Enrich events** with system ID, job class, and business unit metadata.
4. **Visualize** end-to-end transactions in Grafana, combining API and COBOL job telemetry.
5. **Implement immutable S3 archive** for compliance storage.

#### **Results:**

* 70% reduction in mean time to resolution (MTTR).
* Unified dashboards for both mainframe and cloud.
* Successful audit sign-off on telemetry integrity.

> **“For the first time, the mainframe wasn’t a black box — it was a participant.”**

---

### 🔐 **5. Organizational and Cultural Lessons**

Integrating legacy telemetry isn’t only a technical effort — it’s deeply cultural.

Riedesel describes two archetypes:

| Legacy IT Culture                            | Modern Observability Culture                |
| -------------------------------------------- | ------------------------------------------- |
| Change-averse (“Don’t touch it if it works”) | Experiment-driven (“Instrument everything”) |
| Manual log reviews                           | Automated event correlation                 |
| Uptime obsession                             | Insight obsession                           |
| Ownership silos                              | Shared telemetry governance                 |

> **“Modern observability doesn’t replace reliability culture — it expands it.”**

She stresses that modernization requires **trust and translation** between mainframe engineers and cloud-native teams.

> **“Mainframe admins think in decades; SREs think in minutes. Telemetry has to speak to both.”**

This often means forming **cross-generational teams**:

* Senior COBOL experts provide data semantics.
* Modern engineers design ingestion and enrichment pipelines.

---

### 🧩 **6. Migration Pitfalls and Anti-Patterns**

Riedesel warns of common traps in legacy telemetry modernization:

1. **“Big Bang” Rewrites**

   * Attempting to replace mainframe telemetry entirely in one go.
   * Leads to system risk and downtime.

   > **“Mainframes don’t respond to revolutions — only to diplomacy.”**

2. **Unbounded Data Feeds**

   * Ingesting everything without filtering leads to cost blowouts.
   * Normalize and compress early.

3. **Schema Drift**

   * Legacy event formats changing without notice.
   * Require version-controlled schema registry.

4. **Over-Visualization**

   * Dumping raw legacy data into dashboards without context.
   * Always interpret through enrichment and correlation.

---

### 🧠 **7. Chapter Summary — Observability Across Generations**

Riedesel closes the chapter with a timeless insight:

> **“Telemetry is the only way generations of systems can coexist.”**

Legacy systems will remain for decades. Modern observability doesn’t seek to replace them — it seeks to **connect their wisdom** to today’s speed.

**Core Lessons:**

| Theme                         | Takeaway                                                   |
| ----------------------------- | ---------------------------------------------------------- |
| **Integrate, don’t rewrite.** | Teach mainframes to emit events, not rebuild them.         |
| **Normalize and correlate.**  | Convert old formats to modern schemas with shared IDs.     |
| **Secure and immutable.**     | Treat telemetry as evidence — tamper-proof and auditable.  |
| **Bridge cultures.**          | Unite COBOL-era stability with DevOps agility.             |
| **Respect the legacy.**       | Every mainframe log is history — handle it with precision. |

Final quote:

> **“Mainframes were built to last. Telemetry makes them part of the future.”**

---

✅ **Summary Checklist: Legacy/Mainframe Telemetry Modernization**

| Layer             | Practice                                           | Tools                       | Key Insight                           |
| ----------------- | -------------------------------------------------- | --------------------------- | ------------------------------------- |
| **Extraction**    | Non-invasive log scraping, SMF feeds, MQ hooks     | SMF, JES, CICS exits        | *“Listen without touching.”*          |
| **Normalization** | Convert EBCDIC → UTF-8, add metadata               | NiFi, Logstash, ETL scripts | *“Normalization is archaeology.”*     |
| **Integration**   | Stream via Kafka or REST into ELK/Prometheus       | Kafka Connect, Fluentd      | *“Middleware makes legacy legible.”*  |
| **Correlation**   | Link events across systems via IDs & timestamps    | OpenTelemetry Collector     | *“Correlation is the Rosetta Stone.”* |
| **Governance**    | Immutable storage, schema registry, audit controls | S3 Glacier, Elasticsearch   | *“Telemetry is evidence.”*            |

---

# ⚙️ **Techniques for Handling Telemetry**

## 🎯 **Purpose of Part 3**

Part 3 of *Software Telemetry* is about **engineering mastery** — the set of **practical techniques, design rules, and architectural guardrails** that make telemetry sustainable and cost-effective over years of operation.

Riedesel introduces this section with an observation every senior engineer knows but rarely articulates:

> **“Telemetry doesn’t fail because of missing data — it fails because of messy data.”**

**Part 3** addresses precisely that mess: redundant logs, inconsistent schemas, runaway cardinality, toxic data leaks, and unscalable ingestion pipelines.
It teaches how to **clean, constrain, and structure** the river of telemetry that modern systems emit.

---

## 🧱 **Standardized Logging and Event Formats**

### 🎯 **Purpose**

Riedesel opens this chapter by stating plainly:

> **“Logging is the most universal form of telemetry — and the most abused.”**

Every system logs something, but without standardization, those logs are **useless at scale**.
This chapter provides the principles, examples, and organizational strategies for **structured logging** — the foundation upon which **metrics, traces, and analytics** depend.

She draws a line between “**log output**” and “**telemetry events**”:

> **“A log line is text; an event is data. The sooner your organization understands that, the sooner your telemetry will grow up.”**

---

### 🧩 **1. Why Standardized Logging Matters**

Riedesel highlights the **fundamental pain** in modern observability:
engineers drowning in text-based logs, trying to extract patterns through brittle regular expressions and guesswork.

She writes:

> **“Every engineer has wasted hours writing regex to extract meaning from chaos — that’s not observability, that’s archaeology.”**

Without standardization:

* Search queries differ per service.
* Correlation breaks between systems.
* Log parsers fail when developers change message phrasing.
* Security tools miss sensitive data because of format drift.

In large systems, these inconsistencies create **millions of dollars of hidden operational waste**.

---

### ⚙️ **2. Structured Logging — The Foundation**

Structured logging is the practice of emitting logs as **structured objects**, not human-readable strings.
Riedesel explains it like this:

> **“Logs should be written for machines first and formatted for humans second.”**

#### **(a) Unstructured (Bad) Example**

```
[ERROR] 2025-10-10 14:32:01 User 3982 failed to log in from IP 10.0.3.7
```

#### **(b) Structured (Good) Example**

```json
{
  "timestamp": "2025-10-10T14:32:01Z",
  "level": "error",
  "event": "login_failed",
  "user_id": 3982,
  "ip_address": "10.0.3.7",
  "service": "auth-service",
  "env": "production"
}
```

**Benefits:**

* Machine-parsable → instantly usable by ELK, Splunk, or Loki.
* Self-describing → no regex required.
* Schema-consistent → resilient across deployments.

> **“When your telemetry is structured, every log line becomes a query.”**

---

### 🧠 **3. Common Structured Formats: JSON, YAML, and Key-Value**

#### **(a) JSON (JavaScript Object Notation)**

* **Most widely adopted** due to its simplicity and tooling support.
* Excellent for ingestion into Elasticsearch, Fluentd, or OpenTelemetry Collectors.
* Easy to parse, serialize, and enrich.
* Human-readable enough for developers.

Riedesel calls JSON **“the lingua franca of modern telemetry.”**

#### **(b) YAML (Yet Another Markup Language)**

* Used in configuration-heavy environments (Kubernetes, CI/CD pipelines).
* Human-friendly but slower to parse for high-volume logs.
* Suitable for **low-frequency, high-context** logs (e.g., configuration audits).

> **“YAML is for humans reading; JSON is for systems talking.”**

#### **(c) Key-Value Pair Logs**

* Example:

  ```
  level=info service=checkout user=3829 duration_ms=324 region=us-east-1
  ```
* Lightweight, line-oriented, and efficient for streaming systems like Fluent Bit or journald.
* Common in systemd and Go-based microservices.

Riedesel notes:

> **“Key-value logs are a good compromise between speed and structure.”**

---

### 🔧 **4. Schema Consistency — The Secret to Scale**

Structured logs alone aren’t enough. Without a **consistent schema**, the ecosystem still breaks down.

> **“Structure without schema is just fancy chaos.”**

#### **(a) The Need for Field Standards**

A schema defines:

* **Field names** (`user_id`, not `userID` or `userid`)
* **Field types** (`integer`, not `string`)
* **Allowed values** (e.g., `level`: info, warn, error, fatal)
* **Optional vs. required fields**

When every service uses the same field semantics, cross-service dashboards and correlation queries become effortless.

Riedesel compares schema consistency to grammar:

> **“If structure is the alphabet of telemetry, schema is its grammar — it’s how systems learn to communicate clearly.”**

#### **(b) Standardization Frameworks**

She recommends adopting existing schemas to avoid reinventing the wheel:

* **Elastic Common Schema (ECS)** — widely supported by ELK-based stacks.
* **OpenTelemetry Semantic Conventions** — designed for cross-platform observability.
* **Google Cloud Logging conventions** — good reference for naming and severity levels.

Adoption of these schemas ensures interoperability across vendors, products, and programming languages.

---

### 🧩 **5. Building Standardized Loggers**

Riedesel emphasizes **“logging libraries as the enforcers of discipline.”**

> **“Your schema isn’t real until your code enforces it.”**

#### **(a) Centralized Logging Library**

Instead of letting every team invent its own logger, organizations should create a **shared internal logging library** that:

* Enforces structured format (e.g., JSON only).
* Automatically injects standard metadata (service name, environment, version, trace_id).
* Validates field types before emission.
* Handles serialization and transport to stdout or queue.

**Example in Python (pseudo-code):**

```python
logger.emit(
    level="info",
    event="order_created",
    order_id=1298,
    user_id=457,
    region="us-west-1",
    trace_id=context.trace_id,
)
```

This enforces a uniform telemetry language across the company.

#### **(b) Mandatory Context Injection**

Each log line should include **contextual identifiers**:

* `trace_id`, `span_id` — for distributed tracing correlation.
* `service`, `env`, `region` — for deployment context.
* `version`, `commit_sha` — for change tracking.
* `user_id` or `tenant_id` — for multi-tenant observability (if compliant).

> **“Context in logs is what joins chaos into stories.”**

#### **(c) Language-Specific Libraries**

* **Go:** `zap`, `zerolog`, `logrus` with JSON encoder.
* **Java:** `logback` or `log4j2` with JSON layout.
* **Python:** `structlog`, `loguru`, or `logging` with `json.dumps()`.
* **Node.js:** `pino` or `winston`.

The goal is not the tool — it’s **enforcing standard semantics** across all languages.

---

### 🧰 **6. Versioning and Evolution of Event Formats**

Once standardized, event schemas must evolve carefully.
Riedesel warns:

> **“Your telemetry schema is an API — treat it like one.”**

#### **(a) Schema Versioning**

* Include a field such as `"schema_version": "1.2"`.
* Maintain backward compatibility in ingestion pipelines.
* Use feature flags to roll out new fields gradually.

This prevents ingestion or parsing failures when newer services emit different formats.

#### **(b) Schema Registry**

* Store and validate schemas in a centralized **registry** (e.g., Confluent Schema Registry or custom JSON Schema validator).
* Enable automated tests during CI/CD that validate new telemetry fields.

> **“If schema drift is undetected, your telemetry’s past becomes unreadable.”**

---

### 🧠 **7. Handling Free-Form Messages and Exceptions**

Structured logging doesn’t eliminate human-readable messages — it complements them.

> **“Developers still need to read logs, but machines should never depend on reading like humans do.”**

Best Practice:

* Keep a free-form `message` or `detail` field for contextual text.
* Store stack traces or exceptions in a `stack_trace` field as a multiline string.
* Avoid mixing structured data inside message text.

Example:

```json
{
  "level": "error",
  "event": "db_connection_failed",
  "service": "billing",
  "message": "Unable to connect to PostgreSQL after 3 retries",
  "stack_trace": "psycopg2.OperationalError: timeout expired"
}
```

> **“Humans debug; machines correlate. Don’t confuse their diets.”**

---

### 🔐 **8. Security and Privacy in Standardized Logging**

Once logging is standardized, it becomes powerful — but also **dangerous**.
Structured logs are easy to search, but that also means **sensitive data becomes easy to expose.**

Riedesel’s rule:

> **“Standardized logging without sanitization is just standardized leakage.”**

**Best Practices:**

1. **Never log secrets** — API keys, passwords, tokens.
2. **Mask sensitive fields** before emission (`credit_card_last4` instead of full number).
3. **Redact PII** (names, emails, IPs) where unnecessary.
4. **Encrypt transport** between emitters and collectors.
5. **Tag sensitive logs** (`"data_classification": "confidential"`) for access control.

These protections ensure compliance with **GDPR**, **PCI-DSS**, and internal privacy standards.

---

### ⚖️ **9. Organizational Enforcement and Culture**

Riedesel concludes that technical fixes alone aren’t enough — **standardization requires governance**.

> **“You can’t lint culture — but you can guide it.”**

Steps to institutionalize standardization:

* Define a **Telemetry Schema Council** to maintain formats.
* Build **linting tools** that scan repositories for unstructured log usage.
* Include **telemetry compliance checks** in CI/CD pipelines.
* Offer **dashboards as incentives** — standardized logs get better visualizations and faster alerting.

> **“When telemetry quality becomes visible, engineers will start to care about it.”**

---

### 🧩 **10. Chapter Summary — From Logging to Language**

Riedesel ends the chapter with one of her most memorable metaphors:

> **“Standardized logging is how your systems learn to speak the same language — and telemetry is how they tell you the truth.”**

She emphasizes that this chapter is the **linchpin between emission and observability**: without structured, schema-consistent logs, every other telemetry layer (metrics, traces, analytics, alerts) collapses into confusion.

**Core Takeaways:**

| Theme                              | Key Insight                                       |
| ---------------------------------- | ------------------------------------------------- |
| **Structure everything.**          | Unstructured text is human comfort, machine pain. |
| **Define a schema early.**         | Naming consistency outlasts all tools.            |
| **Treat schema as a contract.**    | Version it, validate it, enforce it.              |
| **Enrich every log with context.** | Correlation depends on trace IDs and metadata.    |
| **Govern through automation.**     | Quality enforcement should be continuous.         |

Final quote:

> **“When every log line is a first-class event, telemetry stops being noise and starts being knowledge.”**

---

✅ **Summary Checklist: Standardized Logging & Event Format Best Practices**

| Category       | Best Practice                                       | Key Principle                                               |
| -------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| **Format**     | Use JSON or key-value logs for structure            | *“Logs should be data, not prose.”*                         |
| **Schema**     | Adopt ECS or OpenTelemetry semantic conventions     | *“Schema is grammar — it gives meaning to structure.”*      |
| **Library**    | Centralize logger libraries with metadata injection | *“Your schema isn’t real until your code enforces it.”*     |
| **Security**   | Sanitize, classify, and encrypt logs                | *“Standardization without redaction is standardized risk.”* |
| **Governance** | Version schemas and validate in CI/CD               | *“Telemetry evolves safely when schema drift is visible.”*  |

---


# Quotes


# References
