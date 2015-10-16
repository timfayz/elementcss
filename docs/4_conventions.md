#CSS-ELEMENT CONVENTIONS
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

To create really convenient and reusable styles we should follow some rules. Since the main idea of ELEMENT is using a big amount of classes we take care about class naming and make it logical, intuitive and "ease of remembering" as much as possible. Thus far all classes that you will generate should obey to some rules. Most of all conventions came from best practice in creating styles.

For simplification and standardization purposes general conventions are already defined in the ELEMENT itself. **Full list of available abbreviations** are presented in the examples below available under ``framework/_naming.scss``. This file can be imported anywhere and used for creating standardized class names.

##CSS Naming Conventions
###General Conventions

**All class names must be lowercase**

Examples:
```
| property-name:          | value;          | class name
  long-property-name:       a value;          .long-name-value
```

**Common keyword values that apply to all properties abbreviated as four first letters:**
 - `inhe` = `inherit`
 - `init` = `initial`

Examples:
```
| property-name:          | value;          | class name
  box-shadow:               initial;          .shadow-init
  transition:               inherit;          .shadow-inhe
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
  width:                    0;                .width-0
  width:                    0.25rem;          .width-xxsm
  width:                    0.5rem;           .width-xsm
  width:                    1rem;             .width-sm
  margin:                   180px;            .marg-xlg
  padding:                  180px;            .padd-xlg
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
  top:                      0;                .top-0
  right:                    0;                .right-0
  border-top:               0;                .border-t-0
  border-top-right-radius:  0;                .radius-tr-0
```

Exceptions:
  * The properties `top`, `right`, `bottom`, `left` are not abbreviated.


**Properties with a string values abbreviate as one word of property (or shortened version) + full name of value:**

Examples:
```
| property-name:          | value;          | class name
  word-break:               all-break;        .word-all-break
  overflow-y:               auto;             .over-y-auto
  margin-right:             auto;             .marg-r-auto
  vertical-align:           center;           .vertical-center
  text-align:               center;           .text-center
```


**The most popular and frequently used properties with a demonstrative string values have no abbreviation. Instead, we just use full name of these values without property shorthand:**

Examples:
```
| property-name:          | value;          | class name
  display:                  block;            .block
  position:                 absolute;         .absolute
  visibility:               visible;          .visible
```

Exception:
  * For hypothetical cases where you may need to apply classes with the same values, eg `display: inherit;` and `position: inherit`. Just prefix four first letters of these properties like `.disp-inherit` and `posi-inherit`.


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
  color:                    currentColor;     .color-kccolor
  color:                    transparent;      .color-ktrans
  color:                    red;              .color-kred
  color:                    CadetBlue;        .color-kcadblu
```

**Numerical color values abbreviated as one letter(type of color) + name of color's visual sense + name of alpha channel (if presented):**

  - Hex color values: **no prefix + name of visual sense** 
  - RGB and RGBA color values: **`r` + name of visual sense + alpha channel**
  - HSL and HSLA color values are prefixed by `h` letter
  
Examples:
```
| property-name:          | value;          | class name
  background-color:         #222;             .back-clr-black
  background-color:         rgba(0,0,0,0.3);  .back-clr-rblack_s
  background-color:         hsl(0,0,0,1);     .back-clr-hblack
```

For alpha channel we use size names (see the beginning of the page). See example:
```
| property-name:          | value;          | class name
  color:                    rgba(0,0,0,0);    .color-rblack_
  color:                    rgba(0,0,0,0.3);  .color-rblack_s
  color:                    rgba(0,0,0,0.5);  .color-rblack_m
  color:                    rgba(0,0,0,0.8);  .color-rblack_l
  color:                    hsl(0,0,0,1);     .color-rblack
```


###CSS Complex Values

**For complex CSS values there is no strict rules**

As a rule we abbreviate complex values as one general and demonstrative word. For example:
```
| property-name:          | value;                              | class name
  box-shadow:               0 1px 4px rgba(0, 0, 0, 0.3),
                            0 0 40px rgba(0, 0, 0, 0.1) inset;    .shadow-effectname
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
As you can every variable has it own namespace/prefix. Just make sure that every set of related variables have its own unified namespace/prefix. As a rule we set namespace according to filename of components. For example component `_grid.scss` contains variables start with `$grid-*` etc.

TODO:
- project structure conventions


##Why we should follow naming rules and use standardized class prefixes?
Standardized names and rules are very important for the several reasons:

  1. We can reuse our own sets of classes in new projects with few changes.
  2. We can share sets of classes to different people like snippets.
  3. It is increase readability of our code for ourselves and other people.
  4. Standardized names make it possible to create themes and share it.

---

####Let's do something better together!
Start new issue [here](https://github.com/kalopsia/element/issues/new) if you have found mistake or have any questions, suggestions and problems.