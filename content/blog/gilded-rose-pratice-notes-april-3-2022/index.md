---
title: Notes on gilded rose kata practice April 3rd 2022
date: "2022-04-03T23:46:37.121Z"
description: "Notes on gilded rose kata practice April 3rd 2022"
tags: ["evolutionarydesign", "tdd", "refactoring"]
---

# Questions
- What have you learned?
  - It seems like as soon as we give Quality an abstraction, we can remove more duplication code around increase/decrease quality
  - it seems like verifyAllCombinations is handy, but it's not available as part of jest snapshot testing
  - First, simplify the condition to true/false after the condition is flipped to the top level then leverage 'Alt+Enter' to simplify the conditions as much as possible (instead of manually remove dead-code or code that is highlighted as red from test-coverage)
  - couldn't get the code highlight for warnings and not-covered works as the demonstrated video from Llewellyn
  - it seems like for ... forEach ... stream is a pattern in languages that support stream/functional
  - is there a better and easier way to wrap primitive fields
    - typically, add new field
    - isolate the accessor/updater to the primitive field to reduce the reference to the field that I want to wrap
    - make set/get using both new and old field
    - switch the set/get using the new field as primary field
    - remove the old field
  - remove as many side-effect (command function) as much as possible.
- a strategy I followed?
  - flip conditional with as little effort as possible as demonstrate by Llewellyn Falco
    - https://www.youtube.com/watch?v=wp6oSVDdbXQ&ab_channel=CraftHubEvents
  - avoid mutable state, creating new object instead of updating the state of the object
- the steps I followed?
  - [Arlo commit notation](https://github.com/RefactoringCombos/ArlosCommitNotation)
# References
- https://github.com/tonytvo/coderetreat/pull/1
- https://www.stackbuilders.com/blog/refactoring-javascript-with-functional-patterns/
- https://fsharpforfunandprofit.com/fppatterns/
- https://github.com/ramda/ramda
- https://vimeo.com/45140590
- https://vimeo.com/122645679
- https://www.stackbuilders.com/blog/refactoring-javascript-with-functional-patterns/
- https://www.youtube.com/watch?v=wp6oSVDdbXQ&ab_channel=CraftHubEvents
- https://blog.ninjaferret.co.uk/2015/06/05/Introducing-Functional-Calisthenics.html
- https://www.codurance.com/publications/2017/10/12/functional-calisthenics