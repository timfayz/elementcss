#ELEMENT CONVENTIONS
**[Return to the beginning](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)**<br/>

For ease of remembering ELEMENT have a several important conventions. Most of all came from best practice in creating styles.

##Naming Conventions
Since the main idea of ELEMENT is using a big amount of To make class naming logical and intuitive all predefined classes obey to some rules:

**Words indicating directions of properties abbreviate as first letter of direction and must be always presented in class name:**

  - `t` (top)
  - `r` (right)
  - `b` (bottom)
  - `l` (left)
  - `tl` (top-left)
  - `tr` (top-right)
  - `br` (bottom-right)
  - `bl` (bottom-left) <br>
  *(!) However, the properties `top`, `right`, `bottom`, `left` are not abbreviated.*

Let's look at examples:

```
| property-name:          | value;          | class name
  top:                      auto;             .top-auto
  right:                    custom value;     .right-yourname
  border-top:               custom value;     .border-t-yourname
  border-top-right-radius:  custom value;     .radius-tr-yourname
```

**The most popular and frequently used properties with a limited number of string values have no abbreviation. Instead, it uses only full name of value without property name:**

Let's look at examples:

```
| property-name:          | value;          | class name
  display:                  block;            .block
  position:                 absolute;         .absolute
```

**Properties with a string values abbreviate as one word of property (or any shortened version) + full name of value:**

Let's look at examples:

```
| property-name:          | value;          | class name
  word-break:               all-break;        .word-all-break
  overflow-y:               auto;             .over-y-auto
  margin-right:             auto;             .marg-r-auto
  vertical-align:           center;           .vertical-center
  text-align:               center;           .text-center
```

Common values like `inherited`, `none`, `initial` also subject to this rule.

**Properties with a numeral values abbreviates as one word of property (or any shortened version) + something like this:**

  - `0    -> .classname-0`
  - `100% -> .classname-100`
  - `1rem -> .classname-sm`
  - `3rem -> .classname-md`
  - `6rem -> .classname-lg`

Let's look at examples:

```
| property-name:          | value;          | class name
  word-break:               all-break;        .word-all-break
  overflow-y:               auto;             .over-y-auto
  margin-right:             auto;             .marg-r-auto
  vertical-align:           center;           .vertical-center
  text-align:               center;           .text-center
```

For simplification and standardization many of predefined prefixes for properties are presented in `framework/_naming.scss` file. This file can be imported anywhere and used for creating standardized class names.