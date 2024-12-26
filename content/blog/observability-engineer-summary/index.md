---
title: observability engineer by Charity, Liz Fong and George summary - wip
date: "2024-07-23T22:12:03.284Z"
description: "observability engineer by Charity, Liz Fong and George summary"
tags: ["systemperformance"]
---

# todo
- summarize observability engineer by Charity Majors, Liz Fong, and George Miranda
- summarize practical monitoring from Mike Julian


# key takeaways


# **Part I: The Path to Observability**

## **Debugging Practices: Observability vs. Monitoring**

---

### **Traditional Debugging Methods**

Traditional debugging methods are grounded in the use of monitoring tools that work well for simpler, predictable systems. However, as systems have grown more complex, these methods often fall short.

---

**1. Dashboard-Driven Troubleshooting:**
   - In monitoring-driven debugging, engineers use pre-configured dashboards to track metrics like CPU usage, memory utilization, request latency, and error rates.
   - **Example:** A dashboard might show a graph indicating a spike in CPU usage. Engineers may infer from past incidents that this likely relates to an unoptimized database query or a sudden traffic surge. 
   - **Limitation:** Dashboards rely on **static, predefined metrics**, meaning you can only see what was anticipated during setup. If the spike is due to an entirely new failure mode, the dashboard won’t tell you the cause.

---

**2. Pattern Matching by Intuition:**
   - Debugging often depends on engineers’ past experiences or “gut feelings.” Engineers use known patterns from previous issues to hypothesize what might be wrong.
   - **Example:** “Last time this error occurred, it was due to a misconfigured API gateway.”
   - **Limitation:** This approach works only when the issue resembles past failures. In modern distributed systems with countless unknown-unknowns, relying on intuition becomes increasingly ineffective.

---

**3. Static, Reactive Monitoring:**
   - Monitoring setups are reactive and threshold-based: they alert engineers only when predefined conditions are violated.
   - **Example:** If response times exceed 300ms, an alert triggers for the on-call team.
   - **Limitation:** Reactive monitoring fails to address **emerging issues**. For example, if an issue is causing intermittent timeouts without breaching thresholds, it might go unnoticed until it escalates into a full-blown incident.

---

### **Limitations of Monitoring-Based Approaches**

The growing complexity of modern distributed systems has exposed critical flaws in monitoring-centric debugging.

---

**1. Low Cardinality Restricts Granularity:**
   - Monitoring systems handle data with **low cardinality**, meaning they aggregate events, losing unique details about specific users or requests.
   - **Example:** A monitoring system might show that 0.01% of requests failed but cannot identify the specific user or request responsible. If user ID `12345` reports an issue, engineers must guess or recreate their conditions.
   - **Impact:** Without high cardinality, tracking unique events or diagnosing single-user issues becomes impossible.

---

**2. Threshold Dependency Masks Subtle Issues:**
   - Monitoring relies on arbitrary thresholds (e.g., “alert when latency exceeds 500ms”), but thresholds are often poorly calibrated and may hide problems that occur between defined limits.
   - **Example:** If 95% of requests respond in 200ms but the remaining 5% take over 1 second, monitoring tools focused on the 95th percentile would show **"all is fine"**, even though some users are experiencing significant delays.
   - **Impact:** Teams miss important edge cases that might affect critical users.

---

**3. Fragmented Data Across Silos:**
   - Monitoring tools often silo data into **logs, metrics, and traces**, which are difficult to correlate manually.
   - **Example:** To debug a user complaint, an engineer might need to analyze logs for errors, check metrics for latency spikes, and review traces for distributed system bottlenecks—each requiring a separate tool.
   - **Impact:** Siloed data increases the time-to-resolution as engineers struggle to connect the dots between related issues.

---

**4. Reactive Nature Leaves Teams Unprepared:**
   - Monitoring only triggers alerts when something breaks, forcing engineers into a constant **firefighting** mode.
   - **Example:** A monitoring system might alert that CPU usage is high, but by the time the team investigates, the incident has escalated, causing cascading failures.
   - **Impact:** Teams spend time reacting to incidents instead of proactively preventing them, leading to **alert fatigue** and burnout.

---

**5. Assumption of Simplicity in System Design:**
   - Monitoring assumes **predictable, static systems** where failure modes can be anticipated.
   - **Example:** Legacy systems often had one database and a few application servers, making it feasible to monitor key metrics like database load and request latency. Modern systems, with **microservices, distributed databases, and ephemeral containers**, break this model.
   - **Impact:** Monitoring tools struggle to handle **dynamic scaling**, **service mesh interactions**, and the emergent behaviors of distributed systems.

---

### **Advantages of Observability in Modern Systems**

Observability offers a fundamentally different approach, focusing on capturing **rich, contextual data** to empower engineers to answer new questions in real time.

---

**1. High Cardinality and Dimensionality Enable Granular Insights:**
   - Observability systems capture **high-cardinality data**, like unique request IDs, user IDs, or specific database query details, making it possible to diagnose individual events.
   - **Example:** If user ID `12345` reports slow performance, engineers can trace their exact request across all services and see what caused the issue, even if it’s buried within millions of events.
   - **Key Benefit:** **"Observability lets you find the needle in the haystack by tracking every thread of data, no matter how small."**

---

**2. Hypothesis-Driven Debugging Encourages Exploration:**
   - Observability allows engineers to ask ad-hoc questions and iteratively refine their hypotheses based on real-time data.
   - **Example:** An engineer investigating a spike in error rates might start by querying all 500-level responses, then filter by service, then correlate with recent deploys, narrowing down the cause step by step.
   - **Key Benefit:** **"With observability, you don’t need to know what questions to ask in advance—you can explore as you debug."**

---

**3. Real-Time Querying Enables Rapid Iteration:**
   - Observability tools allow dynamic querying without requiring pre-configured dashboards or metrics.
   - **Example:** Instead of relying on static dashboards, engineers can search for all requests with `status=timeout` in a specific service and immediately see affected user IDs, endpoints, and trace spans.
   - **Key Benefit:** **"Debugging becomes an iterative, real-time process where each answer leads to the next question."**

---

**4. Understanding Unknown-Unknowns:**
   - Observability excels at uncovering **unknown-unknowns**—those unexpected, novel failure modes that monitoring tools fail to predict.
   - **Example:** A microservice in a distributed system suddenly exhibits timeouts due to an unforeseen dependency bottleneck. Monitoring misses this because it wasn’t programmed to track that dependency, but observability surfaces the issue through high-dimensional tracing.
   - **Key Benefit:** **"Observability equips you to debug problems no one anticipated, no matter how bizarre or complex."**

---

**5. Seamless Correlation Across Distributed Systems:**
   - Observability tools trace requests across multiple services, correlating logs, metrics, and traces into a unified view.
   - **Example:** A request traversing 10 services is slow due to a downstream API call. Observability tools let engineers see the entire journey and identify the bottleneck in seconds.
   - **Key Benefit:** **"You can trace every hop of a request and pinpoint failures in complex architectures."**

---

**6. Proactive Debugging Empowers Teams:**
   - Observability encourages engineers to proactively validate system behavior, catching anomalies before they escalate.
   - **Example:** During a deploy, engineers use observability tools to track error rates in real-time, rolling back the change at the first sign of increased latency.
   - **Key Benefit:** **"Teams can ship confidently, knowing they’ll catch and fix issues before users are impacted."**

---

## **Lessons from Scaling Without Observability**

The story of Parse’s evolution is a compelling case study in how traditional monitoring techniques fail to support the growing complexity of modern systems, and how observability practices are essential to overcoming these challenges. Let’s dive deeper into this transformative journey, highlighting specific examples, challenges, and strategies.

---

### **Case Study of Parse’s Evolution**

1. **Early Days of Parse: A Simpler Monolithic System**
   - Parse initially operated as a **monolithic application** serving a backend-as-a-service (BaaS) platform for mobile developers. Its primary functionality included managing API calls, database storage, and push notifications.
   - **Debugging in the Early Stage:** 
     - Monitoring was straightforward because the architecture was simple. Metrics like CPU usage, memory consumption, and database query latency provided enough insight to address most performance issues.
     - **Example:** If the database became slow, a dashboard would show a spike in query latency, and engineers could optimize SQL queries or add database indexes.

2. **Scaling Challenges Begin: Adoption of Distributed Systems**
   - As Parse grew, its customer base expanded rapidly, and the demands on its infrastructure increased.
     - New customers brought diverse usage patterns, such as high volumes of concurrent requests or large-scale batch processing, leading to increased system complexity.
   - To handle this load, Parse transitioned to a **distributed microservices architecture**.
     - **Example:** The monolith was split into separate services for API handling, database interactions, and notification delivery. Each service operated on different servers, connected through REST APIs.

3. **The Growing Pains of Distributed Systems**
   - The move to distributed systems introduced significant **operational complexity**:
     - Requests were no longer confined to a single application but spanned multiple services, databases, and caching layers.
     - Failures in one service could cascade unpredictably across the system.
   - **Example of a Distributed Failure:**
     - An API request to create a user involved:
       1. A call to the authentication service.
       2. A database write for user details.
       3. A notification sent to the monitoring system.
     - A slowdown in the database service caused timeouts in the authentication service, which led to cascading errors in the API gateway, affecting all clients.

---

### **Transition to Modern Systems and Practices**

1. **Challenges with Traditional Monitoring:**
   - **Fragmented Visibility:** Each service had its own metrics (e.g., API request counts, database latency), but no unified way to trace requests across services.
   - **Reactive Debugging:** Incidents required engineers to manually piece together logs and metrics from multiple systems to hypothesize the root cause.
   - **False Positives and Missed Issues:** 
     - Alerts triggered on static thresholds often generated false positives.
     - Critical issues, such as rare user timeouts, went undetected because they fell outside predefined monitoring patterns.

2. **Adopting Observability Practices:**
   - Parse’s team realized they needed a **unified view** of their system to:
     - Trace individual requests across services.
     - Understand the **context** of failures (e.g., which user, service, or feature caused the issue).
   - **Distributed Tracing Implementation:**
     - Parse implemented tracing tools that generated **unique trace IDs** for every API request.
     - **Example:** A trace ID allowed engineers to follow a request from the API gateway, through the authentication service, to the database, pinpointing exactly where delays occurred.
   - **Structured Logging:**
     - Logs were enhanced with structured data (e.g., user IDs, request parameters) to enable **ad hoc querying** during incidents.
     - **Example:** Engineers could search for all failed requests for a specific user (`user_id: 12345`) and identify patterns or anomalies.

3. **Iterative Debugging with Observability:**
   - Observability tools enabled **hypothesis-driven debugging**:
     - Instead of relying on dashboards, engineers could ask specific questions like:
       - **"Which requests to the authentication service are failing?"**
       - **"What percentage of database writes are timing out?"**
     - Each query provided actionable insights, leading to faster root cause identification.

---

### **Challenges Encountered and Resolved**

1. **Challenge: Retrofitting Observability into Existing Systems**
   - **Problem:** Many services lacked instrumentation, making it difficult to capture trace data or high-cardinality metrics.
   - **Solution:**
     - Parse prioritized **incremental instrumentation**, starting with critical services like the API gateway and database layer.
     - Engineers gradually expanded instrumentation to other services, ensuring minimal disruption.
     - **Example:** Initially, only errors were traced. Over time, they added instrumentation for performance metrics and user activity.

2. **Challenge: Cost of High-Cardinality Data**
   - **Problem:** Capturing and storing high-cardinality data (e.g., user IDs, request parameters) required significant storage and computational resources.
   - **Solution:**
     - Parse adopted **dynamic sampling** techniques:
       - Low-value events (e.g., successful requests) were sampled less frequently.
       - High-value events (e.g., errors, slow requests) were captured in detail.
     - **Example:** Only 10% of successful user logins were logged, but all failed logins were traced fully.

3. **Challenge: Resistance to Change**
   - **Problem:** Some engineers were accustomed to traditional monitoring and hesitant to adopt new tools or workflows.
   - **Solution:**
     - Leadership emphasized the **benefits of observability** through success stories and hands-on workshops.
     - **Example:** A post-incident review highlighted how observability reduced debugging time from 4 hours to 30 minutes, demonstrating its value.

4. **Challenge: Siloed Teams and Data**
   - **Problem:** Distributed systems created silos, where each team focused only on their services, leading to blind spots in debugging.
   - **Solution:**
     - Observability tools provided a **shared source of truth**, enabling cross-team collaboration.
     - **Example:** During a major outage, engineers from the API, database, and notification teams used a unified trace view to identify a deadlock in the database layer.

---

### **Outcomes of Observability Implementation**

1. **Faster Incident Resolution:**
   - Debugging times dropped significantly as engineers could trace issues directly to their root causes.
   - **Example:** A high-latency incident in the API gateway was resolved in 15 minutes by tracing slow database queries, compared to hours with traditional monitoring.

2. **Proactive Problem Identification:**
   - Observability tools allowed Parse to identify and fix potential issues before they affected users.
   - **Example:** Engineers noticed increased latencies in a subset of API requests after a deploy. They rolled back the change before it escalated into a full incident.

3. **Improved Team Collaboration:**
   - Observability fostered a culture of shared ownership, where teams worked together to debug and improve system reliability.
   - **Example:** During a peak traffic event, engineers across teams used real-time traces to dynamically allocate resources and prevent bottlenecks.

4. **Enhanced System Reliability:**
   - By identifying and addressing systemic weaknesses, Parse reduced the frequency of outages and improved user satisfaction.
   - **Example:** A recurring issue with notification delivery delays was resolved permanently after observability revealed an underperforming dependency.

---

### **Key Lessons Learned**

1. **Monitoring Alone Is Not Enough:**
   - Monitoring tools highlight symptoms but lack the depth to uncover root causes in complex systems.
   - **"Monitoring told us something was wrong. Observability told us what and why."**

2. **Incremental Change Yields Big Results:**
   - Retrofitting observability into legacy systems can seem daunting, but incremental improvements deliver significant value.
   - **"Every new trace or log added clarity to the chaos."**

3. **Culture Is as Important as Tools:**
   - Observability requires a cultural shift toward **proactive debugging** and **continuous improvement.**
   - **"Debugging isn’t just about fixing problems—it’s about learning and building better systems."**

4. **Observability is a Competitive Advantage:**
   - Faster incident resolution, improved reliability, and better user experiences give organizations a clear edge.
   - **"In the modern era, observability isn’t optional—it’s a necessity."**

### **Part II: Fundamentals of Observability**

#### **5. Structured Events: Building Blocks of Observability**

Structured events form the foundation of modern observability systems, enabling teams to debug and understand their systems effectively. This section delves into the importance of structured events, their unique advantages, and how they address the limitations of traditional metrics and logs.

---

### **Why Structured Events Are Essential**

Structured events provide **rich, contextual telemetry data** that enables engineers to understand the behavior of their systems with unprecedented depth and clarity.

---

**1. Capturing Detailed Context:**
   - Structured events include **key-value pairs** that encapsulate all relevant information about a specific event in your system.
   - **Example:** A structured event for an API request might include:
     - `timestamp`: `2024-12-26T15:30:00Z`
     - `user_id`: `12345`
     - `endpoint`: `/checkout`
     - `status_code`: `200`
     - `latency_ms`: `125`
     - `transaction_id`: `txn-98765`
   - **"Unlike traditional metrics or logs, structured events tell the full story of what happened, when, and why, all in a single data object."**

---

**2. High Cardinality and Dimensionality:**
   - Structured events can handle **high-cardinality data** (e.g., unique user IDs or transaction IDs) and include hundreds of dimensions (key-value pairs).
   - **Example:** In a distributed e-commerce system, structured events can track:
     - Specific user actions (e.g., `add_to_cart`, `checkout`).
     - Unique product IDs involved in transactions.
     - Payment gateway responses.
   - **"Structured events unlock granular insights that are impossible to capture with metrics or logs alone."**

---

**3. Flexible Querying and Debugging:**
   - Structured events allow engineers to query their systems in **real time**, asking open-ended questions without needing predefined dashboards.
   - **Example:** If a subset of users is experiencing slow response times, engineers can:
     - Query for events with `latency_ms > 500`.
     - Filter by `user_region = EU`.
     - Correlate with `deployment_version = v1.2.3`.
   - **"This flexibility enables hypothesis-driven debugging, where every answer leads to a new question until the root cause is found."**

---

**4. Enabling Distributed Tracing:**
   - Structured events are critical for stitching together **distributed traces**, where a single user request spans multiple services.
   - **Example:** A trace for a user checkout process might combine structured events from:
     - The frontend service (capturing the user’s request).
     - The backend API (processing payment details).
     - The database (logging transaction details).
   - **"With structured events, you can reconstruct the journey of any request across your entire system."**

---

### **Limitations of Traditional Metrics and Logs**

Before structured events became widespread, teams relied heavily on **metrics** and **logs** for system monitoring and debugging. While these tools served their purpose in simpler systems, they fail to meet the demands of modern distributed architectures.

---

**1. Metrics: Aggregate Data Without Context**

- **Definition of Metrics:**
   - Metrics are **predefined numerical measurements**, such as CPU utilization, request counts, or average latency.
   - Metrics are often aggregated over time (e.g., 1-minute averages).

---

**Key Limitations of Metrics:**

1. **Loss of Granularity:**
   - Metrics provide high-level summaries but lack details about individual events.
   - **Example:** A metric might show an average latency of 200ms, but it doesn’t reveal:
     - Which users experienced slow responses.
     - Which endpoints were slow.
     - Whether the issue was caused by a specific database query.
   - **"Metrics reduce system behavior to broad averages, hiding the individual outliers that often signal critical problems."**

2. **Low Cardinality:**
   - Metrics cannot handle high-cardinality data effectively.
   - **Example:** Tracking latency by `user_id` or `transaction_id` is impractical with metrics because it generates too many unique combinations.
   - **"When metrics hit their cardinality limits, they force you to sacrifice insight for performance."**

3. **Predefined Use Cases:**
   - Metrics are **static and reactive**, requiring predefined thresholds and aggregation rules.
   - **Example:** If you didn’t predict that database query timeouts would cause latency spikes, your metrics won’t capture this information.
   - **"Metrics can only answer questions you thought to ask in advance."**

---

**2. Logs: Unstructured Data Without Insights**

- **Definition of Logs:**
   - Logs are **unstructured text entries** that record specific events or system outputs.
   - **Example:** A log entry might read:
     - `2024-12-26T15:30:00Z INFO: User 12345 completed checkout with status 200.`

---

**Key Limitations of Logs:**

1. **Unstructured and Hard to Query:**
   - Logs are freeform text, making them difficult to query and analyze programmatically.
   - **Example:** Searching logs for failed checkouts might require writing **complex regex patterns** to parse relevant details.
   - **"Logs are like a haystack where every needle looks different—finding the right one can take hours."**

2. **High Storage Costs:**
   - Logs generate enormous volumes of data, much of which is redundant or irrelevant.
   - **Example:** Logging every API call and database query for a high-traffic application can quickly overwhelm storage systems.
   - **"Teams often face a trade-off: either log everything and pay the cost or log selectively and risk missing critical details."**

3. **Limited Correlation Across Systems:**
   - Logs from different services are disconnected, making it hard to trace events across a distributed architecture.
   - **Example:** If a request fails in the API gateway, you must manually correlate logs from downstream services to understand the failure.
   - **"Logs provide fragments of the story but rarely reveal the full picture."**

---

### **How Structured Events Solve These Issues**

1. **Unified Data Representation:**
   - Unlike metrics (numerical) and logs (textual), structured events combine the **contextual richness of logs** with the **quantifiable precision of metrics**.
   - **"Structured events give you the best of both worlds: detailed, actionable data in a machine-readable format."**

2. **Dynamic and Real-Time Insights:**
   - Structured events are captured for every action, enabling **real-time exploration** of system behavior.
   - **Example:** If user `12345` reports a slow checkout, you can query for all structured events related to that user in seconds.
   - **"With structured events, you don’t need to predict every failure—you can debug any issue as it arises."**

3. **Built for Distributed Systems:**
   - Structured events include trace IDs and span IDs, making it easy to follow requests across multiple services.
   - **Example:** A distributed trace might include:
     - An API request event from the frontend.
     - A database query event from the backend.
     - A cache miss event from the caching layer.
   - **"Structured events stitch together the entire journey of a request, no matter how many services it touches."**

4. **Scalability and Performance:**
   - Modern observability platforms are optimized to store and query structured events at scale, addressing the limitations of logs and metrics.
   - **"Structured events let you retain high-cardinality, high-dimensionality data without breaking your systems or budget."**

---

# **Part II: Fundamentals of Observability**

## **Structured Events: Building Blocks of Observability**

Structured events are critical for modern observability, offering unparalleled visibility into system behavior. Unlike traditional telemetry approaches, structured events provide rich, contextual, machine-readable data that can adapt to the dynamic complexity of distributed systems.

---

### **Why Structured Events Are Essential**

Structured events are central to observability because they provide a **single source of truth** for understanding what’s happening in a system. Here’s an expanded exploration of their importance:

---

**1. Comprehensive Context: Capturing the Complete Picture**

- **What They Are:**
  - Structured events are records of significant actions in a system, described using **key-value pairs**. These pairs can include timestamps, user identifiers, system states, and more.

- **Example:**
  - A structured event for an API request might include:
    ```json
    {
      "timestamp": "2024-12-26T15:30:00Z",
      "user_id": "12345",
      "endpoint": "/checkout",
      "method": "POST",
      "status_code": 200,
      "latency_ms": 125,
      "transaction_id": "txn-98765",
      "service_name": "payment-service",
      "deployment_version": "v1.2.3"
    }
    ```

- **Why This Matters:**
  - **"Unlike metrics, which summarize data, or logs, which are freeform text, structured events provide all the details of an event in a format that’s both human-readable and machine-queryable."**

---

**2. High Cardinality Unlocks Granular Insights**

- **What is Cardinality?**
  - Cardinality refers to the **uniqueness of data** in a dataset. High-cardinality data includes values like user IDs, session tokens, or unique transaction identifiers.

- **Challenges in Traditional Tools:**
  - **Metrics:** Tracking individual user requests (e.g., `user_id: 12345`) or requests tied to specific transactions (`txn_id`) is impractical because of the vast number of unique combinations.
  - **Logs:** While logs may capture unique identifiers, searching and correlating them across services becomes a manual, time-intensive process.

- **How Structured Events Help:**
  - **Example:**
    - When debugging a latency spike for a user, you can:
      - Filter structured events by `user_id` to find all requests made by that user.
      - Correlate these events with deployment versions or server instances to pinpoint the source of the issue.
  - **"Structured events make high-cardinality data easy to query and analyze, turning individual events into actionable insights."**

---

**3. Dimensionality Enables Rich Queries**

- **What is Dimensionality?**
  - Dimensionality refers to the number of attributes (or key-value pairs) recorded for each event.

- **Why Dimensionality Matters:**
  - The more dimensions an event captures, the more ways you can slice and dice your data to investigate issues.

- **Example of Dimensional Queries:**
  - Query: **"Show all events where `endpoint=/checkout`, `status_code=500`, and `deployment_version=v1.2.3`."**
  - Query: **"Filter all requests with `latency_ms > 500` in the `EU` region made by users with premium accounts."**

- **Impact:**
  - **"Structured events transform raw data into a flexible, queryable system, enabling engineers to investigate problems from any angle."**

---

**4. Real-Time and Iterative Debugging**

- **Traditional Monitoring vs. Observability:**
  - Monitoring relies on **predefined dashboards** with fixed thresholds. If a problem arises outside these parameters, engineers must wait until it recurs to set up new metrics or alerts.
  - Observability, with structured events, allows for **real-time queries**, supporting iterative debugging without prior setup.

- **Example:**
  - During an incident, structured events enable engineers to:
    1. Query all requests with `status_code=500` in the last hour.
    2. Filter by `service_name=payment-service` to isolate problematic requests.
    3. Drill down by `user_id` or `transaction_id` to investigate specific failures.
  - **"Structured events make debugging a dynamic, exploratory process, rather than a static, predefined exercise."**

---

**5. Enabling Distributed Tracing**

- **What is Distributed Tracing?**
  - Distributed tracing ties together structured events from multiple services to show the journey of a single request through a system.

- **Example Trace:**
  - A user checkout request might generate structured events across:
    1. **Frontend Service:** Logs the user request and generates a unique trace ID.
    2. **Payment Service:** Processes the payment and adds transaction metadata.
    3. **Notification Service:** Sends a confirmation email to the user.
  - **"With structured events, you can stitch these events into a trace, revealing the exact path, latency, and failures in a multi-service workflow."**

---

### **Limitations of Traditional Metrics and Logs**

Structured events arose in response to the inherent shortcomings of metrics and logs, which struggle to meet the demands of modern distributed systems.

---

**1. Metrics: Aggregates Without Details**

- **What Metrics Offer:**
  - Metrics summarize system behavior using numerical values (e.g., CPU usage, request counts, error rates) aggregated over time.

- **Limitations of Metrics:**
  1. **Loss of Granularity:**
     - **"Metrics only tell you what happened, not why or to whom."**
     - **Example:** A dashboard might show a spike in error rates but won’t identify which requests or users were affected.
  2. **Low Cardinality:**
     - Metrics struggle with unique identifiers like `user_id` or `transaction_id`.
     - **Example:** You can monitor average latency but can’t track latency for a specific user.
  3. **Predefined Use Cases:**
     - Metrics require predefined thresholds (e.g., alert if latency > 500ms), making them reactive rather than exploratory.
     - **"Metrics are excellent for known-unknowns but fall short for unknown-unknowns."**

---

**2. Logs: Unstructured and Difficult to Correlate**

- **What Logs Offer:**
  - Logs record raw text messages about events, such as error messages or status updates.

- **Limitations of Logs:**
  1. **Unstructured and Hard to Query:**
     - Searching logs often requires complex regex patterns or manual correlation.
     - **Example:** Debugging a specific user’s error requires scanning logs across services for matching `user_id`.
  2. **Siloed Data:**
     - Logs are fragmented across services, making cross-service correlation difficult.
     - **Example:** Tracking a user request across services requires stitching together unrelated log entries manually.
  3. **High Storage Costs:**
     - Logs generate significant storage overhead, making comprehensive logging prohibitively expensive.
     - **"Teams must choose between logging everything (at high cost) or risking gaps in visibility."**

---

### **How Structured Events Solve These Issues**

**1. Unified Data Model:**
   - Structured events combine the **contextual richness of logs** with the **efficiency and structure of metrics**.
   - **"A single structured event captures everything you need to debug an issue, without the noise or limitations of logs and metrics."**

**2. Real-Time Correlation:**
   - Structured events link with trace IDs and span IDs, enabling seamless correlation across services.
   - **"You no longer need to manually stitch together data—structured events do it for you."**

**3. Cost-Effective Storage:**
   - Observability platforms optimize storage for structured events, supporting high-cardinality, high-dimensionality data without breaking budgets.
   - **Example:** Use dynamic sampling to capture full details for critical events while summarizing less relevant ones.

---




# References
- https://github.com/keyvanakbary/learning-notes/blob/master/books/distributed-systems-observability.md
- https://github.com/LauraBeatris/observability-notebook/
