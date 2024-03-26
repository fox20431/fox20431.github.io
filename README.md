# Blog

*forked from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)*

## Introduce

This is the source repository of my blog site.

Powered by [Jekyll](https://jekyllrb.com/).

## Usage

### Install Ruby

Install ruby:

```sh
sudo pkg-mgr install ruby
```

Install ruby utils:

```sh
sudo gem install bundler jekyll
```

### Build

Preset the libary path

```sh
bundle config set --local path 'vendor/bundle'
```

Install the dependencies:

```sh
bundle install
```

Build the site and make it available to Jekyll, a local server.

```sh
bundle exec jekyll serve
```

### Contribution

First, you need to know the Jekyll convention, please check [the documentation](https://jekyllrb.com/docs/).

For this project, to learn page construction, you should follow the flow: `_pages` -> `_layout` -> `_includes`.

Of course, the `_config.yml` is import file to configure the site.