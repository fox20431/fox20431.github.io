---
title: Spring authorization server framework guide
---

# Spring authorization server framework guide



## Prerequiste

To make sure that you can understand what is described later, here's what you should know.

### The oauth2 workflow

There is [a detail documentation](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-08).

The ascii picture is digested from the documentation.

```
     +--------+                               +---------------+
     |        |--(1)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(2)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(3)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(4)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(5)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(6)--- Protected Resource ---|               |
     +--------+                               +---------------+
```

## Dive in the project

### Get started

Here are [a official example](https://github.com/spring-projects/spring-authorization-server/blob/main/samples/README.adoc) which demonstrates how to use the work.

1. Download the source and select the appropriate tag.

   ```sh
   git clone git@github.com:spring-projects/spring-authorization-server.git
   git checkout <tag_name> -b <branch_name>
   ```

2. Open and run the project

   ```sh
   ./gradlew -b samples/demo-authorizationserver/samples-demo-authorizationserver.gradle bootRun
   ./gradlew -b samples/demo-client/samples-demo-client.gradle bootRun
   ./gradlew -b samples/messages-resource/samples-messages-resource.gradle bootRun
   ```

3. Go to `http://127.0.0.1:8080`

