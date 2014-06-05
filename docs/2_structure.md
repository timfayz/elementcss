#ELEMENT STRUCTURE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

##File Structure
```
docs/
    module/
    *.md
framework/
    generate/
        _all.scss
        _*.scss
    initialize/
        _all.scss
        _*.scss
    _globals.scss
    _naming.scss
    _functions.scss
    _mixins.scss
    _vr.scss
templates/
    app-minimal/
    module/
.gitignore
LICENSE
README.md
```

``docs/`` - contains ELEMENT's step by step documentation<br/>
``docs/module`` - contains module's line by line explanations and usage example<br/>
``framework/`` - framework files<br/>
``framework/_naming.scss`` - contains all class prefixes and names which are used among all files<br/>
``framework/_globals.scss`` - contains global variables which are used among all files<br/>
``framework/_mixins.scss`` - contains all general mixins<br/>
``framework/_functions.scss`` - contains all general functions<br/>
``framework/_vr.scss`` - contains vertical rhythm mixins and functions that provide vertical synchronization<br/>
``framework/generate/`` - contains files that generates appropriate classes<br/>
``framework/generate/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/generate/_*.scss`` - contains appropriate classes<br/>
``framework/initialize/`` - contains all files that initiate appropriate tags<br/>
``framework/initialize/_all.scss`` - combine all files in the folder. Just shortcut for including all files easily<br/>
``framework/initialize/_*.scss`` - initializes appropriate category of tags<br/>
``templates/`` - contains variety of useful templates<br/>
``templates/app-minimal/`` - minimal app template<br/>
``templates/app-basic/`` - basic app template<br/>
``templates/module/`` - module template<br/>
``.gitignore`` - file using by [git](http://en.wikipedia.org/wiki/Git_(software)) to exclude tracking unnecessary files<br/>
``LICENSE`` - licence terms and conditions<br/>
``README.md`` - brief documentation (pieces of text from main documentation)<br/>

``*`` - symbol means any file or any name of files<br/>
``_file-name`` - the fist symbol means file should be compiled into css file and it is just auxiliary or child file (for example of you future project).<br/>
``.md`` - extension means that file uses markdown syntax (like wiki markup)<br/>
``.scss`` - extension means that file uses SCSS syntax of SASS preprocessor

##Logic
ELEMENT has three step to make your app GUI unique:

1. **Tag initialization (normalize).** The module ``modules/_normalize.scss`` responsible for initiating particular [category of tags](http://www.w3schools.com/tags/ref_byfunc.asp). Hence it covers almost all HTML tags like html, body, form, legend, input, button, etc. Tag initiating or normalizing means resetting tags into unified view between different browsers.
2. **Typography.** After tags are initiated we can configure typography. The module ``modules/_type.scss`` responsible for this job. What is typography (abbreviated as *type*)? To put it bluntly, we set font-size, font-family, line-height etc in the right place and in the right units.
3. **Class generating.** The last one we need is generating classes to make our desirable styling.

##Module
Module is the most important component of the framework.
Each file within the framework folder has unified structure. It makes easier to read existing files (modules) and create new one. You can get initial module template under [templates/module](https://github.com/kalopsia/element/tree/master/templates/module) folder. Line by line explanation and its brief using example you can find under [docs/module](https://github.com/kalopsia/element/tree/master/docs/module) directory.

To understand what is module and how to start using framework, please go to the next chapter.
