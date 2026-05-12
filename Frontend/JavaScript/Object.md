Make a new updated copy of an object:

```js
newObj = {name: "ali", age:20};

newObj = {...newObj, ["name"]: "hp"};

// The some
newObj = {...newObj, "name": "hp"};
```

Make a copy of an array:

```js
let newArray = oldArray.slice();
```
## Object keys/values

```js
Object.keys(obj);
Object.values(obj);
Object.entries(obj)
```