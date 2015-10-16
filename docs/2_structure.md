#ELEMENT STRUCTURE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

##File Structure
    docs/
        module/
        *.md
    framework/
        modules/
            _default.scss
            _grid.scss
            _icons.scss
            _normalize.scss
            _type.scss
        _globals.scss
        _naming.scss
        _functions.scss
        _mixins.scss
        _vr.scss
    templates/
        app-minimal/
        app-basic/
        module/
    .gitignore
    LICENSE
    README.md

`docs/` - contains ELEMENT's step by step documentation<br/>
`docs/module` - contains module's line by line explanations and usage example<br/>
`framework/` - framework files<br/>
`framework/_naming.scss` - contains big amount of predefined class prefixes/names<br/>
`framework/_globals.scss` - contains all global variables<br/>
`framework/_mixins.scss` - contains all general mixins<br/>
`framework/_functions.scss` - contains all general functions<br/>
`framework/_vr.scss` - contains vertical rhythm mixins and functions that provide vertical synchronization feature<br/>
`framework/modules/` - contains logical separated modules<br/> 
// наверное надо будет описать все что внутри папки /modules?
`templates/` - contains variety of useful templates<br/>
`templates/app-minimal/` - minimal app template<br/>
`templates/app-basic/` - basic app template<br/>
`templates/module/` - module template<br/>
`.gitignore` - file using by [git](http://en.wikipedia.org/wiki/Git_(software)) to exclude tracking unnecessary files<br/>
`LICENSE` - licence terms and conditions<br/>
`README.md` - brief documentation (pieces of text from main documentation)<br/>

`*` - symbol means any file or any name of files<br/>
`_file-name` - fist symbol means that file shouldn't be compiled into css file and it is just auxiliary/child file<br/>
`.md` - extension means that file uses markdown syntax (like wiki markup)<br/>
`.scss` - extension means that file uses SCSS syntax of SASS preprocessor

##Logic
ELEMENT has three step to make your app GUI unique:

1. **Tag initialization (normalize).** The module ``modules/_normalize.scss`` responsible for initiating particular [category of tags](http://www.w3schools.com/tags/ref_byfunc.asp). Hence it covers almost all HTML tags like html, body, form, legend, input, button, etc. What is normalizing? Tag initiating or normalizing means resetting tags into unified view between different browsers.
2. **Typography.** After tags are initiated we can configure typography. The module ``modules/_type.scss`` responsible for this job. What is typography (abbreviated as *type*)? Typography is a process of arranging type into a legible and aesthetic appearance with appropriate layout. To put it bluntly, we include our custom font, setting font-size, font-family, line-height etc in the right place and in the right units to make web type not only beautiful, but also responsible.
3. **Class generating.** The last one we need is generating classes to bring our desirable styling into reality. At this point the ELEMENT is completely different from other frameworks. The idea is not create structure under your styles, like ``.header``, ``.header__nav``, ``.footer__nav--link`` etc but generate classes at the high level of Object Oriented ideology. To put it simply, create classes like ``.shadow-out``, ``.padding-sm``, ``.border-blue`` and then apply to necessary tags. Yea, it is force you create a huge amount of classes and use them, but at the same time it gives you maximum flexibility.

##Modules
Module is the most important component of the framework.
Each file within the framework folder has unified structure. It makes easier to read existing files (modules) and create new one. You can get initial module template under [templates/module](https://github.com/kalopsia/element/tree/master/templates/module) folder. Line by line explanation and its brief using example you can find under [docs/module](https://github.com/kalopsia/element/tree/master/docs/module) directory.

To understand what is module and how to start using framework, please go to the next chapter.

---

####Please, help us improve these docs!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.
