##Usage [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

**Please, before using or reading the source code you need to learn HTML/HTML5, CSS/CSS3 and basics of SASS.**<br/>
SASS unlike CSS allows us to make separate files and combine them into something single. The idea of this framework is include and generate exactly what you need and what you want. That is why we have a big amount of logically separated modules.

###Module explanation

**Module** is a little piece of code that generates logically related classes, @media rules, tag styles etc. For example, ``generate/_grid.scss`` module generates in accordance with your settings something like this: ``.container``, ``.row``, ``.column-1``, ``.column-2`` and so on. Thus you can define necessary variables to the desired module and then include them separately:
```SCSS
// activate module
$grid: true;
// exclude unnecessary components of grid system
$grid-excludes: column-offset, column-push, column-pull;
// set 12 column grid
$grid-columns-number: 12;
// import and generate
@import 'path/to/framework/generate/_grid.scss';
```

###Create basic app
Lets imagine we need to create a simple web app that must be responsible, vertical synchronized and ...

First of all we need to choose template under ``templates/app-*`` folder where do we start. As you are newbie we choose ``app-minimal`` template. Copy and paste contents of the ``templates/app-minimal`` near to the whole *element* folder. From now on we have a structure as follows:

```
|-- styles.scss
|-- element
```

Lets explore line by line a very basic usage which is the basis of ``app-minimal/styles.scss``:

```SCSS
// 1. Make short description of your project. This is special comment block that gives strangers
// useful information about the project. Exclamation mark at the beginning indicates that the
// comment must not be excluded when we compress out styles via SASS itself or third-party tools

/*!
 * Name: Your Name
 * Version:
 * Author:
 * Author URL:
 * Powered by:
 * ELEMENT | MIT License | github.com/kalopsia/element
 */

// 2. Define/redefine global variables. Here we can dramatically change the base ELEMENT's behavior.
// We must define them before importing any modules in order to make custom variables work.
// For example, we can change base font-size and line-height, device names and width range, disable
// or enable vertical synchronization, change text direction and a little bit more. A complete list
// of default globals you can find in the ``framework/_globals.scss`` file.

// Global Variables
// ----------------
//$line-height:         1.7;
//$font-size:           100%;


// 3. Initiate and normalize all tags. HTML tags within modules are grouped by function as presented
// at w3schools.com/tags/ref_byfunc.asp page.

// Initiating Tags
// ---------------
// You can delete commented variables below, because they are set to true by default. They are presented
// only in case you need to exclude appropriate range of tags.
//$basic: true;
//$forms: true;
//$lists: true;
//$type: true;
//$links: true;
//$formatting: true;
//$media: true;
//$images: true;
//$polyfills: true;
//$tables: true;

// Import the whole bunch of tag modules via file below which is simple shortcut importing all
// files within 'framework/initialize' folder:
@import 'element/framework/initialize/_all.scss';
// Hence, instead of the line above you can import modules separately:
// @import 'element/framework/initialize/_basic.scss';
// @import 'element/framework/initialize/_forms.scss';
// @import 'element/framework/initialize/_lists.scss';


// 4. Generate necessary classes.

// Generating Classes
// ------------------
// Uncomment necessary variables to make appropriate module work.
//$content: true;
//$list: true;
//$shadow: true;
//$transition: true;
//$text: true;

// For example, to activate grid system and change some settings make the following:
$grid: true;
$grid-columns-number: 10;
$grid-calc-method:    gap;
$grid-calc-value:     1%;
// Now we have 10 column grid system and 1% gap between columns. Other available options you can find
// within appropriate module.

//$icons: true;
//$border: true;
//$positioning: true;
//$opacity: true;
//$displaying: true;
//$dimension: true;
//$visibility: true;
//$utilities: true;
//$indention: true;
//$background: true;

// Import the whole bunch of classes. The same principle as mentioned previously.
@import 'element/framework/generate/_all.scss';

// Styles
// -------
// There is your own styles

```

###Create module

If you want to create your own module, go to ``templates/module`` folder. It is the basic
