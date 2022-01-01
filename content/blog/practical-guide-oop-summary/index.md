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
- [TDD as design](#tdd-as-design)
  - [writing cost-effective tests](#writing-cost-effective-tests)
    - [intentional testing](#intentional-testing)
      - [test benefits](#test-benefits)
      - [knowing what to test](#knowing-what-to-test)
      - [knowing when to test](#knowing-when-to-test)
      - [knowing how to test](#knowing-how-to-test)
    - [testing incoming messages](#testing-incoming-messages)
      - [deleting unused interfaces](#deleting-unused-interfaces)
      - [providing the public interface](#providing-the-public-interface)
      - [isolating the object under test](#isolating-the-object-under-test)
      - [injecting dependencies using classes](#injecting-dependencies-using-classes)
      - [injecting dependencies as roles](#injecting-dependencies-as-roles)
    - [creating test double](#creating-test-double)
    - [using tests to document roles](#using-tests-to-document-roles)
    - [testing private methods](#testing-private-methods)
    - [testing outgoing messages](#testing-outgoing-messages)
    - [testing duck types](#testing-duck-types)
    - [testing inherited code](#testing-inherited-code)
- [unearthing concepts](#unearthing-concepts)
  - [creating classes with single responsibility](#creating-classes-with-single-responsibility)
  - [creating flexible interfaces](#creating-flexible-interfaces)
- [practising horizontal refactoring](#practising-horizontal-refactoring)
  - [technique 1: flocking rules for refactoring](#technique-1-flocking-rules-for-refactoring)
  - [technique 2: the open-closed flowchart](#technique-2-the-open-closed-flowchart)
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
- If your goal is to write straightforward code, these metrics (ABC metrics) point you toward `Shameless Green`
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
- metrics are not direct indicators of quality but are proxies for a deeper measurement.
- The ultimate software metric would be cost per feature over time interval that matters, but this is not easy to calculate. Cost, feature, and time are individually difficult to define, track and measure.
- your goal is to write software with teh lowest cost per feature.
- you decision about how much design to do depends on 2 things: your skills and your time frame.
  - there is a tradeoff between the amount of time spent designing and the amount of time this design saves in the future (and there is a break-even point).
  - when the act of design prevents software from being delivered on time, you have lost.
# TDD as design
- **as the tests get more specific, the code gets more generic**
- while it is important to consider the problem and sketch out an overall plan before writing the first test, don't over think it
- you can't figure out what's right until you write some tests. The purpose of some of your tests might very well be to prove that they represent bad ideas.
## writing cost-effective tests

### intentional testing
#### test benefits
- finding bugs
- supplying documentation
  - write tests that remind you the story you once have
- deferring design decisions
  - intentionally depending on interfaces allows you to use tests to put off design decision safely and without penalty
- supporting abstractions
  - tests are your record of hte interface of every abstraction. They let you put off design decisions and create abstractions to any useful depth.
- exposing design flaws
  - if a test requires painful setup, the code expects too much context.
  - if the test is hard to write, other objects will find the code difficult to reuse.

#### knowing what to test
- dealing with objects as if they are only and exactly the messages to which they respond lets you design a changeable application, and it is your understanding of the importance of this perspective that allows you to create tests that provide maximum benefit at minimum cost.
- tests should concentrate on the incoming or outgoing messages that cross an object's boundaries. The incoming messages make up the public interface of hte receiving object. The outgoing messages, by definition, are incoming into other objects and so ar part of some other object's interface.
- the general rule is that objects should make assertions about state only for messages in their own public interfaces.
- some outgoing messages have no side effects and thus matter only to their senders.
  - outgoing messages like this are known as queries and they need not be tested by the sending object.
  - query messages are part of the public interface of their receiver, which already implements every necessary test of state.
- many outgoing messages do have side effects (a file gets written, a database record is saved, an action is taken by an observer) upon which your application depends.
  - proving that a message gets sent is a test of behavior, not state, and involves assertions about the number of times, and with what arguments, the message is sent.
- incoming messages should be tested for the state they return. 

#### knowing when to test
- you should write tests first, whenever it makes sense to do so

#### knowing how to test
- if you understand the costs and benefits, feel free to choose any framework that suits you.
- BDD takes an outside-in approach, creating objects at the boundary of an application and working its way inward, mocking as necessary to supply as-yet-unwritten objects.
- TDD takes an inside-out approach, usually staring with tests of domain objects and then reusing these newly created domain objects in the tests of adjacent layers of code.
- when you tests know more about the internal inside of the object under test, it allows knowledge that should be private eto the object leak into the tests, increasing coupling between them and raising the likelihood that changes the code will require changes in tests.

### testing incoming messages
- incoming messages make up an object's public interface, the face it presents to the world. these messages need tests because other application objects depend on their signatures and on the results they return.

#### deleting unused interfaces
- incoming messages ought to have dependents. Some object other than the original implementer depends on each of these messages.
- do not test an incoming messages that has no dependents; delete it.
- unused code costs more to keep than to recover.

#### providing the public interface
- if Wheels are expensive to create, the Gear test pays that cost even though it has no interests in Wheel.
- an application constructed of tightly coupled, dependent laden objects is like a tapestry where pulling on one thread drags the entire rug along.
  - running Gear test would then create a large network of objects, any of which might break in a maddeningly confusing way.
- tests are the first reuse of code.

#### isolating the object under test
- when you can't test object in isolation, it bodes ill for the future.
- the diameter method is part of hte public interface of a role, one that might reasonably be named diameterizable.
- thinking of the injected object as a instance of its role gives you more choices about what kind of Diameterizable to inject into Gear during your tests.

#### injecting dependencies using classes
- when the code in your test uses the same collaborating objects as the code in your application, your tests always break when they should.

#### injecting dependencies as roles
- ![injecting roles](./behaves-like-inject-into.png)
- the whole point of dependency injection is that it allows you to substitute different concrete classes without changing existing code.
- Object-oriented design tells you to inject dependencies because it believes that specific concrete classes will vary more than these roles, or conversely, roles will be more stable than the classes from which they were abstracted.
- if your application contains many different diameterizables, you might want to create an idealized one so your tests clearly convey the idea of this role.
  - if all diameterizables are expensive, you may want to fake a cheap one to make your tests run faster.
  - if you are doing BDD, your application might not yet contain any object that plays this role; you may be forced to manufacture something just to write the test.

### creating test double
- [more on test doubles](/growing-object-orented-guided-by-tests-summary#mock-roles-not-objects)
- when diameterizable's interface changes from diameter to width, and `Wheel` get updated but `Gear` does not
  - since the dimeterizabledouble is injected, the test continues to pass even though the application is definitely broken
  - this is where the stubbing and mocking could make the tests brittle.
  - "when interface of a role changes, all players of the role must adopt the new interface", dynamic language like ruby doesn't complain about the incompatible implementation with the interface.

### using tests to document roles
- injecting the same objects at test time as are used at runtime ensures that tests break correctly but may lead to long running tests.
- injecting doubles can speed tests but leaves them vulnerable to constructing a fantasy world where tests work but the application fails

### testing private methods
- if you can't get/access the structure you need, then the tests tell you that it's time to break up the class into more minor/composable features.
  - the extracted methods form the core of responsibilities of the new object and so make up its public interface, which is (theoretically) stable and thus safe to depend upon.
- tests of private methods are therefore coupled to application code that is likely to change.
- since tests provide documentation about the object under test, it could mislead others into using them.
- never write private methods, and if you do, never ever test them, unless of course it makes sense to do so

### testing outgoing messages
- outgoing messages are either queries or commands. Query messages matter only to the object that sends them, while command messages have effects that are visible to other objects in your application.
- ignoring query messages
  - it's redundant for Gear to duplicate correctness tests from Wheel, maintainance costs will increase if it does.
- proving command messages
  - sometimes, it does matter that the message get sent and the object under test is responsible for sending the message
  - your tests must prove that the command messages got sent
- if you have proactively injected dependencies, you can easily substitute mocks. Setting expectations on these mocks allows you to prove that the object under test fulfills its responsibilities without duplicating assertions that belong else where
### testing duck types
- Using role tests to validate doubles
  - use dynamic module interface test to ensure the test double honor the interface
```ruby
module DiameterizableInterfaeTest
  def test_implements_the_diameterizable_interface
    assert_respond_to(@wheel, :diameter)
...
class DiameterDoubleTest < MiniTest::Unit::TestCase
  include DiameterizableInterfaceTest
```
- From the point of view of the object under test, every other object is a role, and dealing with objects as if they representative of the roles they play loosens coupling and increases flexibility, both in your application and in your tests.
- If you fear that human communication will be insufficient to keep all players of a role in sync, write the tests.

### testing inherited code
- prove that all objects in this hierarchy honor their contract
  - subtypes should be substitutable for their subtypes
  - write a shared test for the common contract and include this test in every object.
- confirming subclass behavior
- confirming superclass enforcement
  - `bicycle` class should raise an error if a subclass does not implement `default_tire_size`. Even though this requirement applies to subclasses, the actual enforcement behavior is in Bicycle.

```ruby
def test_forces_subclasses_to_implement_default_tire_size
  assert_raises(NotImplementedError) { @bike.default_tire_size }
```
- testing concrete subclass behavior
  - it's important to test these specializations without embedding knowledge of the superclass into the test.
    - the `RoadBikeTest` should ensure that `local_spares` works while maintaining deliberate ignorance about the existance of `spares` method

- testing abstract super class behavior
  - you can stub the behavior that would normally be supplied by subclasses (follow liskov substitution principle)
  - be especially careful when testing subclass specializations to prevent knowledge of the superclass from leaking down into the subclass's test
# unearthing concepts
## creating classes with single responsibility
## creating flexible interfaces


# practising horizontal refactoring
## technique 1: flocking rules for refactoring
- steps
  - select the things that are most alike
  - find the smallest difference between them
  - make the simplest change that will remove that difference.
- making existing code open to a new requirement often requires identifying and naming abstractions. The flocking rules concentrate on turning difference into sameness, and thus are useful tools for unearthing abstractions.

## technique 2: the open-closed flowchart
- [open closed flowchart](./open-closed-flowchart.png)
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

"Quick green excuses all sins"

"good design preserves maximum flexibility at minimum cost by putting off decisions at every opportunity, deferring commitments until more specific requirements arrive."

"think of an object oriented application as a series of messages between a set of black boxes"

"the reason you're writing tests is to save money, and every potential test must be evaluated against that criteria"

"when your intention is to defer a design decision, do the simplest thing that solves today's problem. Isolate the code behind the best interface you can conceive and hunker down and wait for more information"

"the rules of thumb for testing private methods are: never write them, and if you do, never ever test them, unless of course it makes sense to do so."

"making existing code open to a new requirement often requires identifying and naming abstractions. The flocking rules concentrate on turning difference into sameness, and thus are useful tools for unearthing abstractions."

"the best tests are loosely coupled to the underlying code and test everything once and in the proper place. They add value without increasing costs"

# References
https://github.com/keyvanakbary/learning-notes/blob/master/books/99-bottles-of-oop.md
https://github.com/serodriguez68/poodr-notes
https://matteopallini.com/bottles-oop-summary/
https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html
https://lionadi.wordpress.com/2020/12/04/oop-tdd-99-bottles-notes-part-1-simplicity/
https://gist.github.com/speric/31ae0987d21eac1d4f87