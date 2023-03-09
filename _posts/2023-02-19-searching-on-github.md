# Searching on GitHub

[Searching On GitHub](https://docs.github.com/en/search-github/searching-on-github)

## Search for repositories

### Search by content

```
in: name | description | topics | readme
```

### Search by repository size

```
size: n
# for example
size:1000 # matches repositories that are 1 MB exactly
size:50..120 
```

### Search by forks

Whether to include forks

```
fork: true | false | only
```

### Search by stars

```
stars:n
```

### Search by number of followers

```
followers: n
# for example
followers:>=10000
followers:1..10
```

### Search by number of forks

```
forks:n
```

### Search by language

```
language:LANGUAGE
```



### Search by time

```
created:YYYY-MM-DD
pushed:YYYY-MM-DD
```

### Search by topic

```
topic:TOPIC
topic:n
```

### Search by license

```
license:LISENSE_KEYWORD
```

### Search by repository visibility

```
is:public | private
```

### Search base on whether a  repository is a mirror

```
mirror:true | false
```

### Search based on whether a repository is archived

```
archived: true | false
```

### Search based on number of issues with `good first issue` or `help wanted` labels

```
good-first-issues:>n
```

### Search based on ability to sponsor

```
is:sponsorable # matches repositories whose owners have a GitHub Sponsors profile.
has:funding-file # matches repositories that have a FUNDING.yml file.
```

## Search Issues & PR

### Search only issues or pull requests

```
type: pr | issue
# or
is: pr | issue
```

### Search by the title, body, or comments

```
in:title
in:body
in:comments
```

### Search within a user'sor organizatin's repositories

```
user:USERNAME
org:ORGNAME
repo:USERNAME/REPOSITORY
```

### Search by open or closed state

```
state:open | closed
is:open | closed
```

### Search by the reason an issue was closed

```
reason:completed
reason:"not planed"
```

### Search by author

```
author:USERNAME
author:app/USERNAME
```

### Search by assignee

```
assignee:USERNAME
```

### Search by mention

```
metions:USERNAME
```

### Search by team mention

```
team:ORGNAME/TEAMNAME
```

### Search by commenter

```
commenter:USERNAME
```

