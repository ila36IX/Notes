
These closures are not a snapshot of the msg variable’s value; they are a direct link and preservation of the variable itself. That means closure can actually observe (or make!) updates to these variables over time.

```js
function counter(step = 1) { 
	var count = 0; 
	return function increaseCount(){ 
		count = count + step; 
		return count; 
	}; 
}

var incBy1 = counter(1); 
var incBy3 = counter(3); 

incBy1(); // 1 
incBy1(); // 2 

incBy3(); // 3 
incBy3(); // 6 
incBy3(); // 9
```

Each instance of the inner increaseCount() function is closed over both the count and step variables from its outer counter(..) function’s scope. step remains the same over time, but count is updated on each invocation of that inner function. Since closure is over the variables and not just snapshots of the values, these updates are preserved.