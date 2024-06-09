# CSS selectors
### `:nth-of-type()`

 Is used to target specific elements based on their order among siblings of the same type.

```css
tr td:nth-of-type(3) {
	background-color: red;
}
```

This selector will select the third td within every `tr` element.
### `elem.class__name`

Select every `elem` that its class name includes giving `class__name`.

```css
tr.total {
	background-color: red;
}
```