---
title: Notes on coffee machine kata practice Feb 18th 2023
date: "2023-02-18T23:46:37.121Z"
description: "Notes coffee machine kata practice Feb 18th 2023"
tags: ["evolutionarydesign", "tdd", "refactoring"]
---

# Questions
- github repo for this kata: https://github.com/tonytvo/coffee-machine-kata
- what's the right input?
- how can we write tests without writing the parser
- which one is correct?
  - seems like we lean toward T:0:1 on the input intent? 
- here's the PR I have on refactoring practice -> https://github.com/tonytvo/coffee-machine-kata/pull/1
- What have you learned?
  - this kata is very rich in term of domain/functional tibbits
  - once I finish encapsulating drinks and ingredients, I started to realize couple other domain concepts like inventory, recipes, etc....
  - seems like introduce parameter is very helpful, keep surface to the top as much as possible
  - the better we are as introduce parameter, dependency, the more we can clear recognize the boundaries between different parts, like model, view controller
  - focus more on reading so we can understand more on what's needed
  - we have disagree on what th requirements looks like
  - we don't have to understand test framework, we spend time in the wrong direction
  - before we spend time on the task, we need to spent time on understanding the requirement
  - we expect the string and then use some regex .. kind of like cucumber
  - we all made good points
  - communicate with kindness, intention, respect, and considerate
  - we're confusing on the string format
  - we all have our interpretation
  - we have some difficulty to start up the gitpod from a person that's not the owner of the git repo
  - at the end of refactor, I keep having the feeling that is so close, want to finish it off and getting sloppy and combine multiple small refactor together

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