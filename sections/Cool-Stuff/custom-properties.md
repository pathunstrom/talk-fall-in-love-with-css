One of the big features that css preprocessors provided were CSS variables.
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
