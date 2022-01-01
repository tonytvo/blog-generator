---
title: practical guide to object oriented design
date: "2021-12-31T22:12:03.284Z"
description: "practical guide to object oriented design summary"
tags: ["designpatterns", "oop"]
---
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Goals/Key Ideas/Context](#goalskey-ideascontext)
- [rediscovering simplicity](#rediscovering-simplicity)
  - [simplifying code](#simplifying-code)
    - [incomprehensibly concise](#incomprehensibly-concise)
    - [speculatively general](#speculatively-general)
    - [concretely abstract](#concretely-abstract)
    - [shameless green](#shameless-green)
  - [judging the code](#judging-the-code)
    - [evaluating code based on opinion](#evaluating-code-based-on-opinion)
    - [evaluating code based on facts](#evaluating-code-based-on-facts)
  - [judging the design](#judging-the-design)
- [unearthing concepts](#unearthing-concepts)
  - [creating classes with single responsibility](#creating-classes-with-single-responsibility)
  - [creating flexible interfaces](#creating-flexible-interfaces)
- [TDD as design](#tdd-as-design)
- [practising horizontal refactoring](#practising-horizontal-refactoring)
- [separating responsibilities](#separating-responsibilities)
  - [managing dependencies](#managing-dependencies)
  - [acquiring behavior through inheritance](#acquiring-behavior-through-inheritance)
  - [writing inheritable code](#writing-inheritable-code)
- [Achieving openness](#achieving-openness)
  - [Sharing role behavior with modules](#sharing-role-behavior-with-modules)
  - [combing objects with composition](#combing-objects-with-composition)
- [Quotes](#quotes)
- [References](#references)

# Goals/Key Ideas/Context
- you should not reach for abstractions, but instead you should resist them until they absolutely insist upon being created.
- writing code is the process of working your way to the next stable end point, not the end point itself
- If your goal is to write straightforward code, these metrics point you toward `Shameless Green`
# rediscovering simplicity
- getting insight into potential expense of code
  - how difficult was it to write?
  - how hard is it to understand?
  - how expensive will it be to change?

- terminology: method vs sending messages
  - a "method" is defined on an object and contains behavior
  - a "message" is sent to an object to invoke behavior
    - `song() { verses(); }` means that song method sends the verses message to the receiver this.
    - therefore, **method are defined, and messages are sent**
    - "sending messages" are preferred to "call a method/function" as it implicitly encourage to create message senders that are willfully ignorant of implementation details, and fosters independence between senders and receivers.
- **code is easy to understand when it clearly reflects the problem it's solving, and thus openly exposes that problem's domain**


## simplifying code
- speculatively general and concretely abstract were both written with an eye toward reducing future costs, and it is distressing to see good intentions fail so spectacularly. **The failure here is not bad intention - it's insufficient patience.**
### incomprehensibly concise
- [incomprehensibly concise code](https://github.com/marina-ferreira/99_bottles_of_oop/blob/main/chapter_1/01_incomprehensibly_concise.rb)
  - embeds a great deal of logic into the verse string
  - the code is hard to understand because it is inconsistent and duplicative (pluralization logic), and because it contains hidden concepts that it does not name

### speculatively general
- [speculatively general code](https://github.com/marina-ferreira/99_bottles_of_oop/blob/main/chapter_1/02_speculatively_general.rb)
  - there's far more code here  than is needed to pass the tests. This unnecessary code took time to write
  - the many levels of indirection are confusing. You could study this code for a long time without discerning why they are needed
  - you may feel compelled to understand its purpose before making changes.
  - what is the rule to determine which verse should be sung next? buried deep within the NoMore lambda is a hard-coded "99," which might cause one to infer that verse 99 follows verse 0.

### concretely abstract
- **"DRY makes sense when it reduces the cost of change more than it increases the cost of understanding the code"**
- DRYing out code is not free. It adds a level of indirection, and layers of indirection make the details of what's happening harder to understanding.
- [concretely abstract code](https://github.com/marina-ferreira/99_bottles_of_oop/blob/main/chapter_1/03_concretely_abstract.rb)
  - it clearly took a fair amount of thought and time.
  - the individual methods are easy to understand, it's tough to get a sense of the entire song. The parts doesn't seem to add up to the whole
  - while changing the code inside any individual method is cheap, in many cases, one simple change will cascade and force many other changes.
  - what is the rule to determine which verse should be sung next? Ditto.

### shameless green
- shameless green is defined as the solution that quickly reaches green while prioritizing understandability over changeability.
- it doesn't dispute that DRY is good, rather, it believes that it is cheaper to manage temporary duplication than recover from incorrect abstractions.
- [shameless green](https://github.com/marina-ferreira/99_bottles_of_oop/blob/main/chapter_1/04_shameless_green.rb)
  - it was easy to write and understand
  - it will be cheap to change. Even though the verse strings are duplicated, if one verse changes it's easy to keep the others in sync.
  - what is the rule to determine which verse should be sung next? This is still not explicit. The 0 verse contains a deeply buried, hard-coded 99
  
## judging the code
### evaluating code based on opinion
  - look for context/concrete guidance of what the code trying to accomplish
  - **any pile of code can be made to work; good code not only works, but it also simple, understandable, expressive and changeable**

### evaluating code based on facts
- you can think of metrics as crowd-sourced opinions about the quality of code.
- measuring programmer productivity by counting lines of code (SLOC))
  - easily garnered and reproduced, it reflects code volume but suffers from many flaws
- Cyclomatic complexity
  - an algorithm that counts the number of unique execution paths through a body of source code. The more deeply nested conditionals, the higher Cyclomatic complexity
  - the code with fewer nested conditionals (lower cyclomatic complexity) is easier to reason with and maintain
  - can be used to limit the overall complexity. You can set standards for how high a score you're willing to accept.
  - you can use it to determine if you'ave written enough tests, as it tells you the minimum number of tests needed to cover all the logic in the code.
- Assignments, branches and conditions (ABC) metrics
  - assignments is a count of variable assignments
  - branches counts not branches of an if statement but branches of control, meaning function calls or message sends
  - conditions counts conditional logic
  - ABC scores reflect cognitive load as opposed to physical size. High ABC numbers indicate code that takes up a lot of mental space.
- ![metrics chart comparison](./sloc-abc-metrics.png)
- metrics are fallible but human opinion is no more precise. Checking metrics regularly will keep you humble and improve your code.
## judging the design
- **Don't do** big upfront design (BUFD)
  - designs in BUFD cannot possibly be correct as many things will change during the act of programming
  - BUFD inevitable leads to an adversarial relationship between customers and programmers.
- make design decisions only when you must with the information you have at that time
  - postpone decisions until you are absolutely forced to make them
  - any decision you make in advance on an explicit requirement is just a guess. Preserve your ability to make a decision later
- 
# unearthing concepts
## creating classes with single responsibility
## creating flexible interfaces

# TDD as design
# practising horizontal refactoring

# separating responsibilities
## managing dependencies
## acquiring behavior through inheritance
## writing inheritable code
# Achieving openness
## Sharing role behavior with modules
## combing objects with composition
# Quotes

"Writing code is the process of working your way to the next stable end point, not the end point itself"

**"DRY makes sense when it reduces the cost of change more than it increases the cost of understanding the code"**

"metrics are fallible but human opinion is no more precise. Checking metrics regularly will keep you humble and improve your code"

"shameless green is defined as the solution that quickly reaches green while prioritizing understandability over changeability."

"it doesn't dispute that DRY is good, rather, it believes that it is cheaper to manage temporary duplication than recover from incorrect abstractions."


# References
https://github.com/keyvanakbary/learning-notes/blob/master/books/99-bottles-of-oop.md
https://github.com/serodriguez68/poodr-notes
https://matteopallini.com/bottles-oop-summary/
https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html
https://lionadi.wordpress.com/2020/12/04/oop-tdd-99-bottles-notes-part-1-simplicity/
https://gist.github.com/speric/31ae0987d21eac1d4f87