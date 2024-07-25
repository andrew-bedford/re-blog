---
id: using-pandoc-as-a-static-site-generator
title: Using pandoc as a static site generator
abstract: Learn how to generate a stylized static site from markdown using pandoc.
created: 2018-08-10
tags: blog, pandoc
---

# Using pandoc as a static site generator
There has been a resurgence of [static site generators](https://staticsitegenerators.net/) over the last few years (see [Google Trends](https://trends.google.com/trends/explore?date=all&q=static%20site%20generator)), and for good reasons. Static websites present several advantages over dynamic websites such as: they are easier to develop and deploy, cheaper to host, and faster to load.

As I was starting this blog, I considered multiple static site generators, but ultimately chose to use [Pandoc](https://pandoc.org/) due to its simplicity. Pandoc is a universal document converter created by professor [John MacFarlane](https://johnmacfarlane.net/). It supports a variety of input (and output) formats such as markdown, latex, html and microsoft word. To illustrate how to use it as a basic static site generator, we will use markdown as the input format.

## Markdown
Markdown is a widely used plain text format that allows users to insert headers, paragraphs, blockquotes, code blocks, links, images, tables, formatting, and much more, while remaining human readable. It has become my preferred format for notes in recent years. If you are new to Markdown, I recommend checking out the [Markdown Guide](https://www.markdownguide.org/). It even allows you to insert HTML if you need more control. For the fellow academics out there, you can also insert latex content. For example:
```
$$
\begin{equation}
  V_{sphere} = \frac{4}{3}\pi r^3
\end{equation}
$$
```
will generate
$$
\begin{equation}
  V_{sphere} = \frac{4}{3}\pi r^3
\end{equation}
$$

## Example
But enough about markdown, let's get back to pandoc and static site generation. Here is a simple markdown file with a title and two paragraphs.
```md
Hello World
===========

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

```sh
pandoc --from=markdown --to=html --output=hello-world.html --standalone hello-world.md
```

Note that by default, pandoc produces a document fragment. To produce a standalone document (e.g. a valid HTML file including a `<head>` and `<body>`), we have to use the `-s` or `--standalone` flag.

![without css](posts/images/without-css.png)

### Stylesheet
To make it look nicer, you can specify a css file using the `--css` option:

```sh
pandoc --from=markdown --to=html --css=pandoc.css --output=hello-world.html --standalone hello-world.md
```

The css file that I use is based on the one published by [Pascal Hertleif](https://gist.github.com/killercup/5917178).

![with css](posts/images/with-css.png)


### Template
To further customize your page, you can use your own template using the `--template` option:

```sh
pandoc --from=markdown --to=html --template=pandoc.html --css=pandoc.css --output=hello-world.html --standalone hello-world.md
```
I recommend basing your template on Pandoc's default template. It can be retrieved by executing the following command:

```sh
pandoc --print-default-template=html > pandoc.html
```

### Batch conversion
If you have multiple markdown files to convert, you can use a simple bash script:
```sh
#!/bin/sh
for post in $(ls *.md); do    
    mkdir -p $(basename ${post%.md})
    pandoc --from=markdown --to=html --template=pandoc.html --css=pandoc.css --output=$(basename ${post%.md})/index.html --standalone $post; 
done
```
