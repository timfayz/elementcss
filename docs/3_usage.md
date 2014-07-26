#ELEMENT USAGE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

*First of all it is important to learn the basics of HTML/HTML5, CSS/CSS3 and SASS. At the beginning you may find the framework difficult - different logic, many variables, many files, unknown functions, mixins, methods in creating styles etc. However sometime later when you become better acquainted with SASS and ELEMENT you realize that the mentioned difficulties are quite simple and logically required to achieve previously mentioned features.*

##Module Usage

SASS unlike CSS allows us to make separate files and combine them into something single. One of the ideas of ELEMENT is to include and generate exactly what you need and what you want. That is why we have a big amount of logically separated modules.

**Module** is a little piece of code that generates logically related classes, @media rules, tag styles etc. For example, ``modules/_grid.scss`` generates in accordance with your settings something like this: ``.container``, ``.row``, ``.column-1``, ``.column-2`` and so on. Thus you need to define necessary variables before importing desired module(s) to overwrite default settings. For example:
```SCSS
// activate module
$grid: true;
// exclude unnecessary components of grid system
$grid-excludes: column-offset, column-push, column-pull;
// set 12 column grid
$grid-columns-number: 12;
// import and generate
@import 'path/to/framework/modules/_grid.scss';
//or
//@import 'path/to/framework/modules/grid.scss'; //shorthand
//or
//@import 'path/to/framework/modules/grid'; //shorthand
```
I remind you that
All available options you can find in the module itself (*Default Variables* section).

If you want to understand what is in the module itself and what exactly means the *unified structure* go to the following pages in this sequence:
- [basic module usage](https://github.com/kalopsia/element/blob/master/docs/module/0_module-basic-usage.scss)
- [advanced module usage](https://github.com/kalopsia/element/blob/master/docs/module/1_module-advanced-usage.scss)
- [simple module example](https://github.com/kalopsia/element/blob/master/docs/module/2_module-example.scss)

##Creating Project Styles

Lets imagine we need to create a simple web app that must be responsible, has beautiful typography.

First of all we need to choose template under ``templates/app-*`` folder where do we start. As you are newbie we choose ``app-minimal`` template. Copy and paste contents of the ``templates/app-minimal`` near to the whole *element* folder. From now on we have a structure as follows:

```
main.scss
element
```

Lets explore line by line a very basic usage which is the basis of ``app-minimal/main.scss``: **(remake!)**

```SCSS
// 1. Make short description of your project. This is special comment block that gives strangers
// useful information about the project. Exclamation mark at the beginning indicates that the
// comment must not be removed when we compress our styles via SASS itself or third-party tools

/*!
 * Name: Project name
 * Version: 0.0
 * Author: Your Name
 * Author URL: yourpage.com
 * Powered by:
 * ELEMENT | MIT License | github.com/kalopsia/element
 * Another Tool | License | project URL
 */


// 2. Define/redefine global variables. Here we can dramatically change the base ELEMENT's behavior.
// We must define them before importing any modules in order to make custom variables work.
// For example, we can change base font-size and line-height, device names and width range, disable
// or enable vertical synchronization, change text direction and a little bit more. A complete list
// of default globals you can find in the ``framework/_globals.scss`` file.

// Global Variables
// --------------------------------------------
// define global variables prepended by _
$_font-size:    16px;
$_line-height:  1.7;
$_media-unit: rem; //converts media values within $_media into the rem unit
$_media:
  (
    default:    null,
    mobile:     (media 'screen and (max-width:' 740px ')'),
    tablet:     (media 'screen and (max-width:' 1024px ')'),
    laptop:     (media 'screen and (min-width:' 1366px ')'),
    landscape:  (media '(orientation: landscape)'),
    portrait:   (media '(orientation: portrait)'),
    touch:      ('.touch'),
  );
//etc


// 3. Activating modules. If we need some ELEMENT's features we must import each module separately
// to generate its content and make it work.
// The reasons to import modules separately are:
// - order of styles are generated in the document's flow
// - reimporting the same modules but with different settings

// Normalize Module
// -----------------
// Normalize initiates and normalize all tags. HTML tags within ``_normalize.scss`` are grouped by function
// as presented at w3schools.com/tags/ref_byfunc.asp page.
$normalize: true; //this line isn't necessary, because all modules active by default
@import 'path/to/element/framework/modules/normalize.scss'; //import module


// Grid System Module
// --------------------
// Grid system creates layout of all HTML elements. If you need to change grid settings make the following:
$grid: true;
$grid-calc-data: (
    columns: 12,
    calc-method: gap,
    calc-data: 1.5%,
);
// Here we set 12 column grid system and 1.5% gap between columns. Other available options you can find
// within appropriate module.
@import 'path/to/element/framework/modules/grid.scss';


// Defaults Module
// -----------------
// generate the basic predefined styles. For more information see the source code
$defaults: true;
@import 'path/to/element/framework/modules/defaults.scss';


// 4. Creating low level classes. Low level abstraction means that one class contains only one CSS property.
// It sounds crazy but it works! This is one of the key ELEMENT's concepts. Due to
// big amount of low level classes we get unprecedented flexibility and uniqueness in building design.

// Classes
// ------------------
// Let's take example with line by line explanation how we can create them easily:

//name of variable should match to real CSS property name it is necessary to improve readability in a future
$color: color //first value "color" defines CSS property on which classes will be based
(
  //classes without media query
  default: (

    //postfix, value,
    black, #333,              //-> .color-black {color:#333;}
    white, #fff,              //-> .color-white {color:#fff;}
    //(prefix, postfix), value,
    (no, black), #fff,        //-> .no_color-black {color:white;}

    //('selector before'_'selector after'),
    ('a '_':hover'),
    black, #333,              //-> a .color-black:hover {color:#333;}
    green, green,             //-> a .color-green:hover {color:green;}
    (a, green--hover), green, //-> a .a_color-green--hover:hover {color:green;}

    //clear selectors
    (''_''),
    black, #333,              //-> .color-black {color:#333;}
  ),

  //classes under media query (see $_media var)
  //@media screen and (max-width: ...rem) {
  mobile: (
    black, #333,              //-> .color-black {color:#333;}
    //activate auto-prefixing
    prefix,
    black, #333,              //-> .mobile-color-black {color:#333;}
    green, green,             //-> .mobile-color-green {color:green;}
    //activate auto-postfixing
    postfix,
    black, #333,              //-> .color-black-mobile {color:#333;}
    green, green,             //-> .color-green-mobile {color:green;}
    //deactivate
    unfix,
    black, #333,              //-> .color-black {color:#333;}
    white, #fff,              //-> .color-white {color:white;}
  ),
  //}
);

//"classes" mixin generates classes in accordance to values and names inside $color variable
//- first argument sets prefix for CSS classes. All variables defining CSS prefixes begin with a capital.
//  Full list of predefined prefixes you can find under naming.scss file
//- second argument is what we defined above.
//- third argument is media map which will be used to create CSS classes under media queries;
@include classes($Color, $color, $_media);

// Styles
// --------------------------------------------
// create your own styles here

```

##Creating Module

If you want to create your own module explore the source files and go to ``templates/module`` folder
for more information.
