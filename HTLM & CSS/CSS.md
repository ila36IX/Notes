## Shorthand Background Image Values

```css
div {
  background: #b2b2b2 url("alert.png") 20px 10px no-repeat;
}
```


## Centering a div

### Using position

```css
.child {
	postion: relative;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}
```

### Using `flexbox`

```css
html, body { height: 100%; }

.parent {
  height: 200px;
  background: gray;
  display: flex;
  align-items: center;
  justify-content: center;
}

.child {
  background-color: orange;
  width: 100px;
  height: 100px;
}
```

The `abolute` position is making by default the element to be relative to the whole html page, you may fix this by adding `position: relative` to its parent element.

```css
.parent {
    width: 500px;
    height: 500px;
    outline: 5px solid red;
    position: relative;
}

.child {
    font-size: 50px;
    text-align: center;
    width: 60px;
    height: 60px;
    border: 1px solid green;
    position: absolute;
    top: 20px;
    left: 20px;
}

.child span {
    margin: auto;
    padding-block: 15px;
    /* background-color: red; */
    height: 10px;
    position: relative;
    bottom: 6px;
}
```



## Background image tips

```css
background-image: url(<link_to_image>);
background-color: #fff;
background-size: cover, demantions-of-image;
background-postion: center center;
background-repeat: no-repeat;
```

### Box shadow

```css
box-shadow: 0 2px 5px 0 rgba(0, 0, 0, .1); 
```