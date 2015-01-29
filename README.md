# JSONing
A multi purpose JSON desktop application, that allows to read, analyze and manipulate JSON documents.

## Features
* Pretty Printing / Minifiying
* Error Analysis
* Search Tools to find groups of matching elements
* Collapse/Expand view
* Selector interface for easier navigation/manipulation/collapsing
* Convert to/from yaml and xml
* Convert to/from Javascript object
* Multi Object File Parsing (with or without newline separation)
* Support for both ' and " style (and fix format option)

## Buidling
These are the instructions for developing and building on MacOSX. The app uses the PyGUI framework which you can download from here:
```http://www.cosc.canterbury.ac.nz/greg.ewing/python_gui/```
On OSX Yosemite the required PyObjC libraries should already be installed so this is the only library you need to install. To do so extract the downloaded tar into a directory and execute the following commands:
```
python configure.py
make
sudo make install
```
With this the library should be available as a system library and can be used in your projects.

## Running
To run the source code just execute ```python src/main.py```

## Distributing
The application can be built using py2app. You can install py2app using easy_install, pip, port, homebrew or even manually. Once py2app is install just run
```python setup.py py2app```
and you will have a working application located in the dist folder.
