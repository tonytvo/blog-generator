---
title: Notes on Necklace refactoring May 22th 2022
date: "2022-05-22T23:46:37.121Z"
description: "Notes on Necklace May 22th 2022"
tags: ["evolutionarydesign", "tdd", "algorithm"]
---

# Questions
- What have you learned?
  - it's a refactoring to pattern exercise
  - take this opportunity to review into domain/refactoring to patterns and Arlo commits -> https://jay.bazuzi.com/why-acn/

- A strategy I followed?
  - I stumble upon the pyramid of refactoring [refactor pyramid](https://www.udemy.com/course/pyramid-of-refactoring-java-interpreter-factories/learn/lecture/17510056#overview)
- https://github.com/emilybache/Necklace-Refactoring-Kata
    - it turns out that it has a very good examples to illustrate the introduction indirect layer, so I have added a new example to the https://github.com/tonytvo/introduce-indirection-layer/tree/main/pyramid-refactor-example
    - didn't realize it such a foundational patterns that allow other patterns/flow in the system to emerge
  - it seems like for this exercise I would lean more using these examples to update introduction to indirect layer kata, so it can be used to practice refactoring to patterns as well.
  - attempt the chain of responsibility refactoring from wlodekkr here -> https://github.com/tonytvo/chain-of-responsibility/pull/1
  - once I finish with updating the introduction indirect layer, I will try to finish this kata.

# References
- [refactoring to chain of responsibility pattern](https://www.udemy.com/course/pyramid-of-refactoring-java-chain-of-poker-hands/?referralCode=AEBB17F034F9012157F6)
- [refactor pyramid](https://www.udemy.com/course/pyramid-of-refactoring-java-interpreter-factories/learn/lecture/17510056#overview)
- https://github.com/emilybache/Necklace-Refactoring-Kata
- https://www.youtube.com/watch?v=-2I5mgY-sQY&t=4s&ab_channel=LlewellynFalco
- https://blog.ploeh.dk/2019/07/22/chain-of-responsibility-as-catamorphisms/
- https://jay.bazuzi.com/why-acn/
- https://ardalis.com/domain-modeling-anemic-models/
- https://ardalis.com/what-are-abstractions-in-software-development/
- https://ardalis.com/aggregate-responsibility-design/
- https://ardalis.com/domain-modeling-encapsulation/
- https://refactoring.pl/en/pyramid-of-refactoring-discovery/
- https://refactoring.pl/en/pyramid-of-refactoring-example/
- https://lostechies.com/jimmybogard/2010/02/04/strengthening-your-domain-a-primer/