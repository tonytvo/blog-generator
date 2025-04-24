---
title: Notes on N Queen problem May 7th 2022
date: "2022-05-07T23:46:37.121Z"
description: "Notes on N Queen problem May 7th 2022"
tags: ["evolutionarydesign", "tdd", "algorithm"]
---
# Backtracking
- systematic method to iterate through all the possible configurations of a search space
- at each step in the backtracking algorithm, we start from a given partial solution, say, a = (a1, a2, ..., ak) and try to extend it by adding another element at the end.
  - after extending it, we must test whether what we have so far is a solution - if so, we should print it, count it, or do what we want with it. If not, we must then check whether partial solution is still potentially extendible to some complete solution. If so recur and continue. If not, we delete the last element from a and try another possibility for that position, if one exists
- backtracking templates
```
boolean finished = false;
backtrack(int a[], int k, data input) {
  int c[MAX_CANDIDATES];
  int ncandidates;
  int i;

  if (isASolution(a, k, input)) {
    processSolution(a, k, input);
  } else {
    k = k+1;
    construct_candidates(a, k, input, c &ncandidates);
  }

  for (i=0; i<ncandidates; i++>) {
    a[k] = c[i];
    backtrack(a, k, input);
    if (finished) return;
  }
}
```
- `isASolution(a, k, input)` tests whether the first k elements of vector a are a complete solution for the given solution. The last argument, input, allows us to pass general information into the routine.
- `construct_candidates(a, k, input, c, ncandidates)` - this routine fills an array `c` with the complete set of possible candidates for the kth position of a, given the contents of the first k -1 positions. The number of candidates returned in this array is denoted by ncandidates. 

# Questions
- What have you learned?
  - This is a classic application for backtracking algorithm
  - There's lots of solutions but none of them really shares the approach on how to get to the solution and how to TDD it.
  - I were a little confuse on how to mark and unmark the position we have visited, but it turns out that the simplest thing is just avoid side-effects for the currentPosition parameter
  - I still don't like the side-effects I have on QueenPositions to keep track all of the possible solutions on queen positions
- A strategy I followed?
  - I was on my bucket list to read through these programming challenges and algorithm design manual from Steven S Skiena as it seems to have good documentation on how to design algorithm.
  - start with smallest solution is n=4
  - it's expensive to go through 2<sup>64</sup> true/false vector for 8x8 board.
  - to make a backtracking program efficient enough to solve interesting problems, we must **prune the search space by terminating every search path the instant it becomes clear it cannot lead to a solution.**
  - Since no 2 queens can occupy the same column, we know that the n columns of a complete solution must form a permutation of n, this reduce the search space to 8! = 40320.
  - try to start from the client first/intention first
  - avoid using getter (help to reasoning where to put the behavior to avoid the getter method)
  - try to use approvals, but needs to reset the approved file whenever I need to change the test name
  - here's the PR -> https://github.com/tonytvo/n-queens/pull/1
  - takes about 2 mins and 500MB to find solution for 12x12 board

# References
- [Programming Challenges - Steven S Skiena, Miguel A. Revilla](https://www.amazon.ca/Programming-Challenges-Contest-Training-Computer-ebook/dp/B008AFF2ZU/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1651932964&sr=8-1)
- [The Algorithm Design Manual](https://www.amazon.ca/Algorithm-Design-Manual-Steven-Skiena/dp/3030542556/ref=sr_1_1)