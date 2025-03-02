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


# unsorted

---

## **Part 1: Understanding EventStorming**

---

## **Part 2: Running Effective EventStorming Workshops**

### **5. Playing with Value**
- **Explore Value**: Identifying key value drivers in business processes.
- **Explore Purpose**: Understanding why processes exist.
- **When Should We Apply This Step?**: Situations where value exploration is critical.

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
