
## ``argv``

```js
const { argv } = require('node:process');

if (!Number(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(Number(argv[2])));
}
// ["node", "file_path", ...argv]
```

## File system

The `fs` module of Node.js implements the File I/O operation:

```js
const fs = require("fs");
```

## Reading file

```js
// Notice the prefix "./" in file
const data = fs.readFileSync('./input.txt',
    { encoding: 'utf8', flag: 'r' });

console.log(data);
```


```js
// Asynchronous approach
fs.readFile('./input1.txt',
    { encoding: 'utf8', flag: 'r' },
    function (err, data) {
        if (err)
            console.log(err);
        else
            console.log(data);
    });
```

## Write

```js
fs.writeFile(file, 'Hello world!', function(err) { 
	if(err) { 
		console.log ( err ); 
	} else { 
		console.log('The file was written successfully!'); 
	} 
});

// For append
fs.writeFile(file, 'Hello world!', {flag: "a+"}, callback);
```

```js
const file = "file.txt";

function callback(content) {
	const options = {
	  encoding: "utf8",
	  flag: "a+"
	};
	fs.writeFileSync(file, content, options);
}

for (let i = 0; i < 5; i++) {
    callback("Movie " + i + "\n")
}
```

you can use the `fs` for dealing with files. [more info](https://geekflare.com/handling-files-in-javascript/)