---
title: dependency injection summary
date: "2021-12-23T22:12:03.284Z"
description: "dependency injection summary"
tags: ["designpatterns", "evolutionarydesign"]
---

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
https://fsharpforfunandprofit.com/posts/dependencies/
https://blog.thecodewhisperer.com/series#dependency-inversion-principle-dip
https://blog.ploeh.dk/2017/01/27/from-dependency-injection-to-dependency-rejection/
