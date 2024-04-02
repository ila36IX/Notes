
## argv

```js
const { argv } = require('node:process');

if (!Number(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(Number(argv[2])));
}
// ["node", "file_path", ...argv]
```

## readFileAsync

you can use the `fs` for dealing with files. [more info](https://geekflare.com/handling-files-in-javascript/)