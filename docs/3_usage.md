##Usage [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

SASS unlike CSS allows us to make separate files and combine them into something single. The idea of this framework is include and generate exactly what you need and what you want. That is why we have a big amount of logically separated modules.

**Module** is a little piece of code that generates logically related classes, @media rules, tag styles etc. For example: module ``classes/_grid.scss`` generates in accordance with your settings something like this: ``.container``, ``.row``, ``.column-1``, ``.column-2`` and so on.

###Create basic app
Lets imagine we need to create a simple web app that must be responsible, vertical synchronized and ...

First of all we need to choose template under ``templates/app-*`` folder where do we start. As you are newbie we choose ``app-minimal`` template. Copy and paste contents of the ``templates/app-minimal`` near to the whole *element* folder. From now on we have a structure as follows:

```
|-- styles.scss
|-- element
```

Lets explore the code of ``styles.scss`` line by line:

```SCSS
// 1. Make short description of your project. This is special comment block that gives strangers
// useful information about the project. Exclamation mark at the beginning indicates that the
// comment must not be excluded when we compress out styles via SASS itself or third-party tools
//
/*!
 * Name: Your Name
 * Version:
 * Author:
 * Author URL:
 * Powered by:
 * ELEMENT | MIT License | github.com/kalopsia/element
 */

// 2. Define global variables. Here we can dramatically change the base ELEMENT's behavior. For example
// we can change base font-size and line-height, device names and width range, disable or enable
// vertical synchronization, text direction and a little bit more. A complete list of globals
// we can find in the ``framework/_globals.scss`` file.
//
// Global Variables
// ----------------
//$line-height:         1.7;
//$font-size:           100%;

// 3. Initiate and normalize all tags. Modules and tags within are grouped by [function](http://www.w3schools.com/tags/ref_byfunc.asp)
//
//
// Initiating Tags
// ---------------
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
@import 'element/framework/tags/_all.scss';

```
