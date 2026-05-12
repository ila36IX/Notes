# let's talk about prototypes

JavaScript functions are objects that have methods like `call`, `bind` and properties like `func.length` (number of arguments that been given to the function).

```js
function test(var1, var2) {}

console.log(test.length); // 2
console.log(test.prototype); // {}
console.log(typeof test.prototype); // Object
```

From above examples you can see that all function have a weird property named `prototype` and it's an empty `Object`, so do we can mutate it?

```js
function foo() {
	return "I'm fine!"
}

foo.prototype = {
	name = "alien",
	getName = () => this.name;
}
```

Running this snippet of code doesn't throw any error and changing the prototype doesn't change that much in the function but where do we can inspect that change?

 The answer is when we use the function as a constructor:

```js
const newFoo = new foo();
console.log(newFoo.name) // "alien"
```

OK! I know that using the `this` keyword in a constructor function will cause every instance created from that constructor to have properties and methods defined with `this`, according to the logic inside the function.

So what is the relation between that instance and our mutated `prototype` property?

```js
function Person(name) {
	this.name = name;
	this.showName = () => "Hello " + name;
}

Person.prototype = {
	age: 26,
	Info: function { this.name + "-" + this.age };
}

const user = new Person("alien");
console.log(user); // Person { name: 'alien', showName: [Function (anonymous)] }

console.log(user.name) // alien
console.log(user.age) // 26
console.log(user.Info) //alien-26
```

It's like magic – we can make one object inherit stuff from another!

When we create a new `Person` (like our `user`), it gets its own `name` property. But the `age`? That's coming from the prototype! It's like a shared template for all Persons.

See how the `console.log` doesn't show `age`? That's because it's not `user`'s own property – it's inherited!

We can assign any created Object to be a prototype of another object, which will cause the second object to inherit all the properties and method of the first object

## Family tree

```js
function Person(name) {
	this.name = name;
	this.showName = () => "Hello " + name;
}

const address = {
	state: "Boston"
}

Person.prototype = address;

const user = new Person("alien");
console.log(address.isPrototypeOf(user)); // true
console.log(Object.getPrototypeOf(user) === address); // true

let itsPrototype = user;

while (itsPrototype)
{
	itsPrototype = Object.getPrototypeOf(itsPrototype);
	console.log(itsPrototype);
	// { state: 'Boston' }
	// [Object: null prototype] {}
	// null
}
```

In fact every object in JavaScript is built on top of another object! Sounds crazy, right?

You create a new object, feeling pretty proud of yourself. But that object you just made? It's standing on another!

![](https://c.tenor.com/UkMNKRHSyQsAAAAC/tenor.gif)

Wait! what? but when it stops?

The answer is: it stops at the very top of the object mountain. In JavaScript, this is called `null`. It's like the grandparent of all objects. Hello again `null` I didn't think you'd be that useful :)

Now you know what it is [**The prototype chain**](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes#the_prototype_chain).

![](https://pbs.twimg.com/media/GUghXL5X0AAuxPu?format=png&name=small)