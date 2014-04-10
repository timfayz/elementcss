#ELEMENT INSTALLATION [&laquo;back](https://github.com/kalopsia/element/blob/master/docs/0_preface.md)

To use ELEMENT efficiently and successfully we need to install some additional popular tools. Do not confuse about a huge amount of necessary software - don't hesitate, they certainly will be useful in future.<br/>
*Please, googling if you experience difficulties in installation.*

##Install SASS
SASS is written in Ruby, so we need to install Ruby first. Please, don't confuse about unawareness of Ruby or Ruby on Rails, it is not necessary for successfully using SASS and certainly ELEMENT. Let's start:
1. [Install Ruby](https://www.ruby-lang.org/en/installation/)
2. [Install SASS](http://sass-lang.com/install)
3. From now on you can use GUI **application** or **command line** to make compilations

##SASS Usage
First of all, create empty ``styles.scss`` file at the same place as if you create normal CSS file and write some SASS code into the file.<br/>
Next we need to make our first compilation from SASS to plain CSS. If you choose command line, the steps below is for you:

* Go to directory where ``styles.scss`` is placed:<br/>
	Windows: open the directory by file explorer, run ``Shift`` + ``Right Click`` at a pane and choose ``Open command line`` in the context menu<br/>
	Unix: open terminal, run ``cd path/to/directory``
* Run one of the following commands:<br/>
	``sass styles.scss styles.css`` - single compilation<br/>
	``sass styles.scss styles.css --style compressed`` - single compilation and minification<br/>
	``sass --watch styles.scss:styles.css`` - compilation on change without minification (recommended)<br/>

	If you are faced with ``LoadError: cannot load such file -- rb-inotify``<br/>
	Please, run ``gem install rb-inotify``

##Autoprefixer

##Gruntjs
Using command line and ``sass`` command quite enough, but for successfully using ELEMENT I recommend you to use [Gruntjs](http://gruntjs.com/getting-started) or GUI application like .... Gruntjs allows performing repetitive tasks like watching, compilation, minification and etc. Let's imagine we have styles.scss which need to be compiled after changes was made, then add [vendor prefixes](http://webdesign.about.com/od/css/a/css-vendor-prefixes.htm) and make compress (remove all indents, spaces and new line breaks). To do so we

* [Install Nodejs](http://nodejs.org/download/) (required for Gruntjs)
* [Install Gruntjs](http://gruntjs.com/getting-started)
* [Install Autoprefixer](https://github.com/nDmitry/grunt-autoprefixer) (Gruntjs' module)

1. [Download ELEMENT](https://github.com/kalopsia/element/archive/master.zip)
2. Extract the directory where you store your own styles
3. Choose initial app template under ``templates/`` folder. Copy contents of template to
3. Include CSS file into project: ``<link rel="stylesheet" type="text/css" href="path/to/styles.css">``

