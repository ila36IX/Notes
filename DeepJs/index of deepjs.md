- [You don't know js Yet](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/types-grammar/ch1.md)
- [Slides from frontendMasters](https://static.frontendmasters.com/resources/2019-03-07-deep-javascript-v2/deep-js-foundations-v2.pdf)

## Everything is not an object!

This is a meth, there are primitives in js that are not objects, and you can use `typeof` to know if a type of varaible is primitive, there is two exceptions:

- `typeof function_varaible`: will return `function` even though function is a sub-type of an object
- `typeof null`: Gives `Object` even though `null` is considered a primitive type. ^73ceea

 `NaN`: is special number type which indicates invalid number (`Number("NOT_NUMBER")`). notice that (`NaN !== NaN`), use `Number.isNaN` to check.
 
 `NaN` is a "falsy" value.
 
## Falsy and Truthy

Those are the "falsy" values, everything else is "truthy":

```js
"" 0 -0 null Nan false undefined
```

### immediate function call

A way to use try/catch and assign to variable accordingly.

```js
let name = (function getName()
{
	try {
		return dengerous_func();
	}
	catch (err){
		return "Unknown";
	}
})();
```

## Function hoisting

You can use function hoisting to improve readability.

```js
function getUsers(id) {
	users.find(findById);
	
	function findById(record) {
		return (record.id == id);
	}
}
```

## Vanilla js

Recourses:
- [Vanilla JS: You Might Not Need a Framework](https://firtman.github.io/vanilla)

## Entry point

Before executing any line, first wait for the HTML document to be parsed.
Use the [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event).

```js
window.addEventListener('DOMContentLoaded', main);


function main()
{
  const app = document.querySelector('#app');
  app.innerHTML = "Testing";
}
```

## Event binding

Handling events:

- `x.on"event"`: in this case sitting multiple event handlers will override each other.
- `x.addEventListener('event', callback)`: all events handlers will run
- - `x.removeEventListener('event', callback)`

## Helpful shorthand

```js
const $ = function(args){ return document.querySelector(args);}
const $$ = function(args){ return document.querySelectorAll(args);}

HTMLElement.prototype.on = function(a, b, c){ return this.addEventListener(a, b, c); }
HTMLElement.prototype.off = function(a, b){ return this.removeEventListener(a, b); }
HTMLElement.prototype.$ = function(s){ return this.querySelector(s); }
HTMLElement.prototype.$$ = function(s){ return this.querySelectorAll(s); }

$('#currentPage').textContent = '1';
``` 