##Installation
If you've never used the tools below, don't confuse about a huge amount of necessary software.<br/>
Do not hesitate, some of them will be useful in future<br/>
*Please, googling if you experience difficulties in installation.*

* [Download ELEMENT](https://github.com/kalopsia/element/archive/master.zip)
* Extract the directory where you store your own styles
* Include CSS file into project:
```HTML
	<head>
		...
		<link rel="stylesheet" type="text/css" href="path/to/styles.css">
		...
</head>
```
* [Install Ruby](https://www.ruby-lang.org/en/installation/) (required for SASS language)<br/>
	Please, don't confuse about unawareness of ruby/ruby on rails, it is not necessary*<br/> *for successfully using SASS and ELEMENT.*
* [Install SASS](http://sass-lang.com/install)
* From now on you can use GUI application or command line to make compilation

If you choose command line, the steps below for you:

* Go to directory where ``styles.scss`` is placed:<br/>
	Windows: ``Shift`` + ``Right Click`` in the directory and ``Open command line``<br/>
	Unix: ``cd path/to/directory``
* Run one of the following:<br/>
	``sass styles.scss styles.css`` - single compilation<br/>
	``sass --watch styles.scss:styles.css`` - compilation on change (recommended)<br/>
	``sass --watch styles.scss:styles.css --style compressed`` - compilation and minification on change<br/>
	If you have the following probelm ``LoadError: cannot load such file -- rb-inotify``. Please run:<br/>
	``sudo gem install rb-inotify``

Using command line and ``sass`` command quite enough, but for successfully using ELEMENT I recommend you to use [Gruntjs](http://gruntjs.com/getting-started). Gruntjs allows performing repetitive tasks like watching, compilation, minification and etc. For example, let's imagine that we have styles.scss file..

to make additional steps:
* [Install Nodejs](http://nodejs.org/download/) (required for Gruntjs)
* [Install Gruntjs](http://gruntjs.com/getting-started)
* [Install Autoprefixer](https://github.com/nDmitry/grunt-autoprefixer) (Gruntjs' module)
