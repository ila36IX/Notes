![](https://i.imgur.com/dfbZ1QP.png)

```css
background: repeating-linear-gradient (
	/* 45deg to make it diagonal */
	red,
	red 6%,
	black 6%,
	black 9%
);
```

## Draw triangle

![](https://i.imgur.com/pSqgqHc.png)

```css
.triangle {
  border-bottom: 1->5vw solid #000;
  border-left: 5vw solid transparent;
  border-right: 5vw solid transparent;
}
```

## Big first letter

![Imgur](https://i.imgur.com/bZzv0Yi.png)

```css
.first-paragraph::first-letter {
	font-size: 6rem;
	color: orangered;
	float: left;
	margin-right: 1rem;
}
```