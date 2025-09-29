---
title: Software Telemetry by Jamie Riedesel summary
date: "2025-10-10T22:12:03.284Z"
description: "Software Telemetry by Jamie Riedesel summary"
tags: ["systemperformance", "softwaredevelopment", "softwaredesign", "observability"]
---

# Table of Contents

```toc
exclude: Table of Contents
tight: false
from-heading: 1
to-heading: 6
class-name: "table-of-contents"
```

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

### ⚙️ The “Four Golden Signals” and the “Three Pillars of Observability” (Google SRE Framework)

Wilkins connects logging directly to **Google’s Site Reliability Engineering model**, which defines two intertwined frameworks:

#### **The Four Golden Signals:**

1. **Latency** — how long a request takes to complete.
2. **Traffic** — how much demand the system is handling.
3. **Errors** — the rate of failed requests.
4. **Saturation** — how “full” your service or resource is (CPU, threads, memory).

Logging helps quantify each:

> **“Metrics tell you *how much* pain the system feels; logs explain *why*.”**

#### **The Three Pillars of Observability:**

1. **Metrics** — numerical trends over time.
2. **Traces** — end-to-end causal chains of requests.
3. **Logs** — **contextual breadcrumbs** giving human-readable evidence behind metrics and traces.

Together they provide the *observability triad* — visibility into both *symptoms* and *causes*. Fluentd’s role is to **feed the logging pillar** and to **enrich metrics and traces** by exporting consistent contextual data across systems.


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


# 🌐 **Use Cases: Applying Architecture Concepts**

## 🎯 **Purpose of Use cases**

Riedesel takes the reader through **eleven progressively complex organizational case studies**, each demonstrating how **telemetry architecture evolves with scale, culture, and maturity**.

> **“Every organization already has telemetry — the question is whether it’s intentional or accidental.”**

This part answers:

* How do telemetry systems **start small and scale up**?
* When do they **outgrow vendor dashboards** and build custom pipelines?
* What are the **failure patterns** at each stage of telemetry maturity?
* How do compliance, cost, and chaos shape architectural choices?

## possible use cases

- I want to see all of the logs for the module I'm working on
  - set the logger name to the module name (the module name typically could be java class name or javascript file name)
- I want to see all the logs for a specific request for jobs within single node or across nodes
  - use open telemetry and tag your logs with with traceId and spanId
    - traceId generally represents a http request
    - spanId generally represents unique identifer for a single unit of work within a trace such as
      - database query
      - call to another service
      - long running compute process
- I want to see all logs for a specific user
  - tag specific user to all of the logs
  - tag specific host to all of the logs
- I want to see all logs for specific web server because the specific web server is behaving
- I want to see specific version of the software in the logs (like git hash)
- I want to see the important configurations for the software and server at start up
- I want to see the information to correlate the logs such as host, pid
- I want to see the information to help me with the software development process including deployment, debuging, health of system, security.
- I want to see logs for specific service I'm working on
  - filter out all of the noise until I can find relevant logs the issue I'm debugging
  - narrow the logs to specific time frame, process, machine
  - prefer to have better correlate logs
- "Be conservative in what you do, be liberal in what you accept"
- The large source of problem coming from the boundaries of the service/system.
  - parse, don't validate [parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
  - logging requests/response could create lots of logs and security/risks concerns regarding to PII, PHI
    - we could save the data in S3, database on demand, and retrieving those data for debugging purposes.
      - we can put more stringent constraints on s3, databases for auditing, access control and security purposes.
    - as a note, we could use dynamic logging to turn on the logs for requests/response at runtime on development environment
  - metrics around response time
  - metrics could indicate some signals where the system is underload or overload and the system can be scaled dynamically


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

## 🏗️ **Real-World Fluentd Use Case: Monitoring Challenges, Cloud Migration, and Solution Design**

---

### 🌐  D.1  **The Real-World Context — Monitoring Chaos in a Hybrid Landscape**

Wilkins begins the appendix with a real enterprise scenario inspired by projects he’s advised on at Oracle and other clients.
A large organization — **a global financial services provider** — had embarked on a **multi-year digital transformation**: migrating from **on-premises data centers** to **public cloud (AWS/Azure)** while modernizing monolithic applications into **microservices and container-based workloads**.

#### **Initial State: “Fragmented Monitoring and Log Silos”**

> **“Each system spoke its own language — and none could understand the other.”**

They had:

* Multiple **application servers (WebLogic, Tomcat, IIS)** each writing to local disk.
* Legacy **syslog servers** with inconsistent formats.
* **Cloud-native apps** emitting JSON logs directly to **stdout** in containers.
* Separate tools: Splunk, ELK, and a homegrown SQL reporting database.
* No unified alerting or correlation across systems.

This caused:

* **Blind spots** between infrastructure and application layers.
* **Duplicate logs and inconsistent time zones.**
* **Massive storage costs** from redundant ingestion pipelines.
* **Ineffective incident response** — root cause analysis took days.

> **“The organization had monitoring tools, but no observability discipline.”**

---

### ☁️  D.2  **The Cloud Migration Challenge**

As workloads moved to the cloud, the old logging approach **broke down**:

* Application logs no longer lived on a single VM.
* Auto-scaling created **ephemeral containers** — logs disappeared when pods died.
* Security demanded **centralized visibility** for both on-prem and cloud.
* Compliance teams required **audit-ready, immutable storage** of security events.

Wilkins notes:

> **“Cloud migration doesn’t just move servers; it multiplies log sources and shortens their lifespan.”**

The team needed:

* A **unified ingestion layer** that worked across **data centers, Kubernetes clusters, and serverless environments.**
* **Flexible routing** — to send the same data to **multiple backends** (security, analytics, compliance).
* **Minimal operational overhead** — since infrastructure teams were already stretched thin.

---

### 🧠  D.3  **Why Fluentd Was Chosen**

The organization evaluated several options — **Logstash, Vector, Fluent Bit, Cloud-native agents** — but ultimately chose **Fluentd** because of its:

1. **Plugin Ecosystem:** 1000+ input, filter, and output plugins.
2. **Lightweight Ruby Core + Extensible Architecture.**
3. **Cloud-native integration:** Kubernetes metadata enrichment, container tailing.
4. **Scalability and buffering** for unreliable networks.
5. **Vendor neutrality:** Works with ELK, Splunk, Datadog, S3, or any HTTP/Sink.

> **“Fluentd became the Switzerland of their monitoring stack — neutral, flexible, and fluent in every dialect of log.”**

They paired Fluentd (central aggregator) with **Fluent Bit** (lightweight agents) running as:

* **DaemonSets** on Kubernetes clusters (collecting container logs),
* **Windows/Linux services** on legacy servers,
* and **sidecar containers** for special applications.

---

### 🧩  D.4  **Solution Design – The Unified Logging Pipeline**

Wilkins details a **multi-layered Fluentd architecture** that balanced **scalability, compliance, and developer autonomy.**

#### 🧱 **1. Collection Layer**

* **Fluent Bit agents** deployed across all environments:

  * Kubernetes pods (collecting `/var/log/containers/*.log`),
  * On-prem file systems (tailing log files),
  * Syslog streams for network and firewall logs.
* Each agent tagged events by environment, service, and severity:

  ```
  tag: prod.app.auth
  tag: dev.web.frontend
  ```

#### ⚙️ **2. Aggregation & Transformation Layer**

* **Regional Fluentd hubs** ran as centralized aggregators.
* They:

  * **Validated** log formats (JSON, syslog, plain text),
  * **Redacted** sensitive data (GDPR compliance),
  * **Normalized** timestamps and schemas,
  * **Enriched** logs with metadata from Kubernetes and CMDB (e.g., app name, region, owner).

> **“Fluentd acted as the refinery — converting crude log oil into refined observability fuel.”**

Typical configuration snippet:

```conf
<filter *.app.*>
  @type record_transformer
  enable_ruby true
  <record>
    timestamp ${time.strftime("%Y-%m-%dT%H:%M:%SZ")}
    region "us-east-1"
    cluster "#{ENV['CLUSTER_NAME']}"
  </record>
</filter>
```

#### ☁️ **3. Distribution & Storage Layer**

Logs were **fanned out** via Fluentd’s routing and buffering mechanisms to:

* **Elasticsearch (for search & dashboarding)**
* **Splunk (for compliance & security)**
* **Amazon S3 (for archival, 1-year retention)**
* **Prometheus & Grafana (for metrics derived from logs)**

> **“The same event could serve three masters — observability, compliance, and audit — without tripling the cost.”**

#### 🔄 **4. Buffering & Reliability**

* **File-based buffers** with exponential backoff.
* **Chunk retry policies** to handle downstream failures gracefully.
* **At-least-once delivery** for audit logs.

> **“Even if Splunk or Elasticsearch went down, Fluentd quietly held the truth until the world came back.”**

---

### 🧰  D.5  **Operational Challenges and Tuning**

Wilkins discusses several *real* engineering lessons learned:

#### ⚡ **Performance Tuning**

* Introduced **multi-worker mode** to utilize multiple CPU cores.
* Used **chunk size tuning** to balance throughput and reliability.
* Deployed **round-robin load balancing** across multiple aggregators.

#### 🔒 **Security**

* TLS encryption for all agent → aggregator connections.
* Role-based authentication using Fluentd’s **`secure-forward` plugin**.
* Logs containing PII were filtered at the edge before leaving origin clusters.

#### 🧾 **Compliance & Retention**

* Data lifecycle managed via:

  * **Index lifecycle policies (ILM)** in Elasticsearch,
  * **S3 Glacier deep archive** for audit trails,
  * **Automated deletion** after 18 months for GDPR.

> **“Compliance became a configuration, not an afterthought.”**

#### 📈 **Monitoring Fluentd Itself**

* Self-logging to Prometheus using the **`monitor_agent` plugin.**
* Exposed metrics such as:

  * Buffer queue length,
  * Retry counts,
  * Event throughput (events/sec).
* Integrated Fluentd’s health into Grafana dashboards for proactive alerts.

> **“If Fluentd is your nervous system, you must also track its pulse.”**

---

### 🧩  D.6  **Outcome and Measurable Results**

The enterprise achieved remarkable results after implementing Fluentd:

| **Metric**                         | **Before Fluentd** | **After Fluentd Implementation**    |
| ---------------------------------- | ------------------ | ----------------------------------- |
| **Mean time to detect (MTTD)**     | 4–6 hours          | **<15 minutes**                     |
| **Mean time to resolution (MTTR)** | 2–3 days           | **<4 hours**                        |
| **Log storage cost (monthly)**     | 100% baseline      | **↓ 45% reduction**                 |
| **Duplicate data across tools**    | Common             | **Eliminated via routing logic**    |
| **Compliance visibility**          | Manual exports     | **Automated continuous audit feed** |

> **“Centralized, structured logging turned firefighting into engineering.”**

Developers could now:

* View cross-service errors instantly through **Kibana dashboards**.
* Correlate user IDs, trace IDs, and API latency in real-time.
* Deploy new microservices without reconfiguring central logging.

---

### 💡  D.7  **Lessons Learned and Design Principles**

Wilkins summarizes the team’s lessons as universal principles for modern observability architecture:

1. **Design Logging as a Platform, Not a Project**

   > “Treat your logging layer as a shared utility — like DNS or networking — with clear contracts, SLAs, and governance.”

2. **Filter Early, Enrich Smartly, Route Intelligently**

   * Reduce data before storage.
   * Add context before analysis.
   * Send data only where it’s needed.

3. **Security and Privacy Are Non-Negotiable**

   * Logs must respect privacy laws and organizational boundaries.
   * Filtering and redaction pipelines are essential, not optional.

4. **Monitor the Monitor**

   * Fluentd’s metrics should be visible to the same dashboards it feeds.
   * Treat your telemetry system as a living service with SLOs.

5. **Automate and Version-Control Configurations**

   * Store Fluentd configs in Git, deploy via CI/CD.
   * Version changes and roll back bad configurations safely.

6. **Empower Developers with Observability Standards**

   * Provide SDKs or logging templates.
   * Make structured logging a default part of development practices.

---

### 🧭 **Appendix D Summary — Fluentd as an Enterprise Observability Backbone**

Phil Wilkins concludes:

> **“A well-architected Fluentd pipeline doesn’t just move logs; it moves organizations from reaction to anticipation.”**

Through filtering, normalization, and reliable routing, Fluentd becomes:

* **A unifying data layer** across hybrid and multi-cloud systems.
* **A compliance-friendly audit framework.**
* **An enabler for DevOps and SRE culture**, where evidence is shared, structured, and searchable.

He closes with a reminder that:

> **“Observability isn’t about watching your systems fail — it’s about giving your teams the confidence that they can understand anything, anytime.”**

---


# ⚙️ **Techniques for Handling Telemetry**

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


## 🔢 **Managing Cardinality in Telemetry**

### 🎯 **Purpose and Context**

Riedesel opens the chapter with a stark warning:

> **“Cardinality is the hidden tax of telemetry — you pay it in memory, compute, and money.”**

In other words, even when your logs and metrics appear well-structured, a **high number of unique label combinations** can **explode storage**, **slow queries**, and **cripple dashboards**.

This chapter teaches how to understand, diagnose, and control that explosion. It’s not just about saving cost — it’s about preserving **the stability and responsiveness of your observability system itself**.

> **“If you’ve ever opened a Grafana dashboard that froze for 20 seconds, you’ve probably met cardinality — you just didn’t know its name.”**

---

### 🧩 **1. Understanding Cardinality**

Riedesel defines **cardinality** as:

> **“The count of unique combinations of label keys and values in your telemetry.”**

In time-series systems (Prometheus, InfluxDB, Datadog, etc.), each unique set of labels — even if it’s the same metric name — creates a **new time series**.

**Example:**

```promql
http_requests_total{region="us-west", service="auth"}
http_requests_total{region="us-east", service="auth"}
http_requests_total{region="us-west", service="checkout"}
```

Even though all share the same metric name (`http_requests_total`), there are **three unique series** due to the combinations of `region` and `service`.

Add a new label like `user_id`, and your system could generate **millions of unique series**.

Riedesel notes:

> **“Cardinality doesn’t scale linearly — it multiplies explosively.”**

---

#### **(a) Why Cardinality Matters**

High cardinality impacts telemetry systems in multiple ways:

* **Memory pressure** — Each series consumes storage and in-memory index entries.
* **CPU load** — Every query must scan and aggregate over more series.
* **Query latency** — Dashboards slow down, alerts delay.
* **Retention cost** — Data volume grows exponentially.

And worst of all:

> **“Cardinality failures are invisible until they’re catastrophic.”**

You rarely see them coming — the system works fine until a small change (like a new metric label) suddenly doubles your dataset.

---

#### **(b) The Root Causes of Cardinality Explosion**

Riedesel identifies several **common anti-patterns**:

1. **User identifiers as labels**

   ```
   http_requests_total{user_id="A123"}
   ```

   → Creates one series per user.

2. **Session or request IDs**

   ```
   latency_seconds{request_id="8f92a3..."}
   ```

   → Infinite cardinality as every request is unique.

3. **Dynamic resource names**

   * Containers (`pod_name`), VMs (`instance_id`), network flows (`src_ip`)
   * Each new instance creates new label combinations.

4. **Unbounded tags in logs**

   * Logging arbitrary strings in structured fields like `"error_message"`.

5. **Accidental label combinations**

   * Joining two labels that weren’t meant to multiply.
   * e.g., `{region, instance, user_role}` across 10×1,000×50 = **500,000 series**.

> **“Every label combination is a new time series. Every new series is a cost. Every cost compounds.”**

---

### ⚙️ **2. Detecting and Measuring Cardinality**

Before you can manage it, you must **measure it**.
Riedesel provides practical strategies for detecting cardinality problems before they overwhelm the system.

#### **(a) System Metrics**

Prometheus and other TSDBs expose their own telemetry about series count, e.g.:

```promql
prometheus_tsdb_head_series
prometheus_tsdb_series_created_total
```

> **“The telemetry system should monitor itself — if it’s observant, it can prevent its own blindness.”**

#### **(b) Cardinality Audits**

Run regular **cardinality audits**:

* Query unique label combinations per metric (`count by (labelname)`).
* Identify metrics with the highest label explosion.
* Track growth trends weekly.

**Example:**

```promql
count(count(http_requests_total) by (user_id))
```

Riedesel suggests automating these audits with **Grafana dashboards** or **nightly scripts**, tagging metrics with a `cardinality_risk` label.

---

### 🧠 **3. Strategies to Limit High Cardinality**

Riedesel structures mitigation into **three layers** — *Prevent*, *Reduce*, and *Control*.

---

#### **(a) Prevent — Design for Low Cardinality Up Front**

> **“Cardinality prevention begins at instrumentation.”**

1. **Eliminate unique identifiers** — Never use user IDs, session IDs, or request hashes as labels.

   * Instead, record them as **event fields** in logs (non-aggregated telemetry).

2. **Use categorical values** — Limit labels to a small set of expected options.

   * e.g., `region ∈ {us-east, us-west, eu-central}`

3. **Predefine label sets** — Document allowed label keys and values in your schema.

4. **Apply sampling** — Record only a percentage of events (e.g., 1 in 1000 requests) for metrics.

5. **Normalize resource identifiers** — Use stable IDs (`instance_type`, `service_group`) instead of ephemeral (`instance_id`).

> **“If you design metrics like you design APIs — intentionally and with limits — your telemetry will stay sane.”**

---

#### **(b) Reduce — Aggregate Early and Often**

If cardinality already exists, **reduce it through aggregation and rollup.**

1. **Aggregation by dimension**

   * Aggregate fine-grained metrics into coarser views.
   * e.g., from `per-instance` → `per-service` or `per-region`.

   ```promql
   sum(rate(http_requests_total[5m])) by (service, region)
   ```

2. **Downsampling**

   * Store high-resolution data (e.g., 10s) short-term (7 days).
   * Retain low-resolution aggregates (e.g., 5m or hourly) for long-term analysis.

3. **Rollup Jobs**

   * Periodic ETL tasks that compute aggregates and delete raw data.
   * Common in **Thanos**, **Cortex**, and **VictoriaMetrics** clusters.

> **“Aggregation is the art of deciding which precision is worth paying for.”**

4. **Retention Tiers**

   * Keep detailed metrics short-term, summarized metrics long-term.
   * Example:

     * 7 days → per-instance metrics
     * 30 days → per-service aggregates
     * 90 days → per-region summaries

---

#### **(c) Control — Manage What You Can’t Reduce**

Even after reduction, some cardinality is unavoidable.
Riedesel explains how to **control** it through configuration and policy.

1. **Enforce Limits in Telemetry Tools**

   * Prometheus: `--storage.tsdb.retention.size`, `--storage.tsdb.max-block-chunk-segments`
   * Datadog: Cardinality quotas per host/service.
   * New Relic: Series and label count caps.

> **“If you don’t set limits, your vendors will — and you’ll discover them the hard way.”**

2. **Sampling and Tracing Filters**

   * Use **tail-based sampling** in OpenTelemetry for traces — keep only slow or error traces.
   * Discard repetitive low-value events.

3. **Dynamic Label Whitelists**

   * Allow only approved labels at ingestion (e.g., drop unknown tags).
   * Fluentd / Vector filters can enforce these policies.

4. **Cost Monitoring**

   * Treat cardinality as a **cost driver** in your observability budget.
   * Regularly review ingestion volume, retention size, and query duration.

---

### 🧩 **4. Organizational Practices for Cardinality Control**

Riedesel argues that **technical fixes won’t last** without cultural change.

> **“Every engineer adds a label with good intentions — and ten others pay the bill.”**

She proposes embedding cardinality management into daily engineering practice:

#### **(a) Education and Review**

* Train developers on **metric design patterns**.
* Include cardinality impact assessment in **code reviews**.

> **“Code review isn’t complete until you’ve reviewed what it emits.”**

#### **(b) Budgeting and Accountability**

* Assign **“cardinality budgets”** to teams — define max allowed series count per service.
* Monitor cardinality growth with CI checks.
* Enforce quotas automatically.

> **“Budgets turn observability from chaos into discipline.”**

#### **(c) Governance and Schema Ownership**

* A **Telemetry Council** should define acceptable label patterns.
* Maintain a **metric registry** documenting:

  * Metric name
  * Purpose
  * Owner
  * Expected labels
  * Cardinality estimate

> **“If you can’t name the owner of a metric, it doesn’t belong in production.”**

---

### 🧠 **5. Real-World Examples and Failure Stories**

Riedesel illustrates the cost of ignoring cardinality with several anonymized incidents.

#### **Example 1 — The Exploding Dashboard**

A SaaS company added `customer_id` as a Prometheus label to track per-client latency.
Within 24 hours, the system had **500,000 active time series**, memory usage spiked, and Prometheus crashed.

**Fix:** Move `customer_id` into log events and aggregate latency at query time by region, not by individual ID.

> **“When your observability stack goes down before your production system, you’ve inverted your priorities.”**

---

#### **Example 2 — Tag Storm in Cloud Monitoring**

A cloud team configured every container label (`pod_name`, `namespace`, `image_hash`, `deployment_uid`) to propagate to Datadog metrics.
Each new deployment generated thousands of new tag combinations — billing tripled in one month.

**Fix:** Introduced a tag whitelist and enforced cardinality budgets per namespace.

> **“Unbounded tags are observability’s version of unbounded spending.”**

---

#### **Example 3 — Success Through Early Design**

A fintech startup adopted **metric design reviews** — no new metric could be added to production without schema and cardinality approval.
Result: consistent query performance, predictable costs, and dashboards that loaded in milliseconds.

> **“Telemetry discipline is cheaper than telemetry debt.”**

---

### ⚖️ **6. Balancing Precision and Practicality**

Riedesel concludes that managing cardinality is not about **reducing visibility**, but about **prioritizing it**.

> **“The goal isn’t less telemetry — it’s smarter telemetry.”**

Guiding principle:

* **Keep logs detailed, metrics concise, and traces selective.**
* Design for **clarity per byte**, not “collect everything.”

> **“If every signal is high fidelity, your observability will drown in its own accuracy.”**

---

### 🧩 **7. Chapter Summary — Containing the Infinite**

Riedesel closes with one of her most quoted insights:

> **“Cardinality is entropy. You can’t eliminate it, but you can slow its decay.”**

By mastering cardinality control, organizations make telemetry **sustainable, predictable, and actionable** — transforming it from a resource sink into a strategic asset.

---

✅ **Summary Checklist: Managing Cardinality in Telemetry**

| Layer       | Strategy                           | Technique                                | Key Insight                                            |
| ----------- | ---------------------------------- | ---------------------------------------- | ------------------------------------------------------ |
| **Prevent** | Design low-cardinality metrics     | Avoid user/session IDs; limit label sets | *“Prevention begins at instrumentation.”*              |
| **Reduce**  | Aggregate early and downsample     | Summarize by service, region, or tier    | *“Aggregation decides what precision you can afford.”* |
| **Control** | Enforce quotas and sampling        | Whitelist labels, monitor budgets        | *“If you don’t limit it, it will limit you.”*          |
| **Govern**  | Embed discipline in reviews        | Metric registries, schema ownership      | *“Telemetry debt is real debt.”*                       |
| **Observe** | Audit and monitor telemetry health | Count unique series regularly            | *“Your telemetry system must observe itself.”*         |

---

### 💡 **Final Takeaway**

> **“Cardinality doesn’t just kill observability — it kills curiosity. When dashboards slow down, teams stop asking questions.”**

Riedesel’s message is clear: managing cardinality is not optional — it’s what separates **sustainable observability** from **expensive chaos**.

---


## 🧨 **Redacting and Reprocessing Telemetry**

### 🎯 **Purpose and Context**

Riedesel opens with a chilling statement that captures the entire problem:

> **“All telemetry is evidence. Some of it is evidence you were never supposed to have.”**

This chapter focuses on how organizations **detect, isolate, and neutralize toxic telemetry** — especially personally identifiable information (PII), secrets, and regulated data that **slipped into logs, metrics, or traces**.

She ties this directly to regulatory pressure:

* **GDPR (Europe)** → Right to erasure (Article 17)
* **CCPA (California)** → Consumer data rights
* **HIPAA / SOX / PCI-DSS** → Privacy and audit control
* **Corporate security policies** → Confidential data exposure

> **“Telemetry is exempt from nothing. If it contains PII, it is personal data.”**

The chapter is divided into three parts:

1. Understanding and identifying **toxic telemetry**
2. Techniques for **redaction** (real-time and batch)
3. Methods for **reprocessing and re-ingestion** when migrations or retroactive cleanup are required.

---

### ☣️ **1. Understanding Toxic Telemetry**

#### **(a) What Is “Toxic” Data?**

“Toxic” telemetry refers to **data that introduces legal, reputational, or operational risk** if retained or exposed.

Riedesel defines it precisely:

> **“Toxic telemetry is any data that can identify a person, reveal a secret, or compromise your system — even unintentionally.”**

Examples include:

* **PII (Personal Identifiable Information):**

  * Full names, addresses, emails, phone numbers, national IDs
* **Sensitive identifiers:**

  * Credit card numbers, bank accounts, SSNs, passport numbers
* **Authentication materials:**

  * API tokens, passwords, OAuth bearer tokens, session cookies
* **Confidential business data:**

  * Customer contracts, transaction details, or unannounced product info

---

#### **(b) Common Sources of Toxic Telemetry**

1. **Developer negligence** — Logging sensitive request payloads during debugging:

   ```
   logger.info(f"User submitted form: {form_data}")
   ```

   → Includes names, addresses, or passwords.

2. **Third-party SDKs or middleware** — Auto-log headers or parameters without filtering.

3. **Customer support scripts** — Dumping full request objects to trace issues.

4. **Security misconfigurations** — Logging decrypted data that should’ve stayed encrypted.

> **“Every system eventually logs something it regrets.”**

---

#### **(c) The Three Phases of Toxic Data Lifecycle**

| Phase           | Description                                    | Risk                            |
| --------------- | ---------------------------------------------- | ------------------------------- |
| **Emission**    | Data logged before sanitization                | Immediate privacy violation     |
| **Storage**     | Data persisted in telemetry databases          | Compliance exposure             |
| **Replication** | Data copied to backups, analytics, or archives | Hard to remove, multiplies risk |

Riedesel notes:

> **“Once telemetry turns toxic, every copy is a contamination vector.”**

This is why **early detection and standardized scrubbing** must be built into every telemetry pipeline.

---

### 🔍 **2. Detecting Sensitive or Regulated Data**

You can’t fix what you don’t know you have.

#### **(a) Automated Pattern Scanning**

Use **regex-based detection** or **data classification engines** to identify potential toxic fields.

Examples:

* Credit cards: `\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b`
* Emails: `[\w\.-]+@[\w\.-]+\.\w+`
* SSNs: `\b\d{3}-\d{2}-\d{4}\b`
* JWT tokens: `eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+`

Tools:

* **AWS Macie**, **Azure Purview**, **Google DLP API**
* **Open-source**: `truffleHog`, `detect-secrets`, `Gitleaks`, or custom Fluentd filters

> **“Pattern scanning is your Geiger counter — it won’t fix the leak, but it’ll tell you where it glows.”**

---

#### **(b) Machine Learning for Data Classification**

For large-scale telemetry lakes (petabytes of logs or traces), manual regex breaks down.
Riedesel discusses using ML-based detection tools that classify fields based on content entropy and context (e.g., recognizing a base64 token or a ZIP code pattern).

Examples:

* **Google DLP**, **BigID**, **OneTrust**, **Immuta**.

These systems analyze telemetry streams, tag fields by sensitivity, and mark datasets for redaction.

> **“The smarter your detection, the less false comfort you’ll have.”**

---

### 🧹 **3. Redacting Telemetry in Real-Time**

Once sensitive data is identified, the next step is **real-time redaction** — filtering or replacing it *before* it reaches storage.

Riedesel distinguishes between **inline scrubbing** and **post-ingestion redaction**.

---

#### **(a) Inline Redaction (Preferred)**

> **“The best toxic data is the kind that never leaves the system.”**

Inline redaction happens **during telemetry emission** — within the logger, agent, or collector — before the event hits disk or queue.

**Techniques:**

* Regular expression filters in **Fluentd**, **Fluent Bit**, or **Vector**.
* **Processor plugins** that replace patterns with placeholders:

  ```json
  {
    "email": "[REDACTED_EMAIL]",
    "credit_card": "**** **** **** 1234"
  }
  ```
* **Middleware sanitizers** inside application code:

  ```python
  safe_data = sanitize(request)
  logger.info("Processed request", extra={"user": safe_data})
  ```

Advantages:

* Complies instantly with privacy laws (no exposure).
* No costly reprocessing later.
* Works with live telemetry pipelines.

> **“Inline redaction is prevention — everything else is cleanup.”**

---

#### **(b) Redaction via Streaming Filters**

For containerized or distributed telemetry:

* Use **sidecar collectors** (Fluent Bit, Vector, or OpenTelemetry Collector) that apply **filter rules** before forwarding.
* Example: Fluent Bit `modify` filter:

  ```ini
  [FILTER]
      Name modify
      Match *
      Remove_key password
      Remove_key token
      Add key pii_redacted true
  ```
* Encrypt sensitive fields before shipping downstream.

> **“Your redaction layer is your last firewall between privacy and liability.”**

---

### 🕰️ **4. Batch Redaction and Historical Cleanup**

When data has already been stored (e.g., in Elasticsearch, S3, or BigQuery), you must **retroactively clean it** — often mandated by GDPR’s *“right to be forgotten.”*

#### **(a) Challenges of Post-Storage Redaction**

* Telemetry is often **append-only** and immutable by design.
* Data exists in **multiple replicas, indexes, and backups**.
* Systems like Elasticsearch or Loki are **not built for in-place edits**.

> **“Telemetry systems are historians by nature — they hate rewriting history.”**

Therefore, retroactive cleanup is **expensive and complex**.

---

#### **(b) Batch Redaction Pipelines**

To handle this, Riedesel describes the **Extract–Transform–Reingest (ETR)** model:

```
[Extract] → Pull affected data from storage (via query or export)
     ↓
[Transform] → Apply scrubbing, masking, or field deletion
     ↓
[Reingest] → Write cleaned data into new sanitized indices
```

Key requirements:

* **Immutable backups** for audit traceability.
* **Checksum verification** to prove data integrity post-cleanup.
* **Deletion logs** documenting which records were altered.

> **“If you can’t prove what you removed, compliance will assume you didn’t.”**

---

#### **(c) Deletion vs. Redaction**

* **Deletion** — Remove the entire record (for GDPR erasure).
* **Redaction** — Keep event but scrub sensitive fields.

Decision depends on:

* Regulatory mandate (full erasure vs anonymization).
* Business impact (can analytics tolerate missing data?).
* Technical capability (can the store handle field-level edits?).

**Example (Anonymized Redaction):**

```json
{
  "user_id": "anon_73c2d9",
  "email": null,
  "ip_address": "0.0.0.0",
  "action": "purchase",
  "timestamp": "2025-10-10T12:00:00Z"
}
```

Riedesel calls this approach **“data surgery”** — invasive but survivable.

---

### 🔄 **5. Reprocessing and Re-Ingestion for Platform Migrations**

Telemetry systems evolve — new vendors, schema upgrades, or cloud migrations require **reprocessing entire datasets** to ensure compatibility and compliance.

> **“Every migration is a second chance to fix the sins of your first ingestion.”**

#### **(a) When Reprocessing Is Necessary**

* Moving from one observability stack to another (e.g., ELK → OpenSearch → Splunk).
* Upgrading schemas (adding trace IDs, removing PII fields).
* Normalizing formats for multi-cloud analytics.
* Auditing and cleaning historical data before regulatory inspection.

---

#### **(b) Reprocessing Architecture**

A modern reprocessing pipeline follows a pattern similar to ETL, but designed for telemetry:

```
[Cold Storage / Archive]
    ↓
[Batch Extraction (Athena, BigQuery, or S3 Select)]
    ↓
[Transformation Layer (Spark, Flink, NiFi)]
    ↓
[Schema Validator + Redaction Filter]
    ↓
[Re-Ingest into New Observability Stack]
```

Riedesel emphasizes automation:

* Validate every event against the latest telemetry schema.
* Apply **deterministic redaction** (same pattern → same hash).
* Generate **audit trails** documenting before/after states.

> **“Reprocessing is your observability second act — a chance to apply the discipline you didn’t have before.”**

---

#### **(c) Real-World Example: GDPR Compliance at Scale**

A European SaaS provider discovered that email addresses were stored in **application logs and traces** spanning 18 months.

**Action Plan:**

1. Export affected indices from Elasticsearch to S3.
2. Run a Spark job to:

   * Identify PII using regex + ML classification.
   * Replace emails with SHA-256 hashes.
   * Add `"redacted": true` metadata.
3. Re-ingest sanitized logs into a new Elasticsearch cluster.
4. Document and cryptographically sign redaction proof for regulators.

Result:
✅ Compliance validated
✅ Analytics continuity preserved
✅ Legal exposure eliminated

> **“Privacy isn’t deleting data — it’s controlling what it remembers.”**

---

### 🔐 **6. Cryptographic and Audit Considerations**

For compliance, redaction and reprocessing must be **provable**.

Riedesel recommends:

* **Hashing original entries** before redaction for non-repudiation.
* **Signing cleanup batches** with a system certificate.
* **Audit logs** recording operator identity, timestamp, and record counts.
* **Immutable evidence storage** (WORM storage, blockchain-like audit trail).

> **“Regulators don’t trust your intention — they trust your evidence.”**

---

### 🧠 **7. Operational Best Practices**

#### **(a) Preventive Controls**

* **Standardize log sanitization libraries.**
* Use CI/CD telemetry linting to block logging of sensitive fields.
* Maintain a **Data Sensitivity Registry** mapping each telemetry field to a classification level (e.g., `public`, `internal`, `confidential`).

#### **(b) Response Playbooks**

* Define **Incident Class: Data Exposure (Telemetry)**.
* Include steps: detection → quarantine → redaction → verification → report.
* Assign clear roles (Data Protection Officer, Observability Lead, Legal).

> **“Your telemetry pipeline needs a containment protocol as much as your production system does.”**

#### **(c) Testing and Dry Runs**

* Simulate redaction on sample datasets before production.
* Measure loss of analytical fidelity post-cleanup.
* Validate schema compatibility.

---

### 🧩 **8. Chapter Summary — Making Telemetry Safe by Design**

Riedesel closes with one of her most powerful insights:

> **“Telemetry is a mirror. If you don’t clean it, it reflects what you should never see.”**

She warns that **observability and privacy must evolve together** — one cannot mature without the other.

**Key Lessons:**

| Theme                             | Insight                                                           |
| --------------------------------- | ----------------------------------------------------------------- |
| **Prevention > Cure**             | Inline redaction beats post-ingestion cleanup every time.         |
| **Detection Must Be Continuous**  | Treat toxic data scans as recurring security checks.              |
| **Redaction Must Be Auditable**   | Every erased byte needs a corresponding proof.                    |
| **Reprocessing Is Opportunity**   | Use migrations to enforce schema, security, and compliance.       |
| **Telemetry Is a Legal Artifact** | Handle it like financial records — immutable, traceable, minimal. |

Final quote:

> **“A mature telemetry system doesn’t just observe — it remembers responsibly.”**

---

✅ **Summary Checklist: Redacting & Reprocessing Telemetry**

| Stage                | Goal                           | Tools / Techniques                  | Key Principle                           |
| -------------------- | ------------------------------ | ----------------------------------- | --------------------------------------- |
| **Detection**        | Identify PII or secrets        | Regex, DLP scanners, ML classifiers | *“You can’t clean what you can’t see.”* |
| **Inline Redaction** | Prevent toxic emission         | Fluentd filters, app sanitizers     | *“Filter before you forward.”*          |
| **Batch Cleanup**    | Scrub historical data          | ETL + Spark or NiFi pipelines       | *“Redaction is data surgery.”*          |
| **Reprocessing**     | Migrate or normalize telemetry | Schema validators, checksum logs    | *“Migrations are chances to heal.”*     |
| **Audit**            | Prove compliance               | Hash signing, immutable logs        | *“Evidence, not promises.”*             |

---

## 🧱 **Building Policies for Retention and Aggregation**

### 🎯 **Purpose and Context**

Riedesel begins with a sharp insight:

> **“Telemetry doesn’t age gracefully — it either grows stale or grows expensive.”**

Logs, metrics, and traces all generate value when fresh, but over time their relevance drops while their **storage, compliance, and query costs rise**.
This chapter teaches how to design **data-retention lifecycles**, implement **aggregation and sampling strategies**, and balance **historical value** against **operational efficiency**.

> **“Retention policy is observability’s version of time travel — you decide how far back the truth can still be seen.”**

---

### 🧩 **1. Why Retention Policies Matter**

Without clear policies, telemetry systems accumulate endless data: logs from years ago, high-resolution metrics nobody queries, traces from debug runs.
The result: runaway storage costs, slow dashboards, and regulatory risk.

Riedesel summarizes the dangers:

> **“Every byte you keep without purpose becomes a liability.”**

Retention isn’t just technical housekeeping — it’s **risk management**:

* **Cost:** Disk, index, and compute resources.
* **Performance:** Query latency from oversized datasets.
* **Security:** Sensitive data exposure from old logs.
* **Compliance:** Violations of GDPR/CCPA “data minimization” principles.

---

### ⚙️ **2. Telemetry Lifecycles: From Birth to Expiry**

Riedesel defines a **Telemetry Lifecycle Model** — how data moves from *hot* to *warm* to *cold* to *deleted* storage.

| Stage       | Purpose                              | Typical Duration | Storage Type                                     |
| ----------- | ------------------------------------ | ---------------- | ------------------------------------------------ |
| **Hot**     | Real-time monitoring, alerting       | Hours → Days     | Fast SSD / in-memory (Prometheus, Elasticsearch) |
| **Warm**    | Incident analysis, near-term trends  | Weeks → Months   | Object or block storage (S3, Azure Blob)         |
| **Cold**    | Audit, compliance, capacity planning | Months → Years   | Glacier, tape, or compressed archives            |
| **Expired** | No longer needed                     | —                | Securely deleted / purged                        |

> **“Your retention tiers define the cost curve of curiosity.”**

Each tier must have:

1. **Purpose** — why keep this data?
2. **Duration** — how long is it useful?
3. **Access pattern** — who queries it and how often?
4. **Deletion trigger** — when to let it go.

---

### 🧮 **3. Retention Policies by Telemetry Type**

#### **(a) Logs**

Logs are verbose and most prone to uncontrolled growth.

**Best-practice retention tiers:**

* **Hot:** 7–14 days — full logs for debugging and incident response.
* **Warm:** 30–90 days — summarized or sampled logs for trend analysis.
* **Cold:** 6–12 months — compressed or archived for audit only.
* **Expired:** Purged or anonymized beyond compliance period.

Techniques:

* **Index lifecycle management** in Elasticsearch or OpenSearch.
* **S3 lifecycle policies** for automatic tiering and deletion.
* **Log rotation + compression** (gzip, zstd).

> **“Logs tell stories — but even stories expire.”**

---

#### **(b) Metrics**

Metrics have predictable structures but can explode in volume due to **cardinality**.

Typical retention plan:

* **High-resolution (5–10 s)** — keep 1–7 days for SRE dashboards.
* **Medium-resolution (1 m)** — keep 30–90 days for capacity planning.
* **Aggregated (1 h or 1 d)** — keep 6–24 months for trend forecasting.

Aggregation handled by:

* **Prometheus recording rules**
* **Thanos/Cortex compaction**
* **VictoriaMetrics down-samplers**

> **“Metrics age like photos — blur them over time, but don’t delete the picture.”**

---

#### **(c) Traces**

Distributed traces are the most expensive telemetry type.

**Retention Strategy:**

* Keep only **error and high-latency traces** long-term.
* Retain **full traces** for 3–7 days (debugging).
* Store **trace summaries** (service dependency graphs, latency histograms) for months.
* Archive **sampling metadata** for audit compliance.

Techniques:

* **Tail-based sampling** in OpenTelemetry Collector.
* **Adaptive sampling** (dynamic reduction based on traffic or error rate).
* **Span filtering** — drop low-value spans (e.g., health checks).

> **“Traces are gold dust — you can’t keep them all, but you must keep the right specks.”**

---

### 🧠 **4. Aggregation and Sampling Strategies**

Riedesel divides data-reduction techniques into **two philosophies:**

* **Aggregation** — keep *less detail* but maintain completeness.
* **Sampling** — keep *fewer examples* but preserve diversity.

---

#### **(a) Aggregation — Summarize Intelligently**

Aggregation reduces data granularity while maintaining statistical value.

**Examples:**

* Summing counters by region/service:

  ```promql
  sum(rate(http_requests_total[5m])) by (region, service)
  ```
* Computing quantiles for latency (`p50`, `p95`, `p99`).
* Generating daily roll-ups for long-term trends.

Riedesel emphasizes:

> **“Aggregation is not compression — it’s curation.”**

**Best Practices:**

1. Define **aggregation hierarchies** — e.g., instance → service → region → global.
2. Store **metadata lineage** (which data was aggregated from which).
3. Validate that aggregates still answer core SLO questions.

> **“Averages hide pain; quantiles reveal it — aggregate wisely.”**

---

#### **(b) Sampling — Keeping the Right Few**

Sampling controls telemetry flood by selectively keeping representative data.

**Sampling Techniques:**

| Type                   | Description                                            | Use Case             |
| ---------------------- | ------------------------------------------------------ | -------------------- |
| **Head-based**         | Randomly keep X % of events                            | Low-traffic systems  |
| **Tail-based**         | Decide after event completion (keep slow/error traces) | Tracing              |
| **Dynamic / Adaptive** | Adjust sampling rate by load or error rate             | Large, spiky systems |
| **Stratified**         | Ensure each category (region, status) is represented   | Analytics accuracy   |

> **“Sampling trades completeness for clarity — but only fools sample blindly.”**

Riedesel cautions against sampling metrics used for **SLI/SLO enforcement**, since missing data can distort reliability measures.
Instead, sample **telemetry volume**, not the business KPIs themselves.

---

### 🧩 **5. Designing Policy Frameworks**

Riedesel insists that retention must be **codified, automated, and visible** — not tribal knowledge.

> **“If retention lives in someone’s head, it isn’t a policy — it’s a gamble.”**

#### **(a) Policy Definition**

Every telemetry type should have a defined policy document containing:

* **Purpose** (why this data exists)
* **Retention duration**
* **Aggregation schedule**
* **Sampling rules**
* **Access controls**
* **Compliance references (GDPR, SOX, etc.)**
* **Owner and approval date**

This metadata becomes part of the **Telemetry Governance Registry**.

#### **(b) Automation Through Lifecycle Management**

Modern tools support automated enforcement:

* **Elasticsearch ILM**, **Grafana Mimir retention rules**, **S3 Lifecycle**, **BigQuery partition expiration**.
* Scripts that tag datasets with expiration timestamps on ingestion.

> **“Automation turns policy into physics.”**

---

#### **(c) Cost Visibility and Observability Budgets**

Telemetry isn’t free; teams should see the **financial cost of retention**.
Riedesel recommends dashboards showing:

* Cost per telemetry type and environment.
* Storage vs. query load by age.
* Data volume trends per retention tier.

> **“When engineers see the bill, they learn to aggregate.”**

---

### 🧩 **6. Legal, Compliance, and Audit Dimensions**

Retention isn’t only about efficiency — it’s also a **compliance requirement**.
Regulations define *minimum* and *maximum* retention periods.

**Examples:**

* **SOX**: 7 years for financial audit logs.
* **HIPAA**: 6 years for healthcare record access logs.
* **GDPR**: Retain only as long as necessary; delete upon request.
* **PCI-DSS**: 1 year for card-holder activity logs.

> **“Compliance defines the edges of your memory — outside of it lies liability.”**

Riedesel emphasizes that deletion must be **provable**:

* Generate cryptographic checksums before and after deletion.
* Keep immutable deletion logs (“proof of forgetfulness”).
* Align with corporate data-classification levels (`public`, `internal`, `confidential`, `regulated`).

---

### 🧠 **7. Organizational Roles and Accountability**

Riedesel outlines who should own what:

| Role                                      | Responsibility                               |
| ----------------------------------------- | -------------------------------------------- |
| **Telemetry Owner (SRE / Platform Team)** | Implements retention & aggregation pipelines |
| **Security Officer / DPO**                | Approves retention durations for compliance  |
| **Finance / FinOps**                      | Monitors telemetry costs                     |
| **Developers**                            | Respect TTL and sampling settings in code    |
| **Executives**                            | Balance insight vs. liability trade-offs     |

> **“Telemetry policy is everyone’s problem — because data decay is everyone’s cost.”**

---

### 📈 **8. Real-World Example: The 90-Day Rule**

Riedesel presents an anonymized case study from a SaaS provider:

* Original policy: “Keep everything forever.”
* Result: 20 TB/day ingestion → $1.2 M/year in storage.
* New policy: 7 days hot logs, 30 days aggregated, 1 year archived.
* Result: 70 % cost reduction, faster dashboards, and easier GDPR compliance.

> **“Retention discipline paid for an SRE team.”**

---

### 🧩 **9. Building a Living Policy**

A retention policy should evolve alongside systems.

**Key Practices:**

* Review quarterly.
* Adjust per new telemetry sources.
* Treat as **version-controlled artifact** in Git (e.g., `retention.yaml`).
* Document rationale for every duration and aggregation decision.

Example schema snippet:

```yaml
logs:
  retention_days: 30
  aggregation: daily
metrics:
  retention_days: 180
  downsample: 1h
traces:
  retention_days: 7
  sampling_rate: 0.05
```

> **“Your retention file should be as real as your deployment manifest.”**

---

### 🧠 **10. Chapter Summary — Memory With Intention**

Riedesel ends the chapter with an elegant metaphor:

> **“Telemetry is your system’s memory. Retention policy is how you decide what to remember, what to forget, and what to archive in the family album.”**

**Core Insights:**

| Theme                                | Lesson                                                                |
| ------------------------------------ | --------------------------------------------------------------------- |
| **Purpose Defines Value**            | Keep data only as long as it answers a question you still care about. |
| **Aggregation Preserves Trends**     | You don’t need every detail forever — just the story they tell.       |
| **Sampling Manages Scale**           | Fewer data points, smarter insights.                                  |
| **Automation Enforces Discipline**   | Lifecycle rules prevent human forgetfulness.                          |
| **Compliance Frames the Boundaries** | Retention is both a legal and ethical responsibility.                 |

Final quote:

> **“Observability isn’t about seeing everything — it’s about remembering wisely.”**

---

✅ **Summary Checklist: Retention & Aggregation Policy Design**

| Category       | Best Practice                                 | Key Principle               |
| -------------- | --------------------------------------------- | --------------------------- |
| **Logs**       | Tiered retention (hot → warm → cold)          | *“Stories expire.”*         |
| **Metrics**    | Downsample over time (5 s → 1 m → 1 h)        | *“Blur but don’t lose.”*    |
| **Traces**     | Sample intelligently, retain only errors      | *“Keep the gold dust.”*     |
| **Automation** | Enforce via ILM / lifecycle tools             | *“Policy as code.”*         |
| **Compliance** | Align with legal retention windows            | *“Evidence, not excess.”*   |
| **Governance** | Version control and review policies quarterly | *“Memory must be managed.”* |

---


## ⚖️ **Surviving Legal Processes**

### 🎯 **Purpose and Context**

Riedesel begins with a stark warning:

> **“At some point, your telemetry will stop being an engineering tool and start being legal evidence.”**

This chapter teaches engineers and SREs how to **design and manage telemetry under legal pressure** — when lawyers, auditors, regulators, or law enforcement come knocking.

It’s about ensuring that your logs, metrics, and traces:

* Can **prove compliance** (SOX, GDPR, HIPAA, PCI-DSS),
* Can **withstand legal discovery** (eDiscovery, subpoenas),
* And can **be preserved, shared, and deleted lawfully**.

> **“Telemetry that can’t survive legal scrutiny isn’t observability — it’s liability.”**

---

### 🧩 **1. When Telemetry Becomes Evidence**

#### **(a) The Shift from Operations to Litigation**

Riedesel notes that engineers are often blindsided when a **routine operational dataset** suddenly becomes **subject to legal discovery**.

Scenarios include:

* **Data breach investigations**
* **Regulatory audits** (GDPR, SOX, HIPAA, SEC, FCA)
* **Internal misconduct or fraud probes**
* **Civil lawsuits or criminal cases** involving system logs

> **“One day you’re debugging latency — the next, your log is Exhibit B.”**

At that point, **chain of custody**, **integrity**, and **access control** become more important than uptime or metrics freshness.

---

#### **(b) Legal Reality Check: Discovery and Subpoenas**

In U.S. and EU law, discovery is the process by which parties in a legal case obtain relevant evidence — including digital data such as logs and telemetry.

Riedesel explains:

> **“If it’s stored, it’s discoverable.”**

That means:

* Logs, metrics, and traces can be **subpoenaed**.
* Even backup archives and compressed telemetry snapshots may be required to produce.
* Failure to preserve or disclose can result in **sanctions or legal penalties** (e.g., “spoliation of evidence”).

She emphasizes:

> **“Ignorance is not a defense — deletion after notice is destruction.”**

This shifts telemetry from a **technical asset** to a **legal artifact**.

---

### 🔐 **2. Building Legally Defensible Telemetry**

Riedesel stresses that engineers must ensure telemetry can **withstand legal validation**.
The goal is **defensibility** — not perfection, but verifiable integrity and provenance.

#### **(a) Chain of Custody**

Every step of telemetry handling — from emission to archiving — must be **traceable** and **tamper-evident**.

**Best Practices:**

* **Immutable storage** (write-once, read-many, WORM).
* **Cryptographic hashes** for each batch or log block.
* **Access logs** showing who viewed or exported telemetry.
* **Version-controlled configuration** of pipelines and filters.

> **“If you can’t prove who touched the data and when, it won’t hold up in court.”**

---

#### **(b) Time Synchronization and Timestamp Integrity**

In legal contexts, **timing is everything** — disputes often hinge on *when* an event occurred.

**Requirements:**

* Use **UTC timestamps** (ISO 8601) across all systems.
* Enforce **NTP synchronization** enterprise-wide.
* Record both **event time** and **ingest time**.

> **“Two seconds of clock drift can mean two million dollars in liability.”**

---

#### **(c) Data Authenticity**

Authenticity is about proving that telemetry hasn’t been altered.

Techniques:

* Sign log batches with **HMAC or SHA-256** digests.
* Store hash manifests separately (e.g., blockchain, append-only log).
* Validate hash upon retrieval before producing to auditors.

> **“Authenticity turns logs into evidence — without it, they’re just stories.”**

---

### 📦 **3. Record Retention and Legal Hold**

When a company faces litigation or investigation, normal deletion policies are suspended under a **legal hold** — a formal order to **preserve all potentially relevant data**.

#### **(a) What Is a Legal Hold?**

> **“A legal hold is the ‘freeze button’ for your data lifecycle.”**

Once imposed:

* All automated retention or deletion jobs must stop.
* Engineers must ensure telemetry pipelines don’t purge relevant data.
* The organization must isolate and preserve affected datasets.

Failure to comply can result in:

* **Spoliation sanctions** (destruction of evidence).
* **Fines or contempt orders**.
* **Damage to credibility** in court.

---

#### **(b) Engineering Responsibilities During Legal Hold**

1. **Identify affected data sources** (log indices, metrics, traces, backups).
2. **Isolate copies** in immutable storage (S3 Object Lock, WORM disks).
3. **Document the process**: who initiated, which data, and when.
4. **Coordinate with legal team** before resuming normal operations.

> **“Your retention automation must have a brake pedal — not just a gas pedal.”**

Riedesel recommends that **every observability team maintain a “legal hold runbook”** — a step-by-step procedure for suspending deletion, exporting datasets, and verifying data preservation.

---

### ⚙️ **4. eDiscovery Workflows for Telemetry**

When discovery begins, organizations must **collect, review, and produce telemetry data** relevant to the case.
This process must be both **accurate and efficient**, since logs can reach terabytes.

#### **(a) eDiscovery Phases Applied to Telemetry**

| Phase              | Description                            | Example Tools                              |
| ------------------ | -------------------------------------- | ------------------------------------------ |
| **Identification** | Locate relevant telemetry              | Index search, metadata tagging             |
| **Preservation**   | Secure from modification/deletion      | WORM, snapshots, object lock               |
| **Collection**     | Extract specific datasets              | Export API, SQL, BigQuery, Athena          |
| **Processing**     | Normalize, deduplicate, redact         | Spark, NiFi, Fluentd filters               |
| **Review**         | Legal team examines logs               | eDiscovery platforms (Relativity, Everlaw) |
| **Production**     | Deliver to opposing counsel/regulators | CSV, PDF, JSON exports                     |

> **“In eDiscovery, your logs become your testimony — word for word, line for line.”**

---

#### **(b) Minimizing Risk During eDiscovery**

1. **Scope limitation:** Only produce relevant telemetry fields.
2. **Redaction:** Mask PII or unrelated confidential data.
3. **Validation:** Hash and verify dataset integrity before delivery.
4. **Logging of exports:** Record every extraction operation.

> **“Transparency is your legal shield; secrecy is your liability.”**

---

### 🧠 **5. Collaborating with Legal and Compliance Teams**

Riedesel observes a recurring failure pattern:

> **“Engineers speak in timestamps and schemas; lawyers speak in obligations and risks. The two rarely understand each other until it’s too late.”**

This section outlines how to bridge that gap.

#### **(a) Common Disconnects**

| Engineers Think…                    | Legal Thinks…                                        |
| ----------------------------------- | ---------------------------------------------------- |
| “We can delete logs after 30 days.” | “Retention is defined by law, not convenience.”      |
| “We can fix it by reprocessing.”    | “Tampering after notice is destruction of evidence.” |
| “We encrypted everything.”          | “Can you prove who had decryption keys?”             |
| “Our system is redundant.”          | “Redundancy means multiple liabilities.”             |

> **“Your observability system is a compliance system — whether you admit it or not.”**

---

#### **(b) Building a Legal Partnership**

**Practical Steps:**

1. **Appoint a “Telemetry Compliance Liaison”** — a technical person who understands both pipelines and policies.
2. **Maintain a joint Telemetry Retention Policy** signed by engineering and legal.
3. **Include legal counsel in incident postmortems** that produce audit logs.
4. **Run annual “Legal Readiness Drills”** — simulate a subpoena and test the response workflow.

> **“The best time to meet your legal team is before your logs do.”**

---

### 🧩 **6. Privacy and Jurisdictional Challenges**

Global telemetry creates **cross-border data issues**.
Riedesel warns:

> **“Telemetry doesn’t respect borders — but laws do.”**

#### **(a) Cross-Jurisdictional Retention Conflicts**

Example:

* GDPR requires **minimization and deletion**.
* U.S. SEC or IRS rules may require **7-year retention**.

→ **Conflict:** One law says delete, another says keep.

**Solution:**

* Store in **region-specific clusters** (EU telemetry in EU data centers).
* Apply **data residency policies** via cloud provider features.
* Maintain **legal data inventories** — document where regulated data flows.

---

#### **(b) Privacy by Redaction**

For international compliance:

* Use **pseudonymization** for sensitive identifiers (e.g., `user_id → hash(user_id)`).
* Maintain **separate key vaults** for re-identification.
* Implement **field-level encryption** for high-risk logs (e.g., medical, financial).

> **“Privacy is not deletion — it’s separation of meaning.”**

---

### 📜 **7. Case Studies and Lessons Learned**

#### **Case 1: GDPR Audit Incident**

A European telecom was audited for retention compliance. Their metrics store retained full IP addresses for 3 years.

* Result: Violation of GDPR Article 5 (data minimization).
* Fine: €1.6M
* Fix: Adopted automated redaction and 90-day retention for non-aggregated metrics.

> **“Retention without purpose equals punishment.”**

---

#### **Case 2: Security Breach Litigation**

A U.S. fintech firm’s application logs contained customer email addresses. After a breach, plaintiffs used those logs to prove negligence.

* Result: Class-action lawsuit.
* Fix: Redacted historical logs, enforced structured logging guidelines, implemented 180-day TTL.

> **“Every debug statement is a potential deposition.”**

---

#### **Case 3: Legal Hold Drill**

A SaaS company practiced legal hold after a mock subpoena.
They discovered several systems (Kafka, Loki, S3) didn’t support WORM mode — meaning **evidence could be altered**.

* Result: Re-architecture using S3 Object Lock + signed manifests.
* Outcome: 24-hour legal-hold readiness achieved.

> **“You don’t build legal resilience in a panic — you rehearse it.”**

---

### 🧠 **8. Chapter Summary — Legal Resilience as Engineering Discipline**

Riedesel concludes that surviving legal processes isn’t about turning engineers into lawyers — it’s about **building observability that can stand up to scrutiny**.

> **“A well-designed telemetry system should tell the truth — and be able to prove it.”**

She defines **legal resilience** as the fourth pillar of observability, alongside logs, metrics, and traces:

* **Technical visibility** — what happened.
* **Operational visibility** — why it happened.
* **Business visibility** — what it cost.
* **Legal visibility** — can we prove it?

> **“Telemetry is only useful if it can survive interrogation.”**

---

✅ **Summary Checklist: Telemetry Legal Readiness**

| Category                 | Practice                                                  | Key Insight                                           |
| ------------------------ | --------------------------------------------------------- | ----------------------------------------------------- |
| **Chain of Custody**     | Immutable storage, cryptographic signing, access auditing | *“If it’s not provable, it’s not evidence.”*          |
| **Retention & Hold**     | Legal hold runbooks, deletion suspension                  | *“Freeze before you’re told to.”*                     |
| **eDiscovery**           | Automate export, redaction, and review pipelines          | *“Logs are testimony in JSON.”*                       |
| **Compliance Alignment** | Match data residency and privacy laws                     | *“Telemetry crosses borders; laws don’t.”*            |
| **Legal Collaboration**  | Design policies jointly with counsel                      | *“Your best defense is shared understanding.”*        |
| **Training & Drills**    | Annual simulations, documentation                         | *“Legal resilience must be practiced, not declared.”* |

---

### 🧩 **Final Quote:**

> **“Telemetry is the memory of your system — and in court, memory is everything.”**

Riedesel closes with a challenge to engineers:
build systems that can tell the truth **technically, operationally, and legally** — and **prove that truth beyond doubt.**

---


## ⚙️ **Filtering and Extrapolation**

---

### 🧩 **Using Filters to Reduce Noise, Spot Anomalies, and Redact Data**

Wilkins opens the chapter with a reminder that:

> **“The value of your logging pipeline is not measured by how much data you collect but by how much useful signal you preserve.”**

As systems scale, raw log volumes explode — hundreds of thousands of lines per second from Kubernetes nodes, APIs, and sidecars. Without filtering, teams face **alert fatigue, costly storage, and opaque dashboards**.

#### 🎯 **Purpose of Filters**

* **Reduce Noise:** eliminate redundant, irrelevant, or low-value logs.
* **Spot Anomalies:** surface only events that deviate from normal patterns.
* **Redact Sensitive Information:** prevent leaking credentials, tokens, or personal identifiers.
* **Enrich Context:** add or normalize fields before downstream analysis.

#### ⚙️ **Common Filtering Plugins in Fluentd**

| Plugin                          | Use Case                            | Example                                                |
| ------------------------------- | ----------------------------------- | ------------------------------------------------------ |
| **`grep`**                      | Include/exclude events using regex  | Include only `ERROR` messages                          |
| **`record_transformer`**        | Modify or remove keys               | Mask `password`, add `environment`                     |
| **`parser` / `format` filters** | Parse embedded JSON, split fields   | Turn `"msg": "user:123 failed"` into structured fields |
| **`geoip`**                     | Enrich IPs with geographic metadata | Append `"country": "CA"`                               |
| **`throttle`**                  | Suppress duplicate logs             | Log one identical error per minute                     |

> **“Filtering is about intentional reduction, not loss — you remove what distracts so the important becomes visible.”**

#### 🧱 **Example — Noise Reduction**

```conf
<filter app.access>
  @type grep
  <exclude>
    key status
    pattern ^2\d\d$
  </exclude>
</filter>
```

This removes all successful (2xx) HTTP responses, keeping only warnings or failures.

#### 🔒 **Example — Redaction**

```conf
<filter app.auth>
  @type record_transformer
  remove_keys password,token,ssn
</filter>
```

Wilkins notes:

> **“Every byte you don’t log is a byte you don’t have to protect later.”**

#### 🧠 **Filtering for Anomaly Detection**

While Fluentd isn’t an ML engine, smart filtering can pre-select unusual events — e.g.,

* sudden surge in `ERROR` rate,
* requests from new IP ranges, or
* unexpected `service=unknown` tags.

Paired with downstream tools like **Elasticsearch watchers** or **Grafana Loki alerts**, filtered streams form the backbone of **early-warning observability**.

---

### 🔧 **Record Transformation Plugins**

After noise reduction, the next step is **normalization and enrichment** — making logs “speak the same language.”
Phil Wilkins describes record transformation as:

> **“Reshaping events so that downstream systems can query them intelligently without regex acrobatics.”**

#### 🔹 **`record_transformer` Plugin**

The most versatile tool for modifying records:

```conf
<filter app.*>
  @type record_transformer
  enable_ruby true
  <record>
    hostname "#{Socket.gethostname}"
    env "#{ENV['APP_ENV']}"
    log_id "${tag}-${record['request_id']}"
  </record>
</filter>
```

This adds contextual fields (`hostname`, `env`, `log_id`) and can dynamically compute new ones using embedded Ruby.

> **“A well-designed transformer layer turns logs into first-class data assets.”**

#### 🔹 **`parser` Filter**

Used to convert embedded text into structured fields:

```conf
<filter raw.text>
  @type parser
  key_name message
  format regexp
  expression /user=(?<user>\w+)\s+ip=(?<ip>\S+)/
</filter>
```

Resulting structured output enables direct queries such as `user:john` instead of full-text search.

#### 🔹 **`modify` and `record_modifier`**

Simpler variants for field rename, type conversion, or default value injection.
Wilkins emphasizes using transformation layers to **enforce consistency across microservices**, ensuring all logs include standard metadata like:

* `service`
* `version`
* `trace_id`
* `environment`
* `region`

> **“Transformation plugins bring order to a chaotic ecosystem of heterogeneous log formats.”**

---

### 📊 **Deriving New Metrics (Extrapolation from Events)**

This is where the chapter’s title truly shines — “Filtering and Extrapolation.”
Wilkins defines *extrapolation* as:

> **“The art of deriving new insight by aggregating, counting, or calculating from existing log streams.”**

While Fluentd is primarily an event router, it can **generate operational metrics** from logs before they reach analytics systems — a lightweight form of “pre-analytics.”

#### ⚙️ **Examples of Derived Metrics**

* **Event Counting:** tally number of errors or transactions over time.
* **Rate Measurement:** compute throughput per minute.
* **Field Summarization:** count users by region, API by latency.

#### 🔹 **Using the `counter` Filter**

```conf
<filter app.api>
  @type counter
  unit minute
  count_key status
</filter>
```

This counts occurrences of each `status` code every minute, producing metrics like:

```json
{"status.200": 1452, "status.500": 17}
```

#### 🔹 **`aggregator` and `relabel`**

For more complex summaries, Fluentd can aggregate by tag or field and output to Prometheus Exporter or InfluxDB.

> **“A log line is a data point; millions of lines make a metric.”**

#### 🔹 **Business-Driven Derived Metrics**

* Counting `"payment_declined"` events → conversion health metric.
* Tracking `"user_signup"` logs → marketing ROI.
* Measuring `"latency_ms"` averages → performance SLA.

Wilkins notes that deriving such metrics **upstream** reduces load on analytics backends and provides **real-time insight without waiting for batch jobs**.

---

### 🖥️ **Demonstrating Changes with `stdout` Outputs**

Throughout the chapter, Wilkins demonstrates filtering and transformation using the simplest possible sink — the **`stdout` output plugin**, which prints transformed records directly to the console.

> **“Before routing to Elasticsearch or S3, watch what Fluentd actually sees — the console is your microscope.”**

#### 🔹 **Example Pipeline**

```conf
<source>
  @type tail
  path /var/log/nginx/access.log
  tag nginx.access
  format nginx
</source>

<filter nginx.access>
  @type grep
  <regexp>
    key status
    pattern ^5\d\d$
  </regexp>
</filter>

<match nginx.access>
  @type stdout
</match>
```

This prints only 5xx errors to the terminal — a clean, visual confirmation that filtering works.

Wilkins explains that **`stdout`** is invaluable for:

* **Unit-testing configurations** before production deployment.
* **Visual debugging of filter chains** (“Does my parser actually split fields correctly?”).
* **Educational demonstrations** during CI/CD pipeline design.

He also recommends pairing `stdout` with:

* **`@log_level debug`** — to see plugin-level diagnostics.
* **`<label>` routing** — to visualize separate data paths.

> **“Seeing transformed events scroll by on stdout is the Fluentd equivalent of watching packets on Wireshark — it’s how you learn what your system is really doing.”**

---

### 🧭 **Summary — From Raw Logs to Readable Signals**

Wilkins closes with an essential observation:

> **“Filtering and extrapolation are the difference between logging as archiving and logging as intelligence.”**

Key takeaways from this chapter:

* **Filters trim noise and protect privacy.**
* **Transformers normalize and enrich.**
* **Extrapolation derives operational metrics from events.**
* **`stdout` verification ensures transparency and trust in your pipeline.**

When these practices combine, a Fluentd pipeline evolves from a passive data collector into an **active, adaptive, and intelligent telemetry layer** — capable of **turning every log line into actionable signal.**

---

## ⚙️ **Logging Best Practices**

---

### 🧩 **Distinguishing Audit Events vs. Log Events**

Wilkins begins by **drawing a firm boundary between “audit events” and “log events”**, two terms often misused interchangeably:

* **Audit Events**:

  * Are **immutable**, **legally significant**, and **security-focused**.
  * Capture *who did what*, *when*, and *from where*, often for **compliance** (e.g., SOX, PCI DSS, GDPR).
  * Must be **verifiable, traceable, and retained** for regulatory periods.
  * Example:

    > **“User ‘jdoe’ escalated privileges at 2025-10-10T09:43Z from IP 192.168.4.22.”**

* **Log Events**:

  * Are **diagnostic, operational, and transient**.
  * Help developers and SREs **understand system state**, **debug code**, or **trace transactions**.
  * They can be ephemeral, summarized, or transformed before long-term storage.

> **“Audits serve governance; logs serve insight.”**

Wilkins stresses that conflating the two leads to **storage bloat, performance degradation, and security leaks**.
He suggests routing audit data into **dedicated SIEMs (e.g., Splunk Enterprise Security, Azure Sentinel)** and application logs into **Fluentd → Elastic → Kibana pipelines** for operational analytics.

---

### 🔔 **Log Levels and Severity Calibration (Trace → Fatal)**

A key anti-pattern Wilkins warns against is **“log level inflation”** — overusing `ERROR` or `WARN` for normal events.
Instead, teams should **treat log levels as a calibrated scale of importance**, not as emotional reactions from developers.

| **Level** | **Purpose**                                                       | **Example / When to Use**                        |
| --------- | ----------------------------------------------------------------- | ------------------------------------------------ |
| **TRACE** | Deep internal diagnostics; used during development or TDD cycles. | “Entering validation loop for request #4823”     |
| **DEBUG** | Contextual info for debugging; safe to disable in production.     | “Auth token expired; reissuing session key.”     |
| **INFO**  | High-level, expected operations.                                  | “Order #12345 processed successfully.”           |
| **WARN**  | Unexpected but non-fatal conditions.                              | “Retrying connection to payment gateway.”        |
| **ERROR** | Recoverable failures needing attention.                           | “Database write timeout; operation rolled back.” |
| **FATAL** | Irrecoverable system failure; triggers alerts.                    | “Kernel panic detected in pod ‘api-service-3’.”  |

Wilkins highlights:

> **“The power of logs lies not in how many you produce, but how precisely you grade their significance.”**

He recommends **consistent severity mapping across microservices** — e.g., define a shared `logging.yml` standard or adopt **OpenTelemetry semantic conventions**.

---

### 🧠 **Clear, Contextual Logging — The “Five W’s”: What, When, Where, Why, Who**

Phil Wilkins reframes effective logging as **storytelling with data**.
He introduces the **Five W’s** as the foundation of *context-rich observability*:

1. **What** — What event occurred? What resource or operation was involved?

   > e.g., “User registration API failed validation.”
2. **When** — Timestamp, time zone, and duration (use **ISO 8601** for precision).
3. **Where** — System, host, container, function name, or region.

   > e.g., “service=auth-api, pod=auth-api-4f6b, region=us-west-2.”
4. **Why** — Error message, causal stack, or triggering condition.
5. **Who** — Actor identity or system principal.

> **“A good log entry reads like a miniature incident report — complete, compact, and comprehensible.”**

Wilkins urges developers to:

* Always **include correlation IDs or trace IDs** to link logs across microservices.
* Use **structured JSON logging** for machine parsing.
* **Avoid freeform messages** like `"something went wrong"` — instead encode structured context:

  ```json
  {
    "level": "error",
    "service": "payment-api",
    "timestamp": "2025-10-10T16:22:18Z",
    "traceId": "abc123",
    "event": "payment_declined",
    "reason": "insufficient_funds"
  }
  ```

---

### 🔒 **Avoiding Sensitive Data Exposure and GDPR Compliance**

Logging can accidentally become a **data leak vector**.
Phil Wilkins dedicates several pages to **privacy-aware logging practices**, especially under **GDPR**, **CCPA**, and **ISO/IEC 27001** obligations.

He warns:

> **“If it can appear in a subpoena, don’t let it appear in a log.”**

#### ✅ **Recommended Safeguards:**

* **Mask or Hash PII**: Replace sensitive fields (`user_email`, `card_number`, etc.) with hashes or tokens.

  > `"user_email": "hash_5f0f38b4"`
* **Avoid Full Object Dumps**: Logging entire request bodies or ORM entities is a common security smell.
* **Restrict Access**: Apply **role-based log access** and secure storage (e.g., encrypted S3 buckets or WORM storage).
* **Anonymize IPs** where not needed for diagnostics.
* **Data Retention Policies**: Define retention and deletion policies within log aggregation pipelines (e.g., Fluentd → Elasticsearch index lifecycle management).

He also recommends **runtime redaction filters** in Fluentd:

```conf
<filter app.*>
  @type record_transformer
  remove_keys password, ssn, credit_card
</filter>
```

---

### 🧱 **Log Structure and Normalization**

Unstructured logs are easy to write — but hard to search, correlate, or visualize.
Wilkins emphasizes that **“Logs are most valuable when they behave like data, not prose.”**

#### 🔹 **Structure Standards**

* Use **JSON** as the default structure (`key: value` pairs).
* Maintain a **consistent schema** across services:

  ```json
  {
    "timestamp": "...",
    "level": "...",
    "service": "...",
    "event": "...",
    "details": { ... }
  }
  ```
* Use **UTC timestamps** and **ISO 8601 format** to prevent cross-timezone confusion.
* Standardize keys (`service`, `component`, `trace_id`, `env`, etc.) to facilitate correlation in Elastic, Loki, or Splunk.

#### 🔹 **Normalization Techniques**

* **Normalize event naming** (e.g., “user_login” vs. “loginUser” → pick one).
* Use consistent **log keys and hierarchies** for filtering.
* Apply **Fluentd’s `record_transformer` and `parser` plugins** to reshape inconsistent source logs into a canonical schema.
* Add **enrichment metadata**: environment, version, deployment hash, region, etc., for root-cause traceability.

> **“If your logs don’t share a grammar, your tools can’t speak the same language.”**

---

### ⚙️ **Application-Level Guidelines: Exceptions, Standardization, and Avoiding Log Bloat**

Wilkins turns practical here — addressing the human tendency to **over-log** or **misuse exception handling**.

#### 🧯 **1. Handle Exceptions Gracefully**

* **Catch, log, and rethrow only when needed.**
* Don’t log the same exception at multiple layers — **“once per failure”** rule.
* Include **error codes and context** rather than raw stack traces:

  ```json
  {
    "error_code": "DB_CONN_TIMEOUT",
    "component": "order-service",
    "severity": "error",
    "message": "Database timeout during checkout transaction."
  }
  ```

#### ⚖️ **2. Standardization via Frameworks**

* Centralize logging via frameworks like **SLF4J**, **Log4j2**, or **Serilog**.
* Adopt **shared formatters and appenders** to unify structure.
* In distributed environments, integrate with **OpenTelemetry** for consistent trace propagation.

> **“Consistency beats verbosity — the same event format in every service unlocks global observability.”**

#### 🧹 **3. Avoiding Log Bloat**

* Resist logging in tight loops or high-frequency paths.
* Apply **rate limiting or sampling**: e.g., “log every 100th event.”
* Configure Fluentd/Fluent Bit to **filter or aggregate repetitive events** before storage.
* Regularly **review log volume vs. value** using cost dashboards (since each GB stored costs real money in cloud systems).

> **“More logs ≠ more observability. It’s better to have a thousand meaningful messages than a million meaningless ones.”**

---

### 🧭 **Summary – The Mindset of a “Log Engineer”**

Wilkins reframes the role of a developer or SRE:

> **“A log engineer doesn’t just emit data — they curate the story of their system.”**

Logging must balance:

* **Precision** (clear message design),
* **Privacy** (data minimization),
* **Performance** (avoid excessive I/O),
* **Predictability** (consistent schema and severity),
* and **Purpose** (aligned with business and reliability goals).

When combined with **Fluentd’s routing, filtering, and transformation capabilities**, these principles elevate logging from a debugging tool into a **strategic observability practice** that supports DevOps, SecOps, and BizOps alike.


### What to Log

All logging is subject to security standards.  Implicit in the below lists is the fact that you shall not log PII or sensitive data, especially request or response bodies, headers, and credentials.

#### Info to Log

- authentication, authorization, access
- access: system, data, application, remote, remote call (NOC needs to comply)
- changes: db, schema, system, application (rolls), component, pkg (NOC & Release)
- availability issues: startup, shutdown, no response, fault/errs affecting availability,
- resource issues: exhausted, exceeded capacity, reached limits, connectivity issue
- badness: invalid inputs, login fails, any security issues

- transfer of control flow: entry & exit_point

- remote calls: both sync & async, caller/callee/latency

- change / delete of state

- change of config

#### Fields to Log

- **Common fields:**

  - time stamp (Eastern timezone)
  - system time
  - host 
  - container id, cluster id, project name (if deployed in openshift)
  - process id, EASI (if deployed in EDNA or EM)
  - log level  
  - log category  
  - trace id

#### Other fields:

  - User ID
  - Session ID
  - Call tracing ID / Span ID
  - Headers and Payload (Request/Response)
  - Error code, error message
  - Application and version(release), application id, component
  - Binary, process ID 
  - Source file, line number
  - Timing info (start time, end time)
  - Source IP/Port, destination IP/Port

#### Log caught exceptions

Exceptions which are caught, but not rethrown, are typically where you would want to put a log describing what happened with the context (i.e. the values of relevant objects), possibly along with the stacktrace.

Exceptions which are rethrown will either be thrown "to the top" and produce a stacktrace in the logs, or be caught and logged by some other block.

Ignoring a caught exception completely is typically a code smell. If there's some sort of error which "should never happen", then see the next section.

#### Log unexpected exceptions, don't swallow exceptions

Sometimes things go sideways and the "this should never happen" scenario happens. You'll want to log this occurrence, no matter how unlikely.

**Traceable Errors**: You can make your code catch an exception, report the error uniquely, and then continue processing (or rethrow the exception).

One thing we want to avoid is catching exceptions with empty catch blocks. We should at least log something, even if the exception should not cause the request to fail.

***Bad***
```java
try {
 ...
} catch (IOException e) {} //really bad, no way to know when a rare IO exception is because the file already exists, or the disk space is full
```

***Better***

```java
try {
 ... //do some work
} catch (SomeException e) {
	_log.warning("context myId="+idRelated, e);
	//depending on how likely the exception different log levels might be valuable
}
```

OR

```java
try {
 ... //do some work
} catch (NotFoundException e) {
	return TraceableError.newError(e, employeeId, companyId).toSerializableMessage(); //important to call toSerializableMessage() to actually log. 
	//I know the NotFoundException is expected, just means a record not found, traceable exception allows the serializable message to make it to the front end so the user can report it to us
}
```

#### Log the performance of long-running tasks

For long running jobs or processes, we want to have some metrics around how long it takes. Sure we have performance tests to tell us how fast and perhaps we've profiled the code once before, but using Time Monitor to log will tell us just how fast something is every time it runs in production. We can then use Splunk to graph these runs over time to build a picture of our system:


#### Log with context

**Create useful context**

Some log messages may actually have no value when they lack sufficient context.

Consider the following (made up) log message:

<date> <thread>  WARN com.mypackage.MyClass - Expected no fractional part

We can go to the code in MyClass and see exactly the logic that triggers the log message. So, we can understand why it happened, but if we're tasked with investigating and fixing a real issue behind this unexpected state, we need more.

On its own, the log message above is nearly worthless.

Even adding something as small as a single piece of context can help narrow down the location of the bad data:

<date> <thread>  WARN com.mypackage.MyClass - employeePK=<> Expected no fractional part

Now we have a single employee to investigate. Adding more context like

a PK related to what this amount represents
The actual quantity that caused the validation to trip (e.g. "14.72")

would help even more:

<date> <thread>  WARN com.mypackage.MyClass - employeePK=<> someValuePK=<> Expected quantity (14.72) to have no fractional part.

Now we can easily pinpoint the exact data related to the log message.

The useful context is not available where I want to log

For example, you want to log the employee id in a log, but there is no employee id available. One approach is to pass in the employee id into the caller method so you can log it. It's the simpliest approach. But say the caller, and caller's caller, and caller's caller caller do not have employee id. You have have to modify the whole chain of methods.

Log4j2 gives us the ability to use ThreadContext to embed useful log info without needing to modify method signatures. 

**Connect logs with context**

While logs can be useful on their own, they become very informative in aggregate. Even though all these logs have some amount of context (the fully qualified class name, typically), we can add more context to our log messages in order to connect events together, sometimes into one cohesive event.

Think about the following use-cases for someone wanting to look at the logs for a large job that processes data from multiple companies:

I want to see all the logs for a specific run of this job
I want to compare the logs that pertain to one specific company over the runs since the beginning of the month
I want to visualize a value found in some log message per company for a given run

These use-cases are possible in Splunk, but only if the log messages include the proper context. If each log message related to a job run contained something like "jobRunPK={}" and any logs that were company-specific additionally included "companyPK={}", we could filter, group, and visualize the logs based on this information. Without it, there's no way to correlate one log message with another. Relating log messages temporally is extremely error-prone.


### How to Log

#### Requirements

- Auto-configuration. Log level tuned dynamically without rebooting servers.  
- Structured logging with support of line by line, or JSON format.
- Log filtering. Low level log (debug) messages filtered when higher level log level is set (error).
- Log should only write to stdout with tags to identify logging category
- Call tracing id needs to be in performance log, and all application logs.
- Log by categories 
- Snakecase - lowercase separated by underscore naming convention. Example: trace_id
- Dynamically turn on user level logging per use 
- 5Ws 
  - What - Meaningful description
  - When - timestamp (Eastern)
  - Where - host, pid, class/method, source file, line number
  - Why - might include a stack trace or similar concept.
  - Who - user, account

#### Log Levels

Taken from http://commons.apache.org/proper/commons-logging/guide.html#Message_PrioritiesLevels

fatal - Severe errors that cause premature termination. Expect these to be immediately visible on a status console.
error - Other runtime errors or unexpected conditions. Expect these to be immediately visible on a status console.
warn - Use of deprecated APIs, poor use of API, 'almost' errors, other runtime situations that are undesirable or unexpected, but not necessarily "wrong". These might be immediately visible on a status console.
info - Interesting runtime events (startup/shutdown). These might be immediately visible on a console, so be conservative and keep to a minimum.
debug - detailed information on the flow through the system. Expect these to be absent from monitoring and status consoles.
trace - more detailed information. Expect these to be absent from monitoring and status consoles.

***Level Severity***

Some ERRORs, FATALs, and WARNs might be more important than others, especially when FATAL is not present by default under some logging libraries.

There is a mechanism to optionally prioritize or de-prioritize logs by using the "criteria" field in a structured log message.

Any log message without the "criteria" field will be monitored and alerted always.

Log messages with the criteria field will be analyzed based upon the criteria inside the criteria object:

- threshold: if threshold is used, count the number of messages in the past 5 minutes, and alert on every Xth message.
  - Recommend sticking to logarithmically increasing values: 3, 10, 30, 100
- severity: An increasing severity level, where, based upon outside configuration, messages with an equal or higher severity will be logged, and those with lower severity will not be logged.
  - 1 is lowest severity, 100 is highest severity
- reserved for future extension.


#### Log Level Guideline

Type of Information	Recommended Log Level	Comments
Method entry/exit	DEBUG	

Variable inspection	DEBUG	

Value from property	INFO	

Job progress	INFO	Make sure the class or package is set to INFO level in log4j2.xml
Job started, Job finished	INFO	

Exception that should never happen	ERROR	

ObjectNotFoundException exception from user input	INFO	Thinks like ObjectNotFoundException where the input is from a user. 
ObjectNotFoundException exception from internal	WARN	We should fix our algorithms to get rid of these warnings
TimeMonitor or other performance metric logs	INFO	Make sure the class or package is set to INFO level in log4j2.xml
boundary of the system (calling file system, external system)	INFO	make sure to provide information when the application reach externally (such as file system, call external application, etc..) as boundaries where most of the integration problems occurs.

#### Logging For Job Observability

***Logging Job Progress***

Logs are also useful in observing and monitoring the progress of the job. Especially when the job is critical and long running.

When logging progress, it's import the log message sets the correct expectation of completion.

For example: "Completed 50/100 (50.0%) companies in ImportantJob" 

But company A has 10,000 employees, and company B has 10. Company B will run much faster than A so treating companies as equals gives a false impression of real progress. Also, the percentage with one decimal place makes it look like the progress is plus or minus 0.1%.

Better example: "Completed 50 of 100 companies in ImportantJob" 

By removing the fraction and percentage, the job progress is more realistic and it doesn't overpromise accuracy.

Best example: "Completed 747,383 of 1,484,435 employees (50%) in ImportantJob" 

The employees for this job are the scaling variable. For other jobs it can be employee grants, or withdrawals, etc. And even with the more accurate scaling variable used, the percentage is just a whole number so the job has some buffer when assuming it completes 

***Logging Multithreaded Jobs***

When logging the progress of jobs with multiple threads, you will run into race conditions when the threads update the same subtotal and the job progress will move back and forth. See 

could use AtomicLongs. And if there are too many log messages posted by threads, see how a RateLimiter is used.

***Logging Job Start and End***

It's important to log when a job actually starts and finishes. One reason is because while a job is scheduled to start at 1 AM New York, the job doesn't actually start until later due in progress jobs, or jobs already queued ahead of it.

And when job end is logged, we know the job is finished, and if the job finished in time. Also, it's now possible to get a sense on the average time the job takes to finish after a few runs.

#### Log Categories

- Access
- Performance
- Application
- developer app logs
- logs intended for auditing purpose
- logs intended for security monitoring.

**Anti-Patterns**
- Swallowing exceptions
- False positives (No User Account)
- False negative (Data not found)
- Flooding of senseless messages,  messages tagged with wrong logging level
- Having to restart to tune logging

#### Mandated Best Practices

http://commons.apache.org/proper/commons-logging/guide.html#Best_Practices_General

http://commons.apache.org/proper/commons-logging/guide.html#Best_Practices_Enterprise

Use a logging abstraction library, one that is augmented with your company patterns

You MUST always validate the input to your logging statements, due to ability for security vulnerabilities to be exploited.

Similarly, always be on the latest logging library.

Prefer to avoid code with side effects inside logging statements.  This will cause crashes or bugs when logging levels change.  Test your code with and without logging enabled.


```Java
org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(Sample.class);
//The exception is AF which has its own logging abstraction similar in concept to slf4j


// the best supported implementation are logback > log4j2 > log4j, in order of preferences
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-core</artifactId>
</dependency>

// never do a printStackTrace(), instead hand the exception to the logger
logger.error("the exception will be logged with both message and stacktrace", e);

// avoid string concatenation
logger.debug("this" + "wastes" + "memory" + "even" + "when" + "debug==off");
logger.debug("this {} memory {} debug {}", "avoids wasting", "at", "and all levels");

// situationally use logging level checks
if (logger.isDebugEnabled()) {
    logger.debug("this" + "wastes" + "memory" + "only" + "when" + "debug==on");
}

```


**Don't explicitly call toString**	

```java
_log.info("Foobling bar. bar=" + bar.toString()); -> Bad 
_log.info("Foobling bar. bar=" + bar); -> Good

// The bad log will throw a NullPointerException if 'bar' is null.
// The good log will print "Foobling bar. bar=null" if 'bar' is null.
```


**String concatenation vs Placeholders with parameters**

	
```java
_log.info("A foo (foo=" + foo + ") walked into a bar (bar=" + bar + ") and said, " + fooBarSaying); 

_log.info("A foo (foo={}) walked into a bar (bar={}) and said, {}", foo, bar, fooBarSaying);  

// String concatenation
// reduces the risk of transposing parameters. When you have long lists of params place holders can look right but if the argument list is switched around you might not know. This is especially troublesome if there are multiple PKs in the list. 


// Placeholders with parameters
// This is a performance improvement (albeit a mico one). If you use place holders and the log isn't actually logged (due to log level) there will be no time wasted concatenating the string


// For either
// There is some debate about readability some find placeholders easier to read as one can "just read the message" where as others concatenations is more readable as you can place exactly what is being logged where.
```
	

**Do not include PII**

```java
log.warn("Failed to transact. Employee (employee_number={}) is too young (birthDate={})", employeeNumber, birthDate)  Bad

log.warn("Failed to transact. Employee (employeePK={}) has restrictions", employeePK)  Good

//The bad log exposes an employee's employee number and birthday which may be used to identify them
//The good log avoids mentioning any PII and replaces the employee number which personally identifies the employee with the employeePK which identifies them in the system.
```
	

### Requirements

**Log Content**
- Must contain: Timestamp. resource locator, resource id, log level, log content
- Should contain: Code locator, log tags

**Timestamp Precision**
- At least ms precision.
- Both human readable and numeric time.
- For human readable: log with timezone (Eastern). Uses standard ISO format (iso8601)

**Resource Locator**
- Node, container id, application id, process id, service id

**Code Locator (Optional)**
- File, directory, line number, function, class/method

**Resource ID**
- User Id, Customer Id, Account Id

**Log classification**
- Level: Fatal, Error, Warning, Info, Debug, Trace.
- Tags: Flexible for application to define

**Transaction ID**

Used to connect log records across multiple records and resource locators
- Call trace id, application session id, http session cookie

**Format**
Clear record demarcation. Ease for deterministic regular expression to pickup

**Policies**
- Log as much as needed without duplication
- Each record must contain the full context. There should not relies on previous/following record to define the context
- **Should log when call out to external entities**
- Must log at changing system persistent state
- Must log at error condition

**Management**
- System must be synchronized with NTP
- System timing precision/drift must be available/queryable
- Log must be configurable via configuration file
- For long running service, log configuration must be changeable during run-time
- It is expected that PRD system will run at INFO level logging

**Tools/Library**
- Should be implemented via common library to insure format/content consistency
- Library should support dynamic filtering based on ** Log level, Log tag, Resource Id, Transaction Id
- If log is not in ASCII, single line format, generally deployed tool must be available to quickly view and search of records on local device
- Log schema SHOULD be documented and published
- Schema validator SHOULD be available


# Quotes


# References
- https://www.amazon.ca/Software-Telemetry-Reliable-logging-monitoring-ebook/dp/B09D134G82/
- https://www.amazon.ca/Logging-Action-Fluentd-Kubernetes-more-ebook/dp/B09V1Q7QVN/