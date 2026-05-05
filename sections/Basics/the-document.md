The first thing to know is that CSS operates on a document.

Typically, that document is an HTML document being displayed by a browser, but a number of similar markup languages support styles.

The basic building blocks of HTML are elements.
You might know them as "tags".

A basic HTML document could look like this:

```html
<!DOCTYPE html>
<html>
  <head>
  	<style>
  	</style>
  </head>
  <body>
  	<h1>Hello <em>World!</em></h1>
  </body>
</html>
```

We'll be focusing on elements that live in the body, plus the body and the html.

Elements that are meant to be displayed largely fall into two types (with some exceptions):

* block elements
* inline elements

A "block" element typically has two dimensions and takes up a literal block of the render space.

`h1` is a block element, and `div` is the generic block element.

An inline element follows the same basic rules as text for flow.

Our `em` (for emphasis) element is an inline element.
The `span` is the generic inline element.

There's a lot more elements than I've shared here!
I don't have time to give a deeper explanation but you can read all up on semantic HTML at <TODO: find link>
