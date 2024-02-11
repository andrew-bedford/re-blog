# re/blog
A simple client-side markdown blog engine, built for fun! One of the goals is to add a plugin system that would allow users to easily customize it.

*Warning*: Not SEO optimized.

## Features
Clean default interface with a content navigation pane, which allows users to skip to specific sections.
![](wwwroot/images/interface.png)

Navigate posts using a timeline, previous/next buttons, or left/right keyboard arrows.
![](wwwroot/images/timeline.png)

## Usage
Add markdown files to the `wwwroot/posts` folder and update `index.json`. Posts are expected to have the following YAML header:
```
---
id: lorem-ipsum
title: Lorem Ipsum
abstract: Optional abstract
created: 2024-01-01
tags: tag1, tag2
---
```
Where `id` corresponds to the url slug to be used, so it should not contain any spaces.

After customizing `Pages/Index.razor` (e.g., specifying avatar), the blog can be published using:
```
dotnet publish
```
For development:
```
dotnet watch run
```

## Tasks
 - [ ] Add support for cache invalidation.
 - [ ] Add build tasks that would make it easier to publish/deploy the blog.
 - [ ] Create global configuration file to allows users to do things such as set the avatar image, blog name.
 - [ ] (?) Add metainformation panel.
 - [ ] (?) Add support for comments.
