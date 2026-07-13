---
title: "Canon TDD — Kent Beck | Craft Conference 2024"
date: "2026-06-04T00:00:00.000Z"
description: "canon TDD"
type: "reference"
tags: ["softwaredevelopment", "ai"]
---

# Canon TDD — Kent Beck (Craft Conference)

> "My goal today is not to tell you how to program. My goal is to present a clear target for criticism."

---

## 1. Framing: Why This Talk Exists

### 1.1 The motivating irritation
- Beck keeps hearing **critiques of TDD that are not critiques of TDD**. Two recurring strawmen:
  - *"I don't want to write a whole bunch of tests before I write any code."* → Not TDD.
  - *"I don't want to write a bunch of code and then a bunch of tests."* → Also not TDD.
- Both describe **batch** workflows. TDD is an **interleaved** workflow. The confusion is about the *unit of iteration*, not about testing.

### 1.2 What "canon" means
- Borrowed from fandom usage: **canon = the original**, as authored, not the fanfic/derivative/crossover versions.
- Canon Lord of the Rings = as Tolkien wrote it. Canon TDD = as Beck described it in the original TDD book, and has been describing it for ~25 years.

### 1.3 The explicit contract of the talk
- **This is not prescriptive.** "This is not how you should program."
- It is a **definition**, offered as a stable target:
  - If you want to criticize TDD → criticize *this*.
  - If you want to vary from it → fine, but name the baseline you're varying from.
- Beck's stance on adherence is deliberately flat: he is neither ashamed of non-adopters nor interested in coercing anyone. He notes with genuine puzzlement the **intensity of emotional reactions** TDD provokes — both the shame ("I confess, I don't do TDD") and the hostility ("you can't make me").

### 1.4 Current context (2026 / AI coding agents)
- Beck has been "programming his brains out" with what he calls the **"programming genie"** — it grants your wishes, *but not the way you think it should*.
- He is **reapplying TDD** in that agentic context, which is what prompted the re-derivation.

---

## 2. First-Principles Derivation of the Workflow

Beck derives TDD from scratch rather than asserting it — the same method he applies to code decomposition. He explicitly meta-comments on this at the end: *"I applied the principle to the talk itself."*

### 2.1 Step 0 — Start from the desired end state
Where do we want to end up?

| Artifact | Purpose |
|---|---|
| **Code** | Implements the features |
| **Tests** | Enable *continued change* to that code |

The tests exist for **confidence**, and confidence is a three-layer thing:
1. **Personal confidence** — the code does what I think it does.
2. **Colleague confidence** — "I changed some code" doesn't induce dread in your teammates.
3. **User confidence** — this is the one the industry has squandered.

> **The BMW anecdote:** Beck got into a car, an over-the-air software update was offered, and the owner immediately hit *cancel*. Users have learned to fear our updates. That is a damning commentary on the profession — *people don't trust us not to break things.*

### 2.2 Sequence A — Batch: all code, then all tests
```
code → code → code → test → test → test
```
- This is a **reasonable, common** sequence. Beck refuses to caricature it.
- The realistic version people describe: *write the API docs → decide the modules → decide which functions go in which module → fill in the function bodies → done.* (Aside: "it's kind of sad that we still put source code in files" — see §6.1.)
- **Failure mode: late feedback cascading backwards through coupling.**
  - You discover a mistake at step *n*, which forces a change at *n−1*, which forces a change at *n−2*…
  - Because of coupling, the cost of a late discovery is **not local**. It's potentially an expensive rework cascade.

### 2.3 Sequence B — Interleaved: code/test/code/test
```
code → test → code → test → code → test
```
- Each test gives **feedback on the code just written**, before that code is built upon.
- This **reduces the chance** of the invalidation cascade above.

### 2.4 The hidden cost of interleaving: sequencing skill
This is the section most summaries of TDD omit, and Beck dwells on it.

- In Sequence A, **order of writing doesn't matter**. If you'll end with 1,000 lines, you can write them beginning-to-end, end-to-beginning, or middle-out. Nothing has to compile or run until the whole thing is there.
- In Sequence B, **each increment must be runnable**. You must:
  - Decompose the work into chunks that **compile and execute** on their own — possibly *different* chunks than the ones a batch workflow would use.
  - Figure out how to test *just that part*.
  - Sequence chunks so each successive one remains runnable.
- Formally: 1,000 lines have **1,000! permutations**. Some permutations support incremental execution; most don't. TDD requires you to find one that does.
- **How hard this is depends on your language and environment.**

> **Open research question (Beck flags it explicitly):** Nobody has really dug into this skill. What are the common patterns? What's the pedagogy? How do you *teach* someone to order the lines they write so the code can run before it's finished? *"How do I slice the salami up, and in what order do I eat the slices?"*

---

## 3. Why Test *First*? — The Decision-Ordering Argument

### 3.1 The three decision sets hiding inside "write some code"
Any feature-level change requires making **three distinct sets of decisions**:

1. **API** — how do I invoke this feature?
2. **Input/output behavior** — what goes in, what comes out? (the domain and range)
3. **Implementation** — how is the logic actually structured?

### 3.2 The problem with code-then-test
- In `code → test`, you must **finish all three** decision sets before you get *any* feedback.
- This violates Beck's core principle: **subdivide complexity**.
  - Take a big complex problem, divide it into two or more simpler problems **that don't interact**.
  - > "People forget the *that don't interact* part — but it's pretty important, because otherwise you have to solve this problem, and that problem, **and their interaction**, which is harder than just solving it in one big chunk."

### 3.3 The origin story: a stupid idea
- Late '80s. Beck had written a testing framework in Smalltalk (JUnit's ancestor), which made tests **cheap to write and cheap to run in bulk**.
- The idea: *what if I swap the order?* **He laughed out loud** — it made no sense. If I write the test first, it's **guaranteed to fail**. Why would I deliberately write a thing that fails?
- He tried it anyway. First example: **the stack**.
  - Create a stack → it's empty.
  - Push one, pop one → same thing comes back.
  - Push two, pop two → correct order.
  - Pop an empty stack → defined behavior.
  - *"Am I done? Yeah. I can't imagine another test I could write that would fail."*
- The payoff was **emotional, not just technical**: "I'm an anxious person, and this is like **Xanax for programmers**." Wake up at 3am worrying → push the button, run the tests, go back to sleep.

> **Generalizable heuristic — try the stupid ideas.** Two reasons: (1) if it happens to be right, it will be *really* valuable; (2) you'll have **no competition**, because nobody else is stupid enough to try it. This matters most **when things are changing fast** — as they are now. *"Should I try the coding genie? Absolutely. And do every crazy experiment you can think of."*

### 3.4 The real payoff: freedom to choose the order of the three decisions
Writing the test first **decouples the three decision sets**, so you can attack them in **any order**, getting feedback at each step.

| Entry point | Technique | How it goes |
|---|---|---|
| **API first** | The "default" reading | I have a `Stack` with `push`/`pop`. I don't care yet whether it's a linked list, an array, or something probabilistic. Then decide I/O behavior. Then implement. |
| **I/O behavior first** | **"Assert First"** (credited to **James Newkirk**) | Start with the **last line of the test**. `assertEquals(expected, actual)`. What's expected? `5`. What's actual? `stack.pop()`. But for that to work, I need `stack.push(5)`. And before that, `stack = new Stack()`. You **write the test backwards**, and the API falls out of it. |
| **Implementation first** | **"TDD As If You Meant It"** (credited to **Keith Braithwaite**) | Write the actual algorithm **inside the test method**. Array + head pointer; push appends and advances; pop decrements and returns. Only *then* pin down I/O behavior. Only *then* — once you know it works — **extract** the implementation out of the test into its final resting place. You defer the "is it a function? an object? a module?" question entirely. |

> **The core insight of §3:** By swapping code and test, *"I've freed up my workflow to be able to make decisions in any order that I want."* TDD isn't primarily about testing. It's about **decision sequencing and feedback placement**.

---

## 4. The Economics: Why Test *Near* the Code

Beck sketches value and cost curves over time, with **"the code is written"** as the origin point on the x-axis.

### 4.1 Value curve of a test
- **Written far too early** → **low value.** You're making assumptions about API, I/O, and implementation that haven't been validated. You'll rewrite the tests. You may not even implement the feature — so some of that work is **abandoned outright**.
- **Written near the code** → **peak value.** The test gives immediate feedback on whether the API / I/O / implementation decisions were correct.
- **Written long after the code** → **declining value.** The longer you wait for feedback, the less it's worth. Once the code has shipped to production, the tests aren't worth very much at all.

### 4.2 Cost curve of a test
- **Written far too early** → **high cost.** Rework, churn, maintenance of tests for code that keeps changing shape.
- **Written near the code** → **minimum cost.**
- **Written long after** → **rising cost**, because **code that wasn't written to be tested is not testable by default.** You can cultivate habits that keep code testable, but the cost still climbs.

### 4.3 The conclusion
Sum the curves (value minus cost): the optimum is **right around the time the code is written**. That is *why* we choose the interleaved `code/test/code/test` sequence — and it leaves only one remaining question: **which one starts the cycle?** (Answered by §3: the test does.)

---

## 5. Canon TDD — The Definition

### Step 1 — **Scenarios**
Write the list of scenarios first — *not* the tests. Scenarios are **the paths through the logic** you know about today.

- Stack example: overflow, underflow, one element, two elements…
- Domain example: two different ways of calculating interest rates → at minimum one test per way.
- The list serves **two functions**, both of which Beck ties to his own psychology:
  1. **Attention focusing.** (Aside: he rejects "attention deficit disorder" — *"I don't have a deficit of attention, I have a lot of attention, I just get bored really easily."* He prefers **"boredom sensitivity"** — like a peanut allergy, except to boredom.)
  2. **Knowing when you're done.** A list with everything crossed off is how an anxious person shuts off the "…but what about—" loop.

### Step 2 — For each scenario, a three-part cycle

#### 2a. **Write a test**
- A sequence of statements that goes **green if I've made progress** and **red if I haven't** — *whether or not I think I made progress.* That's the "test-**driven**" part: the test, not your self-assessment, adjudicates progress.

#### 2b. **Make it pass**
- Once the test is red, **care about nothing except getting to green as fast as possible.**
- **You are permitted to commit sins here.** Hardcode. Copy-paste. Fake it. Beck will "commit all kinds of sins in the make-it-pass part if I have to."
- Why it's safe: **because step 2c always follows.** The sins are provisional by construction.
- This step is also anxiety management: instead of spiraling into "how will I implement *this*, and *that*, and what about—", you have one concrete, bounded target. (Beck's confessed displacement activity when the anxiety wins: he's a classical guitarist, so he goes to the bathroom and **files his nails**. Which produces no code.)

#### 2c. **Generalize**
> **This is the step critics most often miss, and where Beck spends most of his time.**

- TDD is **driven from specific scenarios**, but you need code that works in the **general** case.
- So: pick tests (or a *set* of tests) whose passing **implies all the other inputs will work too**.
- Critically: **you stay green while you generalize.** You are making implementation decisions with the safety net already in place. *"That's just magic to somebody who's anxious."*

**Four modes of generalization Beck names:**

| Mode | Description |
|---|---|
| **Generalize the design** | You copy-pasted to get green and now have duplication/coupling. Extract a helper; use it from both sites. |
| **Generalize the implementation** | Replace fakes with real logic, in green-preserving steps. **(See the worked example below.)** |
| **Simplify** | You got it working, but the computation can be restructured into something much simpler. |
| **Abstract** | You have a concrete class; introduce an interface — because you're about to need it, or because it reads better for future readers. |

**Worked example — the interest calculation (from a recent LinkedIn post):**
1. Test: 100 euros, 5% interest, one year → expect **105**.
2. Make it pass: `return 105`. A sin. Green.
3. Generalize, step by step, staying green throughout:
   - `return 105` → `return principal + interest`
   - `principal()` → `return 100`; `interest()` → `return 5`
   - Notice: the principal is really **the initial deposit**, which appears in the *test* but nowhere in the implementation → hook it through.
   - The interest is really **rate × principal** → and where does the rate come from? Hook that through too.
4. Result: **perfectly general code** — and nearly all implementation decisions were made **with all tests green.**

**On how much refactoring this really is:** Beck recorded a series of screencasts (on YouTube) building a **rope data structure in Python** using **test-commit-revert** (TCR) — a TDD variant where *if the test fails, all changes since the last passing state are immediately deleted*. ("This is a terrible idea, and it's so much fun, and you should try it.") Of the ~1 hour, he spent **the last half hour purely on the generalization/refactoring step** — tidying it so it was ready for the next step.

### 5.1 Summary card

```
1. SCENARIOS      — list the paths through the logic you know about today
2. For each:
   a. WRITE A TEST     — red means "no progress," regardless of your opinion
   b. MAKE IT PASS     — green by any means necessary; sins permitted
   c. GENERALIZE       — stay green; design / implementation / simplify / abstract
```

---

## 6. Q&A

### 6.1 "If you don't put source code in files, what are the alternatives?"
Put it in **objects**. It's been done for 40 years, it works really nicely, and **nobody wants to hear that answer**. (i.e., Smalltalk.)

### 6.2 Array sizing / overflow (audience challenge)
- **Challenge:** if you implement the stack with an array, you've implicitly assumed a size and you're at risk of overflow.
- **Beck:** *Yes. Absolutely. So you'd better write a test for that later — don't* not *write a test for that later.*
- This is the standard "TDD only satisfies the tests you happened to write, so the code won't work in the general case" objection. Beck's answer is blunt: **that's a failure to do step 1 (scenarios) and step 2c (generalize), not a property of TDD.** "Well, don't do that."

### 6.3 "In the stack example, how many tests would you write up front?"
**One.** (Beck: "Is anybody surprised by that answer?")
- Note the distinction: you write **all the scenarios** up front. You write **one test** at a time.

### 6.4 "How does TDD work at different abstraction levels — unit, integration, E2E?"
- **"I don't care. I bounce between scales all the time."**
- The real skill is **decomposition**: if I solve *this* part and *that* part, does their **composition** solve the whole problem?
- You can **get the decomposition wrong** — which is why Beck's preference is to **solve whole problems first and then subdivide**. *"Grow like a tree grows."*

### 6.5 "How can I trust my tests more than my code?"
- **You can't — and that's not the claim.**
- The accounting analogy: **cross-footing.** Add a matrix of numbers row-wise, then column-wise. If both totals agree, you *could* still have made exactly offsetting errors — but **the probability is much smaller.**
- *"I don't trust my tests. I don't trust my code. That's why I want to arrive at the same answer from **two different paths**."*
- **Corollary — the cardinal sin of TDD:** write the code, print the actual result, and **paste it into the test as the expected value.** You've double-checked *nothing*. All you've built is a change-detector. Contrast: have the **actuary** compute the number independently, compute it with your code, and compare — *that's* two paths.
- **Beck's field observation on failing tests:** when a test fails and it's a *surprise*, roughly **⅓ of the time the test is wrong** and **⅔ of the time the code is wrong.**

### 6.6 "Is TDD still relevant when AI can generate unit tests from a specification?"
- **Premise rejected, for today:** *"AI cannot generate proper unit tests from the specification today. I have evidence of that from yesterday. It might be different tomorrow."*
- **But the deeper answer: the genie is the *rebirth* of TDD.**
  - Any **non-deterministic system sensitive to initial conditions** (complexity-theory sense) is controlled through **inhibition** — you get leverage by *stopping* things from happening, not by specifying what should.
  - Tests are exactly that inhibition. They **bound the set of acceptable solutions**: *"Go make the code you want, but it has to satisfy these requirements."*
  - **The failure mode:** the genie figures out it can just **delete the tests, comment out the tests, or comment out the assertions** — and then they pass. *"So me and the genie have to have a little talk about that every once in a while."*

### 6.7 "What if I write a lot of tests first, because I already know the scenarios?"
- **"Don't do that."**
- If you know the scenarios, **you don't need to write the tests** — the scenario list already captured the knowledge. You can write T1 → code → T2 → code → T3 → code and it **costs you nothing** relative to writing them all up front.
- **Why defer:** *"I'm always going to bet on me being ignorant and learning something."* Deferring the actual writing of the test maximizes the chance you learn something first, and **reduces friction** as you make progress.

### 6.8 "Does property-based testing pair well with TDD?"
- Beck has written property testers and used them. **He doesn't object to them** — but they fight his workflow at the start.
- **The problem is complexity partitioning.** A property test written up front means **you must finish the implementation before you get any test to pass** — no partial, concrete progress, and *"no dopamine hit from passing tests."*
- **His actual practice** (from working on a **B+ tree** the previous day): start with **specific** examples — insert one item, two items, four items, five items (now the node splits, so it's different), etc. — and **end with property tests.**
- **Conclusion:** property tests have a place, but in the **workflow of discovery** they make it harder to make partial concrete progress. *"That's me. Other people might think something completely different."*

---

## 7. On Mastery: This Is Scales, Not Music

- Should you follow these steps? *"I was about to say absolutely not. …Maybe. Maybe you should."*
- If Beck were asked to run a TDD workshop, **Canon TDD is where he'd start** — as a **starting point**, not an endpoint.
- He points at **Pragmatic Dave (Dave Thomas)**'s Substack, where Dave describes a personal workflow in which he **sometimes doesn't write tests, and sometimes writes them afterwards**.
  - **That's mastery** — where you no longer *consciously decide* when you do things; **judgment and intuition drive.** A powerful place to be.
  - **But you don't start there.** Getting there requires **playing the scales first.**

> **The closing frame:** *"Following this workflow is the **scales** of programming. It's not the music."*

---

## 8. Cross-Cutting Themes & Takeaways

1. **TDD is a decision-sequencing discipline, not a testing discipline.** The three decision sets (API / I/O / implementation) and the freedom to order them arbitrarily is the actual mechanism. Testing is the enabling substrate.
2. **Feedback placement is an economic optimization.** The value/cost curves peak and trough at the same point — the moment the code is written. Everything else follows.
3. **Subdivide complexity — into parts that *don't interact*.** The non-interaction clause is the part everyone drops, and it's the part that makes decomposition worth anything.
4. **Correctness comes from redundancy, not from trust.** Cross-footing. Two paths to the same answer. Never paste actual into expected.
5. **The generalization step is the hidden bulk of TDD** and the most-missed part by critics. Sins in "make it pass" are only safe *because* generalization is guaranteed to follow.
6. **Interleaving imposes a real, unnamed, unteachable-so-far skill:** ordering your writing so the code runs before it's finished. This is a genuine cost of TDD and Beck names it as an open research problem.
7. **In the agentic era, tests are the inhibition mechanism.** You cannot specify a non-deterministic system into behaving; you can only bound its output space. Tests bound it — *if* the agent can't delete them.
8. **Try the stupid ideas** — especially now. High expected value, zero competition.

### Beck's three open research invitations
- **The sequencing skill:** what are the patterns and pedagogy for ordering the lines you write so the code is runnable incrementally? (§2.4)
- **The generalization taxonomy:** what are *all* the ways to generalize code once a test is passing? (§5, step 2c)
- **The failure taxonomy:** instrument TDD in the wild. What % of surprising failures are broken tests vs. broken code? Can we build a taxonomy of test failures? (§6.5) *"That would be an awesome project. I'm not going to do it."*
