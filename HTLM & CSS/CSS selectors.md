# CSS selectors
## nth-of-type

 Is used to target specific elements based on their order among siblings of the same type.

```css
tr td:nth-of-type(3) {
	background-color: red;
}

tr td:nth-of-type(even|odd) {
	background-color: red;
}
```

This selector will select the third td within every `tr` element.
### elem.class__name

Select every `elem` that has class name includes the giving `class__name`.

```css
tr.total {
	background-color: red;
}
```

## Last child

```css
.mainNav__ctas .button:last-child {
	margin-right: 0;
}

.mainNav__ctas .button:not(:last-child) {
	margin-right: 1rem;
}
```