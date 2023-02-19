HATEOAS is a concept of *application architecture*. It defines the way in which application clients interact with the server, by navigating hypermedia links they find inside resource models returned by the server.

To *implement* HATEOAS you need some standard way of representing resources, that will contain hypermedia information (links to related resources), for example, something like this:

```json
{
    "links": {
        "self": { "href": "http://api.com/items" },
        "item": [
            { "href": "http://api.com/items/1" },
            { "href": "http://api.com/items/2" }
        ]
    },
    "data": [
            { "itemName": "a" }, 
            { "itemName": "b" } 
    ] 
}
```

HAL is one of such standards. It is a specific format of resource presentation, that can be used to implement HATEOAS. 

You can fully implement HATEOAS without following HAL at all if you prefer to follow another standard or use your own.