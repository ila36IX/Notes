Let's use `esbuild` to compile `jsx` to `js` as fun exercise!

 1. First you'll need a hyper function that will be called by `esbuild` and takes several parameters prototype: `createElement(name, props, ...children)` like react 

```js
function CreateElement(tag, props, ...children) {
  // for new it doesn't do eneything
}
```

 2. Create `Index.jsx` file
 
 ```jsx
const App = (
  <div id="id" style="background: red">
    <h1 class="title">JSX!</h1>
  </div>
);
document.body.appendChild(App);
 ```
3. Install `esbuild` using `npm`

```sh
mkdir esbuild
cd esbuild
npm init
npm install esbuild
```

4. Generate the `js` file

```sh
npx esbuild index.jsx --bundle --jsx-factory=createElement --outfile=out.js
``` 

### Output

```js
(() => {
  // index.jsx
  var App = createElement(
    "div",
    { id: "id", style: "background: red" },
    createElement("h1", { class: "title" }, "JSX!"),
  );
  document.body.appendChild(App);
})();
```
