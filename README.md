**Please, do not read the text below. Readme under heavy development.**

#ELEMENT - CSS/GUI framework
<sub>I'm sorry for the language mistakes I've made - I'm from Russia.</sub>

ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create new project as well as integrate to existing project. ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods to make web more robust and easy. It contains the experience of thousand professionals.

**[Download](https://github.com/kalopsia/element/archive/master.zip)**

##Features
1. Modular
2. Flexibility & Deep customization
3. Best practices
4. Logical naming


##Preface
ELEMENT is based on [SCSS](sass-lang.com) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

**What do I need to know before using?**

Please, before using or reading the source code you need to learn some basics of SASS(SCSS syntax) and know CSS3 basics (@media, @font-face rules, etc). 
Otherwise you will experience difficulties in understanding principles of work and efficiency.

**What is SASS?**

**SASS** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, if/else statements** and so on. Preprocessor is program that simple convert files with the extension .scss into .css. For example: 
```SCSS
/* styles.scss */
$black: #000;
$black-postfix: black;

.text-#{$black-postfix} {
  color: $black;
}
``` 
compiles to
```CSS
/* styles.css */
.text-black {
  color: #000;
}
```
**Why SASS and not LESS?**

Originally I was creating ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. (?) After the release of version 3.3 - SASS become the most advanced preprocessor! 


##Get started
**ELEMENT helps Web developers create complex and thoughtful GUI for the contemporary web applications.**

###Why is need for?
ELEMENT has different structure, abstraction and thus different features

* Full control. Element generates nothing by default, you decide what the module you want to include and what each module includes and excludes inside.
* Normalize & Tags initiating.
* Vertical Rhythm. Vertical line-height synchronization.
* Powerful grid system. But still features (hence code)  can be easily reduced.
* Mobile First. But still responsive features can be easily disabled.

###Installation
1. [Install Ruby]()
*(Don't hesitate about unawareness of ruby/ruby on rails, it is not necessary for successfully using SASS and ELEMENT too. FYI, I doesn't know it too :).)*
2. [Install Gruntjs]()
3. [Install Autoprefixer]()

For successfully using ELEMENT I recommend you to use tools as follows: [Gruntjs](gruntjs.com), [Vagrant](vagrantup.com).


###File structure
``_naming.scss`` - contains all class prefixes which are used among all files<br/>
``_globals.scss`` - contains global variables which are used among all files

``_mixins.scss`` - contains

``_functions.scss`` - contains

``_vr.scss`` - contains

``classes/``

``.md`` extension means that file uses markdown syntax which is used for styling text (like wiki markup).
``.scss`` extension means that file uses SCSS syntax of SASS preprocessor which father will be compiled into CSS. 


###Ideology
The reason to create this project is make something more modular, abstract, flexible, logical, tighten? with community and unique that will differentiate it from other frameworks are existing. Something that without predefined forms, buttons, block-quotes, lists etc.


**Goals of this framework**
- modular
- abstract (OOCSS)
- simple
- strict structure
- good maintenance

###Inspired by
- Bootstrap
- Foundation
- FlatUI
- Gridlover
- Golden Grid System
- KNACSS
- Susy
- GoodUI
- etc


