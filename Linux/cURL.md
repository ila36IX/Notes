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

Send HEAD request (only prints response headers):

```sh
curl -I https://www.inlanefreight.com 
```

Set request header:

```sh
curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://<SERVER_IP>:<PORT>
```

Set request cookies:

```sh
curl -b 'PHPSESSID=c1nsa6op7vtk7kdis7bcnbadf1' http://url
```

Send POST request with `JSON` data:

```sh
curl -X POST -d '{"search":"london"}' -H 'ContentType: application/json' http://url
```