Me

stealthiswebsite.art
teahouse.cafe

My first forays into web design might sound familiar to many:

I had a geocities website in my teens.
I was a neopets user and was very active on the forums.
I was a LiveJournal user.

To say they were the start to a lifelong obsession would be overselling the skills I learned.

I actually started building websites professionally in 2014.
I knew enough not to make a fool of myself, but honestly was figuring everything out as I went.
The space I was growing into, mobile development was finally starting to get focused on.
Mobile first was the hot buzzword.
And the best way to do it, according to the blogs and talks I was paying attention to, was bootstrap.

Two weeks of trying to fit bootstrap's model into my hide left me disheartened.
Every time I thought I had it, I'd run into a new problem.
I gave up for a bit.
I told myself I'd learn the underlying methodology so maybe I could understand the tech.

That was the start of my obsession:

Learning responsive web design from first principles.

Flexbox was stable, but the courses I took still used floats!
I made half a dozen responsive layouts over the next month.
I even produced one for a client.

No bootstrap.
Just a much stronger understanding of CSS and the layout tools available to me.

This is where my obsession started in earnest.
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
This is required in all but the last property of a block, but you should probably always include one.

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

Direct child

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

https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction# The Cascade

Build a model of the cascade.

!! expand

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
The classic way you would define shared, inheritable properties is to define a rule on `body` or `html`.

```css
html {
    
}

body {
    
}
```

With our discussion about the cascade, you should now understand that these are the root elements of your document.
When the properties here are inheritable, any children will default to those values.
The specificity of these rules is `0-0-1` which means they'll be overridden by any rule that follows.

Another way to do this is the `:root` pseudo-class.
It isn't "new" (it was included in the Selectors Level 4 working draft in 2011!)
It represents the root element of the document, usually `html` but counts as a class for specificity, thus `0-1-0`.

As a demonstration, if we set a `:root` rule with a solid border, and then an `html` rule with a dashed border:
 
```css
:root {
    border: red solid 5px;
}

html {
    border: black dashed 5px;
}
```

As you can see, the earlier rule takes effect.

!!Transition!

So we all like websites that respect our color mode preferences, right?

The previous methodology used media queries.

```css
html {
    background-color: black;
    color: white;
}

@media screen and (prefers-color-scheme: light) {
    html {
        background-color: white;
        color: black;
    }
}

/* www.w3.org/TR/2020/WD-mediaqueries-5-20200303/ */
```

You define your primary color scheme in your main styles, then in a media query for the other color scheme you set your alternate color mode.

This was introduced in Media Queries Level 5 in 2020.

```css
:root {
    color-scheme: light dark
}
```
In 2022, the CSS Color Adjustment Module Level 1 was introduced.
This gave us the `color-scheme` property which allows a rule to tell the browser what color modes it supports for the selected elements.
There's also a meta HTML attribute to do this for the entire page.

The values include "normal", "light", and "dark" and also support an "only" modifier.

If you haven't set colors, these all do the same thing:
tell the browser which color mode you prefer and which you support.

`light dark` says the page preference is light mode, but you do support dark mode.
`dark light` is the opposite.
`only light` says you only support light mode.

The next piece of this puzzle is the `light-dark` CSS function, introduced in CSS Color Level 5.
It became baseline in 2024, and allows you to provide two colors, a light mode choice and a dark mode choice.

```css
:root {
    color-scheme: light dark;
    color: light-dark(white, black);
    background-color: light-dark(black, white);
}
```

Now it's possible to declare both modes in a single property, making it much simpler to check that you've covered your bases.

color gamuts and color mixing?One of the big features that css preprocessors provided were CSS variables.
The standard now has CSS custom properties.

```css
:root {
    --primary-color: black;
    --contrast-color: white;
}
```

Any property in your css that starts with two hyphens is a custom property.

They can hold any valid CSS value.

The power of custom properties comes from being to access them later or operate on them.

The way to access your custom properties is the `var` function:

```css
:root {
    --primary-color: black;
    --contrast-color: white;
    background-color: var(--primary-color);
    color: var(--contrast-color);
}
```

`var` returns the value of the custom property, so can be used anywhere that value can be used.
For example, in the light-dark function!

This has become my preferred method for defining color schemes:

```css
:root {
    --primary-color: indigo;
    --contrast-color: gold;
    --highlight-color: darkgreen;
    color-scheme: dark light;
    background-color: light-dark(var(--contrast-color), var(--primary-color));
    color: light-dark(var(--primary-color), var(--contrast-color))
}
```

Variables in `:root` defining our primary, contrast, and highlight colors.
(You can get quite fancy with your colors, but I'm trying to keep my demos short!)
Then you define the colors on your elements using the light-dark function and var.

The next neat trick is that you can rebind these variables.

So if we move our color declarations into a wildcard rule like so:

```css
:root {
    --primary-color: indigo;
    --contrast-color: gold;
    --highlight-color: darkgreen;
    color-scheme: dark light;
}

* {
    background-color: light-dark(var(--contrast-color), var(--primary-color));
    color: light-dark(var(--primary-color), var(--contrast-color))
}

.target {
    --primary-color: blue;
}
```

With this declaration, the `target` class will get the same color rules, but display with a blue color instead of indigo.

The next thing you can do is use these properties in things like `calc` or for colors the various gamuts from an existing color:

```css
/* todo: color gamut example. */
```
Nested CSS!

!! To expand

Children selectors

```css
p {
    & span.excited {
        font-size: 1.1rem;
    }
}

p span.excited {
    font-size: 1.1rem;
}
```

compound selectors

```css
p {
    &.important {
        background-color: darkred;
        color: black;
    }
}
```

Responding to a change in the parent:

```css
span {
    p.quiet & {
        background-color: grey;
        color: black;
    }
}
```
Okay, so I mentioned before I remember doing layout with floats.
Before floats, people would abuse tables.

I am going to share with you the two layout tools that will bury all of those woes.

First, let's talk about some basic concepts.

Generally, layout on the web is two dimensional.
We call the two dimensions axes.
Depending on which tool we're using, the axis names change a bit.

The fundamental axes are the "inline" axis and the "block" axis.
For English text, inline is left to right, and block is top to bottom.

Note that I said "for English."
Not all writing systems follow this rule, and the standard has special properties to support the logical axes.
Instead of height and width, you can discuss the inline-size and block-size.
There's many of this logical properties and I encourage you to read up on them.

In Flexbox, we actually have another step of abstraction:
the main axis and the cross axis.
The main axis is running the direction of the flex, and the cross axis is perpendicular.

With that, let's talk about Flexbox.

The basic way Flexbox works is that it has a direction and children who occupy the flex.

```css
nav {
	display: flex;
	flex-direction: column-reversed;
}
```

The first decision to make is direction.
There's four values:

* row
* column
* row-reversed
* column-reversed

Rows are laid out in the text direction and columns are the block direction.
reversed just means that they are laid out in the opposite order from their counterpart.
In English, column-reversed puts the first child on the bottom, and the last child on the top.

```css
nav {
	display: flex;
	flex-direction: row;
	justify-content: space-between; /* space-around */
	align-content: ;
	align-items: ;
}
```

Justify content is how you align items along the main axis.
You've got the obvious ones: start, end, and center.
But the ones that I find I use most often are `space-between` and `space-around`;

Align content gives very similar control to justify content on the cross axis, but only if you have `flex-wrap: wrap`.
Align-items gives you the ability to see alignment on each row.

This also answers the age old css question on how to center text:
`align-items: center` on a flex container makes its children centered.

I mentioned flex-wrap, but I want to raise special attention:
If you're using flexbox for things like card layouts, you almost definitely want `flex-wrap: wrap`!
I forget to include it and wonder why my flex isn't wrapping constantly.

Flexbox is cool, but it basically only supports one shape of layout.
It's a good layout, but if you want something complex, you want CSS Grid.

Unfortunately, it's complex enough I could write an entire talk on CSS.
So we'll cover the basics and I will encourage you to go play with it.

First, the new unit you'll see a lot: The fractional unit `fr`.
The way `fr` works is for each fr value in definition, that cell will receive that much of the remaining space after content and other limits.

```css
body {
	display: grid;
	grid-template-columns: 1fr 3fr 2fr;
}
```

In this example, I've defined 3 columns.
The middle column will be 3 times bigger than the left column, and the right column will be twice the width of the left column.

Other values you might see are `min-content` and `max-content` values and the `minmax` function.
Min-content is the minimal space the content can take on that axis and max-content is the opposite.
Minmax gives the column at least the minimum value (which can be any length, percentage, or min-content or max-content), and max can also include our new `fr` unit.
If for whatever reason max is less than min than the value is min.

Now, how do you use it?

First, you need to define your grid.
There's a shorthand property, but grid has a lot of concepts, so I'll encourage you to use the longhand properties.

```css
body {
	grid-template-columns: 1fr 3fr 1fr;
	grid-template-rows: 10vh 1fr 5vh;
}
```

First, define your grid using `grid-template-columns` and `grid-template-rows`.
In this example, I've defined the basic grid of the classic 3 column website.
Side bars with 1/5th of the screen, and the center with 3/5ths.
Then I've defined 3 rows, one that is 10% of the viewport for the header, 5% for the footer, and the rest is given to ther body.

This defines the grid and the gridlines.

```css
	body {
		grid-template-areas: "header header header"
		                     "navbar body asides"
		                     "footer footer footer"
	}
```

Now we can define areas using grid-template areas.

Each area is an arbitrary name, and must be rectangular and cannot overlap.

Then, we assign elements to an area via `grid-area`:

```css
	body > header {
		grid-area: header;
	}

	body > nav {
		grid-area: navbar;
	}

	body > .main {
		grid-area: main;
	}

	body > .aside {
		grid-area: asides;
	}

	body > footer {
		grid-area: footer;
	}
```

The neat thing about this pattern is that you can redefine the grid areas and template definition in things like media queries.
When you do so, each item will move to its new home in the grid when the media query matches.

If you're writing mobile first, you can let all of these elements stack in the order you defined them.
Give them their areas in the main body of your css.
Then in each breakpoint, you only need to manipulate their grid parent to change your layout to support different breakpoints!

## Gap

The last thing to discuss is `gap`, a property that works on both flexbox and grid:

It defines the gutters between rows and columns.
It's like `margin` in most respects, but doesn't separate the container from its childern.
It also works with display multi-column!
has

is

where

not

pseudo-classes@media screen and (width > 450px) {
	
}