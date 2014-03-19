**Please, do not read the text below. Readme under heavy development.**

#ELEMENT - CSS/GUI framework
<sub>I'm sorry for the language mistakes I've made - I'm from Russia.</sub>

ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create new project as well as integrate to existing project. ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods to make web more robust and easy. It contains the experience of thousand professionals.

**[Download](https://github.com/kalopsia/element/archive/master.zip)**


##Preface
ELEMENT is based on [SCSS](sass-lang.com) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SASS.

**What do I need to know before using?**

Please, before using or reading the source code you need to learn HTML/HTML5, CSS/CSS3 and basics of SASS(SCSS syntax).
Otherwise you will experience difficulties in understanding principles of work and efficiency.

**What is SASS?**

**SASS** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, mixins, if/else statements** and so on. Preprocessor is program that simple compile files with the extension .scss|.sass into .css. For example: 
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

Originally I was creating ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. So I switched to SASS. Now there is no doubt after the release of version 3.3 - SASS become the most advanced preprocessor! 


##Get started
**ELEMENT helps Web developers create complex and thoughtful GUI for the contemporary web applications.**

###Why is need for?
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

###Installation
If you've never used the tools below, don't confuse about a huge amount of necessary software.<br/>
Do not hesitate, some of them will be useful in future<br/>
Please, googling if you experience difficulties in installation.
 
1. [Install Ruby](https://www.ruby-lang.org/en/installation/) (required for SASS language)<br/>
*Please, do not hesitate about unawareness of ruby/ruby on rails, it is not necessary for successfully*<br/> *using SASS and ELEMENT. FYI, I doesn't know it too.*
2. [Install SASS](http://sass-lang.com/install)
3. [Install Nodejs](http://nodejs.org/download/)
2. [Install Gruntjs](http://gruntjs.com/getting-started)
3. [Install Autoprefixer](https://github.com/nDmitry/grunt-autoprefixer) (Gruntjs' module)

For successfully using ELEMENT I recommend you to use tools as follows: [Gruntjs](gruntjs.com), [Vagrant](vagrantup.com).


###File structure
``_naming.scss`` - contains all class prefixes which are used among all files<br/>
``_globals.scss`` - contains global variables which are used among all files<br/>
``_mixins.scss`` - contains all general mixins<br/>
``_functions.scss`` - contains all general functions<br/>
``_vr.scss`` - contains vertical rhythm mixins and functions that provide vertical synchronization<br/>
``classes/`` - contains all files that generates appropriate classes<br/>
``classes/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily.<br/>
``classes/_*.scss`` - contains appropriate classes<br/>
``tags/`` - contains all files that initiate appropriate tags<br/>
``tags/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily.<br/>
``tags/_*.scss`` - contains appropriate tags<br/>

``.md`` extension means that file uses markdown syntax which is used for styling text (like wiki markup).
``.scss`` extension means that file uses SCSS syntax of SASS preprocessor which father will be compiled into CSS. 


###Ideology
The reason to create this project is make something more modular, abstract, flexible, logical, tighten? with community and unique that will differentiate it from other frameworks are existing. Something that without predefined forms, buttons, block-quotes, lists etc.


##Acknowledgements
List of sources thanks to which this framework is raised.

###Online resources
- [w3schools.com](http://w3schools.com/)
- [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web)
- [CSS-Tricks.com](css-tricks.com) by Chris Coyier
- [Caniuse.com](caniuse.com)

###Tools
- [SASS](http://sass-lang.com/) by Hampton Catlin, Nathan Weizenbaum, Chris Eppstein
- [LESS](http://lesscss.org/) by Alexis Sellier
- [HTML5 Boilerplate](http://html5boilerplate.com/) by Nicolas Gallagher, Paul Irish, Mathias Bynens, Divya Manian, and Hans Christian Reinl
- [Normalize.css](http://necolas.github.io/normalize.css/) by Nicolas Gallagher 
- Just numerous contributors that help to evolve their favorite projects.

###Frameworks
- Bootstrap
- Foundation
- FlatUI
- Gridlover
- Golden Grid System
- KNACSS
- Susy
- GoodUI
