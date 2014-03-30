##Structure [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

###File structure
```
|-- docs
|-- framework
|   |-- classes
|       |-- _all.scss
|       |-- _*.scss
|   |-- tags
|       |-- _all.scss
|       |-- _*.scss
|   |-- _globals.scss
|   |-- _naming.scss
|   |-- _functions.scss
|   |-- _mixins.scss
|   |-- _vr.scss
|-- templates
|   |-- _module.scss
```

``docs/`` - contains ELEMENT's documentation<br/>
``framework/`` - core files of ELEMENT<br/>
``framework/_naming.scss`` - contains all class prefixes which are used among all files<br/>
``framework/_globals.scss`` - contains global variables which are used among all files<br/>
``framework/_mixins.scss`` - contains all general mixins<br/>
``framework/_functions.scss`` - contains all general functions<br/>
``framework/_vr.scss`` - contains vertical rhythm mixins and functions that provide vertical synchronization<br/>
``framework/classes/`` - contains files that generates appropriate classes<br/>
``framework/classes/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/classes/_*.scss`` - contain appropriate classes<br/>
``framework/tags/`` - contains all files that initiate appropriate tags<br/>
``framework/tags/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/tags/_*.scss`` - contain appropriate tags<br/>
``styles.css`` - the destination CSS file that will contain generated SASS code from *styles.scss*
``styles.scss`` - main SCSS file that imports necessary files from *framework* folder
``.gitignore`` - file using by [git](http://en.wikipedia.org/wiki/Git_(software)) to exclude tracking unnecessary files

``.md`` extension means that file uses markdown syntax (like wiki markup)<br/>
``.scss`` extension means that file uses SCSS syntax of SASS preprocessor

###Logic
ELEMENT has two steps:
1. Initiate tags. Appropriate module responsible for particular category of tags. For example ``tags/_basic.scss`` module covers html, body and * (all elements). Initiating means tag normalizing and resetting into unified view.
2. Class generating.

###Module structure
Each module within framework folder has unified structure. It makes easier to read existing modules and create new one. You can get initial module template in the [templates](https://github.com/kalopsia/element/tree/master/templates) folder. Line by line explanation and its brief using example you can find under [docs/code_review]() directory.