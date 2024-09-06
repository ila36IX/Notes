# Initialization

```js
let arr = new Array();
let arr = [];
arr.length;
arr.at(-1);
arr.pop();   // removes the last element and return it
arr.shift(); // removes the first element and return it
arr.shift(el1, el2, /*...*/, elN); // add element to the end
fruits.unshift(el1 /*...*/); // / add element to the beginning
```

## Looping

```js
for (let i = 0; i < arr.length; i++) {
  alert( arr[i] );
}
for (let fruit of fruits) {
  alert( fruit );
}
```

## Splice

```js
arr.splice(0, 3, "Let's", "dance"); // replace the first three elements with ...
arr.splice(1, 0, el1, el2) // insert el1 ... in the index 1
arr.splice(5, 2) // remoeve the 5th end 6th el
```

## slice

Return a subarray

```js
let arr = [el1, el2, /* ... */, elN];
arr.slice(1, 3) // [el2, el3]
arr.slice() // copy of the original
arr.slice(-5) // Lest 5 elements
```

## concat

```js
let arr1 = [el1, el2, /* ... */, elN];
let arr1 = [El1, El2, /* ... */, ElN];
arr1.concat(arr2, elX) // [el1, el2, ..., elN, El1, El2,..., ElN, elX]
```

## foreach

```js
arr.forEach(function(item, index, array) {
  // ... do something with an item
});
```

## Searching

`arr.indexOf(item, from)`: looks for `item` starting from index `from`, and returns the index where it was found, otherwise `-1` (uses `===`).
`arr.includes(item, from)`:  looks for `item` starting from index `from`, returns `true` if found.
`arr.LastIndexOf(item, from)`

```js
alert( arr.indexOf(0) ); // 1
alert( arr.indexOf(0, 5) ); // -1 // No 0 after the 5TH element
alert( arr.includes(1) ); // true
```

```js
let result = arr.find(function(item, index, array) {
  // if true is returned, item is returned and iteration is stopped
  // for falsy scenario returns undefined
});
let result = arr.findIndex(function(item, index, array) {
  // if true is returned, item is returned and iteration is stopped
  // for falsy scenario returns undefined
});
let result = arr.findLastIndex(function(item, index, array) {
  // if true is returned, item is returned and iteration is stopped
  // for falsy scenario returns undefined
});
```

## filter/map

```js
let results = arr.filter(function(item, index, array) {
  // if true item is pushed to results and the iteration continues
  // returns empty array if nothing found
});

let result = arr.map(function(item, index, array) {
  // returns the new value instead of item
});
```

## sort

`sort(fn)`: The original array is modified

```js
let arr = [ 1, 2, 15 ];

// the method reorders the content of arr
arr.sort();

alert( arr );  // 1, 15, 2
```

## reverse

```js
let arr = [el1, el2, /* ... */, elN];
arr.reverse();
```

## split/join

```js
"alien".split() // ['a', 'l', 'i', 'e', 'n']
["alien", "loves", "code"].join() // 'alien loves code'
```

## reduce

```js
let value = arr.reduce(function(accumulator, item, index, array) {
  // ...
}, [initial]);
```

## Check is array

```js
const arr = [el1, el2]
const notArr = {}

Array.isArray(arr) // true
Array.isArray(notArr) // false
```