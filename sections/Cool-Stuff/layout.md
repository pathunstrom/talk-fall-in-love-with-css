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
