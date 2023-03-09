# Blog

*forked from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)*

## Introduce

This is the blog that records the notes.

## Build

If you have installed the ruby on your machine, follow the following steps to run it. If not, check `Install Ruby`.

Build the site and make it available to Jekyll, a local server.

```
bundle exec jekyll serve
```

### Install Ruby

**for Windows**

Download and install `Ruby` from [the official website](https://www.ruby-lang.org/en/) then execute the command:

```sh
bundle install
```

**for Linux**

Install ruby

```sh
sudo apt-get install ruby
```

```sh
sudo gem install bundler jekyll
```

### Donate

First, you need to know the Jekyll convention, please check [the documentation](https://jekyllrb.com/docs/).

For this project, to learn page construction, you should follow the flow: `_pages` -> `_layout` -> `_includes`.

Of course, the `_config.yml` is import file to configure the site.