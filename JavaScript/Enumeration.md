
```js
const obj = {
        a: 1,
        b: 2,
        c: 3
};

for (let i in obj) {
        console.log(i);
}
// a, b ,c
for (let i of obj) {
        console.log(i);
}
// TypeError: obj is not iterable

/* --------------------------------- */

const arr = ["a", "b", "c"];

for (let i in arr) {
        console.log(i);
}
// 0, 1, 2
for (let i of arr) {
        console.log(i);
}
// a, b, c
```

You can see that `Array` data type is an object that has properties, the most obvious properties are the keys which we think of as indexes,  however when using the `for ... in ...` syntax, it seems that the ``length`` property is not appear after the indexes, why?

This is because the `length` preparty is not enumerable, you can check this by your self using this method `Object.getOwnPropertyDiscriptor`

```js
console.log(Object.getOwnPropertyDescriptor(arr, "length"));

// { value: 3, writable: true, enumerable: false, configurable: false }
//                                         ^^^^^^^ <- make you attension to this one.  

// You can do the some with instances
console.log(obj_instance.propertyIsEnumerable("name")); 

// if the property is that in the prototype, you can access its details like this
obj_instance.constructor.prototype.propertyIsEnumerable("property_name");
```


## Prototype

```js
// create an object engine
const engine = {
	version: "2.2"
}

// create a constructor
function Browser(name) {
	this.name = name;
}

// Reference an Object engine
// to the constructor "browser"
Browser.prototype = engine;

```

```js
obj.isPrototypeOf(obj_instance);
Object.getPrototypeOf(obj_instance);
```

## Prototype vs `__proto__`

```js
// prototype is property of the constructor
Browser.prototype // feel free to do whatever you want with it

// __proto__ is property of the instance
const ins = new Browser();
inst.__proto__ // Do not change this property!!
```

