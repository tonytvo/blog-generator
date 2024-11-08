---
title: system performance summary - wip
date: "2024-07-03T22:12:03.284Z"
description: "system performance summary"
tags: ["evolutionarydesign", "systemperformance"]
---

# key ideas
- this is huge topics, so it's continuous progress of updating references to other topics
- here's the interesting topics that has already been discussed summarized before
  - observability
  - site reliability
  - devops handbook
  - design data intensive application
  - systems performance

# **Introduction**

The introduction of "Systems Performance: Enterprise and the Cloud" by Brendan Gregg sets the foundation for understanding the complex field of systems performance. It covers key concepts, methodologies, and examples that lay the groundwork for the rest of the book. Below is an in-depth breakdown of the content found in the Introduction chapter:

### **1.1 Systems Performance**
- **Definition and Scope**: Systems performance is defined as the study of the performance of an entire computer system, including all major software and hardware components. This can include any component within the data path, from storage devices to application software, or even a collection of servers in a distributed system.
- **End-to-End Analysis**: Emphasis is placed on understanding the relationships between components across the entire system stack. For distributed systems, this often means analyzing multiple servers and applications that contribute to a common user experience.
- **Goals**: The two primary goals of systems performance are improving end-user experience by reducing latency and reducing computing costs by eliminating inefficiencies and improving throughput.

### **1.2 Roles**
- **Who Does Systems Performance?**: A variety of roles are involved, including system administrators, site reliability engineers (SREs), network engineers, database administrators, and more. Each of these roles may focus on specific aspects of systems performance, such as network health, application efficiency, or resource allocation.
- **Performance Engineers**: Dedicated performance engineers may work across multiple teams to conduct a holistic study of the entire system, coordinate efforts, and identify bottlenecks that require multidisciplinary expertise to resolve. Gregg provides an example from Netflix, where a cloud performance team assists multiple teams with performance analysis.

### **1.3 Activities**
- **Performance Lifecycle**: Systems performance encompasses a wide range of activities, which can be organized as steps in the lifecycle of a software project. These activities include:
  1. Setting **performance objectives** and creating performance models.
  2. **Characterizing** the performance of prototype software and hardware.
  3. **Analyzing** the performance of in-development products in a controlled environment.
  4. **Non-regression testing** for verifying the performance of new versions.
  5. **Benchmarking** to measure and validate performance metrics.
  6. **Proof-of-concept testing** in production environments.
  7. **Performance tuning** in real-world production.
  8. **Monitoring** systems while in production.
  9. **Analyzing performance issues** in production.
  10. Conducting **incident reviews** for performance problems, looking for ways to prevent similar issues in the future.

### **1.4 Perspectives**
- **Two Primary Perspectives**: Systems performance analysis can be approached from two perspectives:
  - **Resource Analysis**: Analyzing system resources like CPU, memory, disk, and network from the bottom up. This is the typical approach taken by system administrators.
  - **Workload Analysis**: Analyzing workloads, including applications, from the top down. This perspective is used by developers who focus on application performance and seek to optimize how the workload utilizes underlying resources.
- **Full Stack Approach**: Performance engineers often combine both perspectives to conduct a thorough analysis of a system, providing insights that are sometimes missed when only one perspective is used.

### **1.5 Performance is Challenging**
- **Subjectivity**: Performance is often subjective, meaning that a "good" performance level for one user might be "bad" for another. Gregg discusses how setting objective goals, such as specific latency targets, can help eliminate subjectivity.
- **Complexity**: Systems are inherently complex. Performance issues can be influenced by cascading failures between components, making analysis difficult. Performance engineers must understand the interactions between all components and often adopt a holistic approach to analysis.
- **Multiple Causes and Issues**: Performance problems can arise from multiple, simultaneous causes rather than a single issue. Understanding and quantifying the magnitude of various issues is essential to identifying the highest impact opportunities for improvement.

### **1.6 Latency**
- **Key Metric for Performance**: Latency is one of the most important metrics for measuring performance. It measures the time taken to complete operations such as an application request or database query.
- **Estimating Speedup**: The use of latency as a metric can help estimate potential speedups by analyzing time spent in different operations. For example, identifying latency in disk reads can help quantify the benefit of improving or caching those reads.
- **Ambiguity**: The term "latency" can be ambiguous without additional context. In the context of systems performance, latency may refer to the time required for connection setup, data transfer, or other operations. The chapter provides definitions to clarify such ambiguities.

### **1.7 Observability**
- **Understanding Through Observation**: Observability refers to understanding a system by observing its external outputs. The chapter introduces the concepts of counters, metrics, profiling, and tracing.
- **Types of Observability**:
  - **Counters, Statistics, and Metrics**: Basic numerical outputs that give insight into system behavior.
  - **Profiling**: Capturing snapshots of resource usage over time, which is useful for understanding periodic resource bottlenecks.
  - **Tracing**: Tracking the flow of requests through components to understand bottlenecks.

### **1.8 Experimentation**
- **The Importance of Experimentation**: Performance tuning is an iterative process involving trial and error. Experimentation is often essential to gain insights and validate assumptions.

### **1.9 Cloud Computing**
- **Unique Challenges of Cloud**: The chapter introduces cloud computing and the specific challenges it presents for systems performance. Cloud environments are highly dynamic, with frequent scaling and resource sharing. These factors affect observability and optimization efforts.

### **1.10 Methodologies**
- **Linux Perf Analysis in 60 Seconds**: Brendan Gregg provides a practical checklist to quickly assess the performance of a Linux system in under 60 seconds. This rapid analysis method is particularly useful for time-critical scenarios, such as troubleshooting performance issues in production environments. The checklist involves running a series of quick commands to gather an overview of system health:
  1. **uptime**: Checks system load averages to identify if the system is currently overloaded.
  2. **dmesg | tail**: Reviews recent kernel messages to check for errors or warnings.
  3. **vmstat 1 5**: Provides a quick summary of CPU, memory, and I/O activity over a short period. This helps identify CPU saturation, swapping, or I/O bottlenecks.
  4. **mpstat -P ALL 1 5**: Shows CPU usage for all processors to help identify if the workload is balanced across CPU cores.
  5. **pidstat 1 5**: Displays per-process resource usage, including CPU, memory, and I/O, which can help identify processes using the most resources.
  6. **iostat -xz 1 5**: Provides detailed disk I/O statistics, which can indicate if any disks are saturated or experiencing high latency.
  7. **free -m**: Checks memory usage, including available memory and swap usage, to determine if the system is experiencing memory pressure.
  8. **sar -n DEV 1 5**: Monitors network interface statistics to identify potential network bottlenecks.
  9. **top**: Provides a real-time view of system activity, including CPU, memory, and process information, useful for identifying resource-hungry processes.
- **Objective**: The goal is to gather a high-level snapshot of system performance quickly, enabling the performance engineer to identify any glaring issues and determine where more detailed analysis is needed.

- **Performance Analysis Techniques**: Key methodologies for analyzing systems performance are introduced here, including ways to identify and resolve common performance issues.

### **1.11 Case Studies**
- **Real-World Examples**: The chapter concludes with case studies to illustrate common performance problems and solutions, including slow disks, software changes, and more complex scenarios. These examples demonstrate how performance analysis works in practice and serve as practical guides for dealing with similar challenges.

### **1.12 References**
- **Sources for Further Reading**: The introduction provides references to help readers learn more about the topics covered in the chapter and to deepen their understanding of performance analysis.

---


# system performance and design data intensive applications summary
- [system performance and design data intensive applications](/data-intensive-system-perf)

# site reliability and devops handbook summary
- [site reliability and devops handbook summary](/site-reliability-engineer-summary)

# observability engineer summary
- [observability engineering summary](/observability-engineer-summary)

# Quotes


# Game Plan
- surface the critical examples based on experience.
  - it could be code, database queries, etc...
- go as broad as possible for the first attempt
- should at least include perspective from the following references
  - designing data intensive applications -> https://www.amazon.ca/Designing-Data-Intensive-Applications-Reliable-Maintainable-ebook/dp/B06XPJML5D
  - system performance from brendan gregg
  - java performance from Scott Oaks
  - [Thinking in Systems](https://www.amazon.ca/Thinking-Systems-Donella-H-Meadows-ebook/dp/B005VSRFEA)
  - site reliability engineering book
  - database reliability engineering book
  - practical monitoring from mike Julian
  - observability engineering


# References
- https://www.infoq.com/articles/practical-monitoring-mike-julian/
- https://www.amazon.ca/Systems-Performance-Brendan-Gregg-ebook/dp/B08J5QZPNC
- https://www.amazon.ca/Java-Performance-Depth-Advice-Programming-ebook/dp/B084RY5438/
- https://github.com/ScottOaks/JavaPerformanceTuning/tree/master/SecondEdition
- https://www.amazon.ca/Observability-Engineering-Charity-Majors-ebook/dp/B09ZQ6FHTT
- https://elvischidera.com/2022-01-20-designing-data-intensive-applications
- https://danlebrero.com/2021/09/01/designing-data-intensive-applications-summary/
- https://github.com/s905060/site-reliability-engineer-handbook
- https://dev.to/bitmaybewise/series/21343
- https://danluu.com/google-sre-book/
- https://oliver-hu.medium.com/systems-performance-reading-notes-chapter-6-cpu-d70627188b85
- https://oliver-hu.medium.com/systems-performance-reading-notes-chapter-7-memory-6e87ac8fcfdd
- https://oliver-hu.medium.com/system-performance-chapter-8-file-system-7322f82fbc7c
- https://lrita.github.io/images/posts/linux/Percona2016_LinuxSystemsPerf.pdf
- https://www.brendangregg.com/USEmethod/use-rosetta.html
- https://www.brendangregg.com/linuxperf.html
- https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux
- https://github.com/keyvanakbary/learning-notes/blob/master/books/distributed-systems-observability.md
- https://github.com/LauraBeatris/observability-notebook/
