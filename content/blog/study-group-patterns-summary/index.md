---
title: study group patterns summary
date: "2021-12-27T22:12:03.284Z"
description: "study group patterns summary"
tags: ["productivity", "learning"]
---

# todo
- summary continuous learning from joshua kerievsky
- a pattern language for study groups from joshua kerievsky

# The theory and practice of teaching and learning
## Learning outcomes and objectives
- when people return to their desk, will they be able to apply what they've learnt in a useful way
- have a fair idea who will come and what's the production code and tests look like at present
- discuss with attendee what they're interested in learning and what they are currently struggling with.
- bloom's taxonomy, thinking skills can be described in terms of six broad categories
  - remembering, understanding, applying, analyzing, evaluating, creating
  - help you plan exercises and teaching materials at an appropriate level
  - start with materials to build remembering, understanding and applying
  - when those thinking skills are in place, you can do more analyzing, evaluating and creating
  - find a long lists of good **verbs** to describe thinking skills in each category. These words are useful as a prompt or start of a sentence.
## the '4C' learning model
- each person who comes to your learning hour has a unique background, and what they're going to learn needs to be integrated with what they already know for it to stick.
- 4C's:
  - connect: get people in the right head-space for learning about the topic together
  - concept: introduce the new skills or ideas or information you want the participants to learn
  - concrete: hands-on exercises to practice skills or figure out how things work
  - conclusions: an opportunity for people to consolidate and internalize what they've learnt.
- you want to help people to be present mentally, fuel their curiosity, let them work out what they need to do, and to come to their own understanding of the topic.
## Design learning experiences that fit with how the brain works
- useful rules about how the brain works
  - **movement trump sitting**
    - you want people to move out of a sitting position at least every 10-15 minutes
    - arrange the chairs so people physically stand up and move a chair to the right every time you change typist
    - when you gather observations in retrospective, people can each walk up to the whiteboard and stick their notes onto it.
    - when reviewing code, you can stick printouts to the walls and have people move around to look at them.
    - if you're working together remotely, get people to take breaks and leave their desks from time to time.
  - **talking trumps listening**
    - when you talk about what you just heard it reinforces your memory of it.
    - talking also gives opportunities for feedback from others about how well you seem to understand the topic.
    - ask people to pair up to discuss a topic or share experiences.
  - **images trumps words**
    - if the picture and associated story evokes an emotion, it would make it easier to pay attention and recall it later.
    - long-term memories often comprise of images and associated emotions.
  - **writing trumps reading**
    - when you read, it's easier for your mind to wander.
    - writing also makes the information multi-sensory, you physically move a pen on some paper as well as see the text on the page.
    - draw lines and boxes to situate the information in space and relate it to other information.
    - provide handouts, notes and quizzes that people can annotate. Ask people to write conclusions and observations on sticky notes
  - **shorter trumps longer**
    - student's minds tend to drift after about 10 minutes of traditional lecture.
    - to keep people's attention, divide your presentations into 10-20 minute chunks and in between spend at least 1-2 minutes on some other activity.
    - perhaps ask people to review or discuss the material presented so far
    - break off occasionally for Q&A, or to ask people to note down what they observed so far.
  - **different trumps same**
    - anything new or unexpected will catch people's attention.
    - games and simulations an exercises can contain built-in surprises.
    - suddenly change requirement mid-exercise. Keep it fun.
- One example learning objectives
  - describe some characteristics of approval testing -> remembering
  - compare approval testing with assertion-based testing -> understanding
  - use the approvals framework to write test cases -> applying
## Deliberate practice
- in order to use red-green-refactor cycle competently, you need to
  - identify the next test case that will incrementally improve your solution
  - design the specifics of that test case and see it fail
  - implement a solution design which is testable
  - refactor to improve your design.
  - if you're weak in any one of those component skills, you will struggle to do TDD.
- the great advantage of practice exercises is we can find ones that let us work on those component skills individually
- as a teacher, I want to plan a series of learning hours that will be at just hte right level so people don't get bored and don't get overwhelmed or frustrated.
# Sample Learning Hour
## incremental working, driven by tests
- try to get people comfortable with one another and feel safe to work in pairs.
### learning goals
- the learning hour is in the "small steps" theme
- describe the read-green-refactor cycle
- explain why you write the tests first and not all at once
- design a pure function that takes an integer and returns a boolean using TDD

### session outline
- 10 min connect: divide into pairs, 3 benefits of TDD
- 15 min concept: demo leap years
- 20 min concrete: do leap years in pairs
- 10 min conclusions: summary of main idea

### connect
- ask people to form pairs and introduce themselves if they don't know each other.
- ask them to discuss the question "what are some of the main benefits of doing TDD?"
- after 3 mins ask each pair to report one thing they came up with the group

### concept
- starting at a whiteboard, explain the purpose of the kata
- write up all 4 examples given in the kata description on a whiteboard. Note that these will turn into tests
- make it clear you interleave designing tests and writing code.

### concrete
- ask people to work in pairs or an ensemble to do the same thing
- start from problem description and an empty editor, and complete the Leapyear function using TDD
- every 3-4 minutes, remind them to swap the person who has the keyboard
- coach them to write the tests before the implementation, working incrementally and iteratively.

### conclusions
- think about what we did today. If you had to explain the main idea of TDD to someone else, what would you say?
- write your explanation in a sentence or two on a post-it.
- put up a flipchart with the question "what is the main idea of TDD?" Ask people to stick their post-it notes on it.
- read some notes out to the group before you partway.
- hang the poster somewhere prominent afterwards, perhaps in the team area or coffee room.
- if working remotely, they can each write their sentence or two in a shared online document.

# Continuous learning
- [industrial logic continous learning](https://www.industriallogic.com/img/blog/2005/09/ContinuousLearning.pdf)
- XP teams are very code-centric and focused on making functional software. When reflection and learning happen, it's often in a watered down, haphazard way.
- someone has to decide to make learning not just an individual experience but a collective experience. When that happens, learning isn't just something that occurs naturally, it is something that the company uses to drive the future of business.

# A pattern language for study groups
- [a pattern language for study groups](https://www.industriallogic.com/img/blog/2012/03/khdraft1.pdf)
- a study group can make a difficult book easier to understand, it can succeed where an unsatisfying class fails, and it can support you if your environment doesn't support your ongoing learning and growth.
- to get an overall understanding of what generates successful study group, take 15 to 25 minutes to read the name of each pattern, looking at each pattern's picture, and then read each pattern's problem and solution headlines
- for more in-depth study, scan the patterns in 15-25 minutes, and follow this with a patient reading of each and every patterns. As you read the body of each pattern, you will notice that certain sentences are written in italics. read the italics to get to the hear of the idea.

## knowledge hydrant
- where can one obtain knowledge in its fullest unfiltered, unsimplified form.
- great literature tends to be hard to study and understand. Many people either aren't prepared to do this hard work or simply don't want to
- authors of great literature commonly reference, extend, or refute ideas communicated by their ancestors or peers. This can make it doubly hard to understand their writings, since one may need to understand referenced works in order to understand author's own work.
- as great literature ages, people don't believe it will contain the "modern" knowledge they need. So even if some great book written 30 years ago contains the exact knowledge they seek, people won't find it, for they are unaware of the abundance of knowledge contained in older works of literature.
- the hard work put into the study of great literature is worthwhile because it ensures that people retain the knowledge they wish to obtain
- great literature is much easier to understand when it is studied in an intelligent sequence [sequential study](#sequential-study)
- it is easier and more rewarding to study great literature with other people [pool of insight](#pool-of-insight)
- discover the great literature in your profession or area of interest - the finest books, articles, and speeches ever written, and then begin an earnest study of these works.
- how do you find the great literature worthy of study? Ask people. Ask knowledgeable people which authors they like, what are their favorite books, what profoundly influenced them?
- after identifying the works, form or join a study group, [pool of insight](#pool-of-insight), order the works to be studied [sequential study](#sequential-study) and compose an [agenda](#agenda)

## sequential study

## pool of insight
- once you've discovered your [knowledge hydrant](#knowledge-hydrant), it can be overshelming to drink from it. This pattern suggests how to make the study of great literature easier and more rewarding
- there's nothing wrong with reading and studying literature on one's own. But great literature is worth knowing well, and individual study pales in comparison with teh study of literature in a group dialogue.
- in communicating how they understand something, people may
  - clarify what confused others
  - expose their own misunderstandings
  - reveal new ideas
  - articulate that which they didn't know they knew
- in a dialogue, nobody is trying to win. Everybody wins if anybody wins.
  - whenever any mistake is discovered on the part of anybody, everybody gains.
  - there is a spirit present in dialogues that one doesn't find in many other learning environments
  - many groups sustain a group's spirit by meeting weekly or biweekly
- read and study literature on one's own, but discuss it with others in a regular study group. Aim to ask questions about you don't know and explain what you do know. Your exchanges with colleagues will enrich your understanding immensely.
- the best study groups are those in which individuals feel comfortable learning with others [safe place](#safe-place)
- some environments promote dialogues, [common ground](#common-ground) and [public living room](#public-living-room)
- the most enriching study happens when a group has a [motivated moderator](#motivated-moderator) and [prepared participants](#prepared-participants)
## agenda

## safe place

## common ground

## public living room

## motivated moderator

## prepared participants

# Quotes



# References
- https://fs.blog/the-buffett-formula/
- https://www.industriallogic.com/img/blog/2005/09/ContinuousLearning.pdf
- https://www.industriallogic.com/img/blog/2012/03/khdraft1.pdf
