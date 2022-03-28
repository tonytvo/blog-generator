---
title: Evolutionary Design Notes With JBrain Sessions
date: "2022-03-27T23:46:37.121Z"
description: "Summary notes on Evolutionary Design Sessions With JBrain"
tags: ["evolutionarydesign", "tdd", "refactoring"]
---
- Intent revealing names -> https://blog.thecodewhisperer.com/permalink/a-model-for-improving-names
- commit more frequently with the following commit message patterns:
  - https://github.com/RefactoringCombos/ArlosCommitNotation
  - https://www.conventionalcommits.org/en/v1.0.0/#specification
  - describe high level/business intention
- introduce indirection steps to avoid big steps
  - steps for approach 1
    - Create a Warm, Dry Place where I can change code and disrupt clients less.
    - Focus on changes inside the Warm, Dry Place.
    - Publish the changes when they’re ready, which often means inlining the Warm, Dry Place (put it back where it was) or inlining the clients of the Warm, Dry Place (the new code replaces some older code).
  - steps for approach 2 (introduce parameter object)
    - https://www.youtube.com/watch?v=hGkdDxYCCKY&ab_channel=tomphp
  - steps for approach 3 (adding the wrapper)
    - extract a function that takes the primitive value f(p)
    - introduce parameter object to wrap p into wrapper w, so that now we have f(w)
    - move f() onto class W. (what's left is moving any behaviour that ask for w.getP() onto W)
    - for remaining function g(p) put in the line w = new W(p) and then migrate all the internals from p to w.p (or w.getP() or whatever you call it)
    - extract parameter on new W(p), so that g now takes a w instead of p
    - move g() onto W
  - steps for approach 4 (liberating the wrapped)
    - extract all the functions of p that you want
    - promote p to a field on the current class
    - extract delegate to class W, creating a new class that as p as a field, leaving behind this.w = new W(p)
    - clean up
- **read it, understand it, and put the information in the code**
- Clean up as we go
  - keep track of which clean-up items to propose so that we can eventually do them.
- When it's appropriate to isolate production code into their own file/module.
  - "when it's necessary"
  - As a note, we started it out with production code and test code are closed together because it would be easier for us to move in small steps. The production code is still changing quite a bit and we're not sure what kind of abstraction/API we want to publish yet.
  - organize the source code so that the public API functions are closer to the top of the file
- Remove duplication
  - insert the remove duplication patterns here.
- Context Independence
  - helps to decide whether an object hides too much or hides the wrong information
  - has no built-in knowledge about the system in which it executes.
  - should not use terms from multiple domains, unless it's part of a bridging layer
- Null Design -> https://blog.thecodewhisperer.com/permalink/null-design-tool
- Partially Applying Functions
  - https://blog.thecodewhisperer.com/permalink/injecting-dependencies
- When to do inside out (jump to details)
  - when the risks in the details/certain tasks/components are large/noticeable and you want to mitigate the risks
    - https://wbitdd2-prerelease-discuss.jbrains.ca/t/noticing-signals-for-getting-stuck-when-test-driving/108/4?u=ttrung.vo
    - Example: “I need a thing to do X. I think library L can be made to do X. I’d better check that before I continue here.”
  - when the next steps are not clear
- When to do outside in (jump back to the big pictures)
  - when you feel there's a risk in missing some important details and it could delay the project.
  - when you have difficulty in thinking about tests/what to test, it's good to think in term of one level higher in the call stacks.
  - "when in doubt, zoom out"
- How to learn effectively (or how to read a book)
  - first, write a summary of the book to get a high-level overview of the topics of the book cover (I often copied from previous summaries to get things started and update the summaries as I go along)
  - then, elaborate/dig deeper into each topic wherever the curiosity takes you
  - the trick to retention is not to read it once but to write a good summary and review it often as much as you can.
- programming by intention
  - start with the consumer of the API.
  - expressing the highest level of intention possible from the client/consumer perspective.
  - another strategy is to use the pieces already there to build the next test. In the process, I often identify one small piece that is missing or identifies 2 pieces that don't quite fit together yet. In either case, I see a smaller, clearer goal: write the missing piece or refactor so that A and B can connect together more easily.
- refactoring towards functional programming style
  - extract to a separate map in lambda
    - ![extract-variable-as-separate-map-in-lambda|690x374](upload://se0YkkGQg51vP2DJKHRD4cjWxR4.gif)

  - https://wbitdd2-prerelease-discuss.jbrains.ca/t/refactoring-towards-functional-programming-style-notes/113
```
public Barcode(String text) {
    if ("".equals(text)) throw new IllegalArgumentException("barcode can't be empty");
    else this.text = text;
}
```
to this "parse, don't validate" functional programming style
```
public static Either<ParsingFailure, Barcode> parse(String text) {...}
enum ParsingFailure { ... }
```
  - common refactoring path for values that might not be present
    - nullable `String` → `Option<String>` → `Either<ReasonTheStringWasInvalid, String>`
    - In the https://www.vavr.io library, there are library functions that adapt values in order to make this refactoring easier.
      - `Option.ofNullable()` maps `null` to `none()` and `x` to `some(x)`
      - `Option.ofNullable()` maps `null` to `none()` and `x` to `some(x)`.
      - another pattern to map java option
```
if (maybeValue.isPresent()) { 
  return Option.some(f(maybeValue.get()));
} else { 
  return option.none();
}
```
 can become

``` return maybeValue.map(f).getOrElse("fallback value"); ```

- patience in practicing evolutionary design
  - " programmers do not allow the various refactoring patterns to become so easy/comfortable that their fingers can execute them without conscious thought. This interferes with their progress because they have to switch more often among the questions “which refactorings will improve this design?” and “how do I perform this micro-step?” If they don’t become able to perform the micro-steps (a sequence of 3-7 nano steps) *easily*, then they might not breakthrough from “I know how to safely lead the design where I want it to go” to the more-powerful “I can just start removing duplication and improving names and a good design will emerge”.
  - Don’t get me wrong: the first of these two outcomes is *good*, but the second of these two outcomes is *much better*.
  - One consequence of never breaking through is that the programmer will miss out on finding helpful designs that are simpler than the ones that their intuition can see."
- rail-way oriented programming
  - *insert more content here*
- "if the implementation is wrong, how would a business person know?"
  - that helps me to write the tests in higher-level language
  - not only "business person". This is one of those questions to ask when you have trouble writing a test: "if the implementation were wrong, how would I know? what would I check?"
- build the things/abstraction we need in the test and move it to production code later
  - "This is One way that the tests can drive the design, it reminds me of the chapter in the The Goal where the factory engineers a sale for the first time."
- stub query/expect action
  - does the tests detect query or side effect, if it detect side-effects, we would like to make that side effects as direct as possible, like verifying calling the message on the interface.
- poka-yoke
  - which mistake could we make when trying to use this interface?
  - how could we refactor this interface to make those mistakes impossible? (And if not impossible, then less likely)
  - which moves or design concepts are available to me in java that I can use to add poka-yoke to my designs?
  - which moves or design concepts are available to me in other programming languages that I wish I could use to add poka-yoke to my java designs?
- vocabulary problem
  - because you don't know enough "words" (options) to choose from.
  - to build your vocabulary, you need to expose yourself to more "words".
  - try katas.
  - when you aren't sure how to do something, consider these things
    - what do you already know how to do? maybe you can get there, but "the long way". If you understand the long way better, you can turn this into a vocabulary problem: I don't know enough shortcuts.
    - how far can you get before you're stuck? once you're stuck, you can ask a more specific question, which might lead to collecting a new "word"
    - can you get what you want another way?
    - try to practice solving the same problem in different ways and compare/contrast solution

- 
# Quotes
# References
- https://martinfowler.com/tags/evolutionary%20design.html