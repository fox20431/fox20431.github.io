These are different Form content types defined by W3C. If you want to send simple text/ ASCII data, then **x-www-form-urlencoded** will work. This is the default.

But if you have to send non-ASCII text or large binary data, the **form-data** is for that.

You can use **Raw** if you want to send plain text or JSON or any other kind of string. Like the name suggests, Postman sends your raw string data as it is without modifications. The type of data that you are sending can be set by using the content-type header from the drop down.

**Binary** can be used when you want to attach non-textual data to the request, e.g. a video/audio file, images, or any other binary data file.

Refer to this link for further reading: [Forms in HTML documents](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.1)



row有很多格式：text、js、json、html、xml

row/text格式：

这个格式兼容所有类型，是js、json、html、xml超集。

```shell
curl --location --request PATCH 'https://api.github.com/user/email/visibility' \
--header 'Accept: application/vnd.github.v3+json' \
--header 'Authorization: token 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' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "visibility": "public"
}'
```

row/json格式：

```shell
curl --location --request PATCH 'URL' \
--header 'Content-Type: application/json' \
--data-raw '{
    "visibility": "private"
}'
```

x-www-form-urlencoded格式：

```shell
curl --location --request PATCH 'URL' \
--header 'Accept: application/vnd.github.v3+json' \
--header 'Authorization: token OAUTH_TOKEN' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'visibility=public'
```

form-data格式：

```shell
curl --location --request PATCH 'URL' \
--form 'visibility="public"'
```



Content-Type: application/x-www-form-urlencoded