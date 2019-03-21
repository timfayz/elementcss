# Usage
[Return to the beginning](https://github.com/timfayz/elementcss/blob/master/docs/1-preface.md)<br/>

*Before going further it is important to learn basics of HTML, CSS and Sass. At the beginning you may find it difficult - different logic, many variables, many files, unknown functions and mixins to create styles. However, once you learn Sass and elementcss better you realize that the mentioned difficulties are quite simple and logically required to achieve features we strive for.*

### Create New Project
Let's get started by simple example. Go to `templates/app-minimal` dir and copy its content near to the [downloaded](https://github.com/timfayz/elementcss/archive/master.zip) and extracted `master.zip` archive. 

> *master* prefix is added automatically by GitHub - it means you get a copy from *master* branch and usually it points to the latest version of repository. 
 
From now on, we need to bring the structure to the following form:

```
myproject/
    elementcss-master/
    index.html
    main.scss
```
@todo add `sass` command here and warn to change paths!

Lets go through the `main.scss` and explore line by line how elementcss works:

```scss
/*!
 * Name: App Name
 * Authors: Your Name
 * Author URL: example.com
 * Powered by:
 * elementcss | MIT License | github.com/timfayz/elementcss
 */


// 1. Define/overwrite global variables. Here we can dramatically change the elementcss's component behavior.
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


// 2. Activate components. To use maximum of elementcss we should import each component separately. By importing
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


// 3. Creating sets. Set is set of classes where class contain one value and CSS property. Don't think that's crazy
// - it really works! This is one of the key elementcss's concepts. Due to big amount of low level classes we get
// unprecedented flexibility in building GUI.

// Your Own Sets
// ------------------
// It's time to consider one of the key concept and see how it looks! This is what we call
// create styles in elementcss way. Let's create one comprehensive set with line by line explanation:

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

// (!) You can use elementcss built-in base prefixes. Full list of predefined prefixes you can find in _naming.scss file.
// All variables defining CSS prefixes begin with a capital. So in the example above you can set $Color instead "clr"

// Styles
// --------------------------------------------
// create your own styles here

```

## What's Next?

That's it! Now you can using elementcss by your own! Also, do not forget to check other tightly related projects: [SEM](https://github.com/timfayz/SEM) and [init.css](https://github.com/timfayz/init.css).

Also, after playing with `app-minimal` template you can try `app-advanced`. It has well-designed initial structure for scalable and long-term projects.