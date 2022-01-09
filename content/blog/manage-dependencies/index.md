---
title: managing dependencies summary
date: "2021-12-23T22:12:03.284Z"
description: "managing dependencies summary"
tags: ["designpatterns", "evolutionarydesign"]
---
# key ideas
- when we push implementation details up the call stack, we leave behind the minimum context needed to do the work. This makes the code as reusable as possible.
  - injecting an interface up front is *making a guess* about the minimum context needed inside the method.
  - overtime, to make the tests "better", we extract details up into parameters. And then sometimes we extract interfaces on those new parameters. This is "fine tuning" the interactions between objects, gradually/relentlessly removing irrelevant details.
  - the progress is usually similar to:
    - function contains implementation details, forcing us into integrated tests (Example: database access inside domain code)
    - extract and inject implementation details, which improves the design but often doesn't make the tests nicer
    - extract interfaces on the implementation detail parameters, which makes the tests nicer (Example: replace database access with repository pattern)
    - invert the dependency, so that hte client knows there is database access. Client "injects" the data instead of the source of the data. (Example: replace repository pattern with Logic Sandwich/impure-pure-impure)
  - DIP encourage us to isolate the steps from the workflow. This generally makes it easier to rearrange the steps into new workflows (new features are less expensive to build), but perhaps, more importantly, this makes it safer to reimplement some Steps to take advantage of distributed computing and parallelization.
# recognizing dependencies

# solution strategies

- Dependency retention: We don't worry about managing dependencies; we just inline and hard-code everything!
- Dependency rejection, an excellent term (coined by Mark Seemann, above), in which we avoid having any dependencies in our core business logic. We do this by keeping all I/O and other impure code all the "edges" of our domain.
- Dependency parameterization, in which we pass in all dependencies as parameters. This is commonly used in conjunction with partial application.
- Dependency injection and the reader monad, in which we pass in dependencies after the rest of the code has already been constructed. This is typically done via constructor injection in OO-style code, and in FP-style principle, this corresponds to the Reader monad.
- Dependency interpretation: We replace calls to dependencies with a data structure interpreted later. This approach is used in both OO (interpreter pattern) and FP (e.g. free monads)

## isolate the dependency

# Quotes


# References
https://blog.thecodewhisperer.com/series#dependency-inversion-principle-dip
https://fsharpforfunandprofit.com/posts/dependencies/
https://blog.thecodewhisperer.com/series#dependency-inversion-principle-dip
https://blog.ploeh.dk/2017/01/27/from-dependency-injection-to-dependency-rejection/
