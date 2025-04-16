## `<HEAD>`

 [HEAD - A free guide to head elements](https://htmlhead.dev/)

## Text/Typography

- [HTML semantic documentation](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-em-element)

- [All elements and attributes of HTML](https://htmlreference.io/)

 A long list of HTML tags are used to give semantic meaning to specific text. Each tag is essential to help users and browsers understand the specificity of a certain portion of text. It’s crucial to understand which can be used in which situation.
 
- `<q>`: The q element represents some phrasing content quoted from __another source__.

```html
<p>The man said <q>Things that are impossible just take
longer</q>. I disagreed with him.</p>
```

- `<em>` to indicate stress emphasis.

```html
<em>really</em> like driving in San Francisco.
```

- `<i>` to indicate text set off from the normal prose (foreign word, technical term…).

```html
The term <i>voilier</i> is a french word which mean "sailing ship".
```

- `<strong>` to indicate stronger importance.

```html
<p><strong>Warning!</strong> This is not a drill!</p>

<h1><strong>Flowers, Bees, and Honey</strong> and other things I don't understand</h1>
```

- `<b>` to draw attention to specific content (keywords in a summary, product names in a review…).

```HTML
<b>This text is bold.</b>
```

- `<small>` to represent side-comments or small text (copyright, legal text…).

```html

<dl>
    <dt>Single room</dt>
    <dd>199 € <small>breakfast included, VAT not included</small></dd>
    <dt>Double room</dt>
    <dd>239 € <small>breakfast included, VAT not included</small></dd>
</dl>
```

- `<del>` to represent a text that has been deleted.
- `<ins>` to represent a text that has been inserted.
- `<s>` to render text with a strikethough or a line through it.

```html
<p>Buy our Iced Tea and Lemonade!</p>
<p><s>Recommended retail price: $3.99 per bottle</s></p> <!-- no longer -->
<p><strong>Now selling for just $2.99 a bottle!</strong></p>
```

- `<wbr>` to specify where the text could have a line-break.
- `<mark>` to indicate relevance, representing text marked or highlighted for reference.
- `<cite>` to mark the name of a work, such as a book, play, or song (person's name is not the title of a work).

```html
<p>My favorite book is <cite>The Reality Dysfunction</cite> by
Peter F. Hamilton.</p>
```

- `<dfn>` to mark the defining instance of a term.
- `<abbr>` to represents an abbreviation or acronyme.

```html
<p>
The <dfnl><abbr title="hyper text markup langauge">html</abbr></dfn>
is a protocol...
</p>
```
- `<code>` to indicate at short fragment of computer code.
- `<time>` to indicate a specific period in time.

```html
<time>4h 18m 3s</time> <!-- duration -->
<time>14:54:39</time>
```

- `<address>` to indicate contact information (person, people or organization).

Warning!

Some tags like `<strong>` and `<b>` may look the same visually in your browser. Please remember that HTML is about content, semantics, and not the visual aspect.