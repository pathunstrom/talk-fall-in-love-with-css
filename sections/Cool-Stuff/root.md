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
