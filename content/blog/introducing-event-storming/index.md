---
title: introducing event storming by Alberto Brandolini summary
date: "2025-03-02T22:12:03.284Z"
description: "introducing event storming by Alberto Brandolini summary"
tags: ["domaindrivendesign", "design"]
---

# take-aways


Here’s an expanded and detailed breakdown of **Part 1: Understanding EventStorming**, with key insights and highlighted phrases.

---

# **Understanding EventStorming**
EventStorming is more than just a workshop technique—it’s a **highly collaborative** and **visually engaging approach** to uncovering inefficiencies, improving business processes, and designing innovative solutions. This section explores **four key scenarios** where EventStorming proves to be a game-changer.

## **What Does EventStorming Look Like?**

---

### **🔍 Challenging Corporate Processes**
_"When business processes grow unwieldy and bureaucratic, EventStorming can cut through the noise and expose inefficiencies."_

A **mid-sized company** struggling with an outdated **IT infrastructure** faced mounting operational difficulties. Their existing systems, once a competitive advantage, had now become a major bottleneck. The challenge was clear: **how to untangle and modernize a rigid, inefficient system**.

#### **🚀 The EventStorming Approach**
- **Breaking down silos**: The company had multiple teams, each with its own isolated processes. EventStorming facilitated cross-team collaboration to identify systemic bottlenecks.
- **Exposing inefficiencies**: Participants marked **problematic areas** with _purple sticky notes_, highlighting broken workflows and recurring blockers.
- **Enabling rapid solutions**: A critical finding was that a seemingly _mandatory bureaucratic step_ was **not actually necessary**—it had evolved as an unintended side effect of a prior system migration.

_"By visualizing the entire process, teams realized that software constraints were imposing unnecessary manual work, creating inefficiencies that could be removed."_

#### **🎯 The Outcome**
The company **redefined its internal workflow**, eliminating redundant steps, improving system integrations, and ultimately **accelerating its customer acquisition process**.

---

### **🚀 Kicking Off a Startup**
_"For startups, time is everything. EventStorming helps founders and developers align on a shared vision, reducing costly missteps."_

A **new fintech startup** needed to build its **backbone software** from scratch. The **founders were industry veterans**, but the developers **had no domain experience**. The challenge? **Ensuring that the technical team fully understood the business context.**

#### **🔑 EventStorming in Action**
1. **Immediate engagement**: The session started with a _plotter paper roll covering the walls_, hundreds of **orange sticky notes**, and a **focus on Domain Events**.
2. **Rapid knowledge transfer**: Instead of lengthy briefings, developers were asked to _write key Domain Events and arrange them chronologically_.
3. **Pattern discovery**: The team began to see **recurring structures** and natural _boundaries in the system_, helping define Bounded Contexts.
4. **Addressing compliance risks**: The process exposed **hidden regulatory constraints**, allowing the startup to make informed choices early.

_"Within a single day, the entire development team had a clear understanding of the business model, reducing onboarding time from weeks to hours."_

#### **🚀 Key Takeaway**
By **aligning business and technical teams** from the outset, the startup avoided costly rework and ensured **a strong foundation for its Minimum Viable Product (MVP)**.

---

### **💡 Designing a New Feature for a Web App**
_"Adding new features isn’t just about coding—it’s about understanding how they fit into the user journey and business objectives."_

After completing a **Big Picture EventStorming session**, a web app team needed to **zoom in on a new feature**. The goal was to design a **seamless booking experience** without disrupting the existing user flow.

#### **🛠 How EventStorming Helped**
- **Refining Domain Events**: The team iterated over sticky notes, rewriting and improving descriptions.
- **Uncovering dependencies**: The mapping process revealed that certain actions were triggering unexpected side effects.
- **Defining clear responsibilities**: Using _yellow sticky notes_ to group related commands and events, the team **discovered missing user interactions**.

_"What started as a simple feature request turned into a full-fledged user experience discussion, preventing usability pitfalls before development began."_

#### **🔑 Outcome**
- **A well-structured feature** that accounted for real-world edge cases.
- **Avoidance of development waste**, as unnecessary complexity was removed before coding started.

---

### **⚡ Quick EventStorming in Avanscoperta**
_"Sometimes, a quick retrospective can uncover more value than months of traditional analysis."_

A **small training company** noticed a **decline in ticket sales** for their workshops. Instead of guessing, they ran a **Quick EventStorming session** to **analyze their sales funnel**.

#### **🔍 Key Discoveries**
- **Ambiguous discount policies**: Customers were confused by multiple price points.
- **Weak call-to-action**: The workshop descriptions weren’t compelling enough.
- **Marketing gaps**: The team had no clear strategy for promotions.

_"The purple sticky note labeled ‘Training Class Description Sucks!’ became a pivotal insight, shifting the company’s focus toward better messaging."_

#### **📈 Results**
By **prioritizing marketing and communication improvements**, the team **boosted conversions** without making any technical changes.


---

## **Silos: How Organizations Naturally Evolve into Silos and Their Impact on Efficiency**

Silos are a **natural consequence of organizational growth**. As a company expands, roles become specialized, leading to **barriers to effective communication and collaboration**. The author describes this as *organizational gravity*, meaning that **businesses tend to fall into similar dysfunctional patterns regardless of their industry or structure**.

> **"Silos will emerge by default in any organization. They’re easy to establish and very hard to remove."**  

### **How Silos Form**
The formation of silos follows a predictable pattern:
1. Someone becomes overwhelmed managing multiple tasks.
2. They **hire a specialist** to take over a specific function.
3. The new hire starts contributing but remains **focused only on their area**, developing **expertise in isolation**.
4. The former expert **loses touch with the details** of that area.
5. **The cycle repeats**, with more roles being specialized, leading to knowledge fragmentation.

The unintended consequence is that **employees optimize for their own department rather than the company as a whole**, leading to **local optimizations but global inefficiencies**.

> **"In the long term, silos maximize ignorance about the whole."**

Silos also result in a lack of **cross-functional learning**. The problem is not just inefficiency but that **knowledge does not transfer**, making problem-solving more difficult across teams.

---

### **Targets and Goals: The Issue with Management-Driven Goal-Setting Processes**

The way organizations set **targets and goals** often creates **hidden conflicts and inefficiencies**. While goal-setting seems logical, **secrecy and misalignment** in corporate objectives can cause **serious organizational dysfunction**.

> **"Individual goals and targets and the possible monetary rewards that come with them are not discussed publicly. But this means there is no safety check that the goals are compatible between themselves."**  

#### **The Problem with Traditional Goal-Setting**
1. **Secrecy in targets** – Managers often **privately agree on their goals**, which may conflict with the goals of other teams.
2. **Conflicting priorities** – Different departments **compete for limited resources** instead of collaborating.
3. **Bonuses create perverse incentives** – Employees may **game the system** to meet targets at the expense of the broader organization.
4. **Unrealistic expectations** – Management often **demands results that exceed team capacity**, leading to **stress and inefficiency**.

The book illustrates this problem with an example:
> **"Every manager thought they had rights to a 40% of the pie. But there were seven managers, and the pie was not big enough for all of them."**

This scenario describes how **stakeholders refuse to compromise** on deadlines because their bonuses depend on them, even when deadlines are **clearly unachievable**.

---

### **Decisions’ Lifecycle: Understanding How Decisions Evolve Within a Business**

> **"Decisions will pile up."**

Decisions **rarely get revisited or undone**, leading to **a growing list of outdated, ineffective policies**. Organizations often **keep old decisions in place long after they are useful**, creating unnecessary complexity.

#### **Why Old Decisions Persist**
1. **Fear of admitting mistakes** – Decision-makers see reversing a choice as an **admission of failure**.
2. **Bias toward adding, not removing** – It's **easier to keep adding new rules** than to simplify existing ones.
3. **Organizational inertia** – Once a policy is in place, **no one wants to be responsible for removing it**.

An example from the book:
> **"People in different departments had the illusion of collaborating because they performed useless duties for their colleagues."**

This illustrates **how old decisions remain unchallenged**, even when they no longer provide value.

---

### **The Cost of Agreeing: Challenges of Achieving Alignment in Complex Systems**

> **"Centralized, top-down decisions still have the advantage of speed of execution. In contrast, collaborative decisions require reaching an agreement, and achieving it could be incredibly demanding in terms of time, energy, and coordination."**

While **collaborative decision-making is ideal**, it is often **slow and difficult to implement**. **Top-down decisions move faster**, but they can be **misaligned with the realities of teams executing them**.

Key points:
1. **Alignment takes time** – The more people involved, the harder it is to reach a consensus.
2. **Revisiting past decisions is hard** – Decisions become part of **corporate identity**, making change difficult.
3. **Fear of challenging leadership** – Employees may **avoid questioning bad decisions** because it could be seen as **disrespecting authority**.

The book references **Architectural Decision Records (ADRs)** as a way to document decisions **along with their original context**, making it **easier to evaluate when a decision should be reversed**.

---

### **Putting Everything Together: Synthesizing the Key Issues That EventStorming Addresses**

> **"EventStorming can be a handy tool to guide the newly hired into the intricacies of the organization, speeding up onboarding and maximizing confidence."**  

EventStorming helps tackle these issues by:
1. **Breaking down silos** – **Cross-functional teams collaborate** to build a shared understanding.
2. **Revealing hidden dependencies** – Mapping out events exposes **bottlenecks and redundancies**.
3. **Aligning goals** – Helps different departments **visualize conflicts in priorities**.
4. **Encouraging adaptability** – Makes it **easier to challenge outdated decisions** in a structured way.

EventStorming is **not just a tool for software teams**—it’s a **way to uncover and address deep-rooted organizational dysfunctions**.

Here is a detailed expansion of the key sections from *Introducing EventStorming*, **highlighting key insights and challenges** of software development with **bold** phrases and **critical quotes**.

---

## **Pretending to Solve the Problem by Writing Software**

> **"Software engineers often think they are on a mission."**  
> **"Software is the backbone of company operations, it’s the glue that enables successful businesses."**  

However, while **software can solve problems**, it **frequently creates new ones** due to flawed assumptions and misalignment between business needs and technical execution. This section explores why **traditional software development often fails to address real business problems** and how **EventStorming offers a better approach**.

---

### **It’s Not About Delivering Software**
One of the biggest misconceptions in software development is that **"delivering software" is the ultimate goal**. This assumption **misplaces the true value of software development**, which is not just writing code but understanding and solving the actual business problem.

> **"Software development is a learning process, working code is a side effect."**

This quote **reframes** software development: instead of focusing on **fast deployment**, developers should **prioritize learning and understanding the problem space**. However, most teams are **optimized for output (writing code) rather than outcome (solving the real problem)**.

- **The real bottleneck is understanding.** Many organizations **overemphasize delivery speed** without ensuring they truly understand **what needs to be built**.  
- **Developers are trained to "produce" software**, often without **direct contact with users**, leading to **software that doesn’t fit real-world needs**.  
- **"We’ve been optimizing the wrong thing!"** While coding speed has improved exponentially, **the ability to gain meaningful knowledge about business problems has stagnated**.  

> **"What is the value of code written on time and on budget by someone who doesn’t understand the problem?"**

---

### **The Illusion of the Underlying Model**
Another major flaw in traditional software development is the **assumption that a perfect underlying model exists, waiting to be discovered**. 

> **"Naive developers and analysts might have the illusion that the model is there, only the pieces of the puzzle are scattered around. You just have to find the pieces and put them together."**

This **false belief** leads teams to **start with rigid models based on assumptions rather than exploration**. The problem with this approach:
- **Real-world business processes are messy and inconsistent.**  
- **Legacy decisions influence current processes in ways that are not immediately visible.**  
- **Stakeholders often don't fully understand their own needs until they see software in action.**  

A traditional approach assumes that **if we capture enough details, we can design a perfect system from the start**. However, this **ignores that business rules evolve**, and software must **adapt** rather than remain rigid.

> **"It’s actually fun at the beginning. For a detail-obsessed maniac like me, looking for clues in order to design a data model able to represent reality was a rewarding secret pleasure. But reality is always more complex than our models."**

---

### **The Product Owner Fallacy**
In Scrum and Agile methodologies, **the Product Owner (PO) is expected to be the single point of truth between business and development**. However, this **creates an unintended bottleneck**.

> **"Slowly, the Product Owner becomes the only person who’s entitled to learning, while the development team turns into a mere translator of requirements into code."**  

This **recreates the old Waterfall-era separation between analysts and developers**, reducing the **entire development team to order takers**. The **downside**:
- Developers lack **direct exposure to stakeholders and business problems**.  
- **Second-hand learning is inefficient**—misinterpretations multiply at each layer.  
- A **single person (PO) becomes a bottleneck**, limiting knowledge flow.

> **"If your goal is to learn to ride a bike, you can choose between:**
> - **Get a bike and try it.**
> - **Talk with a biker first.**
> - **Talk with a friend who knows a biker.**
> - **Read a specification document written by a friend who talked with a biker."**

**Choice is yours.**

The best learning comes from **direct experience, not layers of abstraction**. **EventStorming removes this bottleneck by bringing all stakeholders into the same room**.

---

### **The Backlog Fallacy**
Most software teams follow **a structured backlog of features**, treating **software development as an ordered queue of tasks**. However, this **gives the illusion that the whole project is just the sum of its parts**.

> **"A backlog is optimized for delivery, but it isn’t optimized for learning."**  

This **creates several problems**:
1. **Backlogs prioritize "planned" work over discovery**, preventing teams from exploring critical unknowns.  
2. **Iterations reinforce existing biases**, making it harder to step back and rethink fundamental assumptions.  
3. **Backlogs assume a predictable path**, which rarely exists in **complex business environments**.  

> **"Some projects follow the plan relatively well—compliance projects, for example. But if your project involves innovation, you need to make room for discovery, not just execution."**

Rather than following a **rigid backlog**, **EventStorming enables teams to uncover what’s truly important through real-time collaboration and dynamic modeling**.

---

### **EventStorming Approach: A Better Way to Model Complex Domains**
Unlike traditional software methodologies, **EventStorming flips the model-first approach on its head** by **starting with real-world events and processes**.

> **"There is no reason not to anticipate learning. It’s assuming that we already learned everything that creates a mess."**

#### **Key Benefits of EventStorming**
- **Encourages direct conversation between business and development.**  
- **Uncovers hidden dependencies and business rules before implementation.**  
- **Allows iterative learning and adjustment before code is written.**  
- **Helps teams visualize the full process rather than just isolated requirements.**  

> **"What about emergent design? Somebody once told me, 'So you’re against emergent design?' …well, I am not. But emergent design is not an excuse to avoid understanding the problem first."**  

EventStorming allows for **controlled discovery**—**teams can iterate rapidly but with an informed starting point**. This results in **faster alignment, fewer late-stage changes, and software that better fits real-world needs**.

---

### **Conclusion**
> **"Software development is not about writing code—it’s about solving problems."**  

The traditional **focus on deliverables over learning leads to inefficiencies, misalignment, and unnecessary complexity**. By **shifting the focus from software output to shared understanding**, **EventStorming helps teams build software that actually works for the business**.


Here’s an expanded and detailed breakdown of **"Your First EventStorming Session"** with key quotes highlighted:

---

## **Your First EventStorming Session**  

> "I’m going on an adventure." – *The Hobbit: An Unexpected Journey*  
> Just like Bilbo Baggins’ journey, an EventStorming session is an adventure into the unknown, uncovering hidden complexities, assumptions, and crucial business insights.

---

### **2.1. Show an Example**  

**"Jump quickly into fun practice rather than get bogged down in abstract explanations."**  
Instead of explaining theoretical concepts, start with an intuitive **example** like a *movie-going experience*. Events are recorded in **past tense** (e.g., *Checked movie schedule*), emphasizing the timeline approach.

> **"It is better to show than tell."**  
> Events should be sequenced visually, from **left to right**, like a **storyboard**.

**Key Takeaway:**  
Use a **familiar scenario** to **quickly engage** participants without overwhelming them.

---

### **2.2. Happily Ever After**  

**"For a group completely new to EventStorming, start with a quick icebreaker."**  
A fun and engaging way to introduce EventStorming is through **well-known stories** like *Cinderella* or *The Lion King*. Participants **write down key events** on sticky notes without worrying about order or correctness.

> **"Once upon a time" at the far left, "They lived happily ever after" at the far right."**  
> A **simple timeline** structure helps participants **naturally organize** events.

**Key Takeaway:**  
Encourages **collaboration and creativity** while building **confidence in the technique**.

---

### **2.3. Start with Events**  

**"Write first, ask questions later. Go for volume in the beginning."**  
EventStorming begins with a **chaotic but productive brainstorming session**. Participants write down **as many events as possible**, without concern for **duplicates or sequence**.

**Common early concerns:**  
- **Duplication** – It’s **okay** initially.  
- **Timeline enforcement** – Not needed **yet**.  
- **Granularity** – Just **get events out** first.  

> **"Embrace diverse perspectives and terminology—at least for now."**  
> **Language differences** emerge but should not be resolved too early.

**Key Takeaway:**  
**Encourage rapid event listing** to **capture the domain’s full complexity**.

---

### **2.4. Capturing Questions**  

**"Capture questions and pain points as hot spots."**  
Early on, **participants go broad rather than deep**. Facilitators should record **uncertainties** rather than getting **stuck debating details**.

> **"What spell?" "In what time zone?"**  
> Questions highlight **gaps in knowledge** that may need further investigation.

**Techniques to capture questions:**  
- Use **brightly colored sticky notes** for questions, risks, and assumptions.  
- If a question **remains unanswered**, **add it to the timeline** instead of debating.  

**Key Takeaway:**  
Encourages **open communication** and **avoids bottleneck discussions**.

---

### **2.5. How to Start?**  

**"How do we actually begin?"**  
Start by defining **a clear objective** for the session and gathering **diverse stakeholders**.

> **"The goal is to learn as much as possible in the shortest time possible."**  
> Avoid wasting time by **focusing on key contributors**.

**Steps to start:**  
1. **Define the scope** – What are we mapping?  
2. **Identify participants** – Business and technical experts.  
3. **Set the ground rules** – Encourage open thinking.

**Key Takeaway:**  
Clarity on **objectives and participation** ensures a **focused session**.

---

### **2.6. Setting Up the Modeling Space**  

**"Both physical and virtual spaces need thoughtful setup."**  
For **in-person workshops**:  
- Use a **large wall** or **whiteboard**.  
- Provide **sticky notes** and **sharpies**.  

For **virtual sessions**:  
- Ensure **everyone is comfortable** with tools like **Miro or Mural**.

> **"Leave some empty space before the trigger—unexpected preconditions often arise."**  
> Over-planning the space **can be limiting**, so maintain flexibility.

**Key Takeaway:**  
The **right setup fosters collaboration** and **keeps the process fluid**.

---

### **2.7. The Invitation**  

**"Who should be involved in an EventStorming session?"**  
A **diverse mix** of **business and technical people** ensures a **comprehensive perspective**.

> **"Subject matter experts, users, business analysts, and developers all have unique insights."**  
> Stakeholders from **different roles** enrich discussions.

**Key Takeaway:**  
A **diverse mix of participants** ensures **holistic domain understanding**.

---

### **2.8. Getting Started**  

**"Brainstorming should begin as soon as possible."**  
Initial steps include:  
1. **Participants write down events independently.**  
2. **Sticky notes are placed on the timeline chaotically.**  
3. **Facilitators encourage sequencing and discussion.**  

> **"The chaos of ideas eventually leads to structured understanding."**  
> **Allow disorder** before refining structure.

**Key Takeaway:**  
**Encourage rapid contributions** before organizing.

---

### **2.9. Things to Avoid**  

**"Common pitfalls can derail an EventStorming session."**  

1. **Over-facilitation** – Let participants explore **without too much control**.  
2. **Getting stuck in details** – Capture **questions as hot spots** rather than debating.  
3. **Forcing a structure too soon** – **Let the natural flow emerge** first.  

> **"Trying to make it perfect too early kills creativity."**  
> **First, generate ideas—then refine.**  

**Key Takeaway:**  
Allow **messiness in the beginning**, **focus on discovery**, and **refine later**.

---

### **Final Thoughts**  
**"Your first EventStorming session is an adventure into complexity."**  
By following these principles:  
- Start with **familiar examples**.  
- Encourage **broad exploration** before refinement.  
- Capture **questions and unknowns openly**.  
- Structure **emerges naturally**—don’t force it too soon.  

> **"Embrace the chaos—it leads to insight."**  

This approach ensures **effective collaboration, deeper understanding, and better decision-making**.


# unsorted

---

## **Part 1: Understanding EventStorming**
### **1. What Does EventStorming Look Like?**
- **Challenging Corporate Processes**: How EventStorming exposes inefficiencies in large organizations.
- **Kicking Off a Startup**: Applying EventStorming for new business ventures to map out workflows.
- **Designing a New Feature for a Web App**: Using EventStorming to define new functionality.
- **Quick EventStorming in Avanscoperta**: A real-world example of how the author used EventStorming for problem-solving.

---

### **2. A Closer Look at the Problem Space**
- **Silos**: How organizations naturally evolve into silos and their impact on efficiency.
- **Targets and Goals**: The issue with management-driven goal-setting processes.
- **Decisions’ Lifecycle**: Understanding how decisions evolve within a business.
- **The Cost of Agreeing**: Challenges of achieving alignment in complex systems.
- **Putting Everything Together**: Synthesizing the key issues that EventStorming addresses.

---

### **3. Pretending to Solve the Problem by Writing Software**
- **It’s Not About Delivering Software**: Why traditional software development often fails to address real business problems.
- **The Illusion of the Underlying Model**: Misconceptions about software modeling.
- **The Product Owner Fallacy**: Issues with relying solely on a product owner.
- **The Backlog Fallacy**: Challenges with backlog-driven development.
- **EventStorming Approach**: A better way to model complex domains.

---

## **Part 2: Running Effective EventStorming Workshops**
### **4. Running a Big Picture Workshop**
- **Inviting the Right People**: Ensuring diverse perspectives.
- **Room Setup**: Creating an optimal physical environment.
- **Workshop Structure**: Phases of the Big Picture Workshop:
  - Kick-off
  - Chaotic Exploration
  - Enforcing the Timeline
  - Identifying People and Systems
  - Discovering Problems and Opportunities
  - Selecting Key Issues to Solve
  - Summarizing the Structure

---

### **5. Playing with Value**
- **Explore Value**: Identifying key value drivers in business processes.
- **Explore Purpose**: Understanding why processes exist.
- **When Should We Apply This Step?**: Situations where value exploration is critical.

---

### **6. Discovering Bounded Contexts with EventStorming**
- **Why Bounded Contexts Are Critical**: Aligning business logic with technical solutions.
- **Finding Bounded Contexts**: Methods for discovery.
- **Structure of a Big Picture Workshop**: The importance of event-driven discovery.
- **Homework Time**: Assigning follow-up tasks.
- **Putting Everything Together**: Synthesizing results.

---

### **7. Making It Happen**
- **Managing Participants’ Experience**: How to keep engagement high.
- **Managing Conflicts**: Handling disagreements during workshops.

---

### **8. Preparing the Workshop**
- **Choosing a Suitable Room**: How to select a space.
- **Providing an Unlimited Modeling Surface**: Using large-scale visualization.
- **Managing Invitations**: Ensuring the right people attend.

---

### **9. Workshop Aftermath**
- **Cooperating Domains**: Understanding domain relationships.
- **When to Stop?**: Knowing when the model is “good enough.”
- **How Do We Know We Did a Good Job?**: Measuring success.
- **Managing the Big Picture Artifact**: Documentation strategies.
- **Focusing on the Hot Spot**: Prioritizing critical areas.

---

### **10. Big Picture Variations**
- **Software Project Discovery**: Adapting EventStorming for software planning.
- **Organizational Retrospective**: Using EventStorming to analyze past performance.
- **Induction for New Hires**: Training employees through domain exploration.

---

### **11. Big Picture in Remote Mode**
- **Main Changes**: Adapting workshops for remote teams.
- **What Role for a Big Picture?**: Why this workshop is still useful remotely.
- **Patterns for Remote Big Picture**: Techniques for online facilitation.
- **Do We Have a Recipe?**: Strategies for running virtual EventStorming sessions.

---

## **Part 3: Advanced Concepts and Implementation**
### **12. What Software Development Really Is**
- **Software Development is Writing Code**
- **Software Development is Learning**
- **Software Development is Making Decisions**
- **Software Development is Waiting**

---

### **13. Process Modeling as a Cooperative Game**
- **Context**
- **Game Goals**
- **Applying Game Strategies**

---

### **14. Process Modeling Building Blocks**
- **Fuzziness vs. Precision**
- **The Picture That Explains Everything**
- **Key Modeling Elements**:
  - Events
  - Commands
  - People
  - Systems
  - Policies
  - Read Models
  - Value
  - Hotspots

---

### **15. Process Modeling Game Strategies**
- **Kicking Off**
- **Mid-game Strategies**
- **Team Dynamics**
- **Are We Done?**

---

### **16. Observing Global State**
- **The Transaction Obsession**
- **Understanding System Consistency Beyond the Obvious**

---

### **17. Running a Design-Level EventStorming**
- **Scope and Participants**
- **Using the Big Picture Artifact**
- **Where Are Events Coming From?**
- **Discovering Aggregates**
- **Determining When You’re Done**

---

### **18. Design-Level Modeling Tips**
- **Making Alternatives Visible**
- **Choosing Later**
- **Picking the Right Problem**
- **Refining the Model**

---

### **19. Building Blocks**
- **Why Domain Events Are Special**
- **Events as State Transitions**
- **Commands, Actions, and Decisions**

---

### **20. Modeling Aggregates**
- **Discovering Aggregates**
- **Best Practices for Aggregate Modeling**

---

### **21. Event Design Patterns**
- **Discovery Strategies**
- **Composite Domain Events**

---

### **22. From Paper Roll to Working Code**
- **Managing EventStorming Artifacts**
- **Coding ASAP**

---

### **23. From EventStorming to User Stories**
- **EventStorming & User Story Mapping**
- **Defining Acceptance Criteria**
- **Combining the Two Approaches**

---

### **24. Working with Startups**
- **Focus Beyond the App**
- **Leveraging the Wisdom of the Crowd**
- **Exploring Multiple Business Models**

---

### **25. Working in a Corporate Environment**
- **Managing the Check-in Process**
- **Handling Corporate Dysfunction**

---

### **26. Designing a Product**
- **Matching Expectations**
- **Simplicity on the Outside, Complexity Within**

---

### **27. Model Storming**
- **Extending EventStorming for More Use Cases**

---

### **28. Remote EventStorming**
- **Handling Remote Collaboration Challenges**

---

### **29-31. Patterns and Anti-Patterns**
- **Effective Strategies**
- **Common Pitfalls to Avoid**

---

### **32-34. Specific EventStorming Formats**
- **Big Picture EventStorming**
- **Design-Level EventStorming**
- **Next Steps and Future Research**

---

## **Final Sections**
- **Glossary**
- **Tools for EventStorming**
- **Bibliography**

Here is a detailed outline of *The EventStorming Handbook: Unlocking Creativity, Collaboration, and Communication for Your Teams* by Paul Rayner:

---

### **About This Book**
- **Purpose**: A concise, actionable guide for facilitating EventStorming sessions.
- **Target Audience**: Beginners looking for a quick start in EventStorming and facilitators seeking practical guidance.
- **Author**: Paul Rayner, a developer, coach, and instructor specializing in Domain-Driven Design (DDD) and EventStorming.

---

## **Part I - Ingredients** (Fundamentals of EventStorming)

### **1. What is EventStorming?**
1.1. *Some Worthy Goals*  
   - Understanding business processes.  
   - Identifying opportunities for automation and streamlining.  
   - Aligning stakeholders and breaking down silos.  
   - Supporting software design by modeling domain complexity.  

1.2. *The Shape of EventStorming*  
   - Visualizing processes with domain events.  
   - Structuring information along a timeline.  

1.3. *How I Started*  
   - Author's first experience using EventStorming for problem-solving.  

1.4. *Visualizing the Invisible*  
   - How EventStorming helps uncover hidden complexities in business processes.  

---

### **2. Your First EventStorming Session**
2.1. *Show an Example*  
   - Using simple examples (e.g., a movie-going experience) to explain concepts.  

2.2. *Happily Ever After*  
   - Icebreaker exercise: retelling stories like *Cinderella* using EventStorming.  

2.3. *Start with Events*  
   - Focusing on business events before introducing other elements.  

2.4. *Capturing Questions*  
   - Collecting uncertainties and questions for future discussion.  

2.5. *How to Start?*  
   - Steps for setting up a first EventStorming session.  

2.6. *Setting Up the Modeling Space*  
   - Physical and virtual space preparation.  

2.7. *The Invitation*  
   - How to invite the right mix of participants.  

2.8. *Getting Started*  
   - Initial brainstorming and structuring techniques.  

2.9. *Things to Avoid*  
   - Common mistakes that derail an EventStorming session.  

---

### **3. Facilitation Basics**
3.1. *Playing the Game*  
   - Treating EventStorming as an interactive learning experience.  

3.2. *Intentional Discovery*  
   - Encouraging diverse perspectives and collaborative problem-solving.  

3.3. *Open at the Close*  
   - Structuring discussions to keep engagement high.  

3.4. *Tips and Tricks*  
   - Practical advice for facilitators.  

3.5. *Dealing with Challenges*  
   - Managing difficult participants, conflicts, and lack of engagement.  

---

### **4. Emerging Structure**
4.1. *Key Events*  
   - Identifying critical moments in a business process.  

4.2. *Milestones*  
   - Recognizing significant transitions in workflows.  

4.3. *Alternate Paths*  
   - Mapping different scenarios and edge cases.  

4.4. *Themes*  
   - Organizing events into meaningful clusters.  

4.5. *Facilitation Tips*  
   - More advanced techniques for guiding workshops.  

4.6. *How to Handle Loops*  
   - Managing circular dependencies and iterative processes.  

4.7. *Emergent Software Boundaries*  
   - Discovering bounded contexts for software design.  

4.8. *Domain Distillation*  
   - Refining domain models based on EventStorming insights.  

4.9. *Bounded Contexts*  
   - Aligning domain concepts with software architecture.  

---

### **5. Actors and Systems**
5.1. *Interactions with People*  
   - Understanding human roles in a business process.  

5.2. *Systems*  
   - Mapping external and internal system interactions.  

5.3. *Sociotechnical Vision*  
   - Combining people, processes, and technology for better decision-making.  

5.4. *SEP Fields*  
   - Separating the essential from the extraneous.  

---

### **6. Walking the Narrative**
6.1. *Why Walk?*  
   - Reviewing and validating workflows through storytelling.  

6.2. *Telling the Story*  
   - Structuring the workshop as a collaborative narrative.  

6.3. *A Sample Story*  
   - Example of using EventStorming to tell a business process story.  

---

### **7. Documenting Language**
7.1. *Exposing Language Messiness*  
   - Identifying inconsistent terminology.  

7.2. *Capturing Critical Concepts*  
   - Standardizing terms to improve communication.  

---

### **8. Policies and Decisions**
8.1. *Making Constraints Explicit*  
   - Documenting rules and policies.  

8.2. *Magic Happens*  
   - Understanding implicit decision points.  

8.3. *What Else Can Happen?*  
   - Exploring alternative scenarios.  

8.4. *Decisions*  
   - Clarifying decision-making processes.  

---

### **9. Visualizing Experiences**
9.1. *Data*  
   - How to integrate data flows into EventStorming.  

9.2. *Mockups*  
   - Creating prototypes based on insights.  

---

### **10. Visualizing Value**
10.1. *Types of Value*  
   - Identifying where business value is created or lost.  

10.2. *Talking About Value*  
   - Aligning stakeholders on what matters most.  

---

### **11. Opportunities**
11.1. *Ideation*  
   - Generating ideas for improvement.  

11.2. *Walkthrough*  
   - Reviewing opportunities through EventStorming artifacts.  

11.3. *Voting*  
   - Prioritizing ideas as a team.  

11.4. *Moving from Ingredients to Recipes*  
   - Transitioning from discovery to implementation.  

---

## **Part II - Recipes** (Practical Applications)

### **12. Exploring the Big Picture**
   - Large-scale process mapping for strategic decisions.  

### **13. Exploring a Business Process Solution**
   - Using EventStorming to refine business operations.  

### **14. Exploring Focus and Flow**
   - Visualizing workflow inefficiencies and improvements.  

---

## **Part III - Cooking** (Advanced Facilitation)

### **15. In-Person or Virtual?**
   - Adapting EventStorming for remote and hybrid settings.  

### **16. Next Steps**
   - Implementing insights from EventStorming sessions.  

### **17. Resources for Further Learning**
   - Additional reading on EventStorming, DDD, and facilitation.  

---

# Quotes

# References
