#CSS-ELEMENT USAGE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

*First of all it is important to learn the basics of HTML/HTML5, CSS/CSS3 and SASS. At the beginning you may find the framework difficult - different logic, many variables, many files, unknown functions, mixins, methods in creating styles etc. However sometime later when you become better acquainted with SASS and CSS-ELEMENT you realize that the mentioned difficulties are quite simple and logically required to achieve previously mentioned features.*

##Component Usage

SASS unlike CSS allows us to make separate files and combine them into single one. One of the ideas of CSS-ELEMENT is to include and generate exactly what you need and what you want. That is why we have a some amount of logically separated components.


##Create New Project

Lets imagine we need to create a simple web app that must be responsible, has beautiful typography.
TODO: due to lack of knowledge how to use CSS-ELEMENT and how its using looks like we need...
First of all we need to choose template under `templates/app-*` folder. As you are newbie we choose `app-minimal` template where do we start. Copy and paste contents of the `templates/app-minimal` near to the whole *element* folder. From now on we have a structure as follows:

```
app.scss
css-element
```

Lets explore line by line a very basic usage which is the basis of `app-minimal/app.scss`:

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
 * CSS-ELEMENT | MIT License | github.com/kalopsia/element
 * Another Tool | License | project URL
 */


// 2. Define/redefine global variables. Here we can dramatically change the base CSS-ELEMENT's behavior.
// We must define them before importing any components in order to make custom variables work.
// For example, we can change base font-size and line-height, device names and width range, disable
// or enable vertical synchronization, change text direction and a little bit more. A complete list
// of default globals you can find in the `framework/_globals.scss` file.

// Global Variables
// --------------------------------------------
// Redefine global variables prepended by _
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


// 3. Activating components. If we need some CSS-ELEMENT's features we must import each module separately
// to generate its content and make it work.
// The reasons to import components separately are:
// - order of styles are generated in the document's flow
// - reimporting the same components but with different settings

// Normalize Component
// -----------------
// Normalize initiates and normalize all tags. HTML tags within ``_normalize.scss`` are grouped by
// function as presented at w3schools.com/tags/ref_byfunc.asp page.
$normalize: true; //this line isn't necessary, because all components active by default
@import 'path/to/element/framework/components/normalize.scss'; //import module


// Grid System Component
// --------------------
// Grid system creates layout of all HTML elements.
$grid: true;
// If you need to change grid settings make the following:
$grid-calc-data: (
    columns: 12,
    calc-method: gap,
    calc-data: 1.5%,
);
// Here we set 12 column grid system and 1.5% gap between columns. Other available options you can find
// within appropriate module.
@import 'path/to/element/framework/components/grid.scss';


// Defaults Component
// -----------------
// Generate the basic predefined styles. For more information see the source code
$defaults: true;
@import 'path/to/element/framework/components/set.scss';


// 4. Creating low level classes. Low level abstraction means one class contains only one CSS property.
// It sounds crazy but it works! This is one of the key CSS-ELEMENT's concepts. Due to big amount of low
// level classes we get unprecedented flexibility and uniqueness in building design.

// Classes
// ------------------
// Let's take example how we can create them easily with line by line explanation:

//name of variable should match to real CSS property name
//it is necessary to improve readability in a future
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
//- first argument sets prefix for CSS classes. All variables defining CSS prefixes begin with a
//  capital. Full list of predefined prefixes you can find under framework/_naming.scss file
//- second argument is what we defined above.
//- third argument is media map which will be used to create CSS classes under media queries;
@include set($Color, $color, $_media);

// Styles
// --------------------------------------------
// create your own styles here

```

##Creating Component

If you want to create your own module explore the source files and go to ``templates/module`` folder
for more information.

---

####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.