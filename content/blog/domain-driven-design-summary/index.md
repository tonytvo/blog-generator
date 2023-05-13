---
title: domain driven design by Eric Evans summary
date: "2021-12-20T22:12:03.284Z"
description: "domain driven design by Eric Evans summary"
tags: ["domaindrivendesign", "evolutionarydesign"]
---

# DDD overview

![domain patterns overview](./domain-patterns-overview.png)

![overview of DDD](./overview-ddd-design.jpg)

# anatomy of domain-driven design

[The anatomy of domain driven design](./theanatomyofdomain-drivendesign.pdf)

# Putting the model to work
Domain-Driven Design is an approach to the development of complex software in which we:

- **Focus on the core domain**
- **Explore the models in a creative collaboration of domain practitioners**
- **speak a ubiquitous language within an explicitly bounded context.**

## Bounded Context
- Explicitly define the context within which a model applies.
- multiple models are in play on any large project. Yet the code based on distinct models is combined, software becomes buggy, unreliable, and difficult to understand. Communications among team members confused. It is often unclear what context a model should not be applied.
- **Explicitly set boundaries in team organization, usage within specific application parts, and physical manifestations such as code bases and database schemas.**
- Apply continuous integration to keep the model concepts and terms strictly consistent within these bounds, but don't be distracted or confused by issues outside. 
- **bounded context are not modules**
  - modules organize the elements within one model
  - the separate name spaces that modules create within a bounded context actually make it harder to spot accidental model fragmentation.

- **recognizing splinters within a bounded context**.
  - **Duplicate concepts**: The same concept is represented and implemented in more than one way. This means that when a concept changes, it has to be updated in several places, and the developers need to be aware of the several different ways of doing one same thing, as well as the subtle difference within them.
  - **False cognates**: When two people are using the same term and they think they are talking about the same thing, but they are actually thinking of different things.

- the internal consistency of a model, such that each term is unambiguous and no rules contradict, is called unification.
  - **total unification of the domain model for a large system will not be feasible or cost-effective.**
  - risks for unifying all the software in a large project under single model
    - too many legacy replacement may be attempted at once
    - large projects may bog down because the coordination overhead exceeds their abilities.
    - applications with specialized requirements may have to use models that don't fully satisfy their needs, forcing them to put behavior elsewhere
    - conversely, attempting to satisfy everyone with single model may lead to complex options that make the model difficult to use.

## Ubiquitous Language
- **Use the model as the backbone of a language. Then, commit the team to exercise that language relentlessly in all communication within the team and in the code.**
- Use the same language in diagrams, writing, and speech within a bounded context.
- Recognize that a change in the language is a change to the model
iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model.
- Resolve confusion over terms in conversation, in just the way we come to agree on the meaning of ordinary words.

![ubiqutous language](./ddd-ubiqutous-language.png)


# model-driven design

- tightly relating the code to an underlying model gives the code meaning and makes the model relevant.
- Design a portion of the software system to reflect the domain model literally so that the mapping is obvious.
- Revisit the model and modify it to be implemented more naturally in software, even as you seek to make it reflect deeper insight into the domain
- demand a single model that serves both purposes well, in addition to supporting a ubiquitous fluent language.
- Any technical person contributing to the model must spend some time touching the code, whatever primary role they play on the project.
- **Anyone responsible for changing code must learn to express a model through the code.**
- Every developer must be involved in discussing the model and contact domain experts.
- Those who contribute in different ways must consciously engage those who touch the code in a dynamic exchange of model ideas through the ubiquitous language.

- A model can be very descriptive of the domain while being unrepresentable in code. If the implementation is not considered while building the model:

  - The model can have objects and relations that cannot be stored in a database.
  - Model will detail irrelevant subjects and ignore important subjects.
  - Some discoveries about the domain might not be apparent without considering the implementation details.

- **Design Model vs Analysis Model**
  - There are 2 types of models:

    - Analysis Model: Captures the fundamentals of the domain concepts in comprehensible, expressive way. (Focuses on the domain)
    - Design Model: Specify a set of components that can be constructed using programming tools and correctly solves the problem. (Focuses on the implementation)
  Model-Driven Design
    - Model-Driven Design integrates both Analysis and Design models and it serves both purposes.

- if the design, or some central part of it, does not map to the domain model, that model is of little value, and the correctness of the software is suspect. At the same time, complex mappings between models and design functions are difficult to understand and, in practice, impossible to maintain as the design changes. A deadly divide opens between analysis and design so that insight gains in each of those activities does not feed into the other.

- design a portion of software system to reflect the domain model in a very literal way, so that mapping is obvious. Revisit the model and modify it to be implemented more naturally in software, even as you seek to make it reflect deeper insight into the domain. Demand a single model that serves both purpose well, in addition to supporting a robust ubiquitous language.

- draw from the model the terminology used in the design and the basic assignment of responsibilities. The code become the expression of the model, so a change to the code may be a change to the model. its effect must ripple through the rest of the project's activities accordingly.

- To tie implementation slavishly to a model usually requires software development tools and languages that support a modeling paradigm, such as object-oriented programming.

- The underlying model of the system should be the same model shown to users. Otherwise, confusion will arise and the language will not be descriptive enough. Having different models can also cause unexpected behaviors to the users. An example to that is how Microsoft Internet Explorer modeled the bookmarks.

  - For the user, "Favorites" was a list of URLs but to the actual implementation a "Favorite" is a file that contains a URL. This meant that URL names had to follow windows file naming restrictions. So if a user saved a URL and named it "AOT: 3" they will get an error stating that file names cannot contain special characters like ":" which is very confusing.

- ![model exploration whirlpool](https://www.domainlanguage.com/wp-content/uploads/2016/04/DDD_Model_Exploration_Whirlpool.png)

- if the people who write the code do not feel responsible for the model, or don't understand how to make the model work for an application, then the model has nothing to do with the software. If developers don't realize that changing code changes the model, then their refactoring will weaken the model rather than strengthen it. Meanwhile, when a modeler is separated from the implementation process, he or she never acquires, or quickly loses, a feel for the constraints of implementation. The basic constraint of MODEL-DRIVEN-DESIGN - that the model supports an effective implementation and abstracts key domain knowledge - is half gone, and the resulting models will be impractical. Finally, the knowledge and skills of experienced designers won't be transferred to other developers if the division of labor prevents the kind of collaboration that conveys the subtleties of coding a MODEL-DRIVEN-DESIGN.

- any technical person contributing to the model must spend some time touching the code, whatever primary role he or she plays on the project. Anyone responsible for changing the model must learn to express a model through the code. Every developer must be involved in some level of discussion about the model and have contact with domain experts. Those who contribute to different ways must consciously engage those who touch the code in a dynamic exchange of model ideas through the UBIQUITOUS LANGUAGE.
## layered architecture
- isolate the expression of the domain model and the business logic, and eliminate any dependency on infrastructure, user interface, or even application reason that is not business logic. Concentrate all the code related to the domain model in one layer and isolate it from the user interface, application, and infrastructure code.
- **The domain objects, free of the responsibility of displaying themselves, storing themselves, managing application tasks, and so forth, can be focused on expressing the domain model.**
- This allows a model to evolve to be rich enough and clear enough to capture essential business knowledge and put it to work.

## entities
- When an object is distinguished by its identity rather than its attributes, make this primary to its definition in the model.
- **Keep the class definition simple and focused on life cycle continuity and identity.**
- Define a means of distinguishing each object regardless of its form or history
- be alert to requirements that call for matching objects by attributes.
- Define an operator that is guaranteed unique. This means of identification may come from the outside, or it may be an arbitrary identifier created by and for the system. Still, it must correspond to the identity distinctions in the model.
- aka reference objects
## value objects
- when you care only about the attributes and logic of an element of the model, classify it as a value object.
- Make it express the meaning of the attributes it conveys and give it related functionality.
- **Treat the value object as immutable. Make all operations side-effect-free functions that don't depend on any mutable state.**
- Don't give a value object any identity and avoid the design complexities necessary to main entities.

![entities vs value in different context](./entities-vs-value-diff-context.png)


## domain events
- model information about activity in the domain as a series of discrete events. Represent each event as a domain event object.
- These are distinct from system events that reflect activity within the software itself. However, a system event is often associated with a domain event, either as part of a response to the domain event or to carry information about the domain event into the system.
- **Ignore irrelevant domain activity while making explicit the events that the domain experts want to track or be notified of or associated with state change in the other model objects.**

## services
- when a significant transformation process in the domain is not a natural responsibility of an entity or value object, add an operation to the model as a standalone interface declared as a service.
- Define a service contract, a set of assertions about interactions with the service. State these assertions in the ubiquitous language of a specific bounded context.
- Give the service a name, which also becomes a ubiquitous language.

## modules
- concepts should be divided into modules.
- Choose modules that tell the story of the system and contain a cohesive set of ideas. Give the modules the names that become part of the ubiquitous language. Modules are part of the model, and their names should reflect insight into the domain.
- Seek low coupling in the sense of concepts that can be understood and reasoned about independently. Then, refine the model until it partitions according to high-level domain concepts and decouples the corresponding code.

## aggregates
- **it challenging to guarantee the consistency of changes to objects in a model with complex associations.**
- Cluster the entities and value objects into aggregates and define boundaries around each.
- **Choose one entity to be the root of each sum, and allow external objects to hold references to the source only (regarding internal members passed out for use within a single operation only).**
- define properties and invariants for the aggregate as a whole and give enforcement responsibility to the root or some designated framework mechanism
- Use the exact aggregate boundaries to govern transactions and distribution
within an aggregate edge, apply consistency rules synchronously. Across borders, handle updates asynchronously
keep an aggregate together on one server. Allow different sums to be distributed among nodes.

## Repositories
- query access to sums expressed in the ubiquitous language.
- For each type of aggregate that needs global access, create a service that can provide the illusion of an in-memory collection of all objects of that aggregate's root type.
- Set up access through a well-known global interface.
  - Provide methods to add and remove objects, encapsulating the actual insertion or removal of data in the data store.
  - **Provide methods that select objects based on criteria meaningful to domain experts. For example, return fully instantiated objects or collections of objects whose attribute values meet the requirements, thereby encapsulating the actual storage and query technology, or return proxies that give the illusion of fully instantiated aggregates lazily.**
- **Provide repositories only for aggregate roots that actually need direct access. Keep application logic focused on the model, delegating all object storage and access to the repositories.**

## factories
- shift the responsibility for creating instances of complex objects and aggregates to a separate object, which may itself have no responsibility in the domain model but is still part of the domain design.
- Provide an interface that encapsulates all complex assemblies and does not require the client to reference the concrete classes of the instantiated objects.
- **Create an entire aggregate as a piece, enforcing its invariants.**
- Create complex value objects like a piece, possibly after assembling the elements with a builder.

# Supple design
- Supple design complements the deep modelling
- client developer, who weaves the domain objects into the application code or other domain layer code.
- **The client developer can flexibly use a minimal set of loosely coupled concepts to express a range of scenarios in the domain.**
- The effects of its code must be transparently obvious, so the consequences of a change will be easy to anticipate.
- **Making behaviour obvious**
- **reduces the cost of change**
- ![supple design overview](./supple-design-overview.png)
  
## intention-revealing interfaces
- if a developer must consider the implementation of a component in order to use it, the value of encapsulation is lost. If someone other than the original developer must infer the purpose of an object or operation based on its implementation, that new developer may infer a purpose that the operation or class fulfills only by chance. If that was not the intent, the code may work for the moment, but the conceptual basis of the design will have been corrupted, and the 2 developers will be working at cross purposes.

- **name classes and operations to describe their effect and purpose, without reference to how they do what they promise.**
- This relieves the client developer of the need to understand the internals.
- **These names should conform to the ubiquitous language so that team members can quickly infer their meaning.**
- **Before creating it, write a test for behaviour to force your thinking into client developer mode.**
  
## assertions
- when the side effects of operations are only defined implicitly by their implementation, designs with a lot of delegation become a table of cause and effect. The only way to understand a program is to trace execution through branching paths. The value of encapsulation is lost. The necessity of tracing concrete execution defeats abstraction.
- state post-conditions of operations and invariants of classes and aggregates with assertions
- **if assertions cannot be coded directly in your programming language, write automated unit tests for them.**
- Write them into documentation or diagrams to fit the project's development process style.
- seek models with coherent sets of concepts, which lead a developer to infer the intended ASSERTIONS, accelerating the learning curve and reducing the risk of contradictory code.

## side effect free functions
- the developer calling an operation must understand its implementation and the implementation of all its delegations in order to anticipate the result. The usefulness of any abstraction of interfaces is limited if the developers are forced to pierce the veil. Without safely predictable abstractions, the developers must limit the combinatory explosion, placing a low ceiling on the richness of behavior that is feasible to build.
- place as much the logic of the program as possible into functions, operations that return results with no observable side effects. Strictly sepregate commands (methods that result in modifications to observable state) into very simple operations that do not return domain information. Further control side effects by moving complex logic into VALUE OBJECTS when a concept fitting the responsibility presents itself.

## standalone classes
- even within a MODULE, the difficulty of interpreting a design increases wildly as dependencies are added. This adds to mental overload, limiting the design complexity a developer can handle. Implicit concepts contribute to this load even more than explicit references.
- Low coupling is fundamental to object design. When you can, go all the way. Eliminate all other concepts from the picture. Then the class will be completely self-contained and can be studied and understood alone. Every such self-contained class significantly eases the burden of understanding a MODULE.

## closure of operations (not very clear to me yet)
- where it fits, define a function whose return type is the same as its arguments
- if the implementer has a state used in the computation. The implementer is a compelling operation argument, so the argument(s) and the return value should be the same type as the implementer.Such an operation is closed under the set of instances of that type.
- A closed operation provides a high-level interface without introducing any dependency on other concepts.

## declarative design
- many of the benefits of the declarative design are obtained once you have combinable elements that communicate their meaning and have characterized or apparent effects or no observable effects at all
- problems with declarative design
  - a declaration language not expressive enough to do everything needed, but a framework that makes it very difficult to extend the software beyond the automated portion.
  - code-generation techniques that cripple the iterative cycle by merging generated code into hand-written code in a way that makes regeneration very destructive.

## conceptual contours
- when elements of a model or design are embedded in a monolithic construct, their functionality gets duplicated. The external interface doesn't say everything a client might care about. Their meaning is hard to understand, because different concepts are mixed together.
- On the other hand, breaking down classes and methods can pointlessly complicate the client, forcing client objects to understand how tiny pieces fit together. Worse, a concept can be lost completely.
- with each decision, ask yourself, "Is this an expedient based on a particular set of relationships in the current model and code, or does it echo some contour of the underlying domain?"
- decompose design elements (operations, interfaces, classes, and aggregates) into cohesive units, considering your intuition of the essential divisions in the domain.
- Observe the axes of change and stability through successive refactorings, and look for underlying conceptual contours that explain these shearing patterns.
- Align the model with the consistent aspects of the domain that make it a viable area of knowledge in the first place.
- INTENTION-REVEALING INTERFACES allow clients to present objects as units of meaning rather than just mechanisms. SIDE-EFFECT-FREE FUNCTIONS, and ASSERTIONS make it safe to use those units and make complex combinations. The emergence of CONCEPTUAL CONTOURS stabilizes parts of the model and also makes the units more intuitive to use and combine.

## supple design strategies
  - carve off subdomains
    - you may see a part of the model that can be viewed as specialized math; separate that.
    - your application enforces complex rules, restricting state changes; pull this out into a separate model or simple framework that lets you declare the rules.
    - with each such step, not only is the new module clean, but also the part left behind is smaller and clearer
    - part of what's left is written in declarative style, a declaration in terms of special math or validation framework
    - it's more useful to make a big impact on one area, making a part of design really supple, than to spread your efforts thin.
  - draw on established formalisms, when you can
    - you can often use and adapt conceptual systems that are long established in your domain or others, some of which have been refined and distilled over centurties.
    - many business applications involve accounting, for example. Accounting defines a well-developed set of ENTITIES and rules that make for an easy adaptation to deep model and a supple design.

## integrating the patterns: Shares Math
- seperate commands and side-effect free functions
  - the `distributePaymentPrincipal()` method does dangerous thing: it calculates the shares for distribution and also modifies the loan.
```
Map distribution = aLoan.calculatePrincipalPaymentShares(paymentAmount)
aLoan.applyPrincipalPaymentShares(distribution)
```
- *make implicit concept explicit*
  - most of the rules and calculation about shares don't apply to single shares, but to groups of them. There are missing concepts: shares are related to each other as parts of making up a whole. The **Share Pie** represents the total distribution of a specific **Loan**. It is an ENTITY whose entity is local within the AGGREGATE of the **Loan**. The actual distribution calculations can be delegated to the **Share Pie**

- certain characteristics of the **SharePie** design make for this easy recombination and communication in the code
  - complex logic is encapsulated in specialized VALUE OBJECTS with SIDE-EFFECT FREE FUNCTIONS. 
  - none of the **SharePie** methods cause any change to any existing object. This allows us to use ``plus(), minus(), and prorated()`` freely in intermediate calculations, combining them, expecting them to do what their names suggest, and nothing more.

- *State-modifying operations are simple and characterized with ASSERTIONS*. The high-level abstractions of Shares Math allow invariants of transactions to be written concisely in a declarative style. For example, the deviation is the actual pie minus the Loan amount prorates based on the Facility's SharePie.

- *model concepts are decoupled; operations entable a minimum of other types*. Some methods on SharePie exhibit CLOSURE OF OPERATIONS (the methods to add or subtract are closed under **SharePie**)

- *familiar formalism makes the protocol easy to grasp*. A wholly original protocol for manipulating shares could have been devised based on financial terminology. In principle, it could have been made supple. But it would have had 2 disadvantages. First, it would have to be invented, a difficult and uncertain task. Second, it would have to be learned by each person who dealt with it. People who see SharesMath recognize a system they already know, and because the design has been kept carefully consistent with the rules of arithmetic, those people are not misled.

- pulling out the part of problem that corresponded to the formalism of math, we arrived at a supple design for Shares that further distills the core **Loan** and **Facility** methods

## continuous integration

- **when a number of people are working in the same BOUNDED CONTEXT, there is a strong tendency for the model to fragment. The bigger the team, the bigger the problem, but as few as 3 or 4 people can encounter serious problems. Yet breaking down the system into ever-smaller CONTEXTs eventually loses a valuable level of integration coherency.**

- CONTINUOUS INTEGRATION means that all work within the context is being merged and made consistent frequently enough that when splinters happen they are caught and corrected quickly. CONTINUOUS INTEGRATION operates at 2 levels: 
  - the integration of model concepts 
  - and the integration of the implementation.

- institute a process of merging all code and other implementation artifacts frequently, with automated tests to flag fragmentation quickly. Relentlessly exercise the UBIQUITOUS LANGUAGE to hammer out a shared view of the model as the concepts evolve in different people's head.

## context map
- we should not directly use functionality and data structures through different bounded contexts. The bounded contexts must be encapsulated, as independent as possible. To reach this goal, bounded contexts must communicate through abstractions (interfaces) and, if necessary, translation layers or even anti-corruption layers.
To make the bounded contexts ecosystems explicitly clear, encapsulated, loosely coupled and high cohesive, we should:

- **people on other teams won't be very aware of the CONTEXT bounds and will unknowingly make changes that blur the edges or complicate the interconnections. When connections must be made between different contexts, they tend to bleed into each other.**

- ![translator example](./translator-example-route-network.png)
```java
public Itinerary route(Specification spec){
  BookingNetworkTranslator translator = new List constraintLocations BookingNetworkTranslator();
  translator.convert(spec);
  //... get access to NetworkTraversalService
  List pathNodes = traversalService.findPath(constraintLocations);
  Itinerary itinerary = translator.convert(pathNodes);
}
```
  - translator objects need to be maintained by both teams.

- testing at CONTEXT boundaries
  - contacts points with other BOUNDED CONTEXTS are particular important to test. Test help compensate for the subtleties of translation and the lower level of communication that typically exists at the boundaries. They can act as valuable early earning systems, especially reassure in cases where you depend on the details of models you don't control

- Create a global view of all bounded contexts and their relations, using context maps, naming them and adding them to the ubiquitous language. 
  - Identify the points of contact between bounded contexts, together with the used translations and abstractions. All developers must know the boundaries and to what context any given code unit belongs to.
  - Personally, I find that having diagrams of the context maps hanging in the walls of the development offices is a great way of communicating the boundaries to the team, and keeping them in mind at all times. They should include their components, contact points, translator layers, and anti-corruption layers.
  - Define teams organization to match the technical and conceptual bounded contexts we (want to) have in the project (Conway’s law).
  - Personally I also find it natural and logic to explicitly define the bounded contexts as modules and sub-modules, in the project structure.
  - Name each bounded context, and make the names part of the ubiquitous language
  - describe the point of contact between the models, outlining explicit translation for any communication. Highlighting any sharing, isolation mechanism, and levels of influence.
  - Map the existing terrain. Take up the transformations later.
  - everyone has to know where the boundaries lie, and be able to recognize the CONTEXT of any piece of code or any situation.
- how to keep track what modules belong to what contexts?
  - maybe naming conventions?
- working the CONTEXT MAP into discussions is essentials if the names are to enter the UBIQUITOUS LANGUAGE. Don't say, "George team's stuff is changing, so we're going to have to change our stuff that talks to it" Say instead, "The Transport Network model is changing, so we're going to have to change the translator for Booking context."

## partnership
- when teams in two contexts succeed or fail together, a cooperative relationship often emerges
where development failure in either of two contexts would result in delivery failure for both, forging a partnership between the teams in charge of the two contexts. Institute a process for coordinated planning of development and joint management of integration.
- The teams must cooperate on the evolution of their interface to accommodate the developments needs of both systems.
- Interdependent features should be scheduled to complete for the same release.

## shared kernel
- sharing a part of the model and associated code is a very intimate interdependency, which can leverage design work or undermine it.
- Design with an explicit boundary some subset of the domain model that the teams agree to share. Keep this kernel small.
- Within this boundary, include this subset of the model, the subset of code or the database design associated with that part of the model.
- This explicitly shared stuff has a special status and shouldn't be changed without consultation with the other team.
- When functional integration is limited, the overhead of continuous integration of a significant context may be deemed too high. This may especially be true when the team does not have the skill or the political organization to maintain continuous integration or when a single team is simply too big and unwieldy.
- uncoordinated teams working on closely related applications can go racing forward for a while, but what they produce may not fit together. They can end up spending more on translation layers and retrofitting than they would have on CONTINUOUS INTEGRATION in the first place, meanwhile duplicating efforts and lose benefits of common UBIQUITOUS LANGUAGE.
- integrate a functional system frequently, but somewhat less often than the pace of CONTINUOUS INTEGRATION within the teams. At these integrations, run the tests of both teams.
- SHARED KERNEL is often CORE DOMAIN, some set of GENERIC SUB-DOMAINS or both, but it can be any part of the model that is needed by both team. The goal is to reduce duplication (but not to eliminate it, as would be the case if there were just one BOUNDED CONTEXT), and make the integration between the two sub-systems relatively easy.

## customer/supplier development
- when 2 teams are in an upstream-downstream relationship, where the upstream team may succeed independently of the fate of the downstream team, the needs of the downstream come to be addressed in a variety of ways with a wide range of consequences.
- Establish a clear customer/supplier relationship between the two teams, meaning downstream priorities factor into upstream planning.
- Negotiate and budget tasks for downstream requirements so that everyone understands the commitment and schedule
- The customer needs are the priority while deciding the schedule of the supplier.
- jointly developed automated acceptance tests and validate the expected interface from the upstream. Adding these tests to the upstream team's test suite, to be run as part of its continuous integration, will free the upstream team to make changes without fear of downstream side effects.
- Crucial, for a customer/supplier relation to work, its that the involved teams work under the same management, who should be as hierarchically close as possible to the actual teams.

## conformist
- similar to customer/supplier, but the upstream has no motivation to provide for the downstream team's need
- to eliminate the complexity of translation between bounded contexts by slavishly adhering to the model of the upstream team.
- Ubiquitous language with your upstream team will be shared.
- Altruism may be sufficient to get them to share information with you.
- **Abandon the supplier**:  In case there are better options or the added value of maintaining such relation is not worth it. [SEPARATE WAYS]
- **Take full responsibility for translation**: If the supplier can not be abandoned but the technical quality is less than acceptable. [ANTI-CORRUPTION LAYER]
- **Adopt the foreign model**: If the quality of the supplier is acceptable and compatible, we can fully adopt its model. [CONFORMIST]
- The conformist approach can simplify integration enormously, as no translation nor anti-corruption layers would be needed, and it would provide the same ubiquitous language to both teams.
- **Shared Kernel Vs Conformist**
  - They both deal with a situation where two bounded contexts share part of the model. However, the shared kernel is appropriate only when the teams owning the modules can coordinate and collaborate tightly. When we have a situation where there is a customer/supplier frame, and collaboration is not possible, we need to use a conformist approach, or an Anti-Corruption layer.

## anti-corruption layer

- Translation becomes more complex when control or communication is insufficient to pull off a shared kernel, partner, or customer/supplier relationship. As a result, the translation takes on a more defensive tone.
- when a new system being built that must have a large interface with another, the difficulty of relating the 2 models can eventually overwhelm the intent of the new model altogether, causing it to be modified to resemble the other system's model, in an adhoc fashion. The models of legacy systems are usually weak, and even the exception that is well developed may not fit the needs of the current project. Yet there is lot of value in integration, and sometimes, it is an absolute requirements.
- create an isolating layer to provide clients with functionality in terms of their own domain model. The layer talks to the other system through its existing interface, requiring little or no modification to the other system. Internally, the layer translates in both directions as necessary between 2 models.
- **Design interface of the ANTICORRUPTION LAYER**
  - the public interface of the ANTICORRUPTION LAYER usually appears as set of services, although occasionally it can take the form of ENTITY.
  - building a whole new layer responsible for the translation between the semantics of the two systems gives us an opportunity to reabstract the other system's behavior and offer its services and information to our system consistently with our model. 
- As a downstream client, create an isolating layer to provide your system with the functionality of the upstream system in terms of your own domain model.
- This layer talks to the other system through its existing interface, requiring little or no modification to the other system. Internally, the layer translates in one or both directions as necessary between the two models.
- functionality an be added to the anticorruption layer if it is specific to the relationship of the 2 subsystems. An audit trail for use of the external system or trace logic for debugging the calls to other interface are 2 examples features.
- The Anti-Corruption layer is implemented using:
  - **FACADE**
    - An abstraction layer on top of a system API, as to limit and simplify the usage of the underlying API. Facade belongs in the BOUNDED CONTEXT of the other system.
  - **ADAPTER**
    - Which allow us to connect to different subsystems/APIs through a stable interface, implemented by all adapters who connect to equivalent subsystems/APIs.
  - **TRANSLATOR**
    - A stateless object used by the adapters, and which belongs to a specific adapter. They hold the logic to perform the conversion of conceptual objects or Entities, from one subsystem to another.

- Translation layer Vs Anti-corruption layer
  - The translation layer is collaboratively maintained by the teams owning both bounded contexts.
  - The anti-corruption layer is fully maintained by one of the team, the one owning the client module.

## open-host service
- Where integration is one-off, this approach of inserting a translation layer for each external system avoids corruption of the models with a minimum cost.
- Define a protocol that gives access to your subsystem as a set of services. Then, open the protocol so that all who need to integrate with you can use it.
- Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the protocol for that particular case so what the shared protocol can stay coherent and straightforward.
- When a subsystem has to be integrated with many others, customizing a translator for each can bog down the team. There is more and more to maintain and more and more to worry about when changes are made.

## Published language
- The translation between the models of two bounded contexts requires a common language.
- Use a well-documented shared language to express the necessary domain information as a common communication medium, translating as essential into and out of that language.
- Published language is often combined with open-host service.
- data must flow through those Services, in some language they can all understand. This language is a textual representation of the data, its a Data Interchange Language. There are currently several examples of such languages, like XML or JSON, and there are even more specific languages based on base languages like the mentioned XML or JSON. For example, a widely used specific XML representation of pharmaceutical data.
- direct translation to and from the existing domain models may not be a good solution. Those models may be overly complex or poorly factored. They are probably undocumented. If one is used as a data interchange language, it essentially become frozen and cannot respond to new development needs.

## separate ways

- declare a bounded context to have no connection to the others, allowing developers to find simple, specialized solutions within this small scope.
- "*Integration is always expensive. Sometimes the benefit is small.*"
- We should only integrate sub-systems if we really, REALLY, need to. We should, as much as possible, define bounded contexts that are completely independent, completely disconnected from other bounded contexts, and therefore have no need for integration.


## big ball of mud
- well-defined context boundaries only emerge from intellectual choices and social forces (even though the people creating the systems may not always have been consciously aware of these causes at the time).
- Draw a boundary around the entire mess and designate it as a big ball of mud. Do not try to apply sophisticated modelling within this context.
- Be alert to the tendency for such systems to sprawl into other contexts.

# Distillation for strategic design
- how do you focus on your central problem and keep from drowning in a sea of side issues?
- Distillation is the process of separating the components of a mixture to extract the essence in a form that makes it more valuable and useful
- A model is a distillation of knowledge.
- Going through this distillation process has several benefits:
  - Makes the overall design explicit and known;
  - Distinguishes what is Core Domain from what is Generic Domain, reducing them to manageable sizes;
  - Focus the software evolution (development and refactoring) in what is more relevant at a given moment.
- strategic distillation of a domain model does all of the following:
  - aids all team members in grasping the overall design of the system and how it fits together
  - facilitates communication by identifying a core model of manageable size to enter the UBIQUITOUS LANGUAGE
  - guides refactoring
  - focuses work on areas of the model with the most value
  - guides outsourcing, use of off-the-shelf components, and decisions about assignment.
- ![navigation map for strategic distillation map](./strategic-distillation-navigation-map.png)

## Integrating sub-modules

- A large scale domain model is composed of smaller domain models.
- However, the smaller domain models don’t even have to agree on their view of the global domain model. As long as they operate on their own, we can maintain their integrity.
- It’s only when they need to integrate, that we might need to find common views on the models.

- Several strategies can be used to integrate sub-models:

  - Draw a Context Map of the **current** state of the model;
  - Define the Bounded Contexts borders with the whole dev team;
  - Guarantee that the Bounded Contexts borders and relation are known and understood by the whole dev team;
  - We must carefully model **aiming at small or large Bounded Contexts** by considering their advantages:
    - Advantages of large models:
      - Its easier to understand one model than several models plus their mappings;
      - There is no need for translation layers, which might be complex;
      - One shared language eases communication.
    - Advantages of small models:
      - Needs less communication between developers working in the same model;
      - Its easier to manage smaller code bases and teams;
      - Smaller contexts are simpler, requiring less skills of versatile abstract models from the developers;
      - Smaller models provide more flexibility to the global model.
      - continuous integration is easier with smaller teams and code bases.
  - Identify and alienate what is not part of our bounded context. A good starting is to exclude **what can not change** and **what we do not need** in our bounded context;
  - When **integrating external systems**, we can consider 3 patterns:
    - SEPARATE WAYS: Only integrate if we really need to, otherwise keep them completely isolated;
    - CONFORMIST: Fully adhere and rely on the external system model;
    - ANTI-CORRUPTION LAYER: Completely isolate the two systems, allowing them to communicate through a middle-ware, requiring no changes to either system.
  - When **integrating internal systems** (inside the same bounded context) we can:
    - Use a SHARED KERNEL to split relatively independent functionality into separate bounded contexts.
    - Set up CUSTOMER/SUPPLIER DEV TEAMS, if all the dependencies of the subsystems go in one direction;
    - Go SEPARATE WAYS, if for some reason its not possible to integrate the sub-systems;
    - Use a TRANSLATION LAYER, to connect both systems, which is maintained by the teams of both systems.
  - Deployment of new versions must be carefully coordinated by the teams owning the bounded contexts that connect, and as such the Bounded Contexts boundaries must be defined with these issues in mind:
    - Customer/Supplier structures must be tested together to prevent regressions;
    - Long deployments must be managed carefully to minimize issues with data migration temporary inconsistencies;
    - A Shared Kernel update must be tested and verified to satisfy all client systems to prevent regressions.
  - In the end, like most architectural decisions, the decision of how to integrate the sub-models in our global model, relies on trade-offs.
  - Here, in the extremes, we are trading off decoupled logic and management of that logic, for easier and faster integration of functionality.
  - ![decouple logic and simplicity trade off](./decoupling_vs_simplicity.png)


## Refactoring Bounded Contexts ecosystem

- When we already have a system in place and we want to refactor it, the first step is to identify the current situation. For this, we need to create a schema of the current configuration of the bounded contexts (sub-models) in our system.

- From this clear view of the current situation, we can start breaking or merging contexts. While breaking up a bounded context is usually easy, merging them is usually quite difficult, as there can exist very different concepts and models. We will typically want to merge contexts when there is too much translation overhead or duplication.

- Eric Evans gives us two options:

  - If in a “pain driven” refactoring, we need to find the root cause of the problem and start there, wherever that is.
  - If in a “all out” refactoring, we need to start by refactoring the Core Domain into segregated Core Domains, Generic Subdomains and Cohesive Mechanisms.

- **From SEPARATE WAYS to SHARED KERNEL**
  - Define one of 3 strategies:
    - Refactor one context into the other context model;
    - Create a new context with the best pieces of each of the contexts;
    - Create a completely new, deeper model, which can replace both the initial models.
  - Create a small team with developers from both the initial teams;
  - Define the new shared model:
    - Decide the code to be shared, identifying overlaps/duplications in both initial models;
    - Decide naming conventions;
  - Create a basic test suite for the shared kernel, which will grow along with the implementation;
  - Implement the new model, merging frequently and rethinking it when needed;
    - Start simple, with code that is non-critical, duplicated in both contexts. Something being translated is a good choice;
  - Integrate the original contexts with the new Shared Kernel;
  - Remove any obsolete code (translation layers, etc.).

- **From SHARED KERNEL to CONTINUOUS INTEGRATION**

  - If the Shared Kernel continues to grow, maybe we should completely merge the Bounded Contexts. This, however, involves not only the code but also the teams structure, their work-flow and their language.

    - Create the same work-flow in both teams;
    - Set-up Continuous Integration in both teams;
    - Circulate developers in both teams, as means to sharing and spreading knowledge;
    - Distill each model individually;
    - Start merging the core domain, doing it as fast as possible, prioritizing it above most new development, so we don’t lose the momentum. Beware not to leave out any specialized functionality needed by the users;
    - As the Shared Kernel grows, increase the integration frequency until we have continuous integration;
    - The goal is to, in the end, have one big team, or two small teams who circulate members and do continuous integration.

- **Phasing out a legacy system**

  - Phasing out a legacy system means, most of the times, replacing it for one or several newer systems.

    - Identify a small piece of the legacy system that can be moved to one of the new systems;
    - Identify additions needed in the Anti-Corruption layer;
    - Implement
    - Deploy
    - Identify obsolete code in the Anti-Corruption layer and remove it;
    - Identify obsolete code in the legacy system and, if possible, remove it.

- **From OPEN HOST SERVICE to PUBLISHED LANGUAGE**

  - Sometimes, when in an Open Host Service architecture, we will have several ad-hoc protocols specific to each communication situation. There is no common, standard communication protocol.

  - As the need to integrate with more systems grows, the amount of communication specificities grows as well: Scalability and maintainability are at risk.

  - Therefore we need a common, standard, communication Interchange Language that any system con use to communicate with our system, we need a published language:

  - If possible, use an industry standard language;
  - If its not possible to use an industry standard language, create your own:
    - Start by making the core domain as clear as possible;
    - Use the core domain as the base for the new interchange language;
    - If possible, use a general purpose Interchange Language Syntax (XML, JSON) as a base for our new Interchange Language;
    - Publish the language, making it known to all involved in the systems collaboration;
    - Publish any architectural changes as well;
    - Build translation layers for all collaborating systems;
    - Switch to the new Interchange Language.
  - the published language must be stable, yet you'll still need the freedom to change the host's model as you continue your relentless refactoring. Therefore, do not equate the interchange language and the model of the host. Keeping them close together will reduce the translation overhead.


## Core Domain

- to make a domain model an asset, the critical core (the real business asset) of that model has to be sleek and fully leveraged to create application functionality.
- Boil the model down. Define a core domain and provide a means of easily distinguishing it from the mass of supporting model and code.
- **Bring the most valuable and specialized concepts into sharp relief. Make the core small.**
- **Spend the effort in the core to find a deep model and develop a supple design - sufficient to fulfill the system's vision. Justify investment in any other party by how it supports the distilled CORE**
- **The harsh reality is that not all parts of the design are going to be equally refined. Priorities must be set. To make the domain model an asset, the model's critical core has to be sleek and fully leveraged to create application functionality. But scarce, highly skilled developers tend to gravitate to technical infrastructure or neatly definable domain problems that can be understood without specialized domain knowledge.**
  - such parts of the system seem interesting to computer scientists, and are perceived to build transferable professional skills and provide better resume material. The specialized core, that part of the model that really differentiates the application and makes it a business asset, typically ends up being put together by less skilled developers who work with DBA(s) to create a data schema and then code feature-by-feature without drawing on any conceptual power in the model at all.
- Within the Domain, the Core Domain (the real business asset) is the actual purpose of the application, is the reason of its existence, its why we started building it in the first place.
- In shipping application, the CORE could be the model of how cargoes are consolidated for shipping, how liability is transferred when containers change hands, or how a particular container is routed on various transports to reach its destination.
- The distillation and definition of the core domain is crucial and it should drive human resources hiring and allocation, as well as the biggest design effort to create a supple and maintainable design:
  - Hire developers that fit best with the Core Domain;
  - Assign the best developers to the Core Domain;
  - Try your best to keep the Core Domain the priority in suppleness and maintainability;
  - Refactorings that most closely affect the Core Domain should have priority;
- **The greatest value of custom software comes from the total control of the Core Domain**.
  - Create long term relations with your best, most committed and interested domain experts;
  - Create opportunities for our best technical experts to learn the Domain;
  - Assign our best, most committed, interested and long term connected developers to develop and maintain the Core Domain;
  - Use a well designed framework to save us from developing the most generic parts and leave us free to focus on the core.
  - a well designed framework may be able to provide high-level abstractions that you can specialize for your use. It may save you from developing the more generic parts and leave you free to concentrate on your CORE, however, cautious the followings:
    - you are losing an essential software asset. Back off restrictive frameworks in your CORE DOMAIN
    - the area treated by the framework is not as pivotal as you thought. Redraw the boundaries of the CORE DOMAIN to the truly distinctive part of the model
    - you don't have special needs in your CORE DOMAIN. Consider a lower-risk solution, such as purchasing software to integrate with your applications


## generic subdomains
- some parts of the model add complexity without capturing or communicating specialized knowledge.
- An example of a Generic Sub-Domain is “time-zones”. Although time-zones are needed, and maybe even crucial, they are not part of our main business.
- We need to:
  - Identify cohesive Sub-Domains that are not the main motivation of our project;
  - Extract those Sub-Domains into cohesive and decoupled modules;
  - Consider using existing solutions (community off-the-shelve solutions).
  - Leave no trace of your specialties in them.
  - once they have been separated, give their continuing development lower priority than the core domain, and avoid assigning your core developers to the tasks (because they will gain little domain knowledge from them)
  - also, consider off-the-shelf solutions or published models for these generic subdomains.

## domain vision statement
- the critical aspects of the domain model may span multiple bounded contexts, but by definition, these distinct models can't be structured to show their common focus.
- Write a short description (about one page) of the core domain and the value it will bring, the "value proposition." ignore those aspects that do not distinguish this domain model from others.
- Write this statement early and revise it as you gain new insight.
- It can be derived from a Project Vision Statement, but it is more specific, it focus on the nature of the Domain Model, its value and differential.
- It is a document that should be used through the whole development process, helping to guide resource allocation, guide modelling choices and educate team members.
- This will help keep the team focus on what is really important in the project and the Domain at hand.
- ![domain vision example 1](./domain-vision-example-1.png)
- ![domain vision example 2](./domain-vision-example-2.png)

## highlighted core
- a domain vision statement identifies the core domain in broad terms, but it leaves the identification of the specific core model elements up to the vagaries of individual interpretation. Unless there is an exceptionally high level of communication on the team, the vision statement alone will have little impact.
- **The mental labour of constantly filtering the model to identify the essential parts absorbs concentration better spent on design thinking, and it requires comprehensive knowledge of the model. Therefore, the core domain must be made easier to see.**
  - extensive formal documentation, using UML and other diagramming. For example, a digital document vault
  - reduced and informal, but visible, documentation of concepts. For example, a context diagram, hand drawn, hanging on the office wall.
  - light-weight architecture records.
  - brief documents describing the Core Domain and the interactions between its elements. This document should be minimalistic, should not contain implementation details, on the contrary, it should focus on abstraction, broad strokes, the stable concepts.
- **Write a brief document (3-7 sparse pages) describing the core domain and the primary interactions among core elements.**
- Flag the elements of the core domain within the primary repository of the model without particularly trying to elucidate its role. Make it effortless for a developer to know what is in or out of the core.
- Although the vision statement and highlighted core inform and guide, they do not modify the model or the code itself.
- Partitioning generic subdomains physically removes some distracting elements.

## cohesive mechanisms
- structurally change the model and the design to make the core domain more visible and manageable.
- **The conceptual "what" is swamped by the mechanistic "how." Many methods that provide algorithms for resolving the problem obscure the methods that express the problem.**
- Partition a conceptually cohesive mechanism into a separate lightweight framework. Particularly watch for formalisms or well-documented categories of algorithms.
- **Expose the capabilities of the framework with an intention-revealing interface.**
- The other elements of the domain can focus on expressing the problem ("what"), delegating the intricacies of the solution ("how") to the framework.
- **Factoring out generic subdomains reduces clutter, and cohesive mechanisms serve to encapsulate complex operations. This leaves behind a more focused model, with fewer distractions that add no particular value to how users conduct their activities.**
- You are unlikely to find good homes for everything in the domain model that is not core.
- To help maintainability, simplicity and usability of the Domain classes, we should extract cohesive mechanisms sets into separate libraries which can then be used by the Domain objects, through interfaces, keeping these smaller, focused and more expressive.

- The CORE DOMAIN and a GENERIC SUBDOMAIN formulate facts, rules or problems.

- A COHESIVE MECHANISM resolves a rule as needed by the model, and can be used as a separate library.

- An example of a COHESIVE MECHANISM is a graph traversal framework which, although being a generic programming theme with many possible algorithms, implements only the traversal algorithms needed by the Domain.

- Another example can be a STATE MACHINE library, which is a generic cohesive concept who’s complexity can be kept away from the Domain and used through an intention revealing interface.

- Yet another example can be a library to construct SPECIFICATION objects.
- **Generic Subdomains Vs Cohesive Mechanisms**
  - Both Generic Subdomains and Cohesive Mechanisms share the goal of responsibility segregation and keeping the Core Domain focused on what is more relevant in the domain.
  - The difference is that the Generic Subdomain is still part of the Domain, although not as important as the Core Domain, and a Cohesive Mechanism is not part of the Domain at all, it is used by the Domain to solve a very generic problem, using a set of cohesive algorithms.

## The segregated core
- approach to structurally marking off the core domain.
- Refactor the model to separate the core concepts from supporting players (including ill-defined ones) and strengthen the cohesion of the core while reducing its coupling to other code.
- Factor all generic or supporting elements into other objects and place them into different packages.

## abstract core
- The core domain model usually has so much detail that communicates the big picture.
- Identify the most fundamental differentiating concepts in the model and factor them into distinct classes, abstract classes, or interfaces.
- Design this abstract model to express most of the interaction between significant components.
- Place this abstract model in its own module, while the specialized, detailed implementation classes are left in their own modules defined by the subdomain.

# large scale structure for strategic design

- *layers would outline their story of the system*

- in a large system without any overarching principle that allows to be interpreted in terms of their role in patterns that span the whole design, developers cannot see the forest for the trees.

- A "large-scale structure" is a language that lets you discuss and understand the system in broad strokes. A set of high-level concepts or rules, or both, establishes a pattern of design for an entire system.

- **Devise a pattern of rules or roles and relationships that will span the entire system and allow some understanding of each part's place in the whole-even without detailed knowledge of the part's responsibility.**

- ![some patterns of large scale structure](./some-patterns-large-scale-structure.png)

## evolving order

- Architectures can straitjacket a project with up-front design assumptions and take too much power away from the developers/designers of particular application parts. Soon, developers/designers of specific details of the applications will dumb down the application to fit the structure, or they will subvert it and have no structure, bringing back the problems of uncoordinated development.
- Let this large-scale conceptual structure evolve with the application, possibly changing to a completely different type of structure along the way. Don't constraint the detailed design and model decisions that must be made with thorough knowledge.
- unlike the CONTEXT MAP, a large-scale structure is optional. One should be imposed when costs and benefits favor it, and when a fitting structure is found.
- The large-scale structure should be applied when a structure can be found that dramatically clarifies the system without forcing unnatural constraints on model development. Because an ill-fitting structure is worse than none, it is best not to shoot for comprehensiveness but rather to find a minimal set that solves the emerging problem. Less is more.

## system metaphor
- software designs tend to be abstract and hard to grasp. Developers and users alike need tangible ways to understand the system and share a view of the system as a whole.
- When a concrete analogy to the system emerges that captures the imagination of team members and seems to lead thinking in a helpful direction, adopt it as a large-scale structure.
- Organize the design around this metaphor and absorb it into the ubiquitous language.
- The system metaphor should facilitate communication about the system and guide the development. This increases consistency in different system parts, potentially even across different bounded contexts.
- Because all metaphors are inexact, continually reexamine the metaphor for overextension or inaptness, and be ready to drop it if it gets in the way.

## responsibility layers
- look at the conceptual dependencies in your model and the varying rates and sources of change of different parts of your domain.
- If you identify natural strata in the domain, cast them as broad abstract responsibilities.
- **These responsibilities should tell a story of your system's high-level purpose and design.**
- **Refactor the model so that the responsibilities of each domain object, aggregate, and module fit neatly within the responsibility of one layer.**

## knowledge level
- a group of objects that describe how another group of objects should behave.
- Create a distinct set of objects that can define and constrain the structure and behaviour of the basic model.
- **Keep these concerns separate as 2 "levels," one very concrete, the other reflecting rules and knowledge that a user or super-user can customize.**
  
## Pluggable component framework
- a pluggable component framework usually only comes into play after a few applications have already been implemented in the same domain.
- Distill an abstract core of interfaces and interactions and create a framework that allows diverse implementations of those interfaces to be freely substituted. Likewise, it will enable any application to use those components, so long as it operates strictly through the interfaces of the abstract core.


# Project assessment
- Draw a context map. Can you draw consistent one, or are there ambiguous situations?
- Establish or refine the Ubiquitous Language. is it rich enough to help development?
- is the CORE DOMAIN identified? is there a DOMAIN VISION STATEMENT? Can you write one?
- Is the technology of the project work for or against a MODEL DRIVEN DESIGN?
- Assess the team developers skills to match them to the project complexity
- Are the developers knowledgeable about the domain? Are they interested in the domain?

# Who sets the strategy?

- **Ivory tower architect**
  - This is an organizational style that has an architect which analyses the project at hand and determines the strategy before the project starts to be developed. This fits with the waterfall project management style but goes against the DDD approach, based in an Agile methodology and evolving architecture.

- **Emergent structure from application development**

  - Typically, in a team doing Extreme Programming, the architectural structure emerges from the development process itself. However, the global design may become inconsistent. In order to keep the global architecture design consistent, it is a good practise to have a strategic design leadership (also hands-on developer), as a role played by one or several of the team developers.

- **Customer focused architecture team**
  - This is a team of architects who is there to serve, to help the development teams by collaborating, experimenting, distillating the domain with the developers.
  - Eric Evans gives us 6 guidelines for this collaboration:
    - **Decisions must reach the entire team**
      - This can achieved by having an architecture team with official authority to formalize rules, or it can be achieved by having the strategy come out of the application development team;
    - **The decision process must absorb feedback**
      - The architecture decision makers need to receive, accept and respond to the development team feedback. This can be achieved through collaboration, and it is a good practise to rotate the architects through the development teams;
    - **The plan must allow evolution**
      - It’s good to have some higher level design rules, but we must be flexible and allow them to change/evolve as needed.
      - EVOLVING ORDER emphasize ongoing change to the large-scale structure in response to deepening insight.
    - **Architecture teams must not absorb all good designers**
      - It is essential to have good designers in all application teams:
        - In the architecture teams, so that a good design is created
        - In the development teams, so that the design is properly implemented
      - It is essential to have domain knowledge in all application teams:
        - In the Architecture teams so that the design created matches the domain
        - In the development teams so that the domain is well reflected in the implementation
  - **Strategic design requires minimalism and humility**
      - We need to not get carried away when creating an architectural design. Over engineering a system will in fact bring more problems than solutions. We need to keep it simple and be humble when our great design idea is found to be, in fact, counter productive.
  - Objects are specialists, developers are generalists
  - Developers, in the other hand, should be application generalists, with knowledge about architecture, development and domain.
  - beware of technical frameworks that interfere with expressive implementation of the domain model and easy change
  - Alexander and his colleagues advocated for a set of principles for all community members to apply to every act of piecemeal growth, so that "organic" order emerges, well adapted to circumstances.

# DDD with legacy code
- [DDD with legacy code](/ddd-with-legacy-code)

# Questions

- **how to mange same model in different sub-systems?**
  - like user in participant? financial reporting? plan admin?

- **Knowledge Crunching: How a team can accumulate, distill and apply domain knowledge to software development?**
  - **Effective modelling is based on:**
    - Binding model and implementation
      - The implementation is strictly based on the model;
    - Cultivating a language based on the model
      - The model contains terms which are the base of a language common to both Domain Experts and Developers;
    - Developing a knowledge rich model
      - The model must be more than a representation of data structures, it must contain all kinds of knowledge. It must contain ideas, data structures, objects, behaviours, enforced rules, etc.
    - Distilling the model
      - A model must contain all, but also only, the relevant knowledge. This means that as we gain knowledge about the domain, we add the relevant knowledge to the model, but we can and must also remove, from the model, the domain knowledge that we end up figuring out that is not relevant after all.
    - Brainstorming and experimenting
      - Brainstorming and experimentation meetings between domain experts and developers, where massive experimentation and discussion takes place, is what ends up providing a distilled and knowledge rich model.
  - **The most productive teams are continuously learning about:**
    - Technical knowledge
    - Domain modeling knowledge
    - Knowledge specific to the domain of the project

- **Ubiquitous Language: How to bring about a clearer and more dynamic flow of domain knowledge throughout the project?**
  - **The Ubiquitous Language will include the terms used to discuss the model and the high level principles and patterns incorporated into the model. It must be used as much as possible, among developers, domain experts and between both of them**.
  - the terminology of day-to-day discussions is disconnected from the terminology embedded in the code (ultimately the most important of a software project). And even the same person uses different language in speech and in writing, so that the most incisive expressions of the domain often emerge in a transient form that is never captured in the code or even in writing.
  - translation blunts communication and makes knowledge crunching anemic
  - iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model. Resolve confusion over terms in conversation, in just the way we come to agree on the meaning of ordinary words.
  - domain experts should object to terms or structures that are awkward or inadequate to convey domain understanding; developers should watch for ambiguity or inconsistency that will trip up design.
  - play with the model as you talk about the system. Describe scenarios out loud using the elements and interactions of the model, combining concepts in ways allowed by the model. Find easier ways to say what you need to say, and then take those new ideas back down to the diagrams and code.
  - if sophisticated domain experts don't understand the model, there is something wrong with the model.

- **How documents & diagrams can work for a project instead of just being work?**
  - It's important to know that diagrams do not need to have the full context of the model. The goal of the diagram is to explain the model and they should be as simple as possible. You should use diagram and documents to explain the model but they don't have to be a replica of the model. 
  - a document should not do what the code already does well, which is to provide details
  - a document must be involved in project activities
  - light-weight architecture decision records?
  - is the document written in the language people speak on the project? is it written in the language embedded in the code?
  - if the terms explained in a design document don't start showing up in conversations and code, the document is not fullfilling its purpose.
  - as the domain model comes to reflect the most relevant knowledge of the business applications become scenarios within that model, and the ubiquitous language can be used to describe such a scenario in terms that directly connect to the model driven design, as a result, specifications can be written more simply because they do not have to convey the business knowledge that lies behind the model.
  - keeping documents minimal and focusing them on complementing code and conversation, documents can stay connected to the project. Let the ubiquitous language and its evolution be your guide to choosing documents that live and get woven into the project's activity.

- **What is model driven design?**
  - contrasting 3 projects
    - project 1 lacked domain model, or even common language on the project and were saddled with unstructured design. A year later, the team found itself bogged down unable to deliver the second version due to complexity in business logic.
    - project 2 has incisive model, repeatedly refined and expressed in code, as the team gained new insight into the new domain, the model deepened. The quality of communication improved not only among developers, but also between developers and domain experts, and the design, far from imposing an ever heavier maintenance burden, became easier to modify and extend.
    - project 3 involves teams with good tools and good understanding of business and it gave careful attention to modeling. But a poorly chosen separation of developer roles disconnected modeling from implementation, so that the design did not reflect the deep analysis that was going on. Repeated iteration produced no improvement in code, due to uneven skill levels among developers, who had no awareness of the informal body of style and technique for creating model-based objects that also function as practical running software. As months rolled by, development work became mired in complexity and the team lost its cohesive vision of the system.
  - a domain model is not a particular diagram, it is the idea that the diagram is intended to convey. It is not just the knowledge in a domain's expert's head. It is a rigorously organized and selective abstraction. 
  - a model is a selectively simplified and consciously structured form of knowledge. An appropriate model makes sense of information and focuses it on a problem.
  - The utility of a model in domain-driven design
    - **the model and the heart of the design shape each other**. It is the intimate link between the model and the implementation that makes the model relevant and ensures that the analysis that went into it applies to the final products.
    - **the model is the backbone of a language used by all team members**.
    - The model is distilled knowledge: the model is the team's agreed upon way of structuring domain knowledge and distinguishing the elements of most interest. The model captures how we choose to think about the domain as we select terms, break down concepts, and relate them.

  - refer to the "How documents & diagrams can work for a project instead of just being work?" question on how documents and diagrams can help with model driven design
  - refer to [model driven design](#model-driven-design)
  - when a design is based on a model that reflects the basic concerns of the users and domain experts, the bones of the design can be revealed to the user to a greater extent than with other design approaches. Revealing the model gives the user more access to the potential of the software and yields consistent, predictable behaviors.


- **What Constitutes a Useful Model-Driven Design and How to Go About Finding Such a Design?**
  - True story: How model-driven design rescued a project and created unexpected opportunities.
    - ![original models](./original-models.png)
    - model incrementally changed to solve problems. Loan Adjustments track departures from the share a lender originally agreed to in the Facility.
      - ![model-incrementally-changed](./incrementally-model-changed.png)
      - refinements of this kind allowed the team to keep up as the rules of various transactions became clearer. But complexity was increasing, and we did not seem to be converging quickly onto really solid functionality.
      - deeper model
        - ![abstract-model-of-shares](./abstract-model-of-shares.png)
        - The **Loan Investment** had disappeared, and at this point we realized that "loan investment" was not a banking term. In fact, the business experts had told us a number of times that they didn't understand it. They had deferred to our software knowledge and assumed it was useful to the technical design. Actually, we had created it based on our incomplete understanding of the domain.
        - suddenly, on the basis of this new way of looking at the domain, we could run through every scenario we had ever encountered relatively effortlessly, much more simply than ever before. And our model diagrams made perfect sense to the business experts, who had often indicated that the diagrams were "too technical" for them. Even just sketching on a whiteboard, we could see that our most persistent rounding problems would be pulled out by the roots, allowing us to scrap some of the complicated rounding code.
        - it takes about 3 weeks to refactor to the new model without enough tests. Luckily, the project manager can take the heat and manage through the unstable political situation.
        - **Share Pie** became the unifying theme of the whole application. Marketing people used it to explain the features to prospective customers. Those prospects and customers immediately grasped it and used it to discuss features. It truly became part of the UBIQUITOUS LANGUAGE because it got to the heart of what loan syndication is about.
        - To set the stage for a breakthrough, concentrate on knowledge crunching andn cultivating a robust UBIQUITOUS LANGUAGE. Probe for important domain concepts and make them explicit in the model. Refine the design to be suppler. Distill the model. Push on these more predictable levers, which crease clarity, usually a precursor of breakthroughs.
        - dont't hold back from modest improvements, which gradually deepen the model, even if confined within the same general conceptual framework. Don't be paralyzed by looking too far forward. Just be watchful for the opportunity.
        - ![another model breakthrough where contrains on transactions could be expressed with easy precision](./another-model-breakthrough-contrains-transactions.png)

  - How software experts can work with domain experts to explore and refine models?
    - **many transformations of domain models and the corresponding code happen when developers recognize a concept that has been hinted at in discussion or present implicitly in the design, and they then represent it explicitly in the model with one or more objects or relationships.**
    - **listen to the language the domain experts use. Are there terms that succinctly state something complicated? Are they correcting your word choice (perhaps diplomatically)? do the puzzled looks on their faces go away when you use a particular phrase? These are hints of a concept that might benefit the model.**
    - ![original cargo design with database](./original-cargo-design-with-database.png)
    - ![after cargo design with routing service](./after-cargo-design-with-routing-service.png)
    - benefits of refactoring to the explicit Itinerary object:
      - Defining the interface of the **routing service** more expressively
      - decoupling the **routing service** from the booking database tables
      - clarifying the relationship between the booking application and the operations support application (the sharing of the **Itinerrary** object)
      - reducing duplication, because the **Itinerary** derives loading/unloading times for both the booking report and the operations support application.
      - removing domain logic from the booking report and placing it in the isolated domain layer.
      - expanding the "UBIQUITOUS LANGUAGE", allowing a more precise discussion of the model and design between developers and domain experts and among the developers themselves.
    - **scrutinize awkwardness**
      - the place to dig is the most awkward part of your design. The place where procedures are doing complicated things that are hard to explain. The place where every new requirements seems to add complexity
      - If you are lucky, the domain experts may enjoy playing with ideas and experimenting with the model. If you are not that lucky, you and your fellow developers will have to come up with the ideas, using the domain expert as a validator, watching for discomfort or recognition on this or her face.
    - **business rules often do not fit the responsibility of any of the obvious ENTITIES OR VALUE OBJECTS, their variety and combinations can overwhelm the basic meaning of the domain object. But moving the rules out of the domain layer is even worse, since the domain code no longer express the model. Logic programming provides the concept of separate, combinable, rule objects called "predicates", but full implementation of this object is cumbersome. It is also so general that it doesn't communicate  intent as much as more specialized designs**
    - **create explicit predicate-like VALUE object for specialized purposes. A SPECIFICATION is a predicate that determines if an object does or does not satisfy some criteria**
    - **Contemplate contradictions**
      - Different domain experts can have different views on a particular part of the domain, according to their knowledge and experience.
      - Most of the times, the contradictions are merely terminology differences and misunderstandings, however sometimes there is an actual clash of ideas.
      - Either way, when we find a contradiction, we need to clarify it with the domain experts.
    - read the book on the domain
    - **try, try again**
      - All the knowledge crunching is interactive, it doesn’t happen in one go. It involves a lot of experimentation, a lot of trial and error. It takes time, but it deepens the model, it makes the model reflect what is indeed needed and, in the long run, it ends up being faster.
  
  - Supple Design: How a system can become easier to extend and adapt rather than ossifying into legacy?
    - **explicit constraints**
      - factoring constraint into its own method allows us to give it an intention-revealing name that makes the constraint explicit in our design.
      - here's some warning signs that a constraint is distorting the design of its host object.
        - evaluating a constraint requires data that does not otherwise fit the object's definition
        - related rules appear in multiple objects, forcing duplication or inheritance between objects that are not otherwise family
        - a lot of design and requirements conversation revolves around the constraints, but in the implementation, they are hidden away in procedural code.
      - when the constraints are obscuring the object's basic responsibility, or when the constraint is prominent in the domain yet not prominent in the model, you can factor it out into an explicit object or even model it as a set of objects and relationships.
    - For this, the **SPECIFICATION Design Pattern** comes up: **A class who’s only purpose is to evaluate if a specific condition/predicate/business rule is met**
      - Eric Evans identifies 3 situations where we should use a Specification pattern:
        - **Validation**: Validate if an object fulfills some need or is ready for some purpose;
        - **Selection**: To select an object from an hydrated collection by cycling through all elements and filtering them or by using a query language like SQL, although in this case we should put the actual SQL outside of the Specification class, in a Repository.
        - **Generation**: Specify what object to create to fit some need. This means we can pass a Specification into a Factory and have it decide what object to instantiate, and how.
    - ![supple design overview](./supple-design-overview.png)
    - [supple design](#supple-design)
  
  - Overview of the rhythm of domain-driven design and how it allows for upside surprise opportunities to emerge.
    - refactoring toward deeper insight
      - it maybe a response to a problem in the code, some complexity of awkwardness. Perhaps a concept is missing. Maybe some relationship is wrong.
      - is the language of the model disconnected from the domain experts?
      - are the requirements fitting in naturally?
      - **exploration teams**
        - self-determination: a small-team can be assembled on the fly to explore a design problem. The team can operate for a few days and then disband. There is no need for long-term, elaborate organizational structures
        - scope and sleep: 2 or 3 short meetings spaced out over a few days should produce a design worth trying. Dragging it out doesn't help. If you get stuck, you may be taking on too much at once. Pick a smaller aspect of the design and focus on that.
        - exercising the UBIQUITOUS LANGUAGE: involving the other team members - particularly the subject matter expert, in the brainstorming session creates an opportunity to exercise and refine the UBIQUITOUS LANGUAGE. The end result of the effort is a refinement of that LANGUAGE which the original developer(s) will take back and formalize in code.
      - **prior art**
        - although the in the field may not have created a model suitable for running software, they may well have organized the concepts and found some useful abstractions.
        - analysis patterns can give you subtle model concepts and help you avoid lots of mistakes. But they don't give you a cookbook recipe. They feed the knowledge crunching process.
      - a design for developers
        - software isn't just for users. It's also for developers. Developers have to integrate code with other parts of the system.
        - a supple design communicates its intent. The design makes it easy to anticipate the effect of running code, and therefore it easy to anticipate the consequences of changing it. A supple design helps limit mental overload primarily by reducing dependencies and side effects. It is based on a deep model of the domain that is fine-grained only where most critical to the users. This makes for flexibility where change is most common, and simplicity elsewhere.
      - **timing**
        - *if you wait until you can make a complete justification for a change, you've waited too long.* Therefore, refactor when:
          - the design does not express the team's current understanding of the domain
          - important concepts are implicit in the design (and you see a way to make them explicit)
          - you see an opportunity to make some important part of the design suppler.

  - What are the three principles for applying domain-driven design to large projects and enterprises?
    - strategic design principles must guide design decision to reduce the interdependence of parts and improve clarity without losing critical interoperability and synergy. They must focus the model to capture the conceptual core of the system, the "vision" of the system. And *they must do all this without bogging the project down*. To help accomplish these goals, there are 3 board theme, context, distillation, and large-scale structures
    - **context**: a successful model, large or small, has to be logically consistent throughout, without contradictory or overlapping definitions. By explicitly defining the BOUNDED CONTEXT within which a model applies and then, when necessary, defining its relationship with other contexts, the modeler can avoid bastardizing the model.
    - **distillation**: reduces the clutter and focuses attention appropriately. Often a great deal of effort is spent on peripheral issues in the domain. The overall domain model needs to make prominent the most value-adding and special aspects of your system and be structured to give that part as much power as possible. While some supporting components are critical, they must be put into their proper perspective. This focus not only helps to direct efforts toward vital parts of the system, but it keeps the vision of the system from being lost. Strategic distillation can bring clarity to a large model. And with clearer view, the design the CORE DOMAIN can be made more useful.
    - **large scale structure**: In a very complex model, you may not see the forest for the trees. Some system-wide design elements and patterns can help. Some such structure can bring a uniformity to the design and accelerates development and improve integration.
    - these 3 principles, useful separately but particularly powerful taken together, help to produce good designs, even in a sprawling system that no one completely understands. Large scale structure brings consistency to disparate parts to help those parts mesh. Structure and distillation make the complex relationships between parts comprehensible while keeping the big picture in iew. BOUNDED CONTEXTS allow work to proceed in different parts without corrupting the model or unintentionally fragmenting it. Adding these concepts to the team's UBIQUITOUS LANGUAGE helps developers work out their own solutions.

- **Bounded Context: Strategies for dealing with the inevitability of multiple viewpoints and conflicting needs.**
  - ![model integrity patterns](./model-integrity-patterns.png)
  - [bounded context](#bounded-context)
  - [continuous integration](#continuous-integration)
  - [context map](#shared-kernel)
  - [customer supplier development](#customersupplier-development)
  - [conformist](#conformist)
  - [anticorruption layer](#anti-corruption-layer)
  - [separate ways](#separate-ways)
  - [open host service](#open-host-service)
  - [published language](#published-language)
  - unifying multiple models almost always means creating a new model.
  - By explicitly defining a context within which each model applies, you can maintain the integrity of each and clearly see the implication of any particular interface you want to create between the two.
  - ![context strategies trade-off](./decoupling_vs_simplicity.png)

- **Distillation: How do you focus on your central problem and keep from drowning in a sea of side issues?**
  - [distillation for strategic design](#distillation-for-strategic-design)
  - [core domain](#core-domain)
  - A Tale of Two Time Zones: A right way and a wrong way to deploy your people to tackle essential supporting components
    - ![tale of 2 timezone trade off](./tale-of-2-time-zone.png)
    - we technical people tend to enjoy definable problem like timezone conversion, and we can easily justify spending our time on them, but disciplined look at priorities usually point to the CORE DOMAIN 
  - Reducing project risk by tackling the core domain early 413-414
    - **generic doesn't mean reusable**
      - you should be applying as much of your effort to the CORE DOMAIN as possible and investing in supporting GENERIC SUB DOMAINS only as necessary.
      - though you should seldom design for reusability, you must be strict about keeping within the generic concept.
      - introducing industry-specific model elements will have 2 costs
        - first, it will impede future development. By introducing anything to the design that is not part of the concept, you make it much more difficult to expand the system cleanly without completely rebuilding the older part and redesigning the other modules that use it
        - second, those industry specific concepts belong either in the CORE DOMAIN or in their own more specialized, subdomains, and those specialized models are even more valuable than the generic ones.
    - **project risk management**
      - tackling the riskiest tasks early, XP specially calls for getting an end-to-end system up and running immediately.
      - some projects have greater technical risks and others greater domain modeling risks
        - therefore, except when the team has proven skills and the domain is very familiar, the first-cut system should be based on some part of the CORE DOMAIN, however, simple.
        - CORE DOMAIN is high risk because it is often unexpectedly difficult and without it, the project can not succeed
        - domain vision statement and high-lighted core shows how the use of supplemental documents can, with a very minor investment, improve communication and awareness of the CORE and focus development effort.
  - [domain vision statement](#domain-vision-statement)

- **Large-scale structure: How to make a sprawling system comprehensible and encourage consistency across subsystems?**
  - [large scale structure for strategic design](#large-scale-structure-for-strategic-design)
  - [evolving order](#evolving-order)
  - Several specific techniques for large-scale structure are discussed, but are skipped in this tour. Non-technical example of how a large-scale structure allowed thousands of people to contribute to the AIDS Memorial Quilt
    - few simple rules provide large-scale structure for the AIDS Memorial Quilt, leaving the details to individual contributor. Notice how the rules focus on the overall mission (memorizing people who have died of AIDS), the features of the component that make integration practical, and the ability to handle the quilt in larger sections.
  - [who sets the strategy](#who-sets-the-strategy)
  - Tracking five real domain-driven design projects and their long-term outcomes.
    - PCB design software
    - loan software
    - shipping examples
    - Evant

- **How to avoid common pitfalls of modeling in software development?**

- **How to bring business people and developers into an effective collaboration?**

- **How to bring rigor to the modeling process to help the system scale?**

- **How to apply modeling in a multi-team environment?**

- **How to focus design effort on high-value areas and avoid over-investing elsewhere?**


- 
# Exercises

- https://medium.com/nick-tune-tech-strategy-blog/architecture-ddd-kata-online-car-dealership-540c534121e2
- https://medium.com/nick-tune-tech-strategy-blog/strategic-domain-driven-design-kata-delivericious-b114ca77163
- https://github.com/ddd-crew/bounded-context-canvas
- https://docs.google.com/forms/d/e/1FAIpQLSeXK2_TTCkPYwobNgDVn0DvZhShm_jO_8gg2Dtqk3HHxx6Wuw/viewform

# Quotes
"Sub-domain is a problem space concept, Bounded context is a solution space concept."

"As software developers, we fail in two ways: We build the thing wrong, or we build the wrong thing."

"A project faces serious problems when its language is fractured."

"Integration is always expensive, and sometimes the benefit is small."

"Architectures can straitjacket a project with up-front design assumptions and take too much power away from the developers/designers of particular parts of the application. Soon, developers/designers of particular parts of the applications will dumb down the application to fit the structure, or they will subvert it and have no structure at all, bringing back the problems of uncoordinated development.."

"Each time we decide to call upon such a capability for some new purpose, someone has to meticulously sift through it all, finding an odd combination of inputs that will evoke the behaviour or return the information we want without messing anything else up, it takes trial and error and extensive testing, and the result is typically brittle. The developer who made it work walks away exhausted, successful on his terms, leaving the system even more complex than before. Then, the next time a closely related yet not identical need comes along, it starts all over.."

"Common context, the tragedy of commons."

"adding data is a way of referring to a core aspect of some business situation, and enriching ubiquitous language to be able to express these concerns. "

Design is intelligence made visible

Design is not just what it looks like and feels like. Design is how it works

People think that design is styling. Design is not style. It's not about giving shape to the shell and not giving a damn about the guts. Good design is a renaissance attitude that combines technology, cognitive science, human need, and beauty to produce something that the world didn't know it was missing.

design is intelligence made visible

[Design is] a plan for arranging elements in such a way as to best accomplish a particular purpose.

What is design? it's where you stand with a foot in 2 worlds - the world of technology and the world of people and human purposes - and you try to bring the 2 together.

Design isn't just to satisfy requirements, but also to uncover requirements.

perfection is not reached when there is nothing to be added anymore, but when there is nothing to be left out anymore.

the design process, at its best, integrates the aspirations of art, science, and culture.

to say that something is designed means it has intentions that go beyond its function. Otherwise, it's just planning.

good design defuses the tension between functional and aesthetic goals precisely because it works within the boundaries defined by the functional requirements of communication problem. Unlike the fine arts, which exists for their own sake, design must always solve a particular real-world problem.

in practice, designing seems to proceed by oscillating between sub-solution and sub-problem areas, as well as decomposing the problem and combining sub-solutions.

when you specify something to be designed, tell what properties you need, not how they are to be achieved.

the trick is to hold "process" off long enough to permit great design to occur, so that the lesser issues can be debated once the great design is on the table - rather than smothering it in the cradle.

good design is good business

if you think it's expensive to hire a professional to do the job, wait until you hire an amateur

design must reflect the practical and aesthetic in business but above all... good design must primarily serve people.

questions about whether design is necessary or affordable are quite beside the point: design is inevitable. The alternative to good design is bad design, not no design at all. Everyone makes design decisions all the time without realizing it - like Moliere's M. Jourdain who discovered he had been speaking prose all his life, and good design is simply the result of making these decisions consciously, at the right stage, and in consultation with others as the need arises.

a good design is not the one that correctly predicts the future, it's one that makes adapting to the future affordable

everyone designs who devises courses of action aimed at changing existing situations into preferred ones.

it's very easy to be different, but very difficult to be better.

we've probably designed 4000 products at IDEO over my career, and for every one of them I'd like to send a little note with it that says, "I'm sorry that it's in this present state. Given what I know now, if I could start over again it would be a lot better"

design is easy. All you do is stare at the screen until drops of blood form on your forehead.

ease of use and ease of learning are not the same.

computer design is often bad design done on a computer

our opportunity as designers, is to learn how to handle the complexity, rather than shy away from it, and to realize that the big art of design is to make complicated things simple

discovery consists of seeing what everybody has seen and thinking what nobody has thought

no, Watson, this was not done by accident, but by design.

design is about making things good (and then better) and right (and fantastic) for the people who use and encounter them.

I never design a building before I've seen the site and met the people who will be using it.

the only important thing about design is how it relates to people.

a design isn't finished until somebody is using it.

Each of these techniques requires a successively greater commitment, but a knife gets sharper as its blade is ground finer. Successive distillation of a domain model produces an asset that gives the project speed, agility, and precision of execution.

Creating distinctive software comes back to a stable team accumulating specialized knowledge and crunching it into a rich model

Generic Subdomains reduce the clutter in the Core Domain, leaving it focused on what is more important.

Cohesive Mechanisms are used to encapsulate complex operations used by the Domain.

Realizing that your best idea is likely to get in somebody’s way takes humility

The essence of good object design is to give each object a clear and narrow responsibility and to reduce interdependency to an absolute minimum

A named thing we can discuss


**still under constructions**
**Next Steps:**
review Distilled DDD from vaugh vernon
review design DDD quickly

# References
- https://www.infoq.com/articles/architecture-modernization-domain-driven-discovery/
- https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
- https://devopedia.org/domain-driven-design
- https://philippe.bourgau.net/categories/#squash-bduf-with-event-storming-series
- https://www.infoq.com/articles/ddd-contextmapping/
- https://github.com/leubedane/iddd-redbook-summary
- https://medium.com/@ruxijitianu/summary-of-the-domain-driven-design-concepts-9dd1a6f90091
- https://www.amazon.ca/Domain-Driven-Design-Distilled-Vaughn-Vernon-ebook/dp/B01JJSGE5S/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=
- https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf
- https://devpath.pro/methodologies/book-review-domain-driven-design-quickly/
- https://medium.com/inato/an-introduction-to-domain-driven-design-386754392465
- https://github.com/ddd-crew/ddd-starter-modelling-process
- https://github.com/orgs/ddd-crew/repositories?type=all
- https://medium.com/nick-tune-tech-strategy-blog/architecture-ddd-kata-online-car-dealership-540c534121e2
- https://medium.com/nick-tune-tech-strategy-blog/strategic-domain-driven-design-kata-delivericious-b114ca77163
- https://speakerdeck.com/mploed/visualizing-sociotechnical-architectures-with-context-maps
- https://www.youtube.com/watch?v=ekMPm78KFj0&t=1820s
- [visual collaboration tools](./visualcollaborationtools.pdf)
- https://dev.to/ielgohary/domain-driven-design-by-eric-evans-part-i-5d8m
- https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD-Nontechnical-path-through-the-blue-book.pdf
- https://herbertograca.com/category/development/book-notes/domain-driven-design-by-eric-evans/
