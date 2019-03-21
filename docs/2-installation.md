# Installation

[Return to the beginning](https://github.com/timfayz/elementcss/blob/master/docs/1-preface.md)<br/>

To use elementcss efficiently we need to install additional packages. If you are newbie do not confuse about a huge amount of necessary software - don't hesitate, it is worldwide practice/tools and they certainly will be useful in the future.<br/>
**If you are already experienced user skip this section and jump to [Usage](https://github.com/timfayz/elementcss/blob/master/docs/3_usage.md).**

*Please, googling if you experience difficulties in installation.*

## Install Sass
Sass is written in Ruby, so we need to install Ruby first. Please, don't confuse about unawareness of Ruby or Ruby on Rails, it is not necessary for successfully using Sass and certainly elementcss. Let's start:

1. [Install Ruby](https://www.ruby-lang.org/en/installation/)
2. [Install Sass](http://sass-lang.com/install)

## Sass Usage
Let's take a closer look at Sass. First of all, create empty ``styles.scss`` file at the same place as if you create normal CSS file, then write a some Sass code into the file. Next we need to make our first compilation from Sass to plain CSS. If you choose command line, the steps below is for you:

* Go to directory where ``styles.scss`` is placed:<br/>
  Windows: open the directory by file explorer, run ``Shift`` + ``Right Click`` at a pane and choose ``Open command line`` in the context menu<br/>
  Unix: open terminal, run ``cd path/to/directory``
* Run one of the following commands:<br/>
  ``sass styles.scss styles.css`` - single compilation<br/>
  ``sass styles.scss styles.css --style compressed`` - single compilation and minification<br/>
  ``sass --watch styles.scss:styles.css`` - compilation on change without minification (recommended)<br/>
  If you are faced with ``LoadError: cannot load such file -- rb-inotify``<br/>
  Please, run ``gem install rb-inotify``

## Autoprefixer
elementcss is designed for use with [Autoprefixer](https://github.com/ai/autoprefixer). Autoprefixer is a tool that help us to parse CSS and add [vendor prefixes](http://webdesign.about.com/od/css/a/css-vendor-prefixes.htm) to CSS rules automatically using the latest data from [Can I Use](http://caniuse.com/) capability tables. Take a look at a little usage example:

```CSS
/* Write any CSS property without vendor prefixes */
.shadow {
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}

/* After parsing we will get the following: */
.shadow {
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}
```

### Compass
Compass as well as Autoprefixer is intended to give us cross-browser support. Compass is a library/framework that provides mixins for CSS properties introduced in CSS3 and some additional features. Compass is based on Sass which means that you have to use the Sass preprocessor. Let's take a little example:

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
As you can see the result is the same as if we use Autoprefixer. To understand how it works let's take example of what libraries and frameworks like Compass are:

```scss
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

```scss
/* styles.scss */

// 2. Import mixins, apply the necessary one where it is needed and then make compilation
@import "_css3-library.scss";
.shadow {
  @include box-shadow(rgba(0, 0, 0, 0.5) 0 2px 5px);
}
```

```css
/* styles.css */

/* 3. After compilation. */
.shadow {
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 10px inset;
}
```

### Why Autoprefixer and not Compass?
Autoprefixer allows us to write *mixins free* CSS (or include less additional mixins when we use Sass) without thinking of what the mixins are available under selected third-party library and how to use it correctly. At first, if we use Sass we compile our styles from SCSS to CSS and then (when we need it) make additional parsing to add cross-browser support. Autoprefixer just analyse your CSS and then add vendor prefixes accordingly to the latest browser support data from [Can I Use](http://caniuse.com/). Autoprefixer is independent of the any preprocessors (eg: Sass, LESS and Stylus). So we can even write plain CSS and parse it when we need to add cross-browser support (for example at the production stage). One of the main advantage of Autoprefixer is when we use Sass we do not need to import any additional third-party mixins or write your own ones, which increase amount of code and compilation time.


## Gulp
Running `sass`  through command line manually can become burdensome. That's why you can use very popular [Gulp](http://gulpjs.com/) tool instead. Gulp allows you performing repetitive tasks on your project files like watching, compilation, autoprefixing, minification etc in more convenient way. Let's imagine we have styles.scss need to be compiled after changes is made, add [vendor prefixes](http://webdesign.about.com/od/css/a/css-vendor-prefixes.htm) and then compress (remove all indents, spaces and new line breaks) to minimize size of styles. Do you want always to do it manually using cli? I don't think so. Gulp does it better, faster and without much complexity. It is the most convenient and simple tool we've ever used.

## Go Next
Go to [Usage](https://github.com/timfayz/elementcss/blob/master/docs/3-usage.md) section and start coding!
