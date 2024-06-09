
[Do this first](https://youtube.com/shorts/ydGti7sLVOc?si=0j_YuIfC0xMwP_0x)
# Do this first

```css
html {

}
img {
	max-width: 100%;
	display: block;
}

body {
	font-family: system-ui;
	font-size: 1.125rem;
	line-height: 1.6;
}

* {
	box-sizing: border-box;
}
```
## Shorthand Background Image Values

```css
div {
  background: #b2b2b2 url("alert.png") 20px 10px no-repeat;
}
```

## img

```css
img {
	object-fit: cover;
	width: 100%;
	max-width: 350px;
	height: 300px;
	object-fit: cover;
}
```

Some of images will become distorted. This is because the images have different aspect ratios. Rather than setting each aspect ratio individually, you can use the `object-fit` property to determine how images should behave.

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

# Box sizing

```css
.gallery {
	 border: 5px solid red;
	 width: 50%;
}

img {
	 width: 100%;
	 border: 5px solid blue;
	 padding: 5px;
}
```

Even though `img` width is 100% of it's container (`.gallery`), the images elements will overflow because of the padding!
The `box-sizing` property, when set to `border-box`, will ensure that the width and height of the selected element will remain the same, even if the padding and border have been changed, The content of the element will shrink to make room for the padding and border.

```css
img {
	box-sizing: border-box;
}
```
### Specificity

The ID selector has a higher specificity weight than the class selector, and the class selector has a higher specificity weight than the type selector.

**ID > class > type_type**

[Specificity ](https://specifishity.com/)
