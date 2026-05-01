Nested CSS!

Children selectors

```css
p {
    & span.excited {
        font-size: 1.1rem;
    }
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