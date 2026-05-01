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

The statement syntax lets you list your layers in priority order.
The first layer will have the lowest priority (like the user-agent from sources).
The last will have the highest.

The block at-rules are how you set the rules for a given layer.

https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer

## Proximity

TODO: Proximity and scopes

## Order

At this point, if you have conflicting rules for a property, the rule defined later is the one that takes.

Order is later in a given file, or if you have multiple style sheets, the one linked further down the HTML file.

## Important

If you can, don't use `!important`.

How it affects the cascade:

1. User-agent becomes highest priority of the origins.
2. user comes next.
3. Author important styles have the lowest priority.

## Transitions and Animations

Animation rules take priority over the standard origin placement.

CSS transitions take the highest priority of all rules.
