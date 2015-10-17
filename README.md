#elementcss

[![Join the chat at https://gitter.im/kalopsia/element](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/kalopsia/element?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> New way of creating CSS.

elementcss providing minimal, strict toolkit (written in Sass). that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create complex, scalable and elaborate GUI for the contemporary web applications as well as integrate to existing project. The way of working, thought-out structure and features make it possible even recreate other popular frameworks or just create your favorite theme, use it and share. ElementCSS is not just framework, but tool and suit of best practices and methods from many professionals around the world to make GUI building more maintainable, easier and faster.

**[Download v1.9.0](https://github.com/timfayz/elementcss/archive/master.zip)**

##Features
 - **grid system**. Flexbox or float-based grid system with customizable number of grids, column number, width, gap. Implements all widely used grid features like changeable column `width`, `push`, `pull`, `offset`, `centering` etc + all delights of the flexbox model.

 - **color utils.** Convert different color models into one another. Adjust, change, scale color params using different color models. Supports `hexadecimal`, `rgb(a)`, `hsb/v(a)`, `hsl(a)` and new CSS4 `color()` function.

 - **unit utils**. Convert, remove, append different CSS units into one another. Using `round-unit()` function makes sure you get integer pixel when the browser finishes rendering. Supports all valid CSS units: `rem`, `px`, `pt`, `%` etc.

 - **vertical rhythm**. Pass a value through `calc-line()` function to snap/restrict any CSS property into invisible grid based on custom baseline (eg your line-height). [edit] Useful for height, margin, padding etc. Automatically calculates the nearest value based on `pitch`, `threshold` and `baseline` params.

 - **init.css**. Get best from both `normalize.css` and `Reset CSS 2.0`. `init.scss` component contains CSS that makes appearance of all HTML tags unified to start styling like from a blank sheet.

 - **helper utils**. Clearfix, image replacement, hiding, visually hiding, text hiding and many more. The most used helper classes designed and gather from best practice.

 - **string utils**. Check occurrence, find, replace, prefix and postfix specified substring.

 - **list/map utils**. Replace, union, append, find indexes and many more handy function to work with lists and maps.

 - **math utils**. Power, root and find great common divider of a number.


##Quick Start
* [Install Sass](http://sass-lang.com/install)
* Create project folder:
```
mkdir myproject
cd myproject
touch index.html
```
* Clone repository or [download](https://github.com/kalopsia/element/archive/master.zip)
```
git clone https://github.com/timfayz/elementcss
```
* Copy content of `templates/app-basic` into your project root:
```
cp -a elementcss/template/app-basic/. ./
ls
index.html  main.scss  elementcss/
```
* Check import path to elementcss core in `main.scss`:
```
...
@import "path-to/elemetcss/core.scss"
...
```
* Compile `main.scss` into `main.css`
```
sass --watch main.scss:main.css
```
* Link `main.css` into your `index.html` and open it in a browser:
```
<!doctype html>
<html>
  <head>
    <link rel="stylesheets" href="main.css">
  </head>
  <body>
    <p class="c-blue">Hello World!</p>
  </body>
</html>
```


##File structure
```
docs/         documentation
utils/        framework core functions & mixins
templates/    project templates
_.scss        elementcss entry point unites all root files
*.scss        logically separated global files
LICENSE       license information
README.md     this is what you are currently reading
```


##Documentation
Documentation is under heavy development.

0. [Preface](https://github.com/timfayz/elementcss/blob/master/docs/0-preface.md)<br/>
1. [Installation](https://github.com/timfayz/elementcss/blob/master/docs/1-installation.md)<br/>
2. [Usage](https://github.com/timfayz/elementcss/blob/master/docs/2-usage.md)<br/>
3. [Structure](https://github.com/timfayz/elementcss/blob/master/docs/3-structure.md)<br/>
4. [Conventions](https://github.com/timfayz/elementcss/blob/master/docs/4-conventions.md)<br/>


##How to participate
If you want to help and contribute this project please make your own pull request or [report issues](https://github.com/timfayz/elementcss/issues). We are very welcome to any kind of ideas and support, even merge to the new repo/project.
