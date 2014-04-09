#ELEMENT DOCUMENTATION

0. [Preface](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)<br/>
1. [Installation](https://github.com/kalopsia/element/blob/master/docs/1_installation.md)<br/>
2. [Structure](https://github.com/kalopsia/element/blob/master/docs/2_structure.md)<br/>
3. [Usage](https://github.com/kalopsia/element/blob/master/docs/3_usage.md)<br/>

##Preface
ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create complex and elaborate GUI for the contemporary web applications as well as integrate to existing project. It provides thought-out structure and many other features, like theming. ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods from many professionals to make web more robust and easy.

ELEMENT is based on [SASS](http://sass-lang.com/guide) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

##Ideology
The reason to create this project is make something modular, abstract, flexible, logical, community aimed and unique that will differentiate it from other frameworks are existing. Something that doesn't have predefined forms, buttons, block-quotes, lists etc.

ELEMENT allows people to choose what they want and generate what they want. Currently framework allow you to outline your desirable GUI and prototype them via classes.

##Features

What the features has ELEMENT? ELEMENT has different structure, abstraction and thus different features:
* **Fast Prototyping**. Do not think about how to change here and there to make you styles unique. Just generate what you want. Outline what you want to see and start to prototype your own GUI.
* **Logical class names**. Every class names enforce to general rules. It provides intuitive and easy remembering.
* **Flexibility & Deep customization**. ELEMENT generates nothing by default so that you decide what the module you want to include and what each module includes and excludes inside. Namespaced variables allow you to remember them easily as well as control and generate necessary features.
* **Best practices**. We merge best experience and ideas from the most popular frameworks and tools like normalize.css, bootstrap and foundation.
* **Modularity**. Modular structure of each framework's component make it possible to read source code and write your own modules easily.
* **Normalize & Tags initiating**. By default most of all tags normalized and have similar appearance.
* **Vertical Rhythm**. ELEMENT provides vertical line-height synchronization. It is mean that all elements follow to invisible vertical grid..
* **Powerful Grid System**. Fully customized grid system which has some "defacto" standards like column offset, pushing, pulling, centering etc. However features (hence code amount) can be easily reduced by excluding unnecessary components.
* **Mobile First**. A lot of modules have responsive additions. However they can be easily disabled that is why you can store static styles and responsible ones into two file separately.

*The word "easily" suggests that you have solid knowledge of CSS, SASS and HTML.*

##What do I need to know before using?

Please, before using or reading the source code you need to learn HTML/HTML5, CSS/CSS3 and basics of SASS.
Otherwise you will experience difficulties in understanding principles of work and efficiency. If you know nothing about previously mentioned technologies go to [w3schools.com](http://w3schools.com) to gain some basic knowledge.

##What is CSS framework?

`[edit]` CSS frameworks are pre-prepared libraries that allow you make easier, more standards-compliant styling of web pages using the Cascading Style Sheets language. ([wiki](http://en.wikipedia.org/wiki/CSS_frameworks))

##What is SASS?

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

##Why SASS and not LESS?

*Skip if you know nothing about LESS.*<br/>
Originally I was creating ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. So I switched to SASS. Now there is no doubt after the release of version 3.3 - SASS become the most advanced preprocessor!