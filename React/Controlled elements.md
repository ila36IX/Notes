# Working with from inputs

When working with form inputs, retrieving their values directly from the DOM can be challenging. That's why the **controlled elements** technique comes in handy. This technique involves controlling and owning the states of the input fields, shifting the control away from the DOM.

In a controlled component, the state is maintained by the React component itself. This state is updated via events, usually tied to input fields in a form. This means that the value of the input field is always controlled by the state of the React component.

Here’s a simple example of a controlled component:

```js
function ControlledForm() {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`input's value: ${value}`);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={value} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

<p style="color:red; font-weight: bord"}>Note</p>
	The values that are taking from DOM are always having **string** type keep in mind that converting it is a required step to avoid getting anonymous bugs when dealing with integers.

## STATE VS. PROPS

![](https://i.imgur.com/9n6iy37.png)