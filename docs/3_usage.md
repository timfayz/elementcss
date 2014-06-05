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

Lets explore line by line a very basic usage which is the basis of ``app-minimal/main.scss``:

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
// ----------------
$_line-height:         1.7;
$_font-size:           100%;
//etc


// 3. Initiate and normalize all tags. HTML tags within ``_normalize.scss`` are grouped by function
// as presented at w3schools.com/tags/ref_byfunc.asp page.

// Normalize
// ---------------
// just activate module
$normalize: true;


// 4. Generate necessary classes.

// Generating Classes
// ------------------
// Uncomment/comment necessary variables to make appropriate module work. This is necessary, because
// they doesn't active by default.

// For example, to activate grid system and change some settings we need to make the following:
$grid: true;
$grid-calc-data: (
    columns: 12,
    calc-method: column-gap,
    calc-data: (60px, 20px),
) !default;
// We set 10 column grid system and 1% gap between columns. Other available options you can find
// within appropriate module.

// Inactive modules
//$utilities: true;
//$icons: true;

// Now we need to import modules that we have activated.
// You can import the whole bunch of modules via "_all.scss" file which is simple shortcut importing all files
// within 'framework/modules' folder:
@import 'element/framework/modules/_all.scss';

// Hence, instead of the line above you can import modules separately:
// @import 'element/framework/modules/_grid.scss';
// @import 'element/framework/modules/_utilities.scss';
// etc

// The reasons to import modules separately are:
// - changing the order of generated styles in the flow
// - generate the same module, but differently tuned

// Styles
// -------
// There is your own styles

```

##Creating Module

If you want to create your own module, go to ``templates/module`` folder.
