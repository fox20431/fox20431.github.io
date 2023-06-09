---
title: GitHub OAuth
---

# GitHub OAuth

It's very recommended that read [the blog](https://www.ruanyifeng.com/blog/2019/04/github-oauth.html).

## Github Create OAuth App

Here is [a quick link](https://github.com/settings/developers) for creating OAuth App.

There are a few concerns related to the creation of the GitHub OAuth App.

1. Once an OAuth App is created, a Client ID is immediately generated.
2. We need to generate the Client Secret manually.
3. The purpose of the `application name` is to display it on the consent page for the user, so fill it in with any name you want.
4. `Homepage URL` and `Application description` are in order to help users learn more about your application, so fill it with any content you want too.
5. The `Authorization callback URL` is important, only the value of the `Authorization callback URL` can carry the `authorization code` and receive the `access token`.

## Create the Application

Oauth2 is based on HTTP, you can check [the GitHub documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) to find out how to use it.

You can see [the simple demo](https://github.com/fox20431/node-oauth-demo) to learn it.