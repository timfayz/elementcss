#CSS-ELEMENT DOCUMENTATION

0. [Preface](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)<br/>
1. [Installation](https://github.com/kalopsia/element/blob/master/docs/1_installation.md)<br/>
2. [Structure](https://github.com/kalopsia/element/blob/master/docs/2_structure.md)<br/>
3. [Usage](https://github.com/kalopsia/element/blob/master/docs/3_usage.md)<br/>
3. [Conventions](https://github.com/kalopsia/element/blob/master/docs/4_conventions.md)<br/>

##Preface
CSS-ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create complex, scalable and elaborate GUI for the contemporary web applications as well as integrate to existing project. It provides thought-out structure and many other features, like theming. CSS-ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods from many professionals to make web more robust and easy.

CSS-ELEMENT is based on [SASS](http://sass-lang.com/guide) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

CSS-ELEMENT allows people to choose what they want and generate what they want. Currently framework allow you to outline your desirable GUI and prototype them via classes. A little bit later we present the ways of doing that.

##The problem
The key reason of CSS-ELEMENT was to create framework and principe of writing styles that allows you don't think about "aging" and "clogging" styles. Something that allow you prototype GUI as fast as "What You See Is What You Get" editor. It is means that "something" should be modular, abstract, flexible, strict and logical that will differentiate it from other frameworks and methods (like OOCSS, ACSS, BEM, SMACSS) are existing. As a result CSS-ELEMENT can be used to create your own themes using known methods (OOCSS, ACSS, BEM) and absolutely unique styles with a very flexible control mechanism. It is worth noting that CSS-ELEMENT is not easy to use at the first time, but the better you know CSS-ELEMENT, the better you understand the power of this instrument and CSS itself.

##The solution
To solve the problems described above we invent new method in creating styles: **one class** = **one CSS property**. At the firs time it sounds a little bit crazy, but time after time we tested it we realized that it works and it works really good! Thus far the rest of this documentation will explain how to use this method to create your own styles in CSS-ELEMENT way. However as an example CSS-ELEMENT already has well-designed built-in components (like grid system, typography, vertical rhythm and normalize) and well-established practice (like clearfix, hidden text etc). They can be used as they are intended or as an good examples to create new ones.

 *CSS-ELEMENT way* means generate CSS selectors that contain only one CSS value and as a rule one property, for this method introduced the term ***set***. *Set* is the set of classes where *one class = one CSS property*. To create *set* we use special mixin, notation and naming rules; it gives ease of creating and using big amount of classes (see section Usage for more information). This approach allow us not to get lost in your own styles when we scale. When you learn more about CSS-ELEMENT and CSS itself you can create GUI on the fly or in WYSIWYG way by applying many CSS classes to HTML elements (similar to OOCSS). As soon as you create sufficient amount of classes you could extend them to more generic classes. But let's not get ahead of ourselves.

##Features
What the features has CSS-ELEMENT? CSS-ELEMENT has different structure, abstraction and thus different features:
* **Fast Prototyping**. Do not think about how to change here and there to make you styles unique. Just generate what you want. Outline what you want to see and start to prototype your own GUI.
* **Logical class names**. Every class names enforce to general rules. It provides intuitive and easy remembering.
* **Flexibility & Deep customization**. CSS-ELEMENT generates nothing by default so that you decide what the component you want to import. Namespace variables allow you to remember them easily as well as control and generate necessary features.
* **Best practices**. We merge best experience and ideas from the most popular frameworks and tools like normalize.css, bootstrap and foundation.
* **Well-designed**. Modular structure of each component make it possible to read source code and learn from the experience.
* **Normalize & Tags initiating**. CSS-ELEMENT make all HTML tags normalized and looking identical.
* **Vertical Rhythm**. CSS-ELEMENT provides vertical line-height synchronization. It is mean that all elements follow to invisible vertical grid.
* **Powerful Grid System (Flexbox included)**. Fully customized grid system which has some "defacto" standards like column offset, pushing, pulling, centering etc. However features (hence code amount) can be easily reduced. Grid system allow you set your own @media queries.
* **Mobile First**. CSS-ELEMENT way of working allow you manage your CSS @media queries easily and strictly.

*The word "easily" suggests that you have solid knowledge of CSS, SASS and HTML.*

##What do I need to know before using?

Please, before using or reading the source code you need to learn HTML/HTML5, CSS/CSS3 and basics of SASS.
Otherwise you will experience difficulties in understanding principles of work and efficiency. If you know nothing about previously mentioned technologies go to [w3schools.com](http://w3schools.com) to gain some basic knowledge.

##What is CSS framework?

`[edit]` CSS frameworks are pre-prepared libraries that allow you make easier, more standards-compliant styling of web pages using the Cascading Style Sheets language. ([wiki](http://en.wikipedia.org/wiki/CSS_frameworks))

##What is SASS?

**[SASS](http://sass-lang.com)** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, if/else statements** and so on. Preprocessor is program that simply compiles selected files with the extension ``.scss`` or ``.sass`` into ``.css``.

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
Originally I was creating CSS-ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. So I switched to SASS. Now there is no doubt after the release of version 3.3 - SASS become the most advanced CSS preprocessor!

---

####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.