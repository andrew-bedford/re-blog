---
id: to-open-source-or-not-to-open-source
title: To open source, or not to open source
abstract: Thoughts on open sourcing projects that you want to productize.
created: 2024-07-21
tags: oss, thoughts
---

# To open source, or not to open source
That is the question that every software developer contemplating productizing one of their personal projects and starting their own company asks themselves. And it is one that I've been increasingly asking myself.

One might wonder, if the objective is to make enough money to live off your project, then why consider making it open source at all? Because making open source presents some interesting advantages.

## Advantages
### Community
If the software is useful, then a community of users and developers will naturally grow around it. The community will contribute to the project by reporting/fixing issues, providing feedback, helping implement new features and sharing it with others, which will help foster adoption.

The other side of this though is that you may end up spending more time than you would like managing the community (e.g., reviewing pull requests, answering questions, debating on the direction) and less time actually developing the product.

### Transparency
Being open source adds an element of trust to your software and your company since users can inspect your source code and validate that it is not doing anything unexpected. Knowing that other people will be looking at your source code may also encourage you to write cleaner code, especially if you are the only one working on it.

You could still get this advantage by making your software open and "source-available", but not actually open source using certain licenses (e.g., Elastic, SSPL).

### Tools
There are multiple tools (e.g., static analyis tools) and features (e.g., GitHub Pro) that are free to use on open source projects, but that require a paid version for private repositories. By making your project open source, you'll be able to benefit from these.

### Bus factor
Simply put, the bus factor refers to the number of people who are essential to maintain a project. If these key individuals were to leave the team suddenly (e.g., hit by a bus), then the project would be at risk of failure. It is something that companies will consider before picking software. By its very nature, open source projects usually have a higher bus factor because of its open collaborative style. Also, if a project grows stale and stops being maintained, it can always be forked and continued by someone else.

---

## Business models
That's all nice, however to be successful and survive, a company has to be profitable. That is, it should make more money than it spends. So then the question becomes: how to monetize open source projects? Let's look at some of the common open source business models.

### Freemium
Under the freemium model, a base version of the software is made open source and available for free, and a premium version with additional features is sold. This model is also known as "open core". Having a free version makes it more likely for people to try your software. The main disadvantage of this is that you end up maintaining two different versions. However, if the software can be made to be extendable, then potentially only certain plugins could require payments. And if it is extendable, then you might be able to build a shop where users could share and/or sell their plugins.

### Software as a service
Offering your software as a service is another popular model (e.g., [Umami](https://umami.is/)). Users may find this option attractive as will be easier for them to get started, they won't have to maintain their own infrastructure, they won't have to worry about upgrades, and it will always be running the latest version thereby reducing your support costs and reducing security risks. On the other hand, *you* will have to worry about all of these. And if you use external infrastructure (e.g., AWS, Azure), you will have to be careful of the costs and your pricing struture.

### Dual licensing
Another possible strategy is to dual-license your software. One license could make it available for free with certain limitations (e.g., only for personal use), and another could be more permissive (e.g., allow commercial use) but require payments. Some people would argue that this isn't really open source, but more of a "source available" kind of thing because of the limitations, but hey, it's your software, you get to decide the terms of use.

### Crowdfunding
Open source projects may try to get donations through crowdfunding platforms such as [Open Collective](https://opencollective.com/), [Buy Me a Coffee](https://buymeacoffee.com/), [GitHub Sponsors](https://github.com/sponsors), [Patreon](https://www.patreon.com/) or other similar platforms. It works for some, but most will be lucky to get more than a handful of donations. Unsurprisingly, it seems that people won't pay for something that they can get for free. Which makes sense, they need something in return (e.g., prioritized issues and support, early access to features, influence on the roadmap).

### Sponsorship
Companies may start to sponsor your project if it becomes an integral part of their products. However, it takes a while to get there.

### Consulting
If the software becomes popular enough, depending on its nature, there might be a demand for consulting and training to help companies set it up, use it and extend it.

<!--
-## Licenses
Depending on the business model being used
-->

---

Frankly, I'm still not sure which way to go. Many successful companies (e.g., Microsoft, Google, Meta) open source tools that they use to build products, but not the products themselves. Maybe that's the way to go?