##Usage [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

SASS unlike CSS allows us to make separate files and combine them into something single. The idea of this framework is include and generate exactly what you need and what you want. That is why we have a big amount of logically separated modules.

**Module** is a little piece of code that generates logically related classes, @media rules, tag styles etc. For example: module ``classes/_grid.scss`` generates in accordance with your settings something like this: ``.container``, ``.row``, ``.column-1``, ``.column-2`` and so on.

###Create basic app
Lets imagine we need to create a simple web app that must be responsible, vertical synchronized and ...

First of all we need to choose template under ``templates/app-*`` folder where do we start. As you are newbie we choose ``app-basic`` template. Copy and paste contents of the ``tempate/app-basic`` near to the whole *element* folder. From now on we have a structure as follows:

```
|-- styles.scss
|-- element
```

Lets explore the code of the styles.scss line by line:

```SCSS
// This is special comment block that give strangers useful information about your project
// Exclamation mark indicate that the comment must not be excluded when we compress out styles via SASS itself or
// third-party tools
/*!
 * Name: Your Name
 * Version:
 * Author:
 * Author URL:
 * Powered by:
 * ELEMENT | MIT License | github.com/kalopsia/element
 */

```
