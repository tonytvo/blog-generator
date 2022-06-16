---
title: Evolutionary Design Notes With JBrain Sessions
date: "2022-03-27T23:46:37.121Z"
description: "Summary notes on Evolutionary Design Sessions With JBrain"
tags: ["evolutionarydesign", "tdd", "refactoring"]
---

# Evolutionary Design Patterns
- introduce indirection steps to avoid big steps
  - [Introduce an indirection layer](https://github.com/tonytvo/introduce-indirection-layer)
- **read it, understand it, and put the information in the code**
- Clean up as we go
- Keep track of which clean-up items to propose so that we can eventually do them.
- When it's appropriate to isolate production code into their own file/module.
  - maybe follow domain oriented guidelines?
  - As a note, we started it out with production code and test code are closed together because it would be easier for us to move in small steps. The production code is still changing quite a bit and we're not sure what kind of abstraction/API we want to publish yet.
- Organize the source code so that the public API functions are closer to the top of the file
- when you aren't sure how to do something, consider these things
  - what do you already know how to do? maybe you can get there, but "the long way". If you understand the long way better, you can turn this into a vocabulary problem: I don't know enough shortcuts.
  - how far can you get before you're stuck? once you're stuck, you can ask a more specific question, which might lead to collecting a new "word"
  - can you get what you want another way?
  - try to practice solving the same problem in different ways and compare/contrast solution
- stub query/expect action
  - does the tests detect query or side effect, if it detect side-effects, we would like to make that side effects as direct as possible, like verifying calling the message on the interface
- When to do inside out (jump to details)
  - when the risks in the details/certain tasks/components are large/noticeable and you want to mitigate the risks
    - https://wbitdd2-prerelease-discuss.jbrains.ca/t/noticing-signals-for-getting-stuck-when-test-driving/108/4?u=ttrung.vo
    - Example: “I need a thing to do X. I think library L can be made to do X. I’d better check that before I continue here.”
  - when the next steps are not clear
- When to do outside in (jump back to the big pictures)
  - when you feel there's a risk in missing some important details and it could delay the project.
  - when you have difficulty in thinking about tests/what to test, it's good to think in term of one level higher in the call stacks.
  - "when in doubt, zoom out"
- Patience in practicing evolutionary design
  - "programmers do not allow the various refactoring patterns to become so easy/comfortable that their fingers can execute them without conscious thought. This interferes with their progress because they have to switch more often among the questions “which refactorings will improve this design?” and “how do I perform this micro-step?” If they don’t become able to perform the micro-steps (a sequence of 3-7 nano steps) *easily*, then they might not breakthrough from “I know how to safely lead the design where I want it to go” to the more-powerful “I can just start removing duplication and improving names and a good design will emerge”.
  - Don’t get me wrong: the first of these two outcomes is *good*, but the second of these two outcomes is *much better*.
  - One consequence of never breaking through is that the programmer will miss out on finding helpful designs that are simpler than the ones that their intuition can see."

- **Context Independence**
  - helps to decide whether an object hides too much or hides the wrong information
  - has no built-in knowledge about the system in which it executes.
  - should not use terms from multiple domains, unless it's part of a bridging layer
- Null Design -> https://blog.thecodewhisperer.com/permalink/null-design-tool
## **Programming by intention/Domain Oriented**
  - start with the consumer of the API.
  - expressing the highest level of intention possible from the client/consumer perspective.
  - another strategy is to use the pieces already there to build the next test. In the process, I often identify one small piece that is missing or identifies 2 pieces that don't quite fit together yet. In either case, I see a smaller, clearer goal: write the missing piece or refactor so that A and B can connect together more easily.
  - "if the implementation is wrong, how would a business person know?"
  - that helps me to write the tests in higher-level language
  - not only "business person". This is one of those questions to ask when you have trouble writing a test: "if the implementation were wrong, how would I know? what would I check?"
- build the things/abstraction we need in the test and move it to production code later
  - "This is One way that the tests can drive the design, it reminds me of the chapter in the The Goal where the factory engineers a sale for the first time."
  - vocabulary problem
    - because you don't know enough "words" (options) to choose from.
    - to build your vocabulary, you need to expose yourself to more "words".

# Intent revealing names 
  - [A Model for Improving Names](https://blog.thecodewhisperer.com/permalink/a-model-for-improving-names)
  - [Naming Process](https://www.digdeeproots.com/articles/on/naming-process/)
- commit more frequently with the following commit message patterns:
  - [Tag as a process from Arlo](https://github.com/RefactoringCombos/ArlosCommitNotation)
  - [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#specification)
  - describe high level/business intention

# Refactoring towards functional programming style
  - https://github.com/tonytvo/refactoring/tree/main/functional
  - Partially Applying Functions
    - https://blog.thecodewhisperer.com/permalink/injecting-dependencies

# How to learn effectively
  - first, write a summary of the book to get a high-level overview of the topics of the book cover (I often copied from previous summaries to get things started and update the summaries as I go along)
  - then, elaborate/dig deeper into each topic wherever the curiosity takes you
  - the trick to retention is not to read it once but to write a good summary and review it often as much as you can.
  - https://tonytvo.github.io/learn-how-to-learn/

# Poka-yoke
  - which mistake could we make when trying to use this interface?
  - how could we refactor this interface to make those mistakes impossible? (And if not impossible, then less likely)
  - which moves or design concepts are available to me in java that I can use to add poka-yoke to my designs?
  - which moves or design concepts are available to me in other programming languages that I wish I could use to add poka-yoke to my java designs?

# Saff Squeeze
- [Saff Squeeze from J.B.](https://blog.thecodewhisperer.com/permalink/the-saff-squeeze)

# Questions
- When it's appropriate to isolate production code into their own file/module?
  - maybe follow domain oriented guidelines?
  - As a note, we started it out with production code and test code are closed together because it would be easier for us to move in small steps. The production code is still changing quite a bit and we're not sure what kind of abstraction/API we want to publish yet.
- What are the patterns for removing duplication?
  - ???
# Quotes

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

# References
- https://martinfowler.com/tags/evolutionary%20design.html
- https://www.stackbuilders.com/blog/refactoring-javascript-with-functional-patterns/