
To request  payload `json`:

Installation:

```bash
sudo npm install request --global
export NODE_PATH="/usr/lib/node_modules"
```

```js
const request = require('request');

const url = 'endpoint/url';
request (url, function (error, response, body) {
 if (error) {
   console.log(error);
 } else {
   console.log(JSON.parse(body));
 }
});
```



