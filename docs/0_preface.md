#Documentation

0. [Preface](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)<br/>
1. [Installation](https://github.com/kalopsia/element/blob/master/docs/1_installation.md)<br/>
2. [Structure](https://github.com/kalopsia/element/blob/master/docs/2_structure.md)<br/>
3. [Usage](https://github.com/kalopsia/element/blob/master/docs/3_usage.md)<br/>

##Preface
ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create new project as well as integrate to existing project. ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods to make web more robust and easy. It contains the experience of thousand professionals.

ELEMENT is based on [SASS](http://sass-lang.com/guide) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

###What is CSS framework?

`[edit]` CSS frameworks are pre-prepared libraries that are meant to allow for easier, more standards-compliant styling of web pages using the Cascading Style Sheets language. ([wiki](http://en.wikipedia.org/wiki/CSS_frameworks))

###What is SASS?

**SASS** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, if/else statements** and so on. Preprocessor is program that simply compiles selected files with the extension ``.scss`` or ``.sass`` into ``.css``.

**SASS** has two variants of syntax: SCSS (CSS-like syntax, files ending with .scss) and Sass (syntactic sugar, files ending with .sass). We use SCSS, because its syntax is the same as CSS. For example:

```SCSS
/* styles.scss */
$black: #000;
$black-postfix: black;

.text-#{$black-postfix} {
  color: $black;
}
```
```SASS
/* styles.sass */
$black: #000
$black-postfix: black

.text-#{$black-postfix}
  color: $black
```
both will be compiled into
```CSS
/* styles.css */
.text-black {
  color: #000;
}
```
[More examples](http://sass-lang.com/guide)

###Why SASS and not LESS?

*Skip if you know nothing about LESS.*<br/>
Originally I was creating ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. So I switched to SASS. Now there is no doubt after the release of version 3.3 - SASS become the most advanced preprocessor!

###What the features has ELEMENT?

ELEMENT has different structure, abstraction and thus different features
* **Fast Prototyping**.
* **Logical class names**. Every class names enforce to rules..
* **Flexibility & Deep customization**.
* **Best practices**.
* **Modularity**.
* **Full control**. Element generates nothing by default, you decide what the module you want to include and what each module includes and excludes inside.
* **Normalize & Tags initiating**. By default most of all tags have similar appearance.
* **Vertical Rhythm**. Vertical line-height synchronization.
* **Powerful Grid System**. Fully customized grid system which has some "defacto" standards like column offset, pushing, pulling, centering etc. However features (hence code amount) can be easily reduced by excluding unnecessary classes.
* **Mobile First**. Many modules have responsive additions, however they can be easily disabled.

###Ideology
The reason to create this project is make something more modular, abstract, flexible, logical, tighten? with community and unique that will differentiate it from other frameworks are existing. Something that doesn't have predefined forms, buttons, block-quotes, lists etc.

All modules(logically separated files) have unified structure and generating techniques. For more information see documentation folder.


