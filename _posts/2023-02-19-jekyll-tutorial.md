---
title: "Jekyll Tutorial"
excerpt: "从零开始的 Jekyll Tutorial，助力搭建 GitHub Pages 。"
---

# Jekyll Tutorial

This is Jekyll's Tutorial. Through this tutorial, you will learn how to create a Jekyll project.

## Introduce Jekyll

Jekyll is a tool that **transforms your plain text into static websites and blogs**.

It has the following feature characteristics:

- Simple
- Static
- Blog-aware

For more detail, you can visit [the official website](https://jekyllrb.com).

## Prepare Environment

It's programmed in `Ruby`, so it is required. Visit [the official website](https://www.ruby-lang.org/en/) and install it.

Check whether the ruby is installed:

```shell
ruby -v
```

If not exiting, install the ruby:

```sh
sudo apt-get install ruby
```

Then Install the tools:

```shell
gem install bundler jekyll
```

## Syntax

Jekyll uses the Liquid templating language to process templates.

{% raw %}

```liquid
# e.g.
{{variable}}
{% if statement %}
```
{% endraw %}

For more details, check [this](https://jekyllrb.com/docs/liquid/).

## Examples

The following example shows you how to make Jekyll work.

### Minimal Mistakes Jekyll theme

Clone [the project](https://github.com/mmistakes/minimal-mistakes) and get in it.

```shell
git clone https://github.com/mmistakes/minimal-mistakes.git && cd minimal-mistakes
```

Fetch and update bundled gems by running the following [Bundler](http://bundler.io/) command:

```
bundle install
```

Start the local service:

```shell
bundle exec jekyll serve
```
