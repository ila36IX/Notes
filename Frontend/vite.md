`Vite` uses a variety of tools, mostly the best ones for the job.

![](https://i.imgur.com/vmFpQ7p.png)

`esbuild` is written in **Go**. It can transpile typescript and `JSX`  files in milliseconds, that's what `vite` in its developing server.
`rollup.js` is a module bundler for JavaScript which compiles small pieces of code into something larger and more complex and ready to production.

## vite build

```js
console.log('Playing...');
// here if you build using vite you will get two files
// this is because vite konws you are trying to split your code logic
// into multiple logically seperated files
if (score > 10) {
	// the achievemnts code will only be executed (parsed, downloaded)
	// if needed
	import('./legendPage.css');
	import('./legendPage.js').then(renderAchievements) {
		renderAchievements();
	}
}
```

### Note about the SHA

![](https://i.imgur.com/CcXvc2b.png)

 The IDs used in the names of the bundle files never change, even if you run a rebuild. Only the changes files will get new IDs. This means you can build over and over again if the CSS file didn't change. The SHA will be the same.

### modules

Any CSS file ending with `.module.css` is considered a [CSS modules file](https://github.com/css-modules/css-modules). Importing such a file will return the corresponding module object:

```css
/* example.module.css */*
.red {
  color: red;
}
```

```js
import classes from './example.module.css';
// obscured class name: _red_foi9ne_ insttead of red
document.getElementById('foo').className = classes.red;
```

