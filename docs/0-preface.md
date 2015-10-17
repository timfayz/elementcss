#CSS-ELEMENT DOCUMENTATION

0. [Preface](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)<br/>
1. [Installation](https://github.com/kalopsia/element/blob/master/docs/1_installation.md)<br/>
2. [Usage](https://github.com/kalopsia/element/blob/master/docs/2_usage.md)<br/>
3. [Structure](https://github.com/kalopsia/element/blob/master/docs/3_structure.md)<br/>
4. [Conventions](https://github.com/kalopsia/element/blob/master/docs/4_conventions.md)<br/>

##Preface
CSS-ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create complex, scalable and elaborate GUI for the contemporary web applications as well as integrate to existing project. The way of working, thought-out structure and features make it possible even recreate other popular frameworks or just create your favorite theme, use it and share. CSS-ELEMENT is not just framework, but tool and suit of best practices and methods from many professionals around the world to make GUI building more maintainable, easier and faster.

The framework is based on [SASS](http://sass-lang.com/guide) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

CSS-ELEMENT allows people to choose what they want and generate what they want. Currently framework allows you to outline your desirable GUI and prototype them via "atomic" classes. A little bit later we present the ways of doing that.

##The Problem or Why I need this yet another framework!?
The key reason of CSS-ELEMENT was to create framework or principe of building styles that allows you don't think about **"aging"** and **"clogging"** styles. Something that allow you prototype GUI as fast as "What You See Is What You Get" editor if you have good CSS knowledge. It is means that "something" should be modular, abstract, flexible, strict and logical that will differentiate it from other frameworks and methods are existing (OOCSS, ACSS, BEM, SMACSS etc). As a result CSS-ELEMENT can be used not only for creating your own styles (eg using the same well-known methods OOCSS, ACSS, BEM), but even shareable themes with consistent API.

As a rule the most of existing frameworks have its own **"look and feel"** which makes it difficult to focus on truly **your** unique design. That is why CSS-ELEMENT doesn't have any predefined "look and feel" (styled forms, buttons etc). It is worth noting the framework is not easy to use at the first time, but the better you know CSS-ELEMENT and CSS itself, the better you understand the power of this instrument.

##The Solution or Why you like this tool!
To solve the problems described above we introduce new method: **one class** = **one CSS property** or **atomic class** (at the moment we can use several properties but with the same CSS value). At the firs time it sounds a little bit crazy, but time after time we tested it we realized that it works and it works really good! Thus far the rest of this documentation will explain how to use this method to create styles *in CSS-ELEMENT way*. CSS-ELEMENT already has well-designed built-in components (grid system, typography, vertical rhythm and normalize) and well-established practice (like clearfix, hidden text etc). However available components designed so they don't affect your "exterior design" and work insensibly. So you don't need to think about how to change here and there to modify default look. Components can be used as they are intended or as an good examples to create new ones.

 *CSS-ELEMENT way* means generate CSS selectors contain only one CSS value and as a rule one property (**atomic classes**). This method introduce new term **set**. **Set** is combined set of atomic classes under the same CSS property(ies). Set can be generated in the main flow as well as under some of @media rules or another CSS selectors. Section *Usage* shows a specific example how it looks like.
 
 To create **set** we use special mixin and notation; it gives ease of creating and using big amount of classes. This approach allows us not to get lost in your own atomic classes when we scale. When you learn more about this tool and CSS itself you can create GUI on the fly or in WYSIWYG way by applying many unified CSS classes to HTML tags without thinking how to organize abstraction level (like we do it in OOCSS method). As soon as you create sufficient amount of classes you could extend them into more generic classes (eg BEM) there is no restrictions. But let's not get ahead of ourselves.

##Features or What can I do with CSS-ELEMENT?
The framework has different structure, philosophy and thus different features:
* **Fast Prototyping**. Think and generate what you want in the beginning. Outline what you want to see and start to prototype your desired GUI.
* **Logical class names**. CSS-ELEMENT has big amount of predefined class names which makes set's class names enforced to general rules. It provides intuitive and easy remembering.
* **Flexibility & Deep customization**. CSS-ELEMENT generates nothing by default so that you decide what the component you want to import. Namespace variables allow you to remember them easily as well as add/remove/overwrite necessary features.
* **Best practices**. We merge best experience and ideas from the most popular frameworks and tools like normalize.css, bootstrap and foundation.
* **Well-designed**. Modular structure of each component make it possible to read source code and learn from the experience.
* **Normalize & Tags initiating**. CSS-ELEMENT make all HTML tags normalized and looking identical.
* **Vertical Rhythm**. CSS-ELEMENT provides vertical line-height synchronization. It is mean that all elements follow to invisible vertical grid.
* **Powerful Grid System (Flexbox included)**. Fully customized grid system which has some "defacto" standards like column offset, pushing, pulling, centering etc. However features (hence code amount) can be easily reduced. Grid system allow you set your own @media queries.
* **Mobile First**. CSS-ELEMENT way of working allow you manage and extend your CSS @media queries easily and strictly.

*The word "easily" suggests that you have solid knowledge of CSS, SASS and HTML.*

##What do I need to know before using?

Please, before using or reading the source code you need to learn HTML/HTML5, CSS/CSS3 and basics of SASS.
Otherwise you will experience difficulties in understanding principles of work and efficiency. If you know nothing about previously mentioned technologies go to [w3schools.com](http://w3schools.com) to gain some basic knowledge.

##What is CSS framework?

CSS frameworks are pre-prepared libraries that allow you prototype your CSS GUI easier, with enhanced cross-browser support using the Cascading Style Sheets language. ([wiki](http://en.wikipedia.org/wiki/CSS_frameworks))

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

##Go Next!
If you are experienced user of SASS and CSS go to section [Usage](https://github.com/kalopsia/element/blob/master/docs/2_usage.md) and to learn more. If you newbie in this area go to next section [Installation](https://github.com/kalopsia/element/blob/master/docs/1_installation.md) to prepare yourself for using SASS.

---

####Let's do something better!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.