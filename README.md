# elementcss

> Rich Sass library to work with CSS4 and generate complex GUI in the [SEM](https://github.com/timfayz/SEM)-way

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timfayz/elementcss?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**elementcss** is a *three* part framework. One is a rich Sass library to manipulate Sass lists, strings & maps. Second is utils to convert CSS4 colors & units back and forth, generate grid layout, define vertical rhythm and easily reset the whole HTML document to style from "scratch". Third is the utils implementing [SEM](https://github.com/timfayz/SEM)-methodology. Idea is simple: put one property per class and apply them in WYSIWYG-way. Full list of available functions & mixins you can found [here](docs/API.md).

**[Download v2.9.0](https://github.com/timfayz/elementcss/archive/master.zip)**

## Demo

The CSS styles for following pages were generated with elementcss:
- [Personal webpage](https://timfayz.github.io) ([repository](https://github.com/timfayz/timfayz.github.io) | [source styles](https://github.com/timfayz/timfayz.github.io/blob/master/styles/main.scss) > [resulting css](https://github.com/timfayz/timfayz.github.io/blob/master/styles/main.css))
- [Birthday gift card](https://marynicole.github.io) ([repository](https://github.com/marynicole/marynicole.github.io) | [resulting css](https://github.com/marynicole/marynicole.github.io/blob/master/css/main.css))


## Features

- **grid system**. Powerful `grid()` mixin generates flexbox or float-based layout with unlimited number of breakpoints. Customize number of columns, width and gap per each `@media` rule. Implements all widely used grid features: column's `width`, `push`, `pull`, `offset`, `center`, etc.

- **metrics**. `snap-len()` "snaps" input values into fixed baseline height (eg. your document's `line-height`). Useful for stepping height, margin, padding, etc. and defining horizontal/vertical rhythm.

- **SEM**. elementcss implements [SEM methodology](https://github.com/timfayz/SEM). Minimalistic syntax of `set()` mixin provides full control over generating dozens of *mixes* and *elements*. [Learn more..](https://github.com/timfayz/SEM/blob/master/docs/guide.md)

- **style reset**. elementcss is backed by [init.css](https://github.com/timfayz/init.css) project. `init.css` is a best from both worlds `normalize.css` and `Reset CSS 2.0`. Both makes an appearance of HTML tags unstyled/unified to start styling from a blank sheet. But, `init.css` merge best practices into one solution. [Learn more..](https://github.com/timfayz/init.css)

- **color utils.** Useful functions to work with colors: `convert-color()` to convert different models back and forth; `color()` to adjust, set and scale internal color parameters using different models; `brightness()` to extract the brightness; `tint()`, `shade()` and `contrast-color()` to tint, shade and get contrast b/w two colors accordingly. Supporting models: `hex`, `rgb(a)`, `hsb/v(a)`, `hsl(a)`.

- **unit utils**. Functions to work with CSS units. `trim-unit()`, `append-unit()`, `convert-unit()` to remove, append and convert different CSS units into one another; `round-unit()` makes sure you get an integer pixel at the end of browser rendering. Supported all valid CSS units: `rem`, `px`, `pt`, `%`, `pc`, etc.

- **helper utils**. Popular helper classes gathered from best practice. Clearfix, image replacement, hiding, visually hiding, text hiding and more.

- **string utils**. Functions to work with strings. `str-exists()`, `has-prefix()/-postfix()`, `str-replace()`, `trim-left()/-right()` to check occurrence, replace and trim specified substring(s) accordingly.

- **list/map utils**. Functions to work with Sass build-in lists and maps. `slice()`, `union()`, `nth-replace()`, `replace-value()`, `nth-remove()`, `remove-value()` to slice, merge, replace and remove items by index/value accordingly; `map-append-val()`, `map-union()` to append key-value pair and union maps.

- **math utils**. Basic math functions. `pow()`, `root()`, `gcd()` to power, root and find great common divider of a number.


## Quick Start
* [Install Sass](http://sass-lang.com/install)

* Create project dir and go inside:
```bash
mkdir myproject
cd myproject
```

* Clone repository, or [download archive](https://github.com/kalopsia/element/archive/master.zip) and extract it into the project root:
```bash
git clone https://github.com/timfayz/elementcss
```

* Copy content of `elementcss/templates/app-minimal` into your project root:
```bash
ls
index.html  main.scss  elementcss/
```

* Open `main.scss` and check if its import path is correct:
```scss
// main.scss
...
@import "elementcss/import"; // correct import path
...
```

* Open command line in the project root and compile `main.scss`:
```bash
sass --watch main.scss:main.css # compile resulting .css file & watch for new changes
```

* `main.css` is already generated, now open `index.html` in your browser and see the results. 

* You've done!


## File structure
```
docs/         documentation
templates/    project boilerplates
src/*.scss    logically separated core files
_import.scss  entry point (unites all src/* files)
LICENSE       license information
README.md     this is what you are currently reading
```

## Documentation
*Documentation is under heavy development.* 

API is always relevant and generated automatically by little script `docs/API.py`. It creates list of links pointing right to source definitions. Such an approach is taken since all the code has a well-written embedded documentation with several examples per each function and mixin definition. So please refer last changes to the source itself! 

1. [API](docs/API.md)
2. [Guide](docs/1-preface.md) 

The guide might be outdated since it was written years ago based on previous versions. Logically it should be correct, but there might be inconsistences.

## Contributing
If you want to help or contribute to this project feel free to make a pull request or create a new [issue](https://github.com/timfayz/elementcss/issues). I'm very welcome to any kind of ideas and support.
