#CSS-ELEMENT STRUCTURE
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

##File Structure
    docs/
        templates/
            app-basic/
            app-minimal/
        *.md
    components/
    _.scss
    _globals.scss
    _naming.scss
    _functions.scss
    _mixins.scss
    _vr.scss
    LICENSE
    README.md

`docs/*.md` - contains CSS-ELEMENT's step by step documentation<br/>
`docs/templates/` - contains variety of useful templates<br/>
`docs/templates/app-minimal/` - minimal app template<br/>
`docs/templates/app-basic/` - basic app template<br/>
`components/` - contains logical separated components are based on framework functionality<br/>
`_.scss` - core framework file, it imports all root files and used by built-in components<br/>
`_naming.scss` - contains big amount of predefined class prefixes/names<br/>
`_globals.scss` - contains global variables<br/>
`_mixins.scss` - contains general mixins<br/>
`_functions.scss` - contains general functions<br/>
`_vr.scss` - contains vertical rhythm mixin and function that provide vertical synchronization feature<br/>
`LICENSE` - licence terms and conditions<br/>
`README.md` - brief documentation (pieces of text from main documentation)<br/>

`*` - symbol means any file or any name of files<br/>
`_file-name.scss` - fist symbol _ means the file shouldn't be compiled into individual CSS file and it is just auxiliary/child part of another one<br/>
`.md` - extension means the file uses markdown syntax (like wiki markup)<br/>
`.scss` - extension means the file uses SCSS syntax of SASS preprocessor

##Logic
Despite the fact that CSS-ELEMENT already has basic well-designed components it doesn't mean you *must* (or it *necessary* to) use them. You can just include CSS-ELEMENT functionality by importing `_.scss` file and start to create your own tool/theme/framework using core mixins or functions. The idea of this project is not to *overwrite* your styles but to *extend* your existing project or create new one in CSS-ELEMENT way.

1. **Tag initialization (normalize).** The module ``modules/_normalize.scss`` responsible for initiating particular [category of tags](http://www.w3schools.com/tags/ref_byfunc.asp). Hence it covers almost all HTML tags like html, body, form, legend, input, button, etc. What is normalizing? Tag initiating or normalizing means resetting tags into unified view between different browsers.
2. **Typography.** After tags are initiated we can configure typography. The module ``modules/_type.scss`` responsible for this job. What is typography (abbreviated as *type*)? Typography is a process of arranging type into a legible and aesthetic appearance with appropriate layout. To put it bluntly, we include our custom font, setting font-size, font-family, line-height etc in the right place and in the right units to make web type not only beautiful, but also responsible.
3. **Class generating.** The last one we need is generating classes to bring our desirable styling into reality. At this point the ELEMENT is completely different from other frameworks. The idea is not create structure under your styles, like ``.header``, ``.header__nav``, ``.footer__nav--link`` etc but generate classes at the high level of Object Oriented ideology. To put it simply, create classes like ``.shadow-out``, ``.padding-sm``, ``.border-blue`` and then apply to necessary tags. Yea, it is force you create a huge amount of classes and use them, but at the same time it gives you maximum flexibility.



---

####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.
