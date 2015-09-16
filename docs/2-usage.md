#CSS-ELEMENT USAGE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

*First of all it is important to learn the basics of HTML/HTML5, CSS/CSS3 and SASS. At the beginning you may find framework difficult - different logic, many variables, many files, unknown functions, mixins and methods in creating styles. However sometime later when you learn SASS and CSS-ELEMENT better you realize that the mentioned difficulties are quite simple and logically required to achieve previously mentioned features.*

##Create New Project
Let's get started with CSS-ELEMENT on an example. First of all, to make the process easier we need to choose template under `docs/templates/app-*` folder. We choose `app-minimal` to start play without the mess. Copy and paste file `app.scss` from the folder near to the [downloaded](https://github.com/kalopsia/element/archive/master.zip) and extracted `element-master` archive. *master* prefix is added automatically by github - it means you get copy from *master* branch and as a rule it's the latest version of repository. From now on we need to bring the structure in the following form:

```
myproject/
    element-master/
    app.scss
```
@todo add `sass` command here and warn to change paths!

Lets explore line by line how to use CSS-ELEMENT:

```SCSS
// 1. Make short description about your project. This is special comment block that gives strangers
// from network useful information about your project. Exclamation mark at the beginning indicates that the
// comment must not be removed or minified when we compress it via "sass" command or by any other third-party tool.

/*!
 * Name: App Name
 * Version: 1.0
 * Authors: Your Name
 * Author URL: example.com
 * Powered by:
 * CSS-ELEMENT | MIT License | github.com/kalopsia/element
 * Another Tool | License | project URL
 */


// 2. Define/overwrite global variables. Here we can dramatically change the CSS-ELEMENT's component behavior.
// As mentioned before core framework files generate no content. So these changes will have an effect only after
// we import some of components. All core global variables start with $_*. So they are easier to recognize.
//
// We must define variables before importing any components in order to overwrite default values.
// For example, we can change:
//      - base font-size, line-height and text direction used by normalize component
//      - @media rule names and query values used by grid component
//      - and a little bit more
// The complete list of available globals you can find in the `framework/_globals.scss` file.

// Global Variables
// --------------------------------------------------
$_font-size:    1rem;
$_line-height:  1.7;
$_media-unit:   rem; //converts media values within $_media into the rem unit
$_media:
  (
    default:    null,
    mobile:     media 'screen and (max-width:' 740px ')',
    tablet:     media 'screen and (max-width:' 1024px ')',
    laptop:     media 'screen and (min-width:' 1366px ')',
    landscape:  media '(orientation: landscape)',
    portrait:   media '(orientation: portrait)',
    touch:      '.touch',
  );


// 3. Activate components. To use maximum of CSS-ELEMENT we should import each component separately. By importing
// components we generate its content/styles and make it work. We can change default behaviour of components by
// overwriting their default variables. All available variables you can find within component itself.

// Normalize
// --------------------------------------------------
// normalize.scss initiates and normalize all tags into one identical appearance. HTML
// tags within _normalize.scss grouped by function. See w3schools.com/tags/ref_byfunc.asp page.
@import 'element-master/components/normalize.scss';


// Grid System
// --------------------------------------------------
// grid.scss generates helper classes for convenient page layout.
// Here we define 12 column grid system and 1.5% gap between columns.
$grid-params: calc-grid(12, gap, 1.5%);

@import 'element-master/components/grid.scss';


// Sets
// --------------------------------------------------
// set.scss generates sets of classes with very basic styles.
// What is set and how it looks like see an example above.
@import 'element-master/components/set.scss';


// 4. Creating sets. Set is set of classes where class contain one value and CSS property. Don't think that's crazy
// - it really works! This is one of the key CSS-ELEMENT's concepts. Due to big amount of low level classes we get
// unprecedented flexibility in building GUI.

// Your Own Sets
// ------------------
// It's time to consider one of the key concept and see how it looks! This is what we call
// create styles in CSS-ELEMENT way. Let's create one comprehensive set with line by line explanation:

// ┌ name of variable should match to real CSS property name. Eg: $myset-backgroud, $myset-border etc
$color: color // "color" defines valid CSS property will be used by future classes.
//  └ it is necessary to improve readability in a future
(
  // ┌ keys of this map associated with keys defined in $_media var (we defined it above)
  default: (
  //  └ because default has null value the set defined under this key will have no query

    // ┌ postfix               ┌ this column shows the result of what we get after including set() mixin
    black, #000,              // .clr-black {color:#000;}
    //      └ value
    white, #fff,              // .clr-white {color:#fff;}
    
    // ┌ (prefix, postfix) - another method of notation
    (no, black), #fff,        // .no_clr-black {color:#fff;}
    //                              └ underscore adds automatically following after prefix
    
    // ┌ ('selector before'_'selector after') - method of notation additional selectors
    ('a '_':hover'),
    black, #000,              // a .clr-black:hover {color:#000;}
    green, green,             // a .clr-green:hover {color:green;}
    (a, green--hover), green, // a .a_clr-green--hover:hover {color:green;}

    // ┌ clear selectors previously defined in the flow
    (''_''),
    black, #000,              // .clr-black {color:#000;}
  ),
  // result: the block above will produce 7 classes

  // @media screen and (max-width: 740px) { - see $_media variable and value opposite mobile key
  //                                └ 740px will be converted into rem automatically, see $_media-unit
  mobile: (
  // └ mobile key will associate these classes with the appropriate media query, see $_media
    black, #000,              // .clr-black {color:#000;}
    // ┌ activate auto-prefix, prefix comes from key "mobile"
    prefix,
    black, #000,              // .mobile-clr-black {color:#000;}
    green, green,             // .mobile-clr-green {color:green;}
    // ┌ activate auto-postfix
    postfix,
    black, #000,              // .clr-black-mobile {color:#000;}
    green, green,             // .clr-green-mobile {color:green;}
    // ┌ deactivate prefix/postfix
    unfix,
    black, #000,              // .clr-black {color:#000;}
    white, #fff,              // .clr-white {color:#fff;}
  ),
  // }
  // result: the block above will produce also 7 classes but under mobile media query defined in the $_media
);

// Let's generate our classes by including set() mixin.
//                           ┌ media map are used to create classes under given media queries
@include set(clr, $color, $_media);
//            └ base prefix applying to entire set

// (!) You can use CSS-ELEMENT built-in base prefixes. Full list of predefined prefixes you can find in _naming.scss file.
// All variables defining CSS prefixes begin with a capital. So in the example above you can set $Color instead "clr"

// Styles
// --------------------------------------------
// create your own styles here

```

##About Components
SASS unlike CSS allows us to make separate files and combine them into single one. One of the ideas of CSS-ELEMENT is to include and generate exactly what you need and what you want. That is why we have some amount of logically separated components.

##What Next?
After playing with `app-minimal` we recommend you to try `app-basic` template. It has well-designed initial structure for scalable and long-term maintainable projects. For now we can go next section and learn more about CSS-ELEMENT structure and functionality.

---

####Let's do something better!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.