##Structure [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

###File structure
```
|-- docs
|   |-- module_review
|   |-- *.md
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
|-- .gitignore
|-- LICENSE
|-- README.md
|-- styles.css
|-- styles.scss
```

``docs/`` - contains ELEMENT's documentation<br/>
``docs/module_review`` - contains module's line by line explanation and usage<br/>
``framework/`` - core files of framework<br/>
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
``.gitignore`` - file using by [git](http://en.wikipedia.org/wiki/Git_(software)) to exclude tracking unnecessary files<br/>
``LICENSE`` - licence terms and conditions<br/>
``README.md`` - brief documentation - pieces of text from main documentation<br/>
``styles.css`` - the destination CSS file that will contain generated SASS code from *styles.scss*<br/>
``styles.scss`` - main SCSS file that imports necessary files from *framework* folder

``*`` - symbol means any file or any name of files<br/>
``.md`` - extension means that file uses markdown syntax (like wiki markup)<br/>
``.scss`` - extension means that file uses SCSS syntax of SASS preprocessor

###Logic structure
ELEMENT has two step to make your app unique:
1. Tags initiating. Appropriate module responsible for particular [category of tags](http://www.w3schools.com/tags/ref_byfunc.asp). For example ``tags/_basic.scss`` module covers html, body, * (all elements), etc. Initiating means tag normalizing and resetting into unified view.
2. Class generating. After tags are initialized we can generate appropriate classes to make our styling.

###Module structure
Module is the most important component of the framework.
Each module within framework folder has unified structure. It makes easier to read existing modules and create new one. You can get initial module template under [templates/module](https://github.com/kalopsia/element/tree/master/templates/module) folder. Line by line explanation and its brief using example you can find under [docs/module](https://github.com/kalopsia/element/tree/master/docs/module) directory.

<hr>

To understand what is module and how to start using framework, please go to the next chapter.

##[next&raquo;]