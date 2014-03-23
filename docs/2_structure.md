##Structure [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

###File structure
```
|-- docs
|
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
|
|-- templates
|   |-- _module.scss
|
```

``styles.css`` - the destination CSS file that will contain generated SASS code from *styles.scss*
``styles.scss`` - main SCSS file that imports necessary files from *framework* folder
``framework/_naming.scss`` - contains all class prefixes which are used among all files<br/>
``framework/_globals.scss`` - contains global variables which are used among all files<br/>
``framework/_mixins.scss`` - contains all general mixins<br/>
``framework/_functions.scss`` - contains all general functions<br/>
``framework/_vr.scss`` - contains vertical rhythm mixins and functions that provide vertical synchronization<br/>
``framework/classes/`` - contains all files that generates appropriate classes<br/>
``framework/classes/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/classes/_*.scss`` - contains appropriate classes<br/>
``framework/tags/`` - contains all files that initiate appropriate tags<br/>
``framework/tags/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/tags/_*.scss`` - contains appropriate tags<br/>

``.md`` extension means that file uses markdown syntax (like wiki markup)<br/>
``.scss`` extension means that file uses SCSS syntax of SASS preprocessor

###Module structure
All modules have unified structure. It makes easier to read existing and create