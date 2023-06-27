---
title: Springboot H2 config
---



spring boot

```yaml
spring:
  h2:
    console:
      enabled: true
  datasource:
    url: jdbc:h2:mem:mydb
    username: sa
    password:
    driverClassName: org.h2.Driver

```

http://localhost:8080/h2-console