#CSS-ELEMENT CONVENTIONS
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

To create really convenient and reusable styles we should follow some rules. Since the main idea of ELEMENT is using a big amount of classes we take care about class naming and make it logical, intuitive and "ease of remembering" as much as possible. Thus far all classes that you will generate should obey to some rules. Most of all conventions came from best practice in creating styles.

For simplification and standardization purposes CSS property prefixes conventions are already defined in the ELEMENT itself. **Full list of available properties' abbreviations** available in ``_naming.scss`` file. This file can be imported anywhere and used for standardized and concise class names.

##CSS Naming Conventions
###General Conventions

**All class names must be lowercase**

**Common keyword values that apply to all properties abbreviated as four first letters:**
 - `inhe` = `inherit`
 - `init` = `initial`

Examples:
```
| property-name:          | value;          | class name
  font:                     initial;          .fnt-init
  animation:                inherit;          .anm-inhe
```

**We should avoid using big amount of digits in class names and use size names instead:**

The most descriptive, mature and convenient set of names for this purposes are presented below:
  - `xxsm` = the smallest value
  - `xsm` = smaller value
  - `sm` = small value
  - `md` = medium value
  - `lg` = large value
  - `xlg` = larger value
  - `xxlg` = the largest value
  
If the above set is not enough we can use:
  - `min` = smaller than `xxsm`
  - `max` = larger than `xxlg`
  
Examples:
```
| property-name:          | value;          | class name
  width:                    0;                .wdt-0
  width:                    0.25rem;          .wdt-xxsm
  width:                    0.5rem;           .wdt-xsm
  width:                    1rem;             .wdt-sm
  margin:                   180px;            .mrg-xlg
  padding:                  180px;            .pdd-xlg
```

This set of names can be used in many cases:
  - top, right, bottom, left
  - width, height
  - z-index
  - margin, padding
  - font-size, line-height
  - border (line thickness)
  - amount of opacity
  - amount of alpha chanel in RGBA\HSLA colors <br>
  etc
  

###CSS Properties

**Words indicating directions of properties abbreviate as first letter of direction and must be always presented in class name:**

  - `t` = top
  - `r` = right
  - `b` = bottom
  - `l` = left
  - `tl` = top-left
  - `tr` = top-right
  - `br` = bottom-right
  - `bl` = bottom-left

Examples:
```
| property-name:          | value;          | class name
  top:                      0;                .t-0
  right:                    0;                .r-0
  border-left:              0;                .brd-l-0
  border-top-right-radius:  0;                .brr-tr-0
```


**Properties abbreviate as one ... + full name of value:**
[todo]

Examples:
```
| property-name:          | value;          | class name
  word-break:               all-break;        .wrb-all-break
  overflow-y:               auto;             .ovr-y-auto
  margin-right:             auto;             .mrg-r-auto
  vertical-align:           center;           .vra-center
```

###CSS Values
[todo]


###CSS Measurement Values

**Measurement values abbreviate as sign(positive have no prefix and negative have "n" prefix) + digits + two letter from CSS unit's name:**

Relative length units
  - Parent-relative length:
    - `` % (percentage)
  
  - Font-relative lengths:
    - `re` = rem
    - `em` = em
    - `ex` = ex
    
  - Viewport-percentage lengths
    - `vh` = vh (1% of the height of the viewport)
    - `vw` = vw (1% of the width of the viewport)
    - `vn` = vmin (1% of the minimum value between height and width of the viewport)
    - `vx` = vmax (1% of the maximum value between height and width of the viewport)

Absolute length units
  - `px` = px (pixel)
  - `cm` = cm (centimeter)
  - `mm` = mm (millimeter)
  - `in` = in (one inch = 2.54 centimeters)
  - `pt` = pt (one point = 1/72 of an inch)
  - `pc` = pc (one pica = 12 points)

Examples:
```
| property-name:          | value;          | class name
  any-property:             0;                .classname-0
  any-property:             10%;              .classname-10
  any-property:             -10%;             .classname-n10
  any-property:             10px;             .classname-10px
  any-property:             -10px;            .classname-n10px
  any-property:             10rem;            .classname-10re
  any-property:             -10rem;           .classname-n10re
```

###CSS Color Values

**Basic color keywords values abbreviated as `k` letter + name of keyword (or shortened version):**

  - `kccolor` = `currentColor` value
  - `ktrans` = `transparent` value
  - `kgreen` = for one word keyword colors like `Green`,`Red`, `Blue` we make no abbreviation and write full name
  - `kdarkoli` = for long keyword colors like `[Dark][Oli]veGreen` we get only 4 first letters from first word and 3 from second <br>
  *Full list of keyword color available [here](http://www.w3schools.com/cssref/css_colornames.asp).*

Examples:
```
| property-name:          | value;          | class name
  color:                    currentColor;     .c-kccolor
  color:                    transparent;      .c-ktrans
  color:                    red;              .c-kred
  color:                    CadetBlue;        .c-kcadblu
```

**Numerical color values abbreviated as one letter(type of color) + name of color's visual sense + name of alpha channel (if presented):**

  - Hex color values: **no prefix + name of visual sense** 
  - RGB and RGBA color values: **`r` + name of visual sense + alpha channel**
  - HSL and HSLA color values are prefixed by `h` letter
  
Examples:
```
| property-name:          | value;          | class name
  background-color:         #222;             .bck-co-black
  background-color:         rgba(0,0,0,0.3);  .bck-co-rblack_s
  background-color:         hsl(0,0,0,1);     .bck-co-hblack
```

For alpha channel we use size names (see the beginning of the page). See example:
```
| property-name:          | value;          | class name
  color:                    rgba(0,0,0,0);    .c-rblack_
  color:                    rgba(0,0,0,0.3);  .c-rblack_s
  color:                    rgba(0,0,0,0.5);  .c-rblack_m
  color:                    rgba(0,0,0,0.8);  .c-rblack_l
  color:                    hsl(0,0,0,1);     .c-rblack
```


###CSS Complex Values

**For complex CSS values there is no strict rules**

As a rule we abbreviate complex values as one general and demonstrative word. For example:
```
| property-name:          | value;                              | class name
  box-shadow:               0 1px 4px rgba(0, 0, 0, 0.3),
                            0 0 40px rgba(0, 0, 0, 0.1) inset;    .bxsh-effectname
```

##Variable Naming Conventions

**Variables should be namespaced**

Let's be less verbose and just see some examples:
```
| variable-name:          | value;
  $hex-dark:                #333;
  $hex-light:               #fdfdfd;
  $rgb-dark:                rgb(10,10,10);
  $rgb-light:               rgb(200,200,200);
  $button-sm:               50px;
  $button-lg:               150px;
```
As you can every variable has it own namespace/prefix. Just make sure that every set of related variables have its own unified namespace/prefix. As a rule we set namespace according to filename of components. For example component `_grid.scss` contains variables all start with `$grid-*` etc.


##Why we should follow naming rules and use standardized class prefixes?
Standardized names and rules are very important for the several reasons:

  1. We can reuse our own sets of classes in new projects with few changes.
  2. We can share sets of classes to different people like snippets.
  3. It is increase readability of our code for ourselves and other people.
  4. Standardized names make it possible to create themes and share it.

---

####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.