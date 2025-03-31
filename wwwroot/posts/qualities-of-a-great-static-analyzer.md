---
id: qualities-of-a-great-static-analyzer
title: Qualities of a great static analyzer
abstract: Learn how static analysis can not only help us find bugs, but also grow as developers.
created: 2024-08-05
tags: static analysis, thoughts
---

# Qualities of a great static analyzer
Demand for static analyzers has [increased significantly in recent years](https://trends.google.ca/trends/explore?date=all&q=sast), and is expected to continue to grow in the future. This is in part due to the rise in cyber threats, the increasing impact that vulnerabilities can have, their mediatization (e.g., heartbleed, spectre, crowdstrike), the emergence of new standards and regulations in certain industries (e.g., automotive, healthcare) and of course, the increasing rate of changes in programming languages. For example, C++ has new versions every 3 years, C# every year, and Rust every month. At this rate, even the most experienced developers can struggle to keep up with the latest best practices.

So, what can static analyzers do to help us better understand problems? What distinguishes good static analyzers from great static analyzers?

## Accuracy
It goes without saying that static analyzers should be as accurate as possible. That is, they should report as few false positives and false negatives as possible, while maximizing the number of true positives and true negatives. Of course, it is not possible to be perfectly accurate as the properties being checked are often [undecidable](https://en.m.wikipedia.org/wiki/Undecidable_problem). So in the world of compliance, static analyzers will often opt to report more false positives to have fewer false negatives, you know, to be on the safe side. A side effect of this though is that it may cause developers to start ignoring problems reported by static analyzers, even start to loathe having to review their results and to want to avoid using them.

## Documentation
Every property being checked should be documented in such a way that a new user, someone who has never encountered this type of problem before, should have all the information they need to understand why it's a problem, what is the potential impact, and what they can do to avoid it. At the same time, the documentation shouldn't be too long to read, and shouldn't repeat itself. One way to avoid repetitions is to provide links to pages that explain specific concepts (e.g., cross-site request forgery). This allows developers who are already familiar with the concept to simply skip that part. The documentation should also include examples of problematic code and their "fixed" versions. It should be clear after reading the documentation what actions should the developer take.

## Traces
Unless the property being checked is trivial and obvious, a static analyzer shouldn't simply tell you that there's a problem at line X, it should give you a trace that helps explain how the problem can occur. This trace should be detailed enough for the developer to understand and confirm that it is indeed a problem, but not overly verbose. It should not present developers with unnecessary details.

<!-- ## Ease-of-use
It should be easy to install and use. [SonarLint](https://www.sonarsource.com/products/sonarlint/) is I think a great example of this. You simply install their extension from the Visual Studio Code marketplace, point it to your [compilation database](https://clang.llvm.org/docs/JSONCompilationDatabase.html) file if it's analyzing C/C++, and off it goes. -->

## Performance
A great static analyzer should be fast, like *really* fast. The slower it is, the less likely people will want to use the tool. One way to deal with this is to support incremental/differential analysis where only the modified files or functions are analyzed and information from previous analyses is re-used. The quicker it is, the more likely the issue will be found while we are coding it and are still in the right context, which will increase the likelihood that we will fix the issue.

To avoid path explosions (i.e., having to explore too many potential execution paths), accuracy often needs to be traded for performance. A great static analysis tool finds the right balance for its target audience.
