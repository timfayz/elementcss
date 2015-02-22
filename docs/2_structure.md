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

<<<<<<< HEAD
1. **Tag initialization (normalize).** The module ``modules/_normalize.scss`` responsible for initiating particular [category of tags](http://www.w3schools.com/tags/ref_byfunc.asp). Hence it covers almost all HTML tags like html, body, form, legend, input, button, etc. What is normalizing? Tag initiating or normalizing means resetting tags into unified view between different browsers.
2. **Typography.** After tags are initiated we can configure typography. The module ``modules/_type.scss`` responsible for this job. What is typography (abbreviated as *type*)? Typography is a process of arranging type into a legible and aesthetic appearance with appropriate layout. To put it bluntly, we include our custom font, setting font-size, font-family, line-height etc in the right place and in the right units to make web type not only beautiful, but also responsible.
3. **Class generating.** The last one we need is generating classes to bring our desirable styling into reality. At this point the ELEMENT is completely different from other frameworks. The idea is not create structure under your styles, like ``.header``, ``.header__nav``, ``.footer__nav--link`` etc but generate classes at the high level of Object Oriented ideology. To put it simply, create classes like ``.shadow-out``, ``.padding-sm``, ``.border-blue`` and then apply to necessary tags. Yea, it is force you create a huge amount of classes and use them, but at the same time it gives you maximum flexibility.
=======
Let's consider two the most important steps that make GUI building with CSS-ELEMENT easy and very scalable:

1. **Tag initialization (normalize).** The component ``components/_normalize.scss`` responsible for initiating particular [category of HTML tags](http://www.w3schools.com/tags/ref_byfunc.asp) to the same general appearance. It covers almost all HTML tags like html, body, form, legend, input, button, etc. What is normalizing? HTML tag initiating or normalizing means applying styles that will make their appearance unified between different browsers. However in the context of CSS-ELEMENT normalize brings HTML tags to almost identical view/appearance so after we do normalize we can start to style them from scratch. The next step will use of different classes to *initiated* HTML tags. Let's bring our desired GUI into reality!
2. **Generating sets.** The last one we need is generating classes where *one class affects one CSS property* (ie *sets*). At this point the CSS-ELEMENT is completely different from other frameworks. The idea is not to start create classes similar to your like `.header`, `.header__nav`, `.footer__nav--link` etc early. Before we need to generate some amount of *sets* (like OOCSS) based on which we can apply them directly or extend into more generic classes (like are mentioned before). To put it simply, we will create *sets* like `.shadow-out`, `.padding-sm`, `.border-blue-thin`, `.color-white` and then apply them to necessary HTML tags or extend them to your favorite (and more generic) classes like `.header`, `.button`, `.field` etc.

##Components
Components are important part of the framework. Each file within the `components/` folder has unified structure. It makes easier to read existing files (components) and create new ones. At the moment we have 4 base components:

 * `_container.scss` - generate classes are intended to wrap and center its content according to @media queries you set.
 * `_grid.scss` - 
>>>>>>> 38a06e3... update repository to v1.5



---

<<<<<<< HEAD
####Please, help us improve these docs!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.
=======
####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.
>>>>>>> 38a06e3... update repository to v1.5
