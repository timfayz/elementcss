#ELEMENT INSTALLATION
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

To use ELEMENT efficiently and successfully we need to install some additional popular tools. Do not confuse about a huge amount of necessary software - don't hesitate, they certainly will be useful in future.<br/>
*Please, googling if you experience difficulties in installation.*

##Install SASS
SASS is written in Ruby, so we need to install Ruby first. Please, don't confuse about unawareness of Ruby or Ruby on Rails, it is not necessary for successfully using SASS and certainly ELEMENT. Let's start:
1. [Install Ruby](https://www.ruby-lang.org/en/installation/)
2. [Install SASS](http://sass-lang.com/install)
3. From now on you can use GUI **application** or **command line** to make compilations

##SASS Usage
Let's take a closer look at SASS. First of all, create empty ``styles.scss`` file at the same place as if you create normal CSS file, then write a some SASS code into the file. Next we need to make our first compilation from SASS to plain CSS. If you choose command line, the steps below is for you:

* Go to directory where ``styles.scss`` is placed:<br/>
	Windows: open the directory by file explorer, run ``Shift`` + ``Right Click`` at a pane and choose ``Open command line`` in the context menu<br/>
	Unix: open terminal, run ``cd path/to/directory``
* Run one of the following commands:<br/>
	``sass styles.scss styles.css`` - single compilation<br/>
	``sass styles.scss styles.css --style compressed`` - single compilation and minification<br/>
	``sass --watch styles.scss:styles.css`` - compilation on change without minification (recommended)<br/>

	If you are faced with ``LoadError: cannot load such file -- rb-inotify``<br/>
	Please, run ``gem install rb-inotify``

##Autoprefixer
ELEMENT is designed for using with [Autoprefixer](https://github.com/ai/autoprefixer). Autoprefixer is a tool that help us to parse CSS and add [vendor prefixes](http://webdesign.about.com/od/css/a/css-vendor-prefixes.htm) to CSS rules automatically using the latest data from [Can I Use](http://caniuse.com/) capability tables. Take a look at a little usage example:

```CSS
/* Write any CSS property without vendor prefixes */
.shadow {
  @include box-shadow(rgba(0, 0, 0, 0.5) 0 2px 10px inset);
}

/* After Autoprefixer parsing we will get the following: */
.shadow {
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}
```

###Compass
Compass as well as Autoprefixer is intended to give us cross-browser support. Compass is a library/framework that provides cross-browser mixins for CSS properties introduced in CSS3 and some additional features. Compass is written in SASS which means that you have to use the SASS preprocessor. Let's take a little usage example:

```SCSS
// 1. Import compass CSS3 mixins
@import "compass/css3";

// 2. Include Compass' mixins where necessary
.shadow {
  @include box-shadow(rgba(0, 0, 0, 0.5) 0 2px 10px inset);
}

// 3. After compilation we will get the following:
.shadow {
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}
```
As you can see the result is the same as if we use Autoprefixer. To understand how it works let's take a example of what libraries and frameworks like Compass are:

```SCSS
/* _css3-library.scss */

// 1. Define mixins with the same names as in CSS3 under separate file
@mixin box-shadow($value) {
  -webkit-box-shadow: $value;
  -moz-box-shadow: $value;
  box-shadow: $value;
}
@mixin text-shadow($value) {
  ...
}
@mixin box-sizing($value) {
  ...
}
// etc
```

```SCSS
/* styles.scss */

// 2. Import mixins, use it where necessary and make compilation
@import "_css3-library.scss";
.shadow {
  @include box-shadow(rgba(0, 0, 0, 0.5) 0 2px 5px);
}
```

```CSS
/* styles.css */

/* 3. After compilation. */
.shadow {
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}
```

###Why Autoprefixer and not Compass?
Autoprefixer allows us to write *mixins free* CSS (or include less additional mixins when we use SASS) without thinking of what the mixins is available under selected library and how to use it correctly. Autoprefixer just analyse your CSS and then add vendor prefixes accordingly to latest browser support data from [Can I Use](http://caniuse.com/). Autoprefixer is independent of the any preprocessors (eg: SASS, LESS and Stylus). So we can even write plain CSS and parse it when we need to add cross-browser support (for example at the production stage). When we use SASS we do not need to write any additional third-party mixins or write your own ones and thus increase compilation time when we use it. We can just parse compiled CSS to add vendor prefixes only when we need it.


##Gruntjs
Using command line and ``sass`` command quite enough, but for successfully using ELEMENT I recommend you to use [Gruntjs](http://gruntjs.com/getting-started) or GUI application like .... Gruntjs allows performing repetitive tasks like watching, compilation, minification and etc. Let's imagine we have styles.scss which need to be compiled after changes was made, then add [vendor prefixes](http://webdesign.about.com/od/css/a/css-vendor-prefixes.htm) and make compress (remove all indents, spaces and new line breaks). To do so we

* [Install Nodejs](http://nodejs.org/download/) (required for Gruntjs)
* [Install Gruntjs](http://gruntjs.com/getting-started)
* [Install Autoprefixer](https://github.com/nDmitry/grunt-autoprefixer) (Gruntjs' module)

1. [Download ELEMENT](https://github.com/kalopsia/element/archive/master.zip)
2. Extract the directory where you store your own styles
3. Choose initial app template under ``templates/`` folder. Copy contents of template to
3. Include CSS file into project: ``<link rel="stylesheet" type="text/css" href="path/to/styles.css">``

