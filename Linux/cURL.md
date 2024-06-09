## curl

[More infos video](https://www.youtube.com/watch?v=I6id1Y0YuNk)

Transfers data from or to a server.
 
```bash
# to see the header response
curl -sI getaline.com
```

`-I`:  For the response header
`-H`: Send a custom request header:

```shell
-H "Content-Type: application/json"
```

`-d`: Send query string

```bash
-d '{"name": "Bossier City", "testing": "isEverything"}'
```

`-X`: Specify the request method

```bash
-X PUT
```

