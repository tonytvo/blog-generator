---
title: Notes on coffee machine kata practice Feb 18th 2023
date: "2023-02-18T23:46:37.121Z"
description: "Notes coffee machine kata practice Feb 18th 2023"
tags: ["evolutionarydesign", "tdd", "refactoring"]
---

# Questions
- what's the right input?
- how can we write tests wihtout writing the parser
- which one is correct?
  - seems like we lean toward T:0:1 on the input intent? 

- What have you learned?
  - this kata is very rich in term of domain/functional tibbits
  - once I finish encapsulating drinks and ingredients, I started to realize couple other domain concepts like inventory, recipes, etc....
  - seems like introduce parameter is very helpful, keep surface to the top as much as possible
  - the better we are as introduce parameter, dependency, the more we can clear recognize the boundaries between different parts, like model, view controller
  - focus more on reading so we can understand more on what's needed
  - we have disagree on what th requiremnts looks like
  - we don't have to understand test fraework, we spend itme in the wrong direction
  - before we spend time on the task, we need to spened time on understanding the r3quiremnt
  - we expect the string and then use some regex .. kind of like cucumber
  - we all made good points
  - communicate with kindness, intention, respect, and considerate
  - we're confusing on the sstring format
  - we all have our interpretation

  - 
- a strategy I followed?
  - functional calisthenics and object calisthenics
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