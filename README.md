**Please, do not read the text below. Readme under heavy development.**

# Element - CSS/GUI framework
<sub>First of all, I'm sorry for the language mistakes I've made - I'm from Russia.</sub>

##Preface
Element is based on [SCSS](sass-lang.com) preprocessor. If you use plain CSS to make your styles, you will love preprocessors, particularly SCSS.

**What is SCSS?**

**SCSS** is CSS preprocessor that make it possible to inject into CSS some "*programming*" features/techniques like  **variables, functions, if/else statements** and so on. Preprocessor is program that simple convert files with the extension .scss into .css. For example: 
```
#styles.scss
$black: #000;
$black-postfix: black;

.text-#{$black-postfix} {
  color: $black;
}
``` 
compiles to
```
#styles.css
.text-black {
  color: #000;
}
```

**What do I need to know before using?**
Please, before using or reading the source code you need to learn some basics of SASS(SCSS) and know CSS3 basics (@media, @font-face rules, etc). 
Otherwise you will experience difficulties in understanding principles of work and efficiency.

##Get started


###Principles/Features of the ELEMENT:
1. Modulness
2. Flexibility & Deep customization
3. Best practices
4. Logical naming

## File structure
.md extension means markdown syntax to style text on the web.

