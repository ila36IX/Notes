# what is state management

**State management:** Deciding when to create a pieces of state, what types of state are necessary, where to place each piece of state, and how data flows through the app,  it's is like *giving each piece of state a home within our code base*.

## Types of state

![](https://i.imgur.com/C6nZqnJ.png)

## When and where to use state

![](https://i.imgur.com/ro5dbbb.png)

## Updating state

When a state depends on the current state, We are not allowed to mutate state, therefor we need to pass in a callback function ( not just a single value) that in its instruction does not change the current state, so doing this is wrong: 

```jsx
const [items, setItems] = useState([]);

setItems((items)=> items.push(newItem));
```

Because with that we would be mutating state, and that again **NOT** allowed in react.

**React states are immutable!**


