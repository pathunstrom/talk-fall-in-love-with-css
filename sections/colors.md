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

color gamuts and color mixing?