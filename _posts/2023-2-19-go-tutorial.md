# Go Tutorial

Go

## Install

Use the package manager to install `go`, or download from go official websites and install it.

```sh
pkg-mgr install go
```

## Editor

### Visual Studio Code

I recommended all to use `Visual Studio Code`(I will abbreviate it to `vscode` later), it's simple and free.

Install Extension:

- Go
- Go Nightly (Optional)

Using go extension feature, install tools about go. Firstly, `ctrl/cmd + shift + p` open `palette` and input `go:install/update tools` to install all go tools.

## Get Started

Create a project, it called module in GO.

More about it, please check [Go Modules Reference](https://go.dev/ref/mod).

```sh
go mod init <PROJECT_NAME>
# for example
go mod init hihusky.com/base
```

create `main.go` file in wordspace and type a snippet:

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, world!")
}
```

Run:

```sh
go run main.go
```

## Learn Module

### go.mod files

After `go mod init <PROJECT_NAME>` was executed, the workspace generate a file called `go.mod`.

I will post the content at the following:

```go.mod
module hihusky.com/punch-power

go 1.19
```

As you saw, `go.mod` just includes moudle path and the version of go.

Of course, it's just a simple example.

Now, let's get some dependencies for current module, use the following command:

```sh
go get [-u] <PACKAGE>
# for example
go get github.com/lib/pq
```

The above commands will append some infomation in `go.mod`.

```sh
require github.com/lib/pq v1.10.7
```

Besides, other `directives` exist in `go.mod`.

Let me show you all key words and usages.

- `module <MODULE_PATH>`:
- `go <GO_VERSION>`:
- `require <PACKAGE>`:
- `replace <MODULE_PATH> => <MODULE_PATH/FILE_PATH>` 


## Syntax

### Declare variable/constant

声明变量或常量

**Variable**

```go

// declare and assign variables
var <IDENTIFIER_1>[, IDENTIFIER_2, ...] = <VALUE_1>[, VALUE_2, ...]
// it allows you to declare different type variables at one time
// for example: `var a, b = 1, "hello"`

// the above can be abbreviated as follows
<IDENTIFIER_1>, [IDENTIFIER_2, ...] := <VALUE_1>[, VALUE_2], ...
// for exmaple: `a, b := 1, "hello"`

// just declare variables
var <IDENTIFIER_1>[, IDENTIFIER_2, ...] <TYPE>[ = VALUE_1[, VALUE_2, ...]]
// due to specify the type, assigning value can be ignore
// if assigning value is ignore, it will be set default value
// compared with previous two, the way has a limitation is that the variable must has the same type, because type is sole and must declare at the end of all variable name
// for example: `var a, b bool`, `var a, b bool = false, true`
```

**Constant**

```go
// it is different from variable
// const requires must assign value and cannot be changed

// declare const
const <IDENTIFIER_1>[, IDENTIFIER_2, ...] = <VALUE_1>[, VALUE_2, ...]
// for example: `const a, b = 1, "hello"`

// declare const and its type
const <IDENTIFIER_1>[, IDENTIFIER_2, ...] <TYPE> = <VALUE_1>[, VALUE_2, ...]
// like variable, the type is sole and at the end of all const names
// so all const must use the same type value
// for example: `const a, b bool = true, false`
```

### Underline

`_` 下划线表示变量不接收

```go
bytes, _ := json.Marshal(fileCount)
```


### defer

用于延迟执行

执行顺序为后进先出（LIFO Last In First Out）

该操作可以用于关闭io流

```go
resp, err := http.Get("http://example.com/")
if err != nil {
	// handle error
}
defer resp.Body.Close()
body, err := io.ReadAll(resp.Body)
// ...
```

### Struct

结构体用语定义数据类型

定义一个结构体

```go
type Article struct {
	id    int    `json:"id"`
	title string `json:"title"`
	body  string `json:"body"`
}

// 创建结构体
var artile Article
// or
var article *Article = new(Article)
// or
var article *Article = &Article(id: 1, title: 'TS', body: 'TypeScript')
```

后面 json 适用于序列化的。如果不先序列化，请使用 json:"-"



### Goroutine


```

```
