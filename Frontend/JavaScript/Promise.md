## Callback hell

- Materials
	- [JavaScript Promises: an introduction](https://web.dev/articles/promises)

```js
/* fooUtilities.js */

document.querySelector("body").innerHTML = "<h1>Fuck the whole universe :(</h1>";
function beNice() {
  document.querySelector("body").innerHTML = "<h1>Hello my friends sorry for being rude :)</h1>";
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>JS callbacks</title>
</head>
<body>
<script>
    document.querySelector("body").innerHTML = "<h1>Hello world!</h1>";
    function loadScript(src, callback) {
        let script = document.createElement("script");
        script.src = src;
        script.onload = callback;
        document.head.append(script);
    }
    loadScript("./fooUtilities.js", () => beNice());
    // Will always cause error 'no such function' because laoding the 
    // script is an asyncournous call which eventlly will be slower that
    // a syncournous action
    /* beNice(); */
</script>
</body>
</htm>
```

From above example you can see why `callback` are essential in some cases, its provided to a function that does something asynchronously and it will call it when the asynchronous action is completed, making sure everything happens in the right order.

```txt
-> function-with-async-actions -> action in progress
-> call other function that depend on that action /* error */

/* Using callbacks instead */
-> function-with-async-actions -> completing the action -> call the `callback`
```

After taking a cup of coffee enjoying your success in solving the above problem, it come to your mind that you need to load 10 scripts in order, that easy, right? you just have to load every script as a `callback` inside the previous loading function call..., that's insigne! look at that piece of art:

```js
loadScript('foo1.js', () => {
	/* ... */
	loadScipt('foo2.js', () => {
		/* ... */
		loadScipt('foo3.js', () => {
			/* ... */
			loadSciprt('foo4.js'), () => {
				/* You got the idea :) */
			}
		})
	})
})
```

So this way of coding isn’t very good, and often it called `callback hell`.
## Promises

Promises are useful when an asynchronous operation is required that means that you are dealing with actions that needs time to be set or update, for example a variable that tends to be a JSON data, and have to be fetched over the network, its basically actions that we initiate now, but they finish later.

### Simple promises

When `new Promise` is called (in the return of a function or when declaring a new variable), it must have as an argument a function with two parameters: `resolve` and `reject`. These functions are pre-defined by the JavaScript engine, so we don’t need to create them. We should only call one of them when ready:

![](https://pbs.twimg.com/media/GU4ejntXAAAoiAG?format=png&name=900x900)

- `resolve`: This is the function that will be called when the asynchronous action is finished without errors. You just need to know that the value given to the `resolve` function will be the first argument of the `then` method's callback of the promise instance. See the example:

```js
const job = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Hello wolrd!');
    resolve('done');
  }, 1000)
}).then((result) => console.log(result));
// Output:
// Hello wolrd!
// done
```

- `reject`: This is the function that will be called if the asynchronous action encounters an error or fails. The value passed to `reject` (usually an error object) will be the argument of the `catch` method's callback of the promise instance.

```js
const job = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Hello wolrd!');
    reject('Sorry :(');
    resolve('done');
  }, 1000)
}).then((result) => console.log(result))
  .catch((e) => console.error(e.message));
// Output:
// Hello wolrd!
// Sorry :(
```

- The call to `resolve(...)` moves the promise object to `"fulfilled"` state;
- The call to `reject(...)` moves the promise object to `"rejected"` state;!

![](https://pbs.twimg.com/media/GU4eO-7XYAEn_UO?format=jpg&name=medium)

Things could be more awesome just make a function that return a promise and have fun!

```js
function doSomething(test) {
  return new Promise((resolve) => {
    setTimeout(() => {
      if (!test)
        console.log('No value arrived :(');
      else
        console.log(test)
      console.log("Did something");
      resolve("https://example.com/");
    }, 1000);
  });
}

doSomething()
  .then(doSomething)
  .then(doSomething)
  .catch(() => console.log("Error accured"));
```

**Settled promise** means  a promise that either got "fulfilled" or "rejected", that means a promise in the state of "pending" is not *yet* settled.

## `fetch` clone

We can made the fetch API using the Promise utility, for example:

```js
function get(url) {
  return new Promise((resolve, reject) => {
    const request = new XMLHttpRequest();
    request.open("GET", url);
    request.onload = function () {
      if (request.status === 200)
        resolve(request.response);
      else
        reject(Error(`Server answers with ${request.status} status code.`));
    }
    request.onerror = (err) => {
      reject(Error(`Error: ${err}`));
    }
    request.send();
  })
}

document.getElementById('load').addEventListener('click', () => {
  get("https://api.github.com/users/ila36IX")
    .then(data => JSON.parse(data).avatar_url)
    .then(avatar => {
      const img = document.createElement('img');
      img.src = avatar;
      img.style.display = 'block';
      img.style.marginTop = '2rem';
      document.querySelector('body').insertAdjacentElement('beforeend', img);
    })
    .catch(e => console.log(e.message))
});
```

### Sync to async trick

`forEach` isn't async-aware, so our chapters would appear in whatever order they download, We want to turn our `chapterUrls` array into a sequence of promises. We can do that using `then()`:

```js
// Start off with a promise that always resolves
var sequence = Promise.resolve();

// Loop through our chapter urls
story.chapterUrls.forEach(function(chapterUrl) {
  // Add these actions to the end of the sequence
  sequence = sequence.then(function() {
    return getJSON(chapterUrl);
  }).then(function(chapter) {
    addHtmlToPage(chapter.html);
  });
})
```

We can even made it more awesome:

```js
// Loop through our chapter urls
story.chapterUrls.reduce(function(sequence, chapterUrl) {
  // Add these actions to the end of the sequence
  return sequence.then(function() {
    return getJSON(chapterUrl);
  }).then(function(chapter) {
    addHtmlToPage(chapter.html);
  });
}, Promise.resolve())
```

## All promises at once

Let's say you have an array of data that you want to manipulate using asynchronous methods, but you need the result to be ready for use after all the data has been processed. To accomplish this, you can use the `Promise.all` function, which will return an array of results from all promises.

```js
let names = ['iliakan', 'remy', 'jeresig'];

let requests = names.map(name => fetch(`https://api.github.com/users/${name}`));

Promise.all(requests)
  .then(responses => {
    // all responses are resolved successfully
    for(let response of responses) {
      alert(`${response.url}: ${response.status}`); // shows 200 for every url
    }

    return responses;
  })
  // map array of responses into an array of response.json() to read their content
  .then(responses => Promise.all(responses.map(r => r.json())))
  // all JSON answers are parsed: "users" is the array of them
  .then(users => users.forEach(user => alert(user.name)));
```

**If any of the promises is rejected, the promise returned by `Promise.all` immediately rejects with that error.**

If this is not what you want, as everything will be ignored if one promise in the inerrable have been rejected, you can use `Promise.allSettled`!

## I'm unstoppable 

`Promise.allSettled` just waits for all promises to settle, regardless of the result. The resulting array has:

- `{status:"fulfilled", value:result}` for successful responses,
- `{status:"rejected", reason:error}` for errors.

```js
let urls = [
  'https://api.github.com/users/iliakan',
  'https://api.github.com/users/remy',
  'https://no-such-url'
];

Promise.allSettled(urls.map(url => fetch(url)))
  .then(results => {
    results.forEach((result, num) => {
      if (result.status == "fulfilled") {
        alert(`${urls[num]}: ${result.value.status}`);
      }
      if (result.status == "rejected") {
        alert(`${urls[num]}: ${result.reason}`);
      }
    });
  });
```

## Promises Race; ready, set, GOOOO!

<iframe src="https://gifer.com/embed/QUC" width=480 height=272.400 frameBorder="0" allowFullScreen></iframe><p><a href="https://gifer.com">via GIFER</a></p>

Now if you want all promises to go in race and get the result of the first settled one, use the `Promise.race` as following:

```js
Promise.race([
  new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000)),
  new Promise((resolve, reject) => setTimeout(() => reject(new Error("Whoops!")), 2000)),
  new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000))
]).then(console.log);
```