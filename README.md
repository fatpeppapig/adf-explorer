# ADF Explorer

- author: Cezary Falba <cezary@falba.net>
- license: GNU Public License V2

## Short Description

ADF Explorer is a simple tool that allows you to create and browse ADF [(Amiga Disk Format)](https://en.wikipedia.org/wiki/Amiga_Disk_File) files.
It is largely based on [Amitools](https://amitools.readthedocs.io/en/latest/) only providing basic PyQT based GUI.
Currently free icons from [Icons8](https://icons8.com) are used for toolbar and files/folders in a browser.
For simple deployments I'm using [pyinstaller](https://www.pyinstaller.org).

## Working with source

To play with the source, all you need to have installed on your machine is:

- Python 3.8
- Pipenv

## Running from source

All you need to do is run:
`pip install -r requirements.txt`
`python main.py`

## Building executables yourself

To build the application on your own, you will need:
`pip install -r requirements.txt`
`pyinstaller main.py`
