---
title: "Jekyll Toturial"
excerpt: "从零开始的 Jekyll Tutorial ，助力搭建 GitHub Pages 。"
---

# Jekyll Toutial

This is Jekyll Toutial. Through this tutorial you will learn how to create a Jekyll project.

## Introduce Jekyll

Jekyll is a tool which **transfiorm your plain text into static websites and blogs**.

It has the following feature characteristics:

- Simple
- Static
- Blog-aware

More Details can visit [the official website](https://jekyllrb.com).

## Prepare Environment

It's programmed in `Ruby`, so the `Ruby` is required. Visit [the official website](https://www.ruby-lang.org/en/) and install it.

Check whether the ruby is installed:

```shell
ruby -v
```

Install the tools:

```shell
gem install bundler jekyll
```

## Syntax

Jekyll uses the Liquid templating language to process templates.

```liquid
# e.g.
{{variable}}
{% if statement %}
```

[More](https://jekyllrb.com/docs/liquid/)

## Examples

Use example show you how the Jekyll work.

### Minimal Mistakes Jekyll theme

Clone [the project](https://github.com/mmistakes/minimal-mistakes) and get in it.

```shell
git clone https://github.com/mmistakes/minimal-mistakes.git && cd minimal-mistakes
```

Fetch and update bundled gems by running the following [Bundler](http://bundler.io/) command:

```
bundle
```

Start the local serve:

```shell
bundle exec jekyll serve
```

