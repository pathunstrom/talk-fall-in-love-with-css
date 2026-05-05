# Structure of CSS

We're going to start with the raw basics: What are the parts of a ruleset?

At the base layer, we have a property.

That's made up of a property name, a colon, and a value.

```
font-family: "Source Code Pro", monospace;
```

The property name is the thing you're defining.
Here, I'm setting a font-family.

The colon separator is just like keys and values in python.

Values can be a little more complicated.

In the case of font-family, I am providing a list of options in priority order.

Some properties allow only a single value, some lists of values, and the shorthand properties allow multiple kinds of values in a single property.

In the case of font-family, the `font` shorthand property lets you set the family, size, weight, and other font specific values.

You end each property declaration with a semicolon.
This is required in all but the last property of a block.

A block is a group of properties wrapped in curly braces.

```css
{
	background-color: black;
	color: white;
}
```

You group a set of properties together so they all apply to the target of your ruleset.

If, for whatever reason, a property in a block is invalid, the browser will silently ignore it.
This can be infuriating if the reason it's invalid is you forgot a semicolon.
CSS will _not_ however try to fix a property.
Either an entire property is active or its ignored.

The next step of understanding a ruleset is the selector.

The selector defines the target of a set of rules.

A basic selector is either a type, class, or id selector.

```css
p {	 }

html {  }

.my-class {  }

#my-id {  }
```

A type selector is the type of an element, like `html` or `p`.

A class selector is prefixed with a period, and selects objects with an author defined class.
Once upon a time, you'd be advised to only use class selectors in mental frameworks like BEM.
That's less true now, as we have a lot of patterns for dealing with ambiguity.
This references the `class` attribute in your HTML.

The final basic selector is the ID selector.
Prefix with an octothorpe (or pound sign) to reference the HTML `id` attribute.
In well formed HTML, there should only ever be a single element that matches a given ID.
So if you need to reference a specific element, this is your go to tool.

You can make a compound selector by combining these options.

```css
p.important {  }

nav#main-nav {  }
```

These selectors use both an element and a class or id to narrow the scope of the rule.

Then you have complex selectors.
These combine basic or compound selectors via combinators.

The most common of these is the descendent operator, which isn't an operator in the sense we're used to at all:
it's a space between selectors.

```css
p.important em {
  
}

ul > li {

}
```

You can also select based on siblings, columns, and namespaces.

Another, extremely powerful, selector type is attribute selectors.

```css
[type] {

}

[type=submit] {

}
```

With this you can target elements with specific attributes set, or set to specific values.
Can also use with things like custom data attributes.

The last two categories I'm going to cover briefly:

Pseudo elements and pseudo classes.

```css
div::after {
	content: "I'm a generated element.";
}

div:focus {
	background-color: red;
}
```

A pseudo-element is the items with two colons before them.
after and before allow you to insert an inline element as the first or last child.
Some pseudo-elements work like queries, targeting things like the text fragment in a browser that supports it.

(text fragments are cool, you should look at the text fragment spec.)

A pseudo-class have a single colon. They represent things like the state of elements, or their relationship to other elements.

A selector list is any of the above selectors grouped via commas.

```css
h1, h2, h3, h4, h5, h6 {
	font-family: serif;
}
```

If any part of a selector list is invalid, the entire ruleset is ignored.

Most likely this failure is from using an namespaced pseudo-element in the wrong browser.

And that's the structure of a ruleset.

https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction