
## Accepting multiple values 

```html
<select name="mulit-values[]">[...]</select>
```
## Validate input

```php
$input['email'] = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
// null if empty
// False if not valide
// The input value if valide.
```

## Prevent cross-site attack

For  encoding HTML entities in a string:

```php
// make sure no bad html code is included in inputs
htmlentities($_POST["name"]);
```


The characters that have a special meaning in HTML (``<``, ``>``, ``&``, and ``"``) have been changed into their entity equivalents:

```
< to &lt;
> to &gt;
& to &amp;
" to &quot;
```