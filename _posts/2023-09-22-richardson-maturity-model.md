---
title: Richardson Maturity Model
date: 2023-09-22
---

# 理查森成熟度模型



Richardson成熟度模型（Richardson Maturity Model）是关于RESTful架构风格的一种分类模型，由Leonard Richardson在他的博客文章《Maturity Heuristics》中提出。该模型旨在评估和定义Web服务的成熟程度，帮助开发者理解和采用REST（Representational State Transfer）原则。

1. Level 0: 原始的HTTP 在Level 0，使用HTTP主要作为通信协议，但没有充分利用REST的特性。通常是使用单一的URL进行数据传输，且操作和状态都通过参数来传递。
2. Level 1: 资源 在Level 1，开始引入REST的概念，将数据视为资源。每个资源都可以通过唯一的URL进行访问和标识。这个级别主要关注资源的标准化和命名。
3. Level 2: HTTP 动词 在Level 2，通过使用HTTP的不同动词（GET、POST、PUT、DELETE等），来对资源进行不同的操作。这种方式更符合REST的原则，使得接口设计更加语义化。
4. Level 3: 超媒体控制 在Level 3（也被称为HATEOAS级别），通过使用超媒体链接（Hypermedia Links）来定义资源之间的关系和操作。客户端可以通过解析这些链接来动态发现和访问相关资源。