---
title: study group patterns summary
date: "2021-12-27T22:12:03.284Z"
description: "study group patterns summary"
tags: ["productivity", "learning"]
---

# todo
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
- "what is the simplest, most cost-effective way to share learnings?"
- a group of people who functioned together in an extraordinary way, who trusted one another, who complemented each others' strengths and compensated for each others' limitations, who had common goals were larger than individual goals, and who produced extraordinary results.
  - the team that became great didn't start off great - it **learned** how to produce extraordinary results.
  - **a programmer's study group will meet regularly in a comfortable place to delve into important technical topics. These topics can come from group's learning repository, from books or articles, or even from a guest participant.**

## a learning repository
- a simple, security-free, browser-based learning repository, such as Ward Cunningham's Wiki
- just install it and asking folks to use it isn't enough. Teams need to establish usage convention
  - developers will quickly jot down learnings on index cards, as they work, and when they integrate their code, they can integrate significant learnings as well.
- atlassian confluence provides similar functionality but how can we organize and maintain the group knowledge effectively?

# A pattern language for study groups
- [a pattern language for study groups](https://www.industriallogic.com/img/blog/2012/03/khdraft1.pdf)
- a study group can make a difficult book easier to understand, it can succeed where an unsatisfying class fails, and it can support you if your environment doesn't support your ongoing learning and growth.
- once teams produce enough learning content they will need to reflect on and discuss it. 
- there are 2 good places to do this: for technical matters, the best place is a programmer's study group; and for team, people or process maters, the best place is in an iteration retrospective.
- **every programmer on the team needed to at least be aware of the system's potent smells. This would enable them all to pay attention to these smells and consider how to refactor them out of existence**.
  - look into process of documenting these potent smells (index cards, wiki, etc...). This would eventually led to direct action
- recommend that groups meet for 2 hours if they want to delve deeply into a subject, though one-hour meetings are fine for covering topics quickly
- absolutely no one should play the role of lecturer or teacher in a study group.
  - the group meets to conduct group learning.
  - if someone is expert in a certain technical area, that individual ought to help others learn, not show off or talk down to participants.
- continuously learning coach
  - the coach is the leader of the team. If the coach doesn't value learning, the team won't either.
  - the coach must lead by example. This means that the coach will seek out and obtain coaching and mentoring from the best sources available.
  - coaches must strive to learn about their customer's needs, team or personality conflicts, new technologies, and the latest wisdom about XP and other lightweight methods.
- patterns are grouped into 4 secions
  - spirit
    - after identifying a great source knowledge in a subject, work to create a rewarding, intellectually safe environment for hte study of that subject. 
    - contains [knowledge hydrant](#knowledge-hydrant), [pool of insight](#pool-of-insight), [safe place](#safe-place), [enduring energy](#enduring-energy), and [kindred collaborator](#kindred-collaborators)
  - atmosphere
    - establish a home for the study group that is centrally located, comfortable, aesthetically pleasing and conductive a dialogue
    - contains [common ground](#common-ground), [public living room](#public-living-room), [intimate circle](#intimate-circle) and [virtual space](#virtual-space)
  - roles
    - lead and energize the group, come prepared and help guide dialogues so that they are insightful and productive
    - contains [enthusiastic leader](#enthusiastic-leader), [motivated moderator](#motivated-moderator), [active participant](#active-participant), [prepared participant](#prepared-participant), and [distinguished participant](#distinguished-participant)
  - customs
    - follow customs that will re-enforce the spirit of the group, piquing participant's interest in dialogues, accomodating different learning levels, making the study of literature easier, recording group experiences, and drawing people closer together.
    - contains [opening question](#opening-question), [sequential study](#sequential-study), [agenda](#agenda), [subgroup](#subgroup), [distributed diary](#distinguished-diary) and [after hours](#after-hours)

## retrospectives
- the continuous learning approach to retrospectives means they come not at the end of a project, but at the end of every iteration.
  - conducting iteration retrospectives will enable teams to quickly adjust and improve their performance, because they will be continuously revisiting these questions:
    - what worked well?
    - what did we learn?
    - what should we do differently next time?
    - what still puzzles us?
    - what happened?
- people have a fear of retrospectives, because they have a fear of being attacked, of being made to look foolish, of getting a poor performance review or of hurting someone's feelings.
- it's detrimental to retrospectives if people are afraid, or if there is an atmosphere of blame, criticism, sarcasm, or even humor at other people's expense.
- "regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills, and abilities, the resources available, and the situation at hand."
- it's vital that the facilitator be an outsider and not a member of the team involved in the retrospective.
- participants take the lessons learned during the retrospective and turn them into concrete ideas for improving their development process.
  - the key to retrospective is to make sure you're solving the correct problem.

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
## safe place
- a good physical environment [common ground](#common-ground), [public living room](#public-living-room) is vital for any study group. Equally vital, is the intellectual environment.
- **loud-mouths, show-offs, know-it-alls, and people who are overly competitive, adversarial or confrontational, can make other uncomfortable or insecure, and create an environment that is not conductive to learning, sharing or the building of ideas**.
- when places of learning have highly critical or judgemental natures, an individual's ability to learn can easily be compromised.
- treat each other as colleagues with respect, despite differences in opinion, acknowledges the mutual risk and establishes the sense of safety in facing the risk.
- generally, as long as the people arguing are remaining civil (treat each other with kindness, consideration and respect) and as long as the argument isn't too far off the subject being studied, it can be quite instructive for a group to listen and learn.
- Usually, it is best for someone who is intimate with the group's customs to approach the individual during a short break or [after hours](#after-hours)
- establish a warm, tolerant, polite and focused environment in which individuals help each other where everyone is comfortable to ask questions and make mistakes.
- in practice, there will always be some level of personality conflicts or discord within a group. It can help if people get together after a session, [after hours](#after-hours), to talk about the issues.
## enduring energy
- this pattern identifies what is needed in a study group to bring it to life, and sustain it over time.
- **it's fairly easy to start a study group. But keeping it going, so that members are active, dialogues are insightful, and the group is long-lived, is another matter altogether.**
- a study group's energy initially comes from its founder. If the founder is genuinely interested in creating thriving, long-lasting [pool of insight](#pool-of-insight), to improve himself/herself and his community, the group will start life with a powerful energy. But if founder is merely interested in short-term gains, or personal recognition, the group will be short-lived.
- In considering the long-term vitality of the group, there are many decisions to make
  - when will the group meet?
  - how long will its meetings be?
  - what will be studied?
  - if poor or uninformed decisions are made about these issues, a group may be never take root or be long-lived.
- frequent meetings
  - it's difficult to maintain any sort of low or continuous energy. A month between meetings is usually far too long for people to maintain focus and enthusiasm. Therefore, have the group meet weekly or bi-weekly
  - these frequent meetings will allow a group to study effectively and may lead some members to become [kindred collaborators](#kindred-collaborators)
  - hour meetings
    - a one hour meeting is typically not enough time for a group to have an insightful dialogue on a piece of literature. But three hours is too much time, since most participants can't actively engage in dialogue for that long
    - therefore, limit dialogues to a maximum of 2 hours, and if energy has waned significantly before that time, finish the meeting early
  - short breaks
    - at a certain time in a dialogue, a group's intensity focus and effectiveness will begin to diminish. If the group doesn't take a break at this time, the quality of the dialogue may begin to deteriorate and people will become uncomfortable.
    - therefore, allow for a short (10 or 15 minute) break in the middle of a study group session, to let members reflect, chat, use the restrooms, and prepare for the next half of the dialogue.
  - avoid group meetings in dull, stuffy, maybe windowless, conference room since the location and space will play a huge role in sustaining a group's energy.
    - places that attract people is usually, spacious, comfortable, energetic. It helps creating bonding and bring life to the dialogues.
  - **create study groups out of genuine enthusiasm to study a subject in-depth. Meet weekly or bi-weekly for 2 hours, and have a short-break in the middle. Choose a meeting location where people will enjoy passing time, and study only those writings which are worthy of group's attention**
  - ![enduring energy](./enduring-energy.png)
  - for ideal meeting environment, look for [common ground](#common-ground) and [public living room](#public-living-room)
  - create [subgroups](#subgroup) and [study cycle](#study-cycle) to let people place their energy where they best see fit. And when group energy is low, have a [distinguished participant](#distinguished-participant) join the group for an evening
  - it is a custom of some groups to go out after meetings [after hours](#after-hours) to partake in food and drink. This social time can go far towards sustaining relationships and adding energy back to a group...
## kindred collaborators
- when a study group has an enduring energy, people get to know each other, a community forms, and there is a lasting possibility for collaborations and working relationships
- **so many people dislike networking. They want to grow professionally, and they think that networking can help, but they don't know how, where and with whom to network effectively.**
- many people feel isolated in their jobs. So much of their time is spent working that there is little time left to pursue genuinely interests them.
  - some try to organize study groups within their own companies, but if often fails due to lack of interest, or because many people prefer to be outside of work when they have any free time.
  - some people go to conferences lectures, user groups and parties in the hope of advancing their careers and themselves. Often, they end up frustrated in reality, they don't grow professionally at these meetings and their networking is ineffective. The trouble often results from what may be described as weak connections that develop between people who meet in large groups.
  - In frequently meeting study group, people get to know each other over time. They learn what they like and dislike, what they excel at and where they are weak, where they are in their careers and where they'd like to go. This level of familiarity forms the foundation for a rich network that can yield very real career and collaboration possibilities.
  - As one gets to know others within a group, one can get a very good idea of who would be good for a specific projects
- ![kindred collaborator](./kindred-collaborator.png)
- quality networking happens best when a study group is a [safe place](#safe-place) composed of diverse individuals and true peers. The best time for networking is either before study groups meets or [after hours](#after-hours)

## common ground
- people lack a place where they can have regular, meaning ful dialogues with other people in a casual, social setting. Work and home don't provide it, and many clubs or groups also don't provide it because they meet in lifeless environments that feel like someone else's turf
- people need informal public places where they can gather, put aside the concerns of work and home, relax and talk. Germany's beer gardens, English's pubs, and French and Viennese cafes created this outlet in people's lives, providing a neutral ground where all are equal and conversation is the main activity.
- without such places, the urban area fails to nourish the kinds of relationships and the diversity of human contact that are essence of the city. Deprived of these settings, people remain lonely within their crowds.
- it's naturally to choose one of the company's conference rooms as a meeting location as it is spacious quiet, filled with white boards, available after hours, and free. However, it's not a good choice, since both employees and visitors to the company, generally don't like to spend their free time in stuffy, stale, office environments.
- **hold public study groups where diverse individuals will all be on common ground. The best locations are easy for people to get to, but not too close to their offices or homes.**
- once common ground has been selected, a group must find a [public living room](#public-living-room), a comfortable, relaxing, dialogue-friendly place.
## public living room
- **inhospitable physical locations - stale, lifeless, badly lit, and uninviting - stifle individuals and thereby hinder lively, engaging dialogues.**
- allow traffic to flow with minimum disruptions since members often arrive late, leave early, get up for snacks or use the restrooms.
- sitting circle
  - place each sitting space in a position which is protected, not cut by paths or movements, roughly circular, made so that the room itself helps suggest the circle, not too strongly, with pats and activities around it, so that people naturally gravitate toward the chairs when they get into the mood to sit.
- different chairs
  - helps people understand that the seating preferences of diverse people differ and that a group will be most comfortable if a space is outfitted with "a variety of different chairs, some big, some small, some softer than others, some rockers, some very old, some new, with arms, without arms, some wicker, some wool, some cloth."
- pool of light
  - place the lights low, and apart, to form individual pools of light which encompass chairs and tables, like bubbles to reinforce the social character of the spaces which they form.
- choose a warm, spacious establishment where people will enjoy mingling before and after study session, where there is comfortable, rearrangable furniture, plenty of warm lighting, and a variety of foods and drinks.
- some groups may choose to reserve space or arrange to meet at a location when it closes to the public to avoid noises at certain times of day.
- ![public living room layout](./public-living-room.png)
## intimate circle

## virtual space

## enthusiastic leader

## motivated moderator

## active participant

## prepared participant

## distinguished participant
## subgroup

## distinguished diary
## study cycle

## opening question

## agenda

## after hours

## sequential study

# Quotes



# References
- https://fs.blog/the-buffett-formula/
- https://www.industriallogic.com/img/blog/2005/09/ContinuousLearning.pdf
- https://www.industriallogic.com/img/blog/2012/03/khdraft1.pdf
