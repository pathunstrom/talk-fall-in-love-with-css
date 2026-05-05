# The Cascade

Build a model of the cascade.

## Relevance

Before any rule is applied, the rule must be relevant to the element.

That means that the element satisfies the selector and that any media queries match

## Origin Types

The first thing that affects the priority of your rules is the origin of the rule.

There's three origins: The User-Agent, the Author, and the User.

The User-Agent is your browser.
These are the styles you see if you don't style a page.
Usually black on white, 16 px serif font, no padding and small margins on things like headings.

The Author is us.
The people writing a style sheet for any given page.

I would say more about the User stylesheet, but very few browsers support them anymore.
In the before times, a user style sheet was a stylesheet authored by the person viewing a page.

The highest priority of these is the Author style sheet.

The second highest is User stylesheets.

The bottom is the user-agent.

### Layers

Inside your author sheet, you can set your own layers using the two forms of the layer at-rule.

```css
@layer layer_1, layer_2

@layer layer_2 {

	/* */
}
```

The statement syntax lets you list your layers in priority order.
The first layer will have the lowest priority (like the user-agent from sources).
The last will have the highest.

The block at-rules are how you set the rules for a given layer.

https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer

### Specificity

At this point in the priority list, we have to consider the specificity of a rule.

Specificity is made up of 3 columns of values: ids, classes, and types.

It will be described as 3 values separated by hyphens.

For each column, you count the number of that column in a selector.

```css
#tool {  } /* 1-0-0 */


#tool #handle {  } /* 2-0-0 */

```

The first value is id.
For each id in a selector (remember, octothorpe), you add one to that column.
Most of the time, you'll see 1 here, but if you're using a complex selector with children, you might have more.

```css
.card {  } /* 0-1-0 */

.card:first-child {  } /* 0-2-0 */


```

The second column is classes.
For each class (period), pseudoclass (single colon), and attribute selector (square braces) you add one to the second column.

```css
div {  } /* 0-0-1 */

div::after {  } /* 0-0-2 */

```

The final column is the type column.
Remember that types are the different element types in your HTML.
Pseudo-elements also add to this column!

There's also no value especially for the universal selector (\*) and the :where pseudoclass.

In addition, most combinators have no weight of their own, but produce higher specificity due to their components.

TODO: Examples

## Order

At this point, if you have conflicting rules for a property, the rule defined later is the one that takes.

Order is later in a given file, or if you have multiple style sheets, the one linked further down the HTML file.

## Important

If you can, don't use `!important`.

How it affects the cascade:

1. User-agent becomes highest priority of the origins.
2. user comes next.
3. Author important styles have the lowest priority.

I am also going to quote MDN directly on a section about tips for specificity headaches:

> Instead of using !important, consider using cascade layers and using low weight specificity throughout your CSS so that styles are easily overridden with slightly more specific rules. Using semantic HTML helps provide anchors from which to apply styling.

## Other

There's three more rules to specificity that I encourage you to go read up on, but I won't be expanding on.

* CSS transitions
* CSS animations
* Scopes and proximity
