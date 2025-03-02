---
title: introducing event storming by Alberto Brandolini summary
date: "2025-03-02T22:12:03.284Z"
description: "introducing event storming by Alberto Brandolini summary"
tags: ["domaindrivendesign", "design"]
---

# Table of Contents

```toc
exclude: Table of Contents
tight: false
from-heading: 1
to-heading: 6
class-name: "table-of-contents"
```

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


# **Running Effective EventStorming Workshops**

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


Here’s a **detailed expansion** of **"Facilitation Basics"** from *EventStorming Handbook*, with **bold highlights** of key phrases and **insightful quotes**.

---

## **Facilitation Basics**  

> **"A facilitator’s job is to support everyone to do their best thinking."** – *Sam Kaner, Facilitator’s Guide to Participatory Decision Making*  

EventStorming facilitation requires **balancing structure with openness**, ensuring **productive conversations** while **allowing for unexpected discoveries**.

---

### **3.1. Playing the Game**  

> **"It can be helpful to think of collaborative, participatory sessions as games."**  

EventStorming follows a **game-like structure**:
1. **Opening:** Generating ideas freely.  
2. **Exploration:** Expanding on ideas, discovering patterns.  
3. **Closing:** Converging towards decisions and action items.

> **"If you struggle with opening, focus on getting ideas flowing without judgment. If you struggle with closing, work backward from what a successful outcome looks like."**  

Facilitators should **embrace the playfulness of exploration** while ensuring the **session remains purposeful**.

---

### **3.2. Intentional Discovery**  

> **"Facilitating the EventStorming game well is fundamentally about enabling people to experience intentional discovery."**  

EventStorming is not just about **capturing what’s already known**, but **creating an environment where new insights emerge**.

Key aspects:
- **Encourage diverse perspectives.**  
- **Avoid premature convergence.**  
- **Embrace ambiguity before narrowing down.**  

> **"Suspend judgment and maintain creative tension as long as necessary."**  

The **"wisdom of the crowd"** becomes evident when **everyone’s ideas integrate into a larger whole**.

---

### **3.3. Open at the Close**  

> **"Begin with the end in mind."**  

A well-structured **opening and closing** are crucial.  
**Common mistakes** facilitators make:
1. **Jumping to conclusions too early.**  
2. **Closing discussions before ideas fully form.**  
3. **Rushing the final insights.**  

> **"If you struggle with closing well, work backwards from a successful ending."**  

Keeping **momentum high** ensures **participants remain engaged** through the **entire process**.

---

### **3.4. Tips and Tricks**  

> **"The best facilitators adapt."**  

**Effective facilitation techniques**:
- **Use timeboxing.** Keep discussions **on track**.  
- **Encourage “Yes, and…” thinking.** Avoid **shutting down ideas too soon**.  
- **Sketch out key concepts.** **Visual representations** help cement ideas.  

> **"Quit while the interest is high."**  

Better to end a **session with high engagement** than **dragging it out until exhaustion**.

---

### **3.5. Dealing with Challenges**  

> **"Facilitators must navigate conflicts, dominant voices, and disengaged participants."**  

Key strategies:
- **Handling dominant voices:** Redirect the conversation, ask quieter participants for input.  
- **Managing disengagement:** Use **breakout groups** to encourage participation.  
- **Addressing unclear goals:** Clearly **define objectives upfront**.  

> **"Your goal is to create a safe place for exploration and learning—not to impress everyone with your expertise."**  

A good **facilitator fosters collaboration, ensures learning, and navigates conflicts constructively**.

---

### **Final Thoughts**  

> **"Embrace the process—structured enough for direction, open enough for discovery."**  

The **best facilitators** maintain a balance of **guidance and flexibility**, **helping participants unlock new insights** while **ensuring discussions remain productive**.


Here’s a **detailed expansion** of **"Emerging Structure"** from *EventStorming Handbook*, with **bold highlights** of key phrases and **critical insights**.

---

## **Emerging Structure**  

> **"A chaotic collection of events is only the beginning—structure must emerge."**  

EventStorming starts as an **exploration of events**, but as patterns appear, **structure emerges naturally**. This structure helps teams **organize workflows, find dependencies, and improve system understanding**.

---

### **4.1. Key Events**  

> **"Key events signal a pivotal change in the narrative."**  

Key events are significant moments in a business process, often marking **shifts in responsibility or state**. For example:
- **In sales**, a key event might be **"Contract Signed"**, shifting responsibility from **Sales to Fulfillment**.  
- **In e-commerce**, a key event could be **"Payment Processed"**, leading to order fulfillment.

> **"We also look for highly duplicated events or marked changes in language as clues that indicate key events."**  

**Key events serve as structural anchors** in the EventStorming timeline. **Teams use them as boundaries to break processes into meaningful chunks**.

---

### **4.2. Milestones**  

> **"Milestones drive the process forward—they are deadlines, not events."**  

Milestones mark **date-driven deadlines** rather than system events. **For example**:
- **A product launch** may have milestones like **"Beta Released," "Marketing Campaign Launched," "Public Release."**  
- **A conference** has milestones for **speaker confirmations, venue booking, and ticket sales deadlines**.

> **"The most interesting learning in the conversation about a milestone is typically triggered when you ask, ‘What happens if this milestone is missed?’"**  

Teams should explore **failure scenarios** around milestones. **Missed deadlines** often reveal **hidden bottlenecks**.

---

### **4.3. Alternate Paths**  

> **"Not all processes follow a single happy path—alternate paths must be explored."**  

To represent **different experiences and subprocesses**, **swimlanes** help differentiate:
- **Customer vs. backend processes** (e.g., ordering vs. order fulfillment).  
- **Automated vs. manual workflows** (e.g., **"Order Approved Automatically"** vs. **"Manual Review Required"**).  
- **Success vs. failure outcomes** (e.g., **"Payment Processed"** vs. **"Payment Failed"**).

> **"Swimlanes make it easier to visualize dependencies and handoffs."**  

By mapping **alternate flows**, teams **proactively identify failure points and inefficiencies**.

---

### **4.4. Themes**  

> **"Some patterns appear repeatedly across the timeline—these should be treated as themes."**  

A **theme** is a set of related events that **cut across different parts of the process**, such as:
- **Security** – Login, authentication, authorization checks.  
- **Monitoring** – Logging, tracking, error handling.  
- **Compliance** – Data retention, auditing, approvals.

> **"Themes should be extracted to reduce clutter and improve focus on the primary workflow."**  

By grouping **related but secondary concerns**, **EventStorming improves clarity**.

---

### **4.5. Facilitation Tips**  

> **"A facilitator's role shifts from generating discussion to guiding structure."**  

Facilitators should:
- **Introduce key events first** before diving into details.  
- **Encourage participants to move and group events** to find emerging patterns.  
- **Use colors or lines** to differentiate structural elements like swimlanes, milestones, and themes.

> **"For people who love structure, this stage can be a big relief!"**  

As structure emerges, **some participants feel more comfortable**, while **others might struggle with too much organization**—**balance is key**.

---

### **4.6. How to Handle Loops**  

> **"Circular dependencies and feedback loops can cause confusion—make them explicit."**  

Some processes naturally loop, such as:
- **Customer support tickets** → **Ticket opened → Assigned → Resolved → Reopened**.  
- **Subscription billing** → **Renewal reminders → Payment → Expiry → Renewal attempt**.

> **"Loops should be visualized, but too many connections can clutter the timeline."**  

Facilitators should:
- **Use color-coded connections** to indicate feedback loops.  
- **Minimize excessive arrows** to keep the timeline readable.  
- **Label repetitive cycles** to avoid unnecessary complexity.

---

### **4.7. Emergent Software Boundaries**  

> **"Business concepts naturally form clusters—these suggest potential software boundaries."**  

Patterns like:
- **Recurring terms** in different areas → **Possible service boundaries**.  
- **Distinct roles handling different parts of the process** → **Microservices alignment**.  
- **Changes in terminology** between sections → **Different bounded contexts**.

> **"Watch for where language shifts—this is where software domains divide."**  

If **Sales talks about "Leads"** but **Marketing calls them "Prospects"**, this indicates **a potential domain boundary**.

---

### **4.8. Domain Distillation**  

> **"The messiness of the timeline hides the essence of the business domain—distillation extracts what really matters."**  

Once a rough structure is in place, teams should:
- **Remove noise** (redundant, low-impact events).  
- **Prioritize key moments** (decisions, handoffs, failure points).  
- **Refine terminology** to align with business language.

> **"Domain distillation helps clarify what the business actually does—not just what the current system does."**  

This step **bridges the gap between current processes and optimal workflows**.

---

### **4.9. Bounded Contexts**  

> **"Bounded contexts are the ultimate structural insight from EventStorming."**  

> **"Every time we see a shift in language or process ownership, we might have found a new bounded context."**  

By mapping **emerging business domains**, teams:
- **Discover the natural decomposition of complex systems**.  
- **Find areas where different teams need autonomy**.  
- **Align EventStorming insights with software architecture**.

> **"Bounded contexts define the edges of microservices, data ownership, and team responsibilities."**  

**Clear boundaries prevent unnecessary coupling**, allowing teams to **design resilient systems**.

---

### **Final Thoughts**  

> **"Emerging structure transforms chaos into insight."**  

By letting structure **naturally emerge**, **EventStorming uncovers how business processes truly work**—not just how they were assumed to work.

> **"Key events, milestones, alternate paths, and themes bring order to complex workflows."**  

These **patterns help teams navigate ambiguity**, ensuring **clearer models, better software, and improved collaboration**.


## **Exploring the Big Picture**  

> **"A Big Picture EventStorming session is a powerful tool for understanding the full complexity of a business process across teams, departments, and systems."**  

A **Big Picture EventStorming workshop** helps organizations **gain a high-level understanding of their current landscape**, **visualize key system interactions**, and **identify areas for improvement**. 

---

### **Why Explore the Big Picture?**  

A Big Picture session **uncovers the broader context behind business operations**, ensuring that **all stakeholders share a unified view of how work gets done**. Key outcomes include:  

- **"Broad understanding of a process that transcends departments, roles, and responsibilities."**  
- **"Visualizing emergent system and organizational boundaries and responsibilities."**  
- **"Highlighting problems, risks, gaps, and bottlenecks."**  
- **"Prioritizing new software development efforts and validating/challenging existing ones."**  

This workshop format is especially useful when organizations **struggle with unclear handoffs, inefficient workflows, and misaligned development efforts**.

---

### **Key Challenges That Big Picture EventStorming Solves**  

A **Big Picture workshop** is particularly effective at addressing:  

- **Problems with organizational handoffs** – Where work transitions from one team or system to another, but inefficiencies or miscommunications cause bottlenecks.  
- **Difficulties in seeing the entire value stream** – Business processes often **span multiple teams, systems, and roles**. This workshop helps visualize those interactions.  
- **Lack of shared understanding** – Teams often have **different interpretations of processes**, leading to misaligned efforts.  
- **Prioritization challenges** – Helps teams **distinguish between core, supporting, and differentiating capabilities**, ensuring focus on **what truly adds value**.  

> **"A high-level map of the existing terrain is critical before charting a journey towards improvement."**  

Understanding the **current state** is a necessary step **before attempting to design an improved future state**.

---

### **Big Picture Workshop Structure**  

> **"The structure of a Big Picture EventStorming workshop follows a logical flow—from initial chaos to meaningful insights."**  

#### **Step 1: Chaotic Exploration**  
- Participants **dump all relevant events** onto the timeline **without worrying about order or consistency**.  
- Different roles contribute **their knowledge**—which **uncovers gaps and inconsistencies** in understanding.  
- This step **is often silent**, as participants focus on **getting everything out of their heads and onto the board**.  

> **"Nobody knows the full picture. The workshop reveals hidden dependencies, unknown bottlenecks, and conflicting perspectives."**  

#### **Step 2: Emergent Structure**  
- Patterns **naturally emerge** as participants **group related events, highlight key transitions, and sequence workflows**.  
- **Critical milestones and dependencies become clear**, exposing **where processes break down**.  

> **"Clarity emerges as the team organizes the chaos into meaningful categories and sequences."**  

#### **Step 3: Identifying Actors and Systems**  
- Teams **map responsibilities** to **specific roles and systems**, making it clear **who does what**.  
- **Swimlanes** can separate **departments, automation vs. manual processes, and system interactions**.  

> **"Teams often uncover redundant work, unnecessary handoffs, and areas where automation could dramatically improve efficiency."**  

---

### **Facilitation Tips for a Big Picture Session**  

> **"Facilitating a Big Picture workshop requires guiding participants from initial information overload to structured insights."**  

- **Encourage broad participation** – Get **subject matter experts, developers, business leaders, and operational staff in the same room**.  
- **Focus on discovery first, structure later** – Let **the full complexity emerge before attempting to clean it up**.  
- **Ask ‘What happens next?’ or ‘What happens if this fails?’** – This exposes **hidden dependencies and critical decision points**.  

> **"Uncovering failure points is just as important as mapping the happy path."**  

- **Use different colors for different elements** – **Events, questions, risks, decisions, and handoffs** should be visually distinct.  
- **Don’t rush conclusions** – The **biggest insights often come later** in the session, once structure begins to emerge.  

---

### **Outcomes and Next Steps**  

By the end of a **Big Picture EventStorming session**, teams typically gain:  

- **A shared understanding of end-to-end workflows.**  
- **Clarity on inefficiencies and bottlenecks.**  
- **Alignment on where to prioritize changes.**  
- **A foundation for deeper exploration into software and organizational improvements.**  

> **"It is a quick and effective method for defining and visualizing a problem space, and identifying potential opportunities."** – *Workshop Attendee Response*.  

### **Inviting the Right People**  

> **"To run a successful workshop, you need the right mix of knowledge and curiosity—but most importantly, people who care about the problem."**  

A **Big Picture Workshop** should include **key stakeholders** who have **both domain knowledge and decision-making authority**. These may include:  

- **Business Experts** – Those who understand the **domain processes and rules**.  
- **Technical Experts** – Engineers and developers who **build and maintain the systems**.  
- **Operations & Support Staff** – Those who **handle real-world exceptions and failures**.  
- **Executives or Decision-Makers** – Those who **fund and approve changes**.  

> **"Getting all these people in the same room is a challenge, but it’s the only way to uncover hidden contradictions and inefficiencies."**  

Having **only developers or only business leaders** leads to **blind spots**, so **diversity in participation is crucial**.  

---

### **Room Setup**  

> **"Your meeting room is your battleground—if it’s set up like a typical meeting, you’ve already lost."**  

A **traditional conference table setup** kills collaboration. Instead, the room should be **open, flexible, and encourage movement**.  

#### **Key Setup Considerations:**  
- **Unlimited modeling surface:** Use a **long, straight wall** (8+ meters) for sticky notes.  
- **Plenty of space:** Avoid crammed setups—people need room to move.  
- **Minimal furniture:** **Remove chairs** initially to prevent passive engagement.  
- **Color-coded sticky notes & markers:** Have enough for **everyone to contribute freely**.  
- **Healthy snacks & drinks:** Workshops are mentally demanding—keep participants energized.  

> **"Don’t let corporate habits take over—people will instinctively sit down, open laptops, and disengage if you let them."**  

A **disruptive room setup** signals that **this is not just another meeting**.  

---

### **Workshop Structure**  

> **"The workshop unfolds in a series of structured phases, each serving a unique purpose—starting with chaos and gradually leading to clarity."**  

The **Big Picture Workshop** follows **a logical sequence of activities** designed to **extract insights progressively**.  

---

#### **Phase 1: Kick-off**  

> **"We are going to explore the business process as a whole by placing all relevant events along a timeline. We’ll highlight ideas, risks, and opportunities along the way."**  

The **facilitator** sets the tone by:  
1. **Introducing the objective** – Understanding the **big picture of a business process**.  
2. **Explaining the format** – Letting participants know **the workshop will be chaotic** but **highly productive**.  
3. **Encouraging participation** – Reinforcing that **there are no wrong answers**.  

> **"Some people may feel uncomfortable at first—reassure them that chaos is part of the process."**  

Avoid **long explanations**—get into action **as quickly as possible**.  

---

#### **Phase 2: Chaotic Exploration**  

> **"The first phase is about dumping everything participants know onto the wall, without structure."**  

- **Each participant writes domain events** on sticky notes **independently**.  
- **Participants place sticky notes onto the timeline** in **no particular order**.  
- **No filtering, no discussing—just rapid output.**  

> **"The model will start messy, with redundant notes, out-of-sequence events, and some unreadable scribbles—but that’s expected."**  

At first, this phase will feel **like total anarchy**—but it’s **essential** to **extract deep domain knowledge quickly**.  

---

#### **Phase 3: Enforcing the Timeline**  

> **"After the initial chaos, we start making sense of the mess."**  

Now, the group:  
1. **Reorders events into a more logical sequence**.  
2. **Merges duplicate or conflicting notes**.  
3. **Highlights dependencies and missing events**.  

> **"This is where inconsistencies emerge—different teams may have very different understandings of how things work."**  

The facilitator helps resolve **contradictions and disagreements**, ensuring the timeline **makes sense across teams**.  

---

#### **Phase 4: Identifying People and Systems**  

> **"Events don’t just happen—people and systems make them happen."**  

At this stage, the group:  
- **Assigns roles (actors) to each event** – Who triggers or handles it?  
- **Maps out supporting systems** – What software, tools, or databases are involved?  

> **"This phase exposes gaps—who is actually responsible for what? Where do handoffs cause delays?"**  

This step **aligns domain understanding with system reality**, **bridging the gap between business and technology**.  

---

#### **Phase 5: Discovering Problems and Opportunities**  

> **"Once we see the whole workflow, the pain points become obvious."**  

Participants **highlight key issues**, such as:  
- **Bottlenecks** – Where do processes get stuck?  
- **Rework & inefficiencies** – Where do unnecessary steps exist?  
- **Hidden risks** – Where do failures, errors, or compliance issues arise?  

> **"These hotspots are often surprising—even to experts who thought they understood the system."**  

Capturing **issues visually** helps teams **prioritize what needs to be fixed**.  

---

#### **Phase 6: Selecting Key Issues to Solve**  

> **"Not all problems are equal—some are urgent, others are secondary."**  

The team now:  
1. **Votes on the most critical issues** to address.  
2. **Clusters related problems** to find **systemic patterns**.  
3. **Identifies quick wins** versus **long-term transformations**.  

> **"This phase transforms the workshop from analysis to decision-making."**  

By focusing on **high-impact areas**, teams ensure **follow-up actions are meaningful**.  

---

#### **Phase 7: Summarizing the Structure**  

> **"By the end, we have a structured model that represents our business reality."**  

A **Big Picture EventStorming outcome includes**:  
- A **visualized business process** with clear **dependencies and responsibilities**.  
- A **list of key problems and opportunities**.  
- A **prioritized action plan for next steps**.  

> **"This is not just a workshop—it’s the first step toward meaningful change."**  

Teams should **document insights** and **assign ownership** for next steps.  

---

### **Final Thoughts**  

> **"Big Picture EventStorming reveals the truth about how a business actually operates—often exposing hidden complexities that no one person fully understands."**  

This method is **powerful for aligning teams**, **breaking down silos**, and **identifying real-world inefficiencies**. **When run well, it can shape strategic decisions and unlock transformative improvements**.

> **"A Big Picture workshop transforms uncertainty into clarity, revealing the true nature of complex workflows."**  

It is **not just about process mapping**—it is about **building a shared narrative, discovering hidden inefficiencies, and aligning teams on what truly matters**.


## **Discovering Bounded Contexts with EventStorming**  

> **"Bounded contexts are a core principle of Domain-Driven Design (DDD), yet many teams struggle to define them effectively. EventStorming offers a collaborative approach to discovering the natural boundaries within a business domain."**  

This section explains **why bounded contexts matter**, how to **discover them using EventStorming**, and how to **translate these insights into actionable software design decisions**.  

---

### **Why Bounded Contexts Are Critical**  

> **"Getting the boundaries right is the single design decision with the most significant impact over the entire life of a software project."**  

Bounded contexts **separate different models** within a system, ensuring that each part of the business operates independently where necessary. Without clear boundaries, software **becomes overly complex, slow to change, and resistant to scaling**.  

#### **Symptoms of Poorly Defined Bounded Contexts**  
- **Overlapping concepts create ambiguity** – e.g., an "Order" in **sales**, **logistics**, and **finance** may mean different things but share the same model.  
- **Security and access issues arise** – Different roles need access to **parts** of the same data, but not all of it.  
- **Changes become risky** – Every modification affects multiple departments, requiring excessive **coordination and approvals**.  
- **Technical debt builds up** – As changes become harder, **workarounds replace well-designed solutions**.  
- **Refactoring is postponed indefinitely** – Business value is hard to quantify, so **developers deprioritize cleanup**.  

> **"A poor domain model slows down the business. A well-defined set of bounded contexts accelerates innovation."**  

By identifying **clear boundaries**, teams can **prevent dependencies from spiraling out of control**.  

---

### **Finding Bounded Contexts**  

> **"A bounded context should contain a model tailored around a specific purpose—the perfectly shaped tool for one specific job."**  

EventStorming **helps uncover natural boundaries** by looking at:  
1. **Diverging language use** – Different departments describe the same concept differently.  
2. **Pivotal business events** – Critical moments where **ownership shifts** across teams.  
3. **Actors involved** – Who interacts with which parts of the system?  
4. **Failure scenarios** – When things go wrong, where does responsibility shift?  

#### **Heuristics for Identifying Bounded Contexts**  
- **Look at the swimlanes** – Different flows often indicate separate contexts.  
- **Follow the experts** – Where domain experts **naturally congregate** in a session **signals distinct business concerns**.  
- **Observe body language** – When participants **disagree** on terminology, it suggests **context misalignment**.  
- **Find where terms change meaning** – If "Customer" means **a buyer in sales** but **a debtor in accounting**, **those are separate models**.  

> **"If two models serve different purposes, they should be separate bounded contexts."**  

By **grouping related events into clear domains**, EventStorming helps **avoid tangled dependencies**.  

---

### **Structure of a Big Picture Workshop**  

> **"EventStorming makes bounded contexts visible through emergent structure."**  

A **Big Picture EventStorming workshop** naturally reveals how different parts of the business interact. The **phases of the workshop** help expose boundaries through:  

1. **Chaotic exploration** – Participants **brainstorm events without structure**.  
2. **Organizing events into sequences** – Finding **dependencies and handoffs**.  
3. **Adding actors and systems** – Who triggers and processes each event?  
4. **Discovering pain points** – Where do **bottlenecks and misunderstandings occur**?  
5. **Distilling bounded contexts** – Where **language, responsibility, or process changes**, a **context boundary exists**.  

> **"Bounded contexts don’t emerge instantly—they become clearer as patterns appear."**  

A **well-run EventStorming session helps teams define software boundaries in a way that reflects real-world business needs**.  

---

### **Homework Time**  

> **"Once the workshop is over, the real work begins—translating insights into an actionable domain model."**  

After the session, teams should:  
- **Review and refine the context map** – Identify gaps and **refactor boundaries** where necessary.  
- **Prioritize domain modeling discussions** – Clarify terms, **remove ambiguity**, and **align expectations**.  
- **Document system interactions** – Define **integration points** between bounded contexts.  
- **Identify areas for improvement** – Highlight **technical debt and inefficiencies** exposed by the workshop.  

> **"A well-defined bounded context is a foundation for scalable, maintainable software."**  

---

### **Putting Everything Together**  

> **"Bounded contexts are the key to sustainable software—EventStorming helps teams find them before they become a problem."**  

By synthesizing the results of a **Big Picture EventStorming session**, teams can:  
- **Clarify business processes and dependencies**.  
- **Ensure software reflects real-world needs**.  
- **Improve communication between business and technical teams**.  

> **"EventStorming provides a shared understanding—ensuring that teams build software that actually works for the business."**  

With **clear bounded contexts**, teams **reduce complexity, improve scalability, and foster innovation**.


## **Modeling Aggregates**  

> **"In Domain-Driven Design, Aggregates are defined as units of transactional consistency."**  

Aggregates **group objects whose state can change** but must always **maintain consistency** as a whole. They enforce **business rules**, ensuring that critical **invariants remain true** across operations.  

A **common example** is a **ShoppingCart** in an online store:  
- It **must maintain a valid subtotal** by ensuring that **item prices and quantities remain synchronized**.  
- The subtotal **must always be the sum of each item quantity multiplied by its unit price**.  
- **Allowing updates to a single field (e.g., item count) without adjusting the total would violate consistency**.  

> **"Aggregates define a behavioral contract—they don’t dictate how calculations are performed, just that they must be correct."**  

### **Key Characteristics of Aggregates**  
- **Encapsulation** → They **hide internal details** while exposing only necessary behaviors.  
- **State Consistency** → Business rules must always be enforced within an aggregate boundary.  
- **Transactional Integrity** → **All changes to an aggregate must happen as a single atomic operation**.  

---

### **Discovering Aggregates**  

> **"Looking at data structures is not the best way to find aggregates."**  

A **common mistake** is to **start with database design** rather than **business behavior**. Aggregates should be **discovered through responsibility-driven modeling**, not by **grouping related fields together**.  

#### **Heuristics for Finding Aggregates**  

1. **Focus on responsibilities, not data**  
   - Ask: **"What must remain consistent?"** rather than **"What data should be grouped?"**  
   - Example: A **ShoppingCart** must enforce price totals, but a **ProductCatalog** does not.  

2. **Identify transaction boundaries**  
   - An aggregate should be **updated as a unit**. If a system **requires multiple transactions** to remain consistent, it **may need separate aggregates**.  

3. **Analyze the lifecycle of business objects**  
   - A **Customer** and an **Order** have **different lifecycles**. If a customer **updates their profile**, it **should not affect order history**. This signals that **Customer and Order should be separate aggregates**.  

> **"Aggregates should be modeled around consistency boundaries, not around what ‘looks good’ in a database schema."**  

---

### **Best Practices for Aggregate Modeling**  

> **"The power of aggregates comes from well-defined boundaries, not from complexity."**  

#### **1. Postpone Naming**  
> **"The moment you name something, you bias your design."**  

- Instead of **naming aggregates too soon**, ask:  
  - **What is this responsible for?**  
  - **What business rules must it enforce?**  
  - **What must always be true?**  
- Only after defining **responsibilities and constraints** should you **assign a name**.  

#### **2. Keep Aggregates Small**  
> **"Aggregates should be as small as possible, but no smaller."**  

- **Avoid ‘God Aggregates’** that try to do too much.  
- **Ensure aggregates don’t become bottlenecks**—if every action requires locking a single object, the system won’t scale.  

#### **3. Model Aggregates as State Machines**  
> **"Aggregates often behave like small state machines—transitions must be well-defined."**  

- Think in terms of **state transitions** rather than CRUD operations.  
- Example: A **SeatReservation** aggregate can only transition from **Available → Reserved → Confirmed → Canceled**, with **strict business rules** governing transitions.  

#### **4. Separate Read and Write Models**  
> **"Not all data belongs in an aggregate—some is just for display."**  

- Use **CQRS** (Command-Query Responsibility Segregation) to separate:  
  - **Aggregates** (handling complex business logic).  
  - **Read models** (optimized for fast queries, stored separately).  

#### **5. Design with Event Sourcing in Mind**  
> **"Aggregates that emit events are easier to reason about."**  

- Instead of storing **only the current state**, consider **storing the history of changes** using **Event Sourcing**.  
- Example: Instead of updating an **Order Status** field, record **OrderCreated, PaymentProcessed, OrderShipped** as events.  

---

### **Final Thoughts**  

> **"Aggregates are more than just collections of data—they enforce consistency, define clear responsibilities, and provide transactional boundaries."**  

By **discovering aggregates through behavior**, **enforcing strong consistency rules**, and **keeping them as simple as possible**, teams can **design scalable, maintainable software systems** that align with **real-world business processes**.


## **Event Design Patterns**  

> **"Domain Events are the core storytelling element of EventStorming, but their design can greatly impact the effectiveness of a system."**  

Event design patterns help teams **structure domain events effectively**, ensuring they are **meaningful, consistent, and useful** across a system. This section dives into **strategies for discovering domain events** and **when to use composite domain events**.  

---

### **Discovery Strategies**  

> **"Most significant events have a high fan-out—meaning they impact many downstream systems."**  

#### **How to Identify Important Events?**  
1. **Look for high fan-out events**  
   - Events with **many consumers** are often **more critical than those with only a few**.  
   - Example: A **Ticket Sold** event affects:
     - **Classroom capacity**
     - **Lunch and coffee break logistics**
     - **Loyalty management systems**
     - **Trainer notifications**.  

2. **Listen to downstream systems**  
   - Instead of focusing **only on event producers**, pay attention to **who consumes the event**.  
   - If multiple teams **depend on an event, it may signal a major system interaction**.  

> **"The real value of an event is often better understood by its consumers than by its producers."**  

3. **Distinguish between true domain events and system noise**  
   - Some technical events are **not meaningful in the business domain**.  
   - Example:
     - **User Clicked a Button** ❌ (Too low-level)  
     - **Order Placed** ✅ (A meaningful business event)  

> **"Every event should tell a meaningful part of the business story—if it doesn’t, question its necessity."**  

By **examining how events impact the broader system**, teams can **prioritize the right events** and **avoid modeling unnecessary details**.  

---

### **Composite Domain Events**  

> **"Sometimes, one event isn’t enough to fully capture a business reality—composite domain events help bridge the gap."**  

#### **What Are Composite Domain Events?**  
- A **composite event** is an event that **summarizes multiple domain events**.  
- Useful for **reducing event noise** and **making high-level decisions easier**.  

#### **When to Use Composite Events?**  
1. **When multiple events always occur together**  
   - If an event **always follows another**, a **composite event might simplify the model**.  
   - Example:
     - **Item Added to Cart** + **Cart Updated** → **Cart Item Added**  

2. **When events are too fine-grained for decision-making**  
   - Some events **are necessary for system state but aren’t helpful for high-level decisions**.  
   - Example:
     - Instead of **User Signed Up**, **User Verified Email**, and **User Completed Profile**,  
       use **User Onboarded**.  

> **"Aggregating events into a meaningful unit makes decision-making easier for both business and technical teams."**  

#### **When NOT to Use Composite Events?**  
- **When losing granularity would remove useful context**  
- **When downstream systems need individual events**  
- **When events don’t always occur together**  

> **"Over-aggregating events can obscure the details needed for debugging and analytics."**  

By **striking the right balance**, teams ensure **event-driven systems remain scalable, flexible, and easy to maintain**.  

---

### **Final Thoughts**  

> **"Events are not just technical artifacts—they shape how a system communicates and operates."**  

By **choosing domain events carefully**, **understanding their impact**, and **using composite events where needed**, teams can **design systems that are both powerful and adaptable**.


## **Big Picture Event Storming in Remote Mode**

> **"A value proposition starting with ‘put all the key people in the same room’ looked doomed, no matter how you would finish the phrase."**  

Running a **Big Picture EventStorming** session remotely **introduces significant challenges**, but **corporate problems haven’t disappeared**—in fact, they’ve often **gotten worse** with remote work. The shift to virtual collaboration requires **new strategies** and **adapted facilitation techniques**.

---

### **Main Changes: Adapting Workshops for Remote Teams**  

> **"At the cost of being tedious, let’s make the obvious explicit."**  

Transitioning from **in-person** to **remote EventStorming** introduces both **advantages and drawbacks**:  

#### **Key Changes in Remote Sessions**  

- **No physical presence** → This means **no body language, no spontaneous conversations, and no reading of subtle social cues**.  
- **No room booking** → While **logistics become simpler**, the **loss of a shared physical space impacts engagement**.  
- **No travel involved** → Budget savings occur, but **losing the sense of urgency and commitment** can be detrimental.  
- **Digital artifact-based** → Every action takes place **digitally**, allowing for **better documentation but less tangible engagement**.  
- **Video conferencing reliance** → Your **internet connection and home environment** are now part of the stack.  

> **"Lower commitment, easier procrastination, and Zoom fatigue become major obstacles in remote sessions."**  

#### **Unexpected Consequences**  

- **Easier to cancel or postpone** → Without travel logistics, **rescheduling a remote workshop is simple**, which **reduces commitment**.  
- **No full-day involvement** → **Zoom fatigue is real**; forcing **full-day workshops doesn’t work**, so **sessions must be split**.  
- **No peer pressure** → In an office, **walking out of a workshop is noticed**. Remotely, participants **mute their mic and disengage unnoticed**.  
- **No informal networking** → In physical settings, **side conversations over coffee** often reveal **critical insights**. Remote meetings **eliminate this entirely**.  

---

### **What Role for a Big Picture in Remote Mode?**  

> **"Looks like most of the tricks that made a Big Picture workshop an interesting opportunity were based on human behavior, and are now gone."**  

Despite the limitations, **Big Picture EventStorming remains useful remotely**, particularly for:  

- **Creating a shared vision** → Remote teams require **even more clarity on processes** due to increased silos.  
- **Reducing communication overhead** → Clearer workflows mean **less back-and-forth for alignment**.  
- **Strategic business redesign** → Many companies have had to **rethink operations quickly**, and EventStorming provides **a structured way to do this**.  

> **"If people in your organization are just ‘doing stuff’ without knowing why, you still need a large-scale model of your business."**  

During the pandemic, many businesses needed to **pivot quickly**—EventStorming became a **critical tool for restructuring entire business models**.  

> **"EventStorming allowed us to say, ‘Yes, we can do it!’ but also, ‘This is the most compelling problem to solve right now.'"**  

By combining **EventStorming with Business Model Canvas or Wardley Maps**, companies **aligned vision with execution**.  

---

### **Patterns for Remote Big Picture**  

> **"A one-day remote workshop is nearly impossible—activities must be split across multiple sessions."**  

#### **Key Adjustments for Remote Facilitation**  

1. **Split the workshop into smaller chunks**  
   - Some parts may **not require the whole team**.  
   - Certain tasks can be done **asynchronously**.  

2. **Use structured facilitation techniques**  
   - **Pre-seed a basic structure** → Too much freeform chaos is **hard to manage online**.  
   - **Provide clear role assignments** → Someone must **monitor discussions**, another must **document key insights**.  

> **"Digital space isn’t a constraint—but it also lacks the ‘feel’ of a physical room."**  

#### **Challenges in Remote Exploration**  

- **Spatial references are lost** → People view **a giant, messy board** through **small screens**, making it **harder to see patterns**.  
- **Reduced engagement** → In-person chaotic exploration **sparks curiosity**, while online, it **feels overwhelming**.  

> **"Seeding a skeleton structure works better—add a few pivotal events to provide structure before participants begin."**  

Using **color-coded stickies**, **pre-defined frames**, and **clear timelines** **reduces confusion** and **keeps people engaged**.  

---

### **Do We Have a Recipe? Strategies for Running Virtual EventStorming Sessions**  

> **"There’s no perfect formula for remote EventStorming—but there are ways to improve the experience."**  

#### **Best Practices for Remote Workshops**  

1. **Introduce an onboarding session**  
   - Some participants may be **unfamiliar with digital tools**.  
   - **Train participants on navigation and interaction techniques**.  

2. **Seed structure before the session starts**  
   - **Provide a draft framework** with **key milestones and constraints**.  

3. **Use color as a signature**  
   - Since **handwriting is lost in digital tools**, **color-coded elements can add clarity**.  

4. **Balance synchronous and asynchronous work**  
   - **Discussions should be real-time**, but **note-taking and structuring can happen asynchronously**.  

> **"People still need to have their voice heard—we’re just moving some of the writing outside the main session."**  

### **Final Thoughts: Making Remote EventStorming Work**  

> **"Remote work is here to stay—so we must adapt our collaboration methods."**  

Although **remote EventStorming lacks in-person energy**, it **offers long-term advantages in documentation, accessibility, and scalability**.  

> **"It may not be perfect, but it’s still one of the best ways to make sense of complex business domains remotely."**  


## **Running a Design-Level EventStorming**  

> **"Big Picture EventStorming focuses on maximizing learning and uncovering complexity, whereas Design-Level EventStorming is about collaboratively designing a solution."**  

A **Design-Level EventStorming workshop** shifts the focus from **understanding business processes** to **shaping software solutions**. Instead of exploring **how things currently work**, the goal is to **define how things should work** in a well-structured system.  

---

### **Scope and Participants**  

> **"In Design-Level EventStorming, we are no longer just exploring—we are converging towards implementation."**  

Unlike Big Picture EventStorming, where the focus is on **broad discovery**, Design-Level EventStorming is **more targeted**:  
- **Scope is narrower** – It focuses on **implementing software features that solve a specific problem**.  
- **Participants are different** – The **business audience shrinks**, while **architects and developers** become more involved.  
- **The outcome is different** – Instead of learning about bottlenecks, the goal is to **produce a robust software design**.  

> **"Here, we’re trying to find one or more solutions to a problem worth solving. The workshop isn’t over until we have something that looks like a robust candidate solution."**  

#### **Who Should Be Involved?**  
- **Domain experts** – To validate business logic.  
- **Architects & senior developers** – To translate domain logic into software.  
- **Product managers** – To ensure alignment with business needs.  

The result of this session is **not just insights—it’s a software design blueprint**.  

---

### **Using the Big Picture Artifact**  

> **"The Big Picture artifact provides a foundation—but at this stage, we must move beyond it."**  

The **Big Picture EventStorming outcome** serves as a **reference** for deeper exploration, highlighting:  
1. **A dictionary of domain events** – A shared vocabulary to ensure clarity.  
2. **Critical pain points** – The areas that need redesign.  
3. **External contexts** – Systems, constraints, and integrations that must be considered.  

#### **Two Approaches to Starting a Design-Level EventStorming Session**  
1. **Start from scratch** – The cleanest option, **rebuilding models from the ground up**.  
2. **Work on the existing model** – Useful in **smaller teams** where the **Big Picture exploration is still fresh**.  

> **"Remember: the Big Picture was a model of our current level of understanding. By digging deeper into key interactions, we are already making it obsolete."**  

---

### **Where Are Events Coming From?**  

> **"In a business system, there are four main sources for domain events."**  

Understanding **where events originate** is crucial to **modeling a realistic system**. Events typically stem from:  

1. **User actions** – A customer clicking "Buy Ticket" triggers a **Ticket Purchased event**.  
2. **External systems** – APIs, sensors, or third-party services generating events.  
3. **Time-based triggers** – Scheduled jobs or expiration events.  
4. **Other domain events** – One event triggering another, such as **Order Paid → Order Shipped**.  

> **"A Ticket Purchased event is a direct consequence of a Buy Ticket action, performed by a Customer."**  

#### **Why Not Use UML?**  
> **"UML severely harms the possibility of productive discussions. EventStorming was designed to encourage meaningful conversations, not compliance with notation."**  

While UML offers **formal precision**, it **limits discussions** by forcing a rigid structure. **EventStorming uses an incremental notation** to maintain flexibility.  

---

### **Discovering Aggregates**  

> **"Aggregates should not be discovered by looking at data structures, but by analyzing responsibilities."**  

#### **Key Principles for Identifying Aggregates**  
1. **Postpone naming** – **Do not name aggregates too soon**; focus on **their responsibilities first**.  
2. **Look for behavior, not just data** – Aggregates should **enforce business rules**, not just hold data.  
3. **Identify information needed for consistency** – What data is **required to enforce transactional consistency?**  
4. **Ask: How would I call a class that manages this responsibility?**.  

> **"The temptation to name things prematurely is strong. Resist it. Look for responsibilities first."**  

#### **Common Mistakes When Identifying Aggregates**  
- **Confusing aggregates with read models** – UI concerns should not dictate aggregates.  
- **Thinking in database terms** – Aggregates are **not** database tables; they **enforce business rules**.  

---

### **Determining When You’re Done**  

> **"Once flattened, this is what we’re expecting—a consistent flow with well-defined aggregates and interactions."**  

#### **How Do You Know the Design-Level EventStorming Is Over?**  
1. **The mechanics are clear** – Each process has a **well-defined sequence of domain events**.  
2. **Aggregates and their boundaries are defined** – There is **no ambiguity about where one starts and another ends**.  
3. **Consistency rules are enforced** – Invariants are clearly **modeled and supported**.  

> **"This session isn’t about endlessly refining models—it’s about reaching a working solution."**  

### **Design-Level Modeling Tips**  

> **"A good model is not one that is perfect, but one that is useful."**  

Design-Level EventStorming is not about **seeking absolute precision from the start**, but rather about **exploring multiple approaches and refining them incrementally**. This section covers **key techniques** for making **better design decisions**.  

---

#### **Making Alternatives Visible**  

> **"We should only choose between visible alternatives."**  

One of the **biggest mistakes** in software design is **arguing over unseen possibilities**. **If a decision is made without considering multiple options, it is likely a suboptimal one.**  

##### **Key Strategies for Visualizing Alternatives:**  
1. **Write it down!** – Ideas that are **not on the modeling surface** remain **abstract and untested**.  
2. **Use parallel modeling spaces** – If teams **disagree on an approach**, map out **both solutions side by side**.  
3. **Break abstract discussions** – Encourage people to **physically place sticky notes** to **explain their perspective visually**.  

> **"Abstract discussions waste time. If we can’t see it, we can’t evaluate it properly."**  

By **forcing visualization**, teams naturally **focus on tangible aspects**, making **comparison easier and faster**.  

---

#### **Choosing Later**  

> **"Prioritize having a visible baseline over visualizing every possible branch of exploration."**  

A common trap in EventStorming is **overanalyzing too early**, leading to **paralysis instead of progress**. Instead, teams should **make incremental decisions** while postponing less important ones.  

##### **How to Decide When to Choose?**  
- **If the choice affects the foundation of the model → Decide now.**  
- **If the choice is about implementation details → Delay until necessary.**  
- **If the choice requires more business validation → Mark it as a "Hot Spot" and revisit later.**  

> **"We are not delaying decisions forever—we are structuring them based on priority and impact."**  

This approach prevents **premature optimization** while ensuring that **important decisions are made at the right time**.  

---

#### **Picking the Right Problem**  

> **"Solving the wrong problem efficiently is still failure."**  

Not all issues **deserve immediate attention**. **Some bottlenecks are more impactful than others**, and teams should focus on the **ones that truly matter**.  

##### **How to Prioritize the Right Problems?**  
- **Follow the domain experts** – **Which pain points do they highlight the most?**  
- **Look for bottlenecks in event flows** – **Where does work get stuck or require frequent rework?**  
- **Ask ‘What happens if we don’t fix this?’** – **If the answer is ‘nothing critical,’ deprioritize it.**  

> **"Not every inefficiency is worth fixing—some friction is natural."**  

By **identifying high-impact areas first**, teams maximize **business value from their modeling efforts**.  

---

#### **Refining the Model**  

> **"A model is only as good as its ability to evolve."**  

The **first version of any model is imperfect**. The key is to **iterate** and **refine over time**.  

##### **Refinement Techniques:**  
1. **Walk the timeline backwards** – Ensure that each event **logically follows from the previous one**.  
2. **Check consistency across contexts** – Do **different teams use the same term in different ways?**  
3. **Capture disagreements explicitly** – If stakeholders **disagree on a concept, mark it as a "Hot Spot" and investigate further**.  

> **"A useful model is one that adapts with new information—not one that is ‘perfect’ but rigid."**  

Continuous refinement **ensures the model remains relevant** as teams **gain new insights**.  

### **Building Blocks**  

> **"Domain Events are more than just data—they are the foundation of how business logic flows in an event-driven system."**  

The **Building Blocks** of EventStorming define **how events, actions, and decisions interact** to create **meaningful business processes**. Understanding these core concepts allows teams to **design scalable, event-driven architectures**.  

---

#### **Why Domain Events Are Special**  

> **"Domain Events are deceptively simple: they represent something relevant that happened in our business, written on an orange sticky note with a verb in the past tense."**  

##### **Key Characteristics of Domain Events:**  
1. **They are easy to understand** – Anyone can **grasp and describe an event**, making it an **inclusive modeling tool**.  
2. **They are precise** – Events help **reduce ambiguity**, ensuring a **shared understanding across teams**.  
3. **They capture meaningful change** – A **Domain Event always represents a state transition** in a system.  
4. **They drive reactive systems** – Events **trigger subsequent actions**, forming the backbone of **event-driven architectures**.  

> **"If no one cares about an event, maybe it’s not that relevant in your system."**  

Unlike **database records**, Domain Events **focus on the business narrative**—they tell a **story of what happened** rather than just **storing data**.  

---

##### **Events as State Transitions**  

> **"Using a verb in past tense forces us to explore the exact moment when something changes."**  

Domain Events mark **critical state transitions** in a system. These transitions:  
- **Define key moments** in a process (e.g., **Order Placed, Payment Processed, Order Shipped**).  
- **Clarify dependencies** (e.g., an **Order cannot be shipped before Payment is processed**).  
- **Create opportunities for automation** (e.g., a **Shipped event triggers an email notification**).  

> **"A Domain Event is not just a log entry—it represents a meaningful change that the system must react to."**  

###### **Example: Modeling State Transitions in Temperature Monitoring**  
1. **Temperature Raised** – An imprecise event; it lacks clarity.  
2. **Temperature Registered** – More precise, capturing **what happened and when**.  
3. **Temperature Threshold Exceeded** – A **state transition** that may **trigger an alert**.  

> **"Don’t try to make events too precise too early—embrace fuzziness until patterns emerge."**  

By **iterating on event definitions**, teams gain a **deeper understanding of business processes**.  

---

##### **Commands, Actions, and Decisions**  

> **"Commands are user or system actions that trigger events—but not every command leads to a successful event."**  

##### **Distinguishing Between Commands, Actions, and Decisions**  

1. **Commands (Blue Stickies)** – A **request for an action** (e.g., **Place Order, Submit Payment**).  
2. **Actions** – The **execution of a command**, but not all actions result in events (e.g., **A payment attempt might fail**).  
3. **Decisions** – A **business rule that determines an outcome** (e.g., **Fraud Check Approved leads to Order Processed**).  

> **"A command does not imply completion—events will eventually reflect its outcome."**  

##### **Example: Ordering a Pizza Online**  
- **Command:** *Place Order*  
- **Decision:** *Verify Payment* (Approved or Denied)  
- **Event:** *Order Placed* (if successful)  

> **"If something fails, an event should still be recorded—failure is part of the system’s story too."**  

By separating **commands from events**, teams build **resilient, event-driven systems** where **failure is explicitly handled**.  

### **From Paper Roll to Working Code**  

> **"A post-it based model does not compile, nor does it deliver a green bar."**  

While EventStorming helps teams **visualize complex business processes**, it is **not the end goal**—**the real objective is to deliver working software**. Transitioning from a **paper-based model** to a **running system** requires careful management of **artifacts and iterative development**.  

---

### **Managing EventStorming Artifacts**  

> **"The roll is not the deliverable—it’s just a way to get to the right implementation faster."**  

After an **EventStorming workshop**, teams are left with a **paper roll or digital board full of domain events, commands, and aggregates**. This artifact acts as a **living reference** that guides the implementation phase.  

#### **How to Use EventStorming Artifacts in Development**  
- **Create a domain dictionary** – Use the terms from the EventStorming session to ensure **consistent language** across development.  
- **Map events to system behaviors** – Each event should **translate into a meaningful software operation**.  
- **Identify dependencies and interactions** – Ensure that **aggregates, read models, and external systems are properly linked**.  
- **Validate domain rules with stakeholders** – Before coding, confirm that **business logic aligns with real-world needs**.  

> **"The visible model provides an intuitive way to detect missing pieces—‘Why is this orange thing without the yellow one?’"**  

The **color-coded sticky notes** allow domain experts and developers to **spot inconsistencies quickly** before committing to a design.  

---

### **Coding ASAP**  

> **"So as soon as you have a reasonably good idea about the underlying model… start coding it."**  

EventStorming is about **reducing uncertainty** before development begins—but **it should not delay implementation unnecessarily**.  

#### **Why Prototyping Early is Crucial**  
- **Exposes design flaws early** – Even the best EventStorming models contain **hidden assumptions** that **only coding can reveal**.  
- **Tests technical feasibility** – Some domain concepts may be **challenging to implement**, requiring **alternative approaches**.  
- **Accelerates feedback loops** – The sooner teams write code, the sooner they can **validate ideas with real users**.  

> **"There’s nothing better than a good prototype to discover flaws in our reasoning."**  

Teams should focus on **implementing core domain behaviors first**, using **simple prototypes to validate key assumptions** before scaling up.  

---

### **From EventStorming to User Stories**  

> **"User Story Mapping and EventStorming share a common goal: making requirements visible and actionable."**  

EventStorming focuses on **business behavior**, while User Story Mapping emphasizes **the user’s journey**. By combining both, teams can create **well-structured, customer-centric development plans**.  

---

#### **EventStorming & User Story Mapping**  

> **"The first main difference is in scope: User Story Mapping focuses on understanding needed to develop a new product, while EventStorming has a broader scope, not necessarily tied to product development."**  

#### **Key Differences Between EventStorming and User Story Mapping**  
| **Aspect**         | **EventStorming**                    | **User Story Mapping**              |
| ------------------ | ------------------------------------ | ----------------------------------- |
| **Scope**          | Broad, system-wide                   | Narrow, user-centric                |
| **Focus**          | Domain events and business processes | User interactions and UI flow       |
| **Starting Point** | Key domain events                    | User tasks and goals                |
| **Output**         | Event-driven model                   | Prioritized backlog of user stories |
| **Best Used For**  | Complex business systems             | New product development             |

> **"EventStorming is about modeling behavior, while User Story Mapping is about defining what the user needs to accomplish."**  

Both methods can **coexist**—**EventStorming helps uncover business logic, while Story Mapping refines it into deliverable features**.  

---

#### **Defining Acceptance Criteria**  

> **"This is where things get trickier: while Domain Events and Read Models have clear completion criteria, user interfaces require subjective evaluation."**  

Defining **acceptance criteria** ensures that **software delivers real value** rather than just meeting functional requirements.  

#### **Key Considerations for Acceptance Criteria**  
1. **Align with Domain Events** – Every feature should be **tied to a meaningful event**.  
2. **Use real-world examples** – Describe how the feature will be **used in practice**.  
3. **Define usability expectations** – Ensure the UI is not just functional but **intuitive and accessible**.  
4. **Test with real users** – Validate that the system **meets business and user needs before release**.  

> **"Even a perfectly coded system is useless if the user experience is poor."**  

Acceptance criteria should **balance functional correctness with usability**, ensuring that the **software aligns with human needs**.  

---

#### **How to Merge EventStorming and User Story Mapping**  
1. **Start with EventStorming** – Identify **domain events, commands, and key business interactions**.  
2. **Extract user stories from domain events** – Translate key interactions into **story-driven deliverables**.  
3. **Prioritize based on user impact** – Not all domain events translate to **high-priority user stories**.  
4. **Use Story Mapping to structure the backlog** – Organize user stories into **a coherent product development plan**.  

> **"The best approach isn’t choosing between EventStorming or User Story Mapping—it’s knowing when to use each."**  

By combining **behavioral modeling with user-centric planning**, teams ensure that software **delivers both business value and an excellent user experience**.  

---

#### **Key Takeaways**  

- **Unlike Big Picture workshops, Design-Level EventStorming is about converging, not diverging.**  
- **Events come from multiple sources—understanding them ensures realistic modeling.**  
- **Aggregates should be discovered by analyzing responsibilities, not by forcing a predefined structure.**  
- **The workshop is done when all major design concerns are addressed, not when everything is ‘perfect.’**.  

> **"EventStorming helps teams model software in a way that aligns with real-world business needs—avoiding overcomplication and ensuring a shared understanding."**  

> **"EventStorming helps teams design software in a way that aligns with business reality—not just technical constraints."**  

By **visualizing alternatives, delaying premature decisions, focusing on the right problems, and refining models incrementally**, teams create **better, more maintainable software architectures**.

By running a **Design-Level EventStorming workshop**, teams ensure their software models **truly reflect business realities**—leading to **better architecture, maintainability, and scalability**.

> **"EventStorming helps teams shift from CRUD-based thinking to event-driven modeling—focusing on what truly matters: meaningful change."**  

By using **Domain Events, State Transitions, and Commands effectively**, teams can **model business processes that are scalable, reactive, and aligned with real-world behaviors**.

> **"EventStorming bridges the gap between business and technical teams—User Story Mapping ensures the result is actionable."**  

By transitioning **from paper-based EventStorming models to working software**, teams create systems that are **better aligned with business goals, user needs, and real-world constraints**.

# **Patterns and Anti-Patterns**  

> **"Patterns help us structure successful EventStorming sessions, while anti-patterns warn us about common pitfalls that can derail them."**  

EventStorming sessions **thrive on open, dynamic exploration**, but they can also **fall into common traps** that reduce their effectiveness. This section explores **effective strategies** for running a productive workshop and **pitfalls to avoid**.  

---

## **Effective Strategies**  

> **"A well-facilitated EventStorming session flows naturally, allowing insights to emerge effortlessly."**  

### **1. Add More Space**  
> **"Even if we start the workshop with the promise of unlimited modeling space, we will quickly hit the boundaries of our modeling surface."**  

- **EventStorming thrives on an expansive workspace**—**restricting the physical area limits exploration**.  
- **Solution** → If space starts to feel constrained, **expand the modeling surface immediately** rather than compressing details.  

### **2. Be the Worst**  
> **"Nobody wants to look stupid in a meeting. But sometimes, being the worst can unlock participation."**  

- **If no one wants to place the first sticky note**, **place one yourself—but deliberately make it wrong**.  
- This encourages **others to jump in and correct mistakes**, sparking discussion and reducing **fear of failure**.  

### **3. Conquer First, Divide Later**  
> **"Prematurely dividing the problem into isolated parts kills creativity."**  

- **Many teams instinctively break problems into smaller segments too early**.  
- Instead, **explore everything broadly first, then identify natural divisions**.  
- **Narrowing too soon** means missing **valuable interactions between parts of the system**.  

### **4. Do First, Explain Later**  
> **"Understanding comes from action, not from long theoretical explanations."**  

- Instead of **starting with lengthy theoretical instructions**, **let participants jump in and experiment**.  
- **Hands-on engagement triggers faster learning and deeper discussions**.  

### **5. Use Fuzzy Definitions**  
> **"Insisting on rigid definitions too early prevents diverse perspectives from emerging."**  

- In the early phase of EventStorming, **allow multiple interpretations**.  
- If two participants **disagree on a term**, **write both down instead of forcing a consensus**.  
- **Rigid definitions too early** stifle creativity and **narrow exploration**.  

### **6. Guess First**  
> **"When learners are allowed to guess, they engage more deeply in the process."**  

- Instead of passively **waiting for explanations**, participants should **attempt to describe system behaviors**.  
- **If they’re wrong, a discussion follows—creating a stronger learning experience**.  

### **7. Mark Hot Spots**  
> **"Not every problem needs to be solved in real-time—but it should be made visible."**  

- **Use purple sticky notes** to flag **uncertainties, risks, or disagreements**.  
- This prevents **the team from getting stuck on debates** while ensuring **issues are revisited later**.  

---

## **Common Pitfalls to Avoid**  

> **"Even a well-intended EventStorming session can fail if it falls into one of these common traps."**  

### **1. The Big Table at the Center of the Room**  
> **"Big tables force people to choose seats, creating artificial group divisions."**  

- **A large central table makes collaboration harder** because people **become less mobile**.  
- **Solution** → Remove tables **to encourage standing, movement, and interaction**.  

### **2. The Committee Trap**  
> **"Committees slow everything down, reducing the group’s bandwidth for parallel exploration."**  

- **Small groups debating what to write on sticky notes** kill spontaneity.  
- **Solution** → Break committees **before they form** by encouraging **parallel writing**.  

### **3. Divide and Conquer Too Early**  
> **"Focusing too soon forces artificial boundaries onto the problem."**  

- Some teams **immediately try to break the problem into smaller parts** instead of **exploring holistically**.  
- **Solution** → Encourage **freeform exploration first**, then **find meaningful separations later**.  

### **4. The Dungeon Master**  
> **"A facilitator who controls every detail stifles participation."**  

- If the facilitator **answers every question** or **drives every decision**, **participants disengage**.  
- **Solution** → Encourage **participants to take ownership of discoveries**.  

### **5. Follow the Leader**  
> **"One dominant voice can overshadow the collective intelligence of the group."**  

- **A strong leader dictating solutions prevents others from contributing.**  
- **Solution** → Distribute engagement **by encouraging quieter voices to contribute first**.  

### **6. The Human Bottleneck**  
> **"If one person becomes the single point of truth, collaboration stops."**  

- When **a single domain expert answers every question**, **the rest of the team waits instead of thinking critically**.  
- **Solution** → Rotate leadership and **force participants to generate hypotheses before seeking validation**.  

### **7. Precise Notation Too Early**  
> **"Requiring a rigid format kills flexibility and excludes non-experts."**  

- If facilitators **enforce strict UML-like notation**, it **scares off non-technical participants**.  
- **Solution** → Keep notation **light and flexible**, ensuring **all participants can engage**.  

### **8. The Karaoke Singer**  
> **"Some people love the sound of their own voice, dominating the conversation."**  

- A participant who **talks constantly without engaging others** slows the session down.  
- **Solution** → Introduce **timeboxing** and **redirect discussions back to the group**.  

---

## **Final Thoughts**  

> **"The success of an EventStorming session depends as much on avoiding pitfalls as it does on applying best practices."**  

By **using effective strategies** and **eliminating common anti-patterns**, teams can **maximize learning, accelerate collaboration, and create truly valuable models**.

---

# Actors and Systems

## **5.1. Interactions with People**
Understanding the **human roles** in a business process is fundamental in EventStorming, as it helps define the key players in a given system. 

- **"An actor usually represents a person or group that the process is serving."** Instead of using the generic term "user," participants are encouraged to assign **meaningful business names** to actors. Examples include:
  - *"Attendee"* for a conference
  - *"Instructor"* for a training session
  - *"Conference Team"* for event organizers.

- **Visualizing Actors:** It is common to use **small yellow sticky notes** to represent actors in an EventStorming timeline. Facilitators often draw **stick figures** on the notes and label them accordingly.

- **UX Personas & Roles:** If an organization already has **UX personas**, these should be incorporated into the timeline instead of generic actor names. For example, a sales representative may be labeled *“Judith”* to reflect their goals and behaviors more accurately.

- **Patterns in Actor Representation:**
  1. A single actor generating a **single event** (e.g., *a workshop attendee requests a refund*).
  2. A single actor generating **multiple events** (e.g., *a conference team prepares a profit-loss report and shares it*).
  3. **Multiple actors collaborating** on a single event (e.g., *an attendee and an instructor interacting during a workshop*).

- **Swimlanes for Role Clarity:** Adding actors can help define **swimlanes**, which represent clear role-based lanes in the workflow. This helps visualize:
  - **Hand-offs** between actors.
  - **Points of delay** due to dependency on another actor’s actions.
  - **Responsibilities & Goals** of different participants in the workflow.

---

## **5.2. Systems**
Mapping **external and internal system interactions** is crucial for understanding the technological dependencies within a business process.

- **Definition of a System:** 
  - **"A system represents something you integrate with that is a source or destination for events in the process."**
  - Systems can be **internal (owned by the company)** or **external (third-party services like APIs, SaaS, or legacy systems)**.

- **Examples of Systems in EventStorming:**
  - Software **applications** (e.g., *Salesforce, Excel, Oracle*).
  - **Cloud services** (e.g., *Amazon AWS, Microsoft Azure*).
  - **APIs** (e.g., *email, calendar, payment gateways*).
  - **Legacy Systems** (e.g., *older in-house applications that still play a role in the process*).
  - **Documents and Reports** (e.g., *spreadsheets or PDFs that influence workflow decisions*).

- **Systems are Non-Human Actors:** Systems act as "non-human actors" that trigger or receive events, just as humans do in a business process.

- **Representation of Systems:**
  - Systems are often visualized as **black sticky notes** (in Miro) or **gold/yellow diamond-shaped notes** (for physical workshops).
  - EventStorming helps identify **opportunities to outsource** generic capabilities to third-party services (e.g., moving from an in-house **fraud detection system** to an external provider like Stripe or PayPal for payment processing).

- **How Systems Are Layered on a Timeline:**
  - Facilitators usually **layer actors and systems together**, allowing for easier identification of event sources (whether human or technical).
  - This activity often uncovers **missing events**, hidden technical gaps, or overlooked software dependencies.

---

## **5.3. Sociotechnical Vision**
Combining **people, processes, and technology** enables organizations to make **better decisions** by visualizing the entire **sociotechnical landscape**.

- **"This is where developers and technical participants see the real value of EventStorming"** because it reveals how software and human interactions create complexity.

- **Why Sociotechnical Visualization Matters:**
  - Business processes are rarely **purely human-driven** or **purely system-driven**. Instead, they emerge as **a mix of both.**
  - **Revealing dependencies** between teams and systems is critical.
  - **Understanding communication bottlenecks** between business teams and IT.

- **Hidden Dependencies:** 
  - **Social dependencies**: *Who owns which decisions? Are there conflicts between teams?*
  - **Technical dependencies**: *Which applications or third-party systems influence our processes?*
  - EventStorming often reveals **"bottlenecks"** where a critical process relies on an external team or a third-party vendor, causing delays.

- **Context Mapping for Strategic Planning:**
  - **"Context mapping is a strategic domain-driven design (DDD) technique for showing relationships between the various language dialects at play."**
  - This method helps teams understand **how software design should align with team structures and business needs**.

- **Avoiding Technical Detours:** 
  - **"When discussing systems, developers may get sidetracked by technical details."** 
  - If the discussion shifts toward **integration mechanics or deployment concerns**, these should be **captured as pink sticky notes** for later discussions rather than derailing the primary business discussion.

---

## **5.4. SEP Fields (Somebody Else’s Problem Fields)**
Understanding **what teams ignore** is as important as understanding what they focus on.

- **Inspired by Douglas Adams' *Life, the Universe and Everything***:
  - **"An SEP is something we can’t see, or don’t see, or our brain doesn’t let us see because we think it’s somebody else’s problem."**
  - In organizations, these **blind spots** can lead to **major bottlenecks** in a workflow.

- **Why SEP Fields Matter in Business Modeling:**
  - **"Systems owned by others still have integration points with systems we own."**
  - These **integration points create dependencies** that teams often **fail to acknowledge**.
  - SEP fields often lead to **frustration** when a process is delayed by a third-party system, yet no one in the workshop initially acknowledges the delay.

- **Identifying SEP Fields in EventStorming:**
  - **Watch for "finger-pointing" discussions** – if multiple participants blame an **external system, regulation, or policy**, it might be an SEP field.
  - **Example SEP Fields:**
    - *Regulations like GDPR that affect data processing.*
    - *A legacy database that everyone avoids modifying.*
    - *A third-party vendor responsible for system outages.*

- **Breaking SEP Fields:** 
  - Facilitators should ask: *"Is this really an external problem, or is there something we can do?"*
  - **"Sometimes a breakout group can help dig deeper into an SEP field without derailing the entire discussion."**
  - Recognizing and documenting SEP fields helps teams proactively address **risks and inefficiencies**.

---

### **Conclusion**
The **"Actors and Systems"** section of EventStorming is about **mapping out both human and technical interactions**, revealing **hidden complexities**, and **surfacing critical dependencies** that impact business processes. 

- **Actors define WHO interacts in the process.**
- **Systems define WHAT non-human elements influence the workflow.**
- **Sociotechnical Vision helps blend business and IT perspectives.**
- **SEP Fields uncover ignored but critical dependencies.**

By incorporating these layers into an **EventStorming timeline**, organizations can **identify inefficiencies, remove bottlenecks, and create a shared understanding of their processes**.


# **Walking the Narrative**

---

## **6.1. Why Walk?**
**"Walking the Narrative"** is a critical step in EventStorming that ensures alignment across different perspectives. The timeline constructed during an EventStorming session represents a shared **story of the business**, integrating both **business and technical viewpoints**.

### **Why is this necessary?**
- It prevents teams from creating a **shallow or incomplete** timeline.
- Reviewing the entire timeline **uncovers gaps**, inconsistencies, and previously unnoticed issues.
- Many people work in **silos**, and this walkthrough helps **bridge knowledge gaps** and illuminate **unspoken expectations**.

### **How is it done?**
- It is typically conducted **after adding actors and systems** to the timeline, which **stabilizes the story**.
- The session **slows down intentionally**, allowing participants to **listen, reflect, and ask questions**.
- Helps teams **converge** on a shared understanding of the workflow.

### **Key Takeaways**
✔ **"Most people in an organization are used to working in their own silos, and telling the story of a process that cuts across silos often illuminates unspoken expectations or opportunities."**  
✔ **"It is easy to create a timeline that looks good but lacks sufficient detail or skips over important details that haven’t yet been noticed because it hasn’t been reviewed as a whole."**

---

## **6.2. Telling the Story**
This phase can be **dull if not handled well**, as it may feel like a **boring review session**. However, if facilitated correctly, it can be **engaging and insightful**.

### **Challenges and Solutions**
🔹 **Fear of public speaking:**  
   - People may hesitate to narrate parts of the timeline, fearing they might get it **"wrong"**.  
   - **Solution:** The facilitator should **go first**, demonstrating that **they don’t have to be an expert**—they are just reading the events.  

🔹 **Low engagement:**  
   - If only one or two people narrate, **others tune out**.  
   - **Solution:** Have people **take turns reading events aloud**—this adds **variety and surprise** to the session.

🔹 **Energy drain:**  
   - If it feels like a **checklist review**, people may disengage.  
   - **Solution:** Encourage the group to see this as a **validation exercise**, where anyone can **ask questions and challenge assumptions**.

### **Key Quotes**
✔ **"All anyone needs to do to be successful in the walkthrough as a reader is to read out each sticky note as if they are telling the story of the process."**  
✔ **"If the reader is reading out the events for a section of the timeline and it doesn’t make sense, that’s a good thing."**  
✔ **"After the first person has read, I like to get everyone to give applause and congratulate them for their courage to get up there and walk through it in front of others/the experts in the domain."**

---

## **6.3. A Sample Story**
This section provides a **concrete example** of how a walkthrough unfolds. The example used is **conference planning**, focusing on **marketing efforts**.

### **Sample Walkthrough**
1️⃣ **Facilitator starts the story**:  
   _"The organizer kicked off the conference planning by getting the venue booked."_  
2️⃣ **A participant continues**:  
   _"They then invited the workshop instructors via Marketing, which we seem to have pulled out as a theme below, since it happens multiple times through the timeline."_  
3️⃣ **Someone asks a clarifying question**:  
   _"Are we using Facebook and Instagram for marketing too?"_  
4️⃣ **If no one knows the answer**, it’s captured on a **pink sticky note** for later discussion.  
5️⃣ **A new reader takes over**, ensuring a **varied and engaging experience**.

### **Why is this format effective?**
- Encourages **broad participation** and **cross-team learning**.
- Highlights **missing details** or areas that require **further refinement**.
- **Surfaces knowledge gaps** before they become roadblocks.

### **Key Quotes**
✔ **"Walking the narrative is a good time for any existing pink stickies on the timeline to be read out to the group, since this is where a lot of the critical learning can take place."**  
✔ **"This is typically the point in the workshop where there is a lot of knowledge being shared across different disciplines and isolated silos."**

---

## **Summary**
**"Walking the Narrative"** is not just a review—it's a critical **alignment exercise** that brings hidden knowledge to the surface and **refines the business process story**. Through a structured but flexible walkthrough process:
- **Key insights emerge** as teams **review the full timeline**.
- **Knowledge is shared** across **business and technical teams**.
- **Clarifications happen in real-time**, making it a **powerful learning tool**.

By following the **facilitation best practices** outlined in this section, organizations can ensure that their EventStorming sessions **not only visualize workflows but also drive real process improvements**.

---

# **7. Documenting Language**
Effective communication is critical in any domain, but **business processes often involve multiple dialects of terminology** that can lead to misunderstandings, inefficiencies, and integration challenges. EventStorming provides a structured approach to capturing and refining language use within an organization.

---

## **7.1. Exposing Language Messiness**
Language in an organization is often a mix of **inconsistencies, legacy terminology, and overlapping meanings**. These differences may seem trivial, but they can cause **major breakdowns in communication** when systems, teams, or business units need to work together.

### **Recognizing Hidden Language Inconsistencies**
One of the key insights from EventStorming is that **terminology changes across different phases of a business process**. This variation can be subtle or significant, but it is often **invisible until explicitly visualized**.

For example:
- A **"Contract Signed"** event in the Sales Process might be called **"Warranty Created"** in the Warranty Administration system.
- A term like **"Approval"** in a legal team might refer to a compliance check, while in engineering, it means moving a feature into production.

### **Why This Matters**
- Different teams may assume they are talking about the **same thing** when, in reality, they are not.
- Standardizing terminology **too early** can **obscure important domain distinctions**, leading to software models that **fail to capture real-world nuances**.

### **Strategies for Handling Language Messiness**
1. **Visualizing the Differences:** Instead of smoothing over discrepancies, EventStorming **makes them explicit** by mapping them onto the timeline. This helps teams discuss inconsistencies openly.
2. **Encouraging Conversations:** Participants should **discuss areas where language gets messy** and explore why different terms exist.
3. **Avoiding Premature Standardization:** The urge to impose a single definition for all terms should be resisted. **Different teams may need different terms** to reflect their distinct perspectives.

---

## **7.2. Capturing Critical Concepts**
Once the **language messiness is exposed**, the next step is **capturing critical domain concepts** and ensuring that essential terms are well understood across the organization.

### **Why Capturing Terms Matters**
- Many key terms are **"caught rather than taught"**, meaning that **new employees struggle** to understand their meaning **without explicit documentation**.
- Creating a **glossary** of key terms reduces the onboarding burden and ensures that everyone understands **how terms are used in different contexts**.

### **How to Capture Critical Concepts**
- **Designate a volunteer** to capture key terms that arise during discussions.
- Write **each term with a short definition** and ensure that the meaning is **clear to non-experts**.
- Identify words that **may cause confusion**, including:
  - **Acronyms** that might not be universally understood.
  - **Industry terms** that have specific meanings.
  - **Synonyms that might mask domain differences**.

### **Where to Document These Concepts**
For **in-person workshops**, key terminology is often captured on **large sticky notes** and placed along the timeline. In **virtual settings**, a dedicated **Glossary section** above the timeline can be used.

### **Making the Glossary Actionable**
- Rather than spending workshop time defining every term in detail, **the glossary can be refined later as a follow-up exercise**.
- **Do not force consensus** on all terms—some terminology will **remain different across contexts**, and that’s okay.
- If terminology varies significantly across a process, consider **dividing the glossary into sections based on key events**.

---

## **Final Thoughts**
By exposing language messiness and systematically capturing critical terms, **EventStorming helps organizations bridge communication gaps** and create **more robust, user-friendly, and precise processes**. This approach ensures that **terminology does not become an invisible barrier** to collaboration and system integration.


# **Reference Materials**  

## **Glossary**  

> **"EventStorming is not about defining terms upfront but about making significant conversations possible."**  

The **glossary** provides **definitions for key concepts** used throughout EventStorming. However, it **deliberately avoids rigid precision**, emphasizing **flexibility in discussion**.  

### **Key Terms in EventStorming**  

1. **Domain Event** – A **business-relevant occurrence**, described in **past tense** (e.g., *Order Placed*, *Payment Processed*).  
2. **Command** – A **request for an action** that **triggers an event** (e.g., *Submit Order*).  
3. **Aggregate** – A **consistency boundary** ensuring that **all changes occur as a single transaction**.  
4. **Bounded Context** – A **clear boundary** around a business domain where **specific terms and models apply**.  
5. **Read Model** – A **representation of data** optimized for queries but **not responsible for enforcing business rules**.  

> **"If language isn't clear, communication breaks down—EventStorming helps expose and refine business terminology."**  

Unlike **static documentation**, the **glossary evolves throughout the workshop**, ensuring **alignment across teams**.  

---

## **Tools for EventStorming**  

> **"The right tools set the stage for an effective workshop—bad tools kill momentum."**  

EventStorming relies on **visual facilitation**, requiring **highly interactive tools** for **capturing discussions and structuring domain models**.  

### **Essential Physical Tools**  
- **Paper Rolls** – Provides an **unlimited modeling surface** (IKEA Måla or professional plotter paper recommended).  
- **Sticky Notes** – Different colors represent **events, commands, actors, and policies** (preferably **3M Super Sticky**).  
- **Markers** – **Fine-tip Sharpies** or **BIC Marking Pocket 1445** for visibility.  
- **Writable Walls** – Whiteboards or **special writable paint** allow **dynamic modeling**.  

> **"Avoid weak glue on stickies—falling notes kill engagement!"**  

### **Digital Tools for Remote EventStorming**  
- **Miro / MURAL** – Online whiteboards with **infinite space** for collaborative EventStorming.  
- **Google Jamboard / FigJam** – Simpler alternatives for lightweight modeling.  
- **Lucidchart / Whimsical** – Best for **structuring finalized insights**.  

> **"Digital tools improve accessibility but lose some of the energy of in-person workshops."**  

Choosing **the right tool depends on the workshop setting**, whether **face-to-face or fully remote**.  

---

## **Bibliography**  

> **"EventStorming stands on the shoulders of giants—these books shaped the practice and philosophy behind it."**  

The **EventStorming bibliography** contains **key references in software design, business modeling, and facilitation techniques**.  

### **Core Domain-Driven Design (DDD) Books**  
- **Domain-Driven Design: Tackling Complexity at the Heart of Software** – *Eric Evans*  
- **Implementing Domain-Driven Design** – *Vaughn Vernon*  
- **Patterns of Enterprise Application Architecture** – *Martin Fowler*  

### **Facilitation & Collaboration**  
- **Gamestorming** – *Dave Gray* (Techniques for **visual collaboration and group creativity**).  
- **Getting to Yes** – *Roger Fisher & William Ury* (Key **negotiation strategies** for consensus-building).  
- **User Story Mapping** – *Jeff Patton* (How to **prioritize work based on user journeys**).  

### **Agile & Lean Thinking**  
- **Extreme Programming Explained** – *Kent Beck* (Fundamentals of **incremental software delivery**).  
- **The Lean Startup** – *Eric Ries* (How to **iterate quickly and validate business assumptions**).  
- **Impact Mapping** – *Gojko Adzic* (A method for **aligning software development with business goals**).  

> **"Understanding software is as much about understanding people as it is about code."**  

These references **provide deep insights** into **why EventStorming works** and **how to integrate it into broader software development practices**.  

---

### **Final Thoughts**  

> **"EventStorming is a constantly evolving practice—it adapts as we learn more about how teams collaborate and build software."**  

The **final sections** of *Introducing EventStorming* **reinforce the importance of collaboration, continuous learning, and practical tools** for modeling **complex business domains**. Whether using **physical sticky notes** or **digital whiteboards**, the principles remain the same:  

- **Make everything visible**  
- **Encourage active participation**  
- **Expose assumptions early**  
- **Iterate and refine**  

By combining **clear terminology, effective tools, and a strong foundation in proven methodologies**, teams can **use EventStorming to create better software, improve business processes, and enhance collaboration across organizations**.


# Quotes

**"By integrating EventStorming and User Story Mapping, teams gain both deep domain insights and a structured roadmap for execution."**  

# References
- https://github.com/mariuszgil/awesome-eventstorming
- https://leanpub.com/eventstorming_handbook
- https://leanpub.com/introducing_eventstorming