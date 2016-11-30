#elementcss

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timfayz/elementcss?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

> Minimal toolkit to work with CSS and Sass.

**elementcss** provides minimal, well-organized, strict, but rich library (written in Sass) that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create complex, scalable and elaborate GUI for the contemporary web applications as well as integrate to existing project. The way of working, thought-out structure and features make it possible even recreate other popular frameworks or just create your favorite theme, use it and share. elementcss is not just framework, but tool and suit of best practices and methods from many professionals around the world to make GUI building more maintainable, easier and faster.

**[Download v2.9.0](https://github.com/timfayz/elementcss/archive/master.zip)**

##Features
elementcss is a minimalistic toolkit of Sass functions and mixins. It allows your to create your own GUI framework on top of it.

- **grid system**. Powerful `grid()` mixin to generate flexbox or float-based grid system with unlimited number of breakpoints and customizable number of columns, width, gap in each breakpoint. Implements all widely used grid features like changeable column `width`, `push`, `pull`, `offset`, `centering` etc.

- **metrics**. `calc-line()` restricts input values into fixed base ("snapping") according to your baseline (eg document's `line-height`). Use it with properties like height, margin, padding etc to provide horizontal/vertical rhythm. `calc-grid()` calculates grid parameters like column width, gap width etc.

- **SEM implementation**. elementcss implements [SEM methodology](https://github.com/timfayz/SEM). Minimalistic syntax of `set()` mixin provide full control over generating dozens of *mixes* and *elements*. [Learn more..](https://github.com/timfayz/SEM)

- **init.css**. elementcss is intended to use with [init.css](https://github.com/timfayz/init.css). init.css is best from both `normalize.css` and `Reset CSS 2.0`, init.css makes appearance of all HTML tags unstyled/unified to start styling from a blank sheet. [Learn more..](https://github.com/timfayz/init.css)

- **color utils.** Useful functions to work with colors. `convert-color()` to convert different color models into one another; `color()` to adjust, change, scale color params using different color models; `brightness()` to get brightness of color; `tint()`, `shade()`, `contrast-color()` to tint, shade and get contrast color b/w two ones. Supporting models: `hexadecimal`, `rgb(a)`, `hsb/v(a)`, `hsl(a)`.

- **unit utils**. Functions to work with CSS units. `trim-unit()`, `append-unit()`, `convert-unit()` etc to remove, append and convert different CSS units into one another. `round-unit()` function makes sure you get integer pixel when the browser finishes rendering. Support for all valid CSS units: `rem`, `px`, `pt`, `%`, `pc` etc.

- **helper utils**. Popular helper classes gathered from best practice. Clearfix, image replacement, hiding, visually hiding, text hiding and more.

- **string utils**. Useful functions to work with strings. `str-exists()`, `has-prefix()/-postfix()`, `str-replace()`, `trim-left()/-right()` to check occurrence, replace and trim specified substring(s).

- **list/map utils**. Handy functions to work with lists and maps. `slice()`, `union()`, `nth-replace()`, `replace-value()`, `nth-remove()`, `remove-value()` to slice, merge, replace and remove by index/value in lists; `map-append-val()`, `map-union()` to append key value pair and union maps.

- **math utils**. Basic math functions. `pow()`, `root()`, `gcd()` to power, root and find great common divider of a number.


##Quick Start
* [Install Sass](http://sass-lang.com/install)
* Create project folder and go inside:
```
mkdir myproject
cd myproject
```
* Clone repository or [download archive](https://github.com/kalopsia/element/archive/master.zip) and extract it into your project root:
```
git clone https://github.com/timfayz/elementcss
```
* Copy content of `elementcss/templates/app-minimal` into your project root:
```
ls
index.html  main.scss  elementcss/
```
* Check import path to elementcss' core in `main.scss`:
```
//main.scss
...
@import "path-to/elementcss/core.scss"; // correct import path
...
```
* Open command line in project root and compile `main.scss` into `main.css`:
```
sass --watch main.scss:main.css
```
* `main.css` already linked, just open `index.html` in your browser and check the result.


##File structure
```
docs/         documentation
templates/    project templates
core/*.scss   logically separated core files
_core.scss    elementcss entry point unites all core/* files
LICENSE       license information
README.md     this is what you are currently reading
```

##API
At the moment there is no API page. However all core files have well-written inline docs with examples and description of each function and mixin. Files splitted and organized so that you can read them as API reference.

###Color utils
- [`shade($clr, $percentage)`](https://github.com/timfayz/elementcss/blob/master/core/_color.scss#L3)
- `tint($clr, $percentage)`
- `convert-color($clr, $model)`
- `contrast-color($clr, $dark, $light, $algorithm:sRGB)`
- `brightness($clr, $algorithm:$brightness-algorithm)`
- `color($action, $clr, $props, $model:hsl)`

##Documentation
Documentation is under heavy development. The current docs for v1.9.0 and below.

1. [API](https://github.com/timfayz/elementcss/blob/master/docs/0-preface.md)<br/>
1. [Usage](https://github.com/timfayz/elementcss/blob/master/docs/2-usage.md)<br/>
1. [Changelog](https://github.com/timfayz/elementcss/blob/master/docs/2-usage.md)<br/>

##Contributing
If you want to help and contribute this project please make your own pull request or [report issues](https://github.com/timfayz/elementcss/issues). We are very welcome to any kind of ideas and support, even tp merge into new repo or project.
