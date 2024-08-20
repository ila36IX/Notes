## Loading attribute

The `loading` attribute on an `img` element can be set to `lazy` to tell the browser not to fetch the image resource until it is needed (as in, when the user scrolls the image into view). As an additional benefit, lazy loaded elements will not load until the non-lazy elements are loaded - this means users with slow internet connections can view the content of your page without having to wait for the images to load.

```html
<img loading="lazy" />
```
## image reset

```css
img {
	object-fit: cover;
	width: 100%;
	max-width: 350px;
	height: 300px;
}
```

Some of images will become distorted. This is because the images have different aspect ratios. Rather than setting each aspect ratio individually, you can use the `object-fit` will set the image to fill the container, cropping as needed to avoid changing the aspect ratio..
## Background image

```css
background-image: url(<link_to_image>);
background-color: #fff;
background-size: cover, demantions-of-image;
background-postion: center center;
background-repeat: no-repeat;
```

Shorthand Background Image Values

```css
div {
  background: #b2b2b2 url("alert.png") 20px 10px no-repeat;
}
```