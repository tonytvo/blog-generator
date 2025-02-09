---
title: system performance summary - wip
date: "2024-12-27T22:12:03.284Z"
description: "system performance summary"
tags: ["evolutionarydesign", "systemperformance"]
---

# system performance and design data intensive applications summary
- [system performance and design data intensive applications](/data-intensive-system-perf)

# site reliability and devops handbook summary
- [site reliability and devops handbook summary](/site-reliability-engineer-summary)

# observability engineer summary
- [observability engineering summary](/observability-engineer-summary)

# common pitfalls/tips/examples

- [How to get consistent results when benchmarking on Linux?](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux)

-** When should I use a cache?**
  - When your data fits all of these characteristics
    - It's used frequently enough to show up as a hotspot on a performance profile of a common workflow
    - It's expensive to gather relative to how frequently it's being used  
      - an expensive SQL query that might be called a few times in a row (eg: participant's current holdings)
      - a simple query that might be called hundreds of times, (eg: Feature toggle cache)
    - It doesn't change that frequently (see stale data below)
    - We don't know beforehand what data is needed to be gathered (see When should I NOT use a cache for more details). 


- **When should I NOT use a cache?**
  - **Lazy Maps**
    - The biggest anti-pattern for caches are "lazy maps".
    - Picture this, you have a report to run, you need to fetch a company's external identifier for a few hundred companies, that identifier is going to be used in several places in the report. You implement the report, but a profile shows that you're spending a ton of time fetching, and re-fetching the company identifiers. Oh easy fix, clearly we should cache these. That way we only need to take the hit the first time we load the identifier, every other access is just a cache hit.

    - What's wrong with this solution? Well your solution is only half-way fixing the problem, you'll still be loading the identifiers one company at a time. You may have reduced duplicate calls for the same company, but you might have only reduced a few thousand calls to a few hundred. Also, and arguably the most important counter-argument to the whole caching exercise, it's a report. You already know at the very beginning exactly which companies you want to run it for. You would be better off just bulk-fetching all of the identifiers in one query up-front, and then pass the resulting map to whoever needs it. Your cache is just an overly complicated map that performs worse.

  - Throw-away caches (aka: short-lived caches)
    - Imagine I'm a participant, I log into system, and am presented with a list of activities that have happened on my account. Imagine that list is expensive to produce, and is re-requested every time the participant navigates back to their home screen in system. I implement a cache for that, and my problems are solved. When the participant logs out, I discard the cache because I don't need it anymore.

    - What's wrong with this solution? The benefit of the cache only exists within the session the participant was logged in for. If the participant logs out (or the session invalidates), and then comes back, I need to go through the expensive operation of re-building the cache. Also, much like the lazy map, I probably already know what I should be putting in there up-front. Either this cache is just a lazy map, or the cache should persist beyond its current scope (which might be a larger architectural change)

- **what are repeating patterns for Cache**?
  - USUALLY the best key for a cache is a primary-key, as we often cache fetched data from the DB. This isn't universally true, but for about 95% of the use-cases for a cache, a PK as the key makes the most sense.
    - If you need to use multiple PKs then maybe your cached value model isn't correct, and we should be breaking down the data into smaller pieces. 
    - If your key is a string or other unique identifier, is it just a PK in disguise? Eg: Using an employee number when we could just as easily use an EmployeePK
    - What data would you need to know about in order to make a decision that you need to invalidate cache entries? Are those data pieces actually your keys?

  - Caches are most effective when they're long lived with few copies in existence (eg: singletons)
    - If your cache is only valid within a certain scope then maybe it's not a cache at all
  - Caches are functionally adding state to an otherwise stateless class. Think about what you might be caching, and when it should be invalidated. 
    - Did you just cache data that was dependent on a feature toggle?
    - Did you just add a cache into an java bean that might affect the results of some integration tests?
    - Did you just cache something that might provide a poor user experience to a participant if the data became stale?
    - Did you just cache something that might contribute to an incorrect calculation if the data became stale?

- **what's are the common problems we face when we do API performance hunting?**
  - when running k6, the http request failure over 1% could skew the results
    - let's assume that we have 100 requests with average 1 second per req, and then we have 1 request failed after 60 seconds which would results in 1.5 seconds average
    - therefore, we would like to get the success rate as close to 100% as much as possible. 
  - there're too many control variables between each k6 run. For example, weblogic, database, network and code change.
  - the data from k6 is sometimes not reliable between each run, hence we typically run k6 multiple times such as 3 times to see where the rough ball parks of the data is pointing to.

  - the data shape is different between companies and between environments, hence we often can't reliably reproduce the problem on local machine.
  - convenient/accidental complexity where we typically just put in the code that is convenient for us and cause performance problem later on 
    - such as getting duplicate data again in method couple times, calling java bean in a loop
    - calling multiple existing java bean to combine the data (instead of creating new query to get the exact data that we want).

- **what're common strategies that we use for hunting API performance?**
  - we need to be aware of the bottleneck? 
    - we want to make the GLOBAL optimization and avoid the LOCAL optimization as much as we can
    - if we're confident that the bottleneck is actually the bottleneck, then any improve on that bottleneck will usually lead to at least the same or more on the Global optimization.
    - if we improve things outside of the bottleneck, then the performance might not be improved globally.
    - hence we need to profile and gather the data as much as we can so we can identify and confident that we have identified the bottleneck.
  - first, we need to gather as much data as we can such as running k6 and looking at appdynamics for slow transactions
    - drill down the call stack to see where the problem is
    - app-dynamics → specific environment → transactions snapshots → click on specific transactions → drill down the call graph
    - we could use splunk queries to get the slow end points → How to get a list of slow endpoints on production sites using splunk and find the related participants and companies
  - app-dynamics is a good tool when we can't reproduce the problem on different environments
  - once we have the call stack, we could essentially walk the callstack (up or down) to review the code site and any potenial fix/solution
    - **walking down the call stack usually give us better experience/more solutions because it kind of provide more oportunities/access to the bad performance coding habits.**
    - start from the bottom would provide more benefit in terms of performance improvement however, it is closer to the hardware, third-party where we have less control and it has already been improved/looked at quite a bit by lots of people already.
  - try to make iteration times fast (from forming hypothesis to commit to see the effects/results on specific environments)
  - reproduce the local performance problems with isolated/not shared database would probably the most effective way to iterate on the problem.
  - we typically use feature toggle to gather the performance improvement for the change. 
    - turn the feature toggle off → run k6 → get data. Turn the feature toggle on → run k6 → get data again. Then we can compare the data between k6 on same environments
  - we want to make sure the number shows that we have improved hte performance and we should abandon the idea/theory if the number prove otherwise.

- what are common strategies for improving Oracle SQL performance?
  - use AWR (automatic workload repository) from Oracle.
  - **finding "bad" SQLs**
    - SQL Developer exposes a tool of the database that is great for identifying performance issues. Click on TOOLS → Real Time SQL Monitor and then specify the connection you want to utilize (likely you will be told this requires the Diagnostic and Tuning pack). There's  STATUS column on the far left of the grid which will tell you which SQLs are currently executing (spinning circle) which are finished (green check mark) and which have errors (red X, could be because the statement failed or was killed or aborted). 

    - The best pieces of information from this would be the DURATION column and the I/O Requests or Buffer Gets columns. 

    - We can watch the SQL execute in real time but also pull historical SQLs from the list. 

    - To use the Real Time SQL Monitor, you need to create a connection to the "system" account first. Note the role is default. And the password is the same as a regular connection to the database.

    - If you try the above and you don't see any information it's very likely we'll need to add some permissions to your account.

  - **SQL performance autotuning**
    - From the Real Time SQL Monitor, you can get the Sql Id of the slow SQL you are interested then. Note that Oracle does not retain these plans forever, so you may have to first rerun the process in the system. Then you can use these SQL commands below to have Oracle analyze and the tune the query. The task takes 1-5 minutes for Oracle to execute. When the task completes, you will see Oracle's recommendation on how to reorganize the query to get the most efficiency. In this example, 8pdg3c4aqnuuz is the Sql Id to replace.

```
-- 1. run this block
DECLARE l_sql_tune_task_id VARCHAR2(100);
BEGIN
   l_sql_tune_task_id := DBMS_SQLTUNE.create_tuning_task ( sql_id => '8pdg3c4aqnuuz', scope => DBMS_SQLTUNE.scope_comprehensive, time_limit => 500, task_name => '8pdg3c4aqnuuz_tuning_task11', description => 'Tuning task1 for statement 8pdg3c4aqnuuz');
   DBMS_OUTPUT.put_line('l_sql_tune_task_id: ' || l_sql_tune_task_id);
END;
/
 
-- 2. run this query if no errors from step 1
-- this can take a few minutes, but you can actually monitor this in the realtime view as well!
EXEC DBMS_SQLTUNE.execute_tuning_task(task_name => '8pdg3c4aqnuuz_tuning_task11');
 
-- 3. run this to grab the results and copy them to SQL Developer or a plain text editor
select dbms_sqltune.report_tuning_task('8pdg3c4aqnuuz_tuning_task11') from dual;
 
-- 4. optional, Oracle may recommend you accept and use the new query plan
execute dbms_sqltune.accept_sql_profile(task_name => '8pdg3c4aqnuuz_tuning_task11', task_owner => 'SYS', replace => TRUE);
```

  - SQL performance evaluation
    - A really good method for analyzing SQL performance is to utilize run time statistics to capture the workload of a query. This can be achieved by adding the GATHER_PLAN_STATISTICS hint into the SQL or by utilizing an alter session (my preference). 

```
set serveroutput off; --quirk of how this works, required to use or you won't get the output you want later
alter session set statistics_level=all;
 
<run your query here>
 
SELECT *
FROM table(DBMS_XPLAN.DISPLAY_CURSOR(FORMAT=>'ALLSTATS LAST ALL +OUTLINE'));
```

    - Here is a full working example

```
set serveroutput off;
alter session set statistics_level=all;
 
--we are using a bind variable in our query most of our queries should be using them
variable col1 number;
exec :col1 := 99236783519
 
SELECT id
FROM table1 
WHERE  id =  :col1;
 
SELECT *
FROM table(DBMS_XPLAN.DISPLAY_CURSOR(FORMAT=>'ALLSTATS LAST ALL +OUTLINE'));

-- highlight ALL of the above commands and choose "run as script" in SQL Developer. The output will contain lots of information but the most important will be the execution plan which looks like the below.
 
---------------------------------------------------------------------------------------------------------------------------------------------
| Id  | Operation                   | Name                | Starts | E-Rows |E-Bytes| Cost (%CPU)| E-Time   | A-Rows |   A-Time   | Buffers |
---------------------------------------------------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT            |                     |      1 |        |       |     2 (100)|          |      1 |00:00:00.01 |       3 |
|   1 |  TABLE ACCESS BY INDEX ROWID| table1     |      1 |      1 |    16 |     2   (0)| 00:00:01 |      1 |00:00:00.01 |       3 |
|*  2 |   INDEX UNIQUE SCAN         | PK_table1_ |      1 |      1 |       |     1   (0)| 00:00:01 |      1 |00:00:00.01 |       2 |
---------------------------------------------------------------------------------------------------------------------------------------------
```

    - So in the above the most important pieces of information are the estimated and actual rows (e-rows / a-rows respectively) and the buffers. We can see that step #2 ran first (index unique scan) and that required 1 buffer (also known as data block). The next step in the plan was #1 which is the table access by rowid which also required 1 block taking us to a total of 2 blocks. The more blocks we see being required the more IO we are doing and the worse the performance is likely to be. 

    - IF the above "doesn't work" it could be a permissions issue

    - A good start for reading execution plans can be found here https://blogs.oracle.com/oraclemagazine/how-to-read-an-execution-plan

    - NOTE : running the above in SQL Developer will stop execution of the query after 5000 records, for larger result sets it would be best to use SQLPLUS for this type of analysis.

- **Creating Indexes**
  - Indexes are great ways to reduce the resource utilization of a query but they aren't always necessary. Say you have a query that is going to run daily, is the cost of the index worth the benefit it will provide? Indexes must track all DML (insert/update/delete) on the indexed columns and this comes with a price so in the case of a daily run query it is likely that not adding an index to speed up the process is a valid option to consider (totally depends on the situation and requires thought and coordination with those consuming the information the process you are working on will output). 

  - There is nothing wrong with a single column index in and of itself, if we have a query with a single filter condition on the table and that lines up with the single column index that's great.
  
  - If for example we had 

```
select * from table where column1 = :x and column2 = :y and column3 between :1 and :2
```

  - What would the best index be?

  - If I told you we also had a query of 

```
select * from table where column2 = :y
```
  - Would that change your answer? 

  - The "best" index for the above 2 queries would likely be an index on (column2, column1) and maybe column3 at the end (would depend on the ranges of values we are looking to filter, etc. The reason for column2 at the leading edge of the index is that Oracle can use it to efficiently filter both of the above queries. If we had an index that led with column1 Oracle may be able to use a skip scan, but that's not as efficient (and often not desirable, certainly not compared to the index where column2 is at the leading edge). 

  - Say we have the following data set up 

    - Table has 300 rows distributed as follows:
    - column1 - 10 rows for every number 1-30
    - column2 - 100 rows for each value A, B, C

``` 
Query is :
select * from table where column1 = :x and column2 = :y
```

  - If we had an index on column1 we would visit the index and get 10 rows after filtering, then we would need to visit the table 10 times to eliminate the rest of the data filtering on column2. If we had an index on column1, column2 we would be able to filter out all the rows via the index and then only visit the table 3 times (3 distinct values for column2 = 1/3rd the data assuming column2 has an even distribution of data across column1 which we are assuming it does here). So with that index we have reduced 66% of the work required (in table visits). 

  - **Function Based Indexes**
    - Function based indexes (applying some logic to a column on a table such as UPPER, TRUNC, etc...) can be very helpful but in general they are not necessary and should be avoided. A great example of this would be applying TRUNC to a date column on a table to perform an operation such as 

```
select * from table where trunc(column_name) = trunc(sysdate)
```

    - However we can easily rewrite that query to be 

```
select * from table where column_name between trunc(sysdate) and trunc(sysdate+1) - interval '1' second
```

    - So we have modified the query slightly so that our variables represent the start of today, and the start of tomorrow less one second (the end of today to the second). 

    - And then having an index on <column_name> instead of trunc(column_name). The benefits of this are many and the detriments are none (aside from a few more keystrokes). Another valid option would be to store the data without a time component to it, truncating it before insert / update. Whenever possible functions should be applied to variables and not to table columns. 


- what are typical performance improvements?
  - Don’t make database calls (use java beans) in a loop
    - Move outside the loop
    - Call in bulk
    - Cache calls
  - Don’t do the same thing multiple times
    - e.g. Don't create the same object in each loop iteration. Move outside of the loop.
  - Fetch everything in a single SQL query instead of combining SQL queries and admin bean method calls
  - Only fetch what you need
  - Use INNER JOINs instead of nested queries
  - Avoid using views
  - Use “UNION ALL” in queries instead of “OR”
  - Oracle only allows up to 1000 keys to be used with the IN clause
    - make use of global temporary tables to get around this
  - Filter in database vs. in code
  - Advanced performance improvements
    - Multithreading using WorkManager 
    - Getting everything in bulk upfront might not be possible so batches might be better instead
  - Use SQLRunner.executeUpdateBatch() instead of EJB3’s crudBulkCreate()
  - Avoid using entities that are connected to the database – have a copy of the data then update later if needed


- **When to Consider Performance?**
  - Whether you're writing new code or fixing an existing performance issue, you should ask: "What are the performance requirements of this feature?". It is not valuable to spend multiple weeks optimizing a piece of code to run in 10 seconds for one million participants when that feature is only used by companies with one thousand employees and runs overnight.  The questions you want answered in your story or epic or even saga are:
    - What is the target number for the scaling variable (Number Participants, number of companies, etc...)
    - What is the target time to complete the job for the target scaling variable (ex. ten thousand participants per minute)
    - PMs are usually the best resource for the above questions. These questions should be answered as a team during story generation.

- **what are common pitfalls/tools used for performance?**
  - EJB3 works best updating single records. It's dramatically slower updating a large collection of records, even using methods "crudBulkCreate". When working on features that work with a large set of records, use SQL runner, and in this case, the executeUpdateBatch method.
  - The database is far more optimized at filtering results than the application layer. Filtering in the database also reduces network and memory costs  as we are no longer loading the unused rows into the application. The solution is to update the method so that the database query is built with the filters included.
  - thread dumps: 
    - low cost way to find application hot spots
    - reveal where threads are stuck in deadlock
  - Jvisualvm
    - Monitor memory usage
    - Thread dump
    - Visualize Application Threads
  - Performance integration/unit tests
    - Lock in hard earned optimizations from future changes
    - Create reliable automated performance tests with realistic data
    - Detect performance regressions for certain processes
  - Eclipse memory analyzer
    - find where the memory is leaking
  - async profiler
    - dynamic run-time profiler for java applications
    - could be setup to provide continuous performance monitoring


# Quotes


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
