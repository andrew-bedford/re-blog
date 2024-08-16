---
id: why-im-creating-my-own-web-analytics-solution
title: Why I'm creating my own web analytics solution
abstract: Learn what lead me to create re/analytics.
created: 2024-07-15
tags: re/analytics, sqlite
---

# Why I'm creating my own web analytics solution
As I began putting more and more content on my personal website, I started to wonder if anyone was actually visiting it. Not that I really cared if anyone read by blog posts or checked my projects, I do those mostly for me, but I was still curious. After all, one of the reasons I publish posts is to share my findings and hopefully help someone. This prompted me to start looking for a web analytics solution. More specifically, one that wasn't Google Analytics; it has too many privacy issues. I found out that there's been a surge of awesome privacy-friendly web analytics solutions in recent years, some closed source (e.g., [Fathom](https://usefathom.com/)) and some open source (e.g., [Plausible](https://plausible.io/), [Umami](https://umami.is/)). Yet, I still decided to create my own web analytics: [re/analytics](https://analytics.andrew-bedford.ca/andrew-bedford.ca/).

![re/analytics](posts/images/re-analytics-2024-07-29.png)

Why? That's a great question, why bother re-inventing the wheel? Well, there's multiple reasons that led me to this decision.

## Learning
I've been tinkering with [.NET Blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor) for a few years now, but have yet to build a fully featured product based on it. Since web analytics software are pretty simple, essentially hit counters on steroids, I thought that it would be a nice project to start with and gain some more Blazor experience. Also, it's fun! I haven't been this productive since the days of Delphi 6.

## Entrepreneurship
I've been thinking about starting my own company for a while, actually since my teenage years, but more seriously recently. I thought that this might make a good first product. Even if it doesn't take off, I'll have learned a ton of things (e.g., lean startup canvas, swot analysis, business models).

## .NET
None of the open-source web analytics solutions that I saw were implemented in .NET, my platform of choice for most things. That's not really an issue for a regular user, you just include a javascript file in your pages and voilà, but as a developer, I knew that I would want to modify it and I knew that I would enjoy it more if I could use my favourite language and tools to do it. At the same time, I think that this presented me with an opportunity to develop something specifically aimed at the .NET community. For example, it would be nice if we could simply do something like:
```
dotnet add Re.Analytics
```
Add an API key in their code, environment, or some kind of secret storage, and that's it!

## Modularity
I'd like to bring [Obsidian](https://obsidian.md/)'s impressive modularity to web analytics software. While there are solutions that support custom events, it would be nice, for example, if users could simply toggle the tracking of file downloads. It would be even nicer if users could easily create their own modules and share it with the community (e.g., to provide new visualizations) or new themes.