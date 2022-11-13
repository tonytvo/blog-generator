---
title: Notes on Mars Rover Kata Nov 13h 2022
date: "2022-05-22T23:46:37.121Z"
description: "Notes on Mars Rover Kata Nov 13h 2022"
tags: ["evolutionarydesign", "tdd", "algorithm"]
---

# Questions
- What have you learned?
  - it's good exercise to practice domain and functional together
  - by implementing the procedure first, it can be fun to practice refactor to state pattern
  - take this opportunity to review into domain/refactoring to patterns and Arlo commits -> https://jay.bazuzi.com/why-acn/
  - push object and function calisthenics as much as I can
    - https://blog.ninjaferret.co.uk/2015/06/05/Introducing-Functional-Calisthenics.html
    - https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf
  - fp-ts with state monoid is pretty crazy and pretty fun
  - https://github.com/tonytvo/marsrover-kata/pull/1

- Questions/thoughts
  - review objects cathestic, functional cathestic and arlo commit notation.
  - what's arlo notion for adding only tests?
  - F!! to add both tests and production code feels like big steps
  - is there a better way to specify any in StateMonoid? feels like when both Output and State are the same ... it seems like there some duplication
  - too many R!!, is there better way make it smaller?
  - what're the languages that I want to use for most of my kata outside of java?
    - seems like typescript is a good one where I can leverage union types and functional libraries from the community

# References
- https://blog.ninjaferret.co.uk/2015/06/05/Introducing-Functional-Calisthenics.html
- https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf
- https://jay.bazuzi.com/why-acn/