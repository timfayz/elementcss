**Please, do not read the text below. Readme under heavy development.**

<sub>I'm sorry for the language mistakes I've made - I'm from Russia.</sub>

#ELEMENT - CSS/GUI framework
ELEMENT is free and open-source CSS framework written in SASS that promotes clean, object-oriented design and encourages rapid prototyping. It helps you to create new project as well as integrate to existing project. ELEMENT is not just framework, but tool and suit of best practices and the most advanced methods to make web more robust and easy. It contains the experience of thousand professionals.


##Features
1. Modular
2. Flexibility & Deep customization
3. Best practices
4. Logical naming


##Preface
ELEMENT is based on [SCSS](sass-lang.com) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SCSS.

**What is SCSS?**

**SCSS** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, if/else statements** and so on. Preprocessor is program that simple convert files with the extension .scss into .css. For example: 
```
#styles.scss
$black: #000;
$black-postfix: black;

.text-#{$black-postfix} {
  color: $black;
}
``` 
compiles to
```
#styles.css
.text-black {
  color: #000;
}
```

**What do I need to know before using?**

Please, before using or reading the source code you need to learn some basics of SASS(SCSS) and know CSS3 basics (@media, @font-face rules, etc). 
Otherwise you will experience difficulties in understanding principles of work and efficiency.

**[Download](https://github.com/kalopsia/element/archive/master.zip)**


##Get started
**ELEMENT helps Web developers create complex and thoughtful GUI for the contemporary web applications.**


###Installation
1. [Install Ruby]()
*(Don't hesitate about unawareness of ruby/ruby on rails, it is not necessary for successfully using SASS and ELEMENT too. FYI, I doesn't know it too :).)*
2. [Install Gruntjs]()
3. [Install Autoprefixer]()

For successfully using ELEMENT I recommend you to use tools as follows: [Gruntjs](gruntjs.com), [Vagrant](vagrantup.com).


###About
ELEMENT means ...

The reason to create this project is make something more modular, abstract, flexible, logical, tighten? with community and unique that will differentiate it from other frameworks are existing. Something that without predefined forms, buttons, block-quotes, lists etc.

**Why SASS and not LESS?**

Originally I was creating ELEMENT in LESS, but sometime later I realized that LESS doesn't have enough features to release necessary and pursued ideas. After the release of version 3.3 - SASS become the most advanced preprocessor! 

**Goals of this framework**
- modular
- abstract (OOCSS)
- simple
- strict structure
- good maintenance


###File structure
.md extension means markdown syntax to style text on the web.

