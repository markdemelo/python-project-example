# Publishing (Perfect) Python Packages on PyPi

Based on material from @Judy2k

[https://www.youtube.com/watch?v=GIF3LaRqgXo](https://www.youtube.com/watch?v=GIF3LaRqgXo)

[](bit.ly/perfectpypi)

## Project structure for packaging

The following sections outline the components of a typical package, relative to the package root.

### /src/package

place packages inside /src

### /setup.py

```python
# simple example
from setuptools import setup 
setup(
	name='helloworld',
	version='0.0.1',
	description='Say hello!',
	py_modules=["helloworld"],
	package_dir={'': 'src'},
)
```

```python
# add classifiers for referencing in git, pypi
setup(
...
	classifiers=[
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"License :: OSI Approved :: GNU General Public
	License v2 or later (GPLv2+)",
	"Operating System :: OS Independent",
	],
)
```

library dependencies

```python
setup(
...
# add dependencies to setup.py
	install_requires = [
	"blessings ~= 1.7",
	],
#  add development dependencies
	extras_require = {
		"dev": [
		"pytest>=3.7",
		],
	},
)
```

### /README.md

```markdown
# Hello World
This is an example project demonstrating how to publish a
python module to PyPI.

## Installation
Run the following to install:
```python
pip install helloworld
```

Add to setup.py:

```python
# add long description based on readme file
with open("README.md", "r") as fh:
	long_description = fh.read()
```

### /LICENCE

[Choose an open source license](https://choosealicense.com/)

### /requirements.txt

- is for Apps being deployed on machines you control.
- Uses fixed version numbers, eg: requests==2.22.0
- Is generated with pip freeze > requirements.txt

### /.gitignore

[gitignore.io](http://gitignore.io)

## Install locally
Run this to install locally and to update the package when modified.  

```
$ pip install -e .

Obtaining file:///path/to/helloworld
Installing collected packages: helloworld
Running setup.py develop for helloworld
Successfully installed helloworld
```

## Test setup

```
$ python setup.py bdist_wheel
running bdist_wheel
…
copying src/helloworld.py -> build/lib
…
creating ‘/path/to/helloworld/dist/
helloworld-0.0.1-py3-none-any.whl’ and adding
'.' to it
removing build/bdist.macosx-10.11-x86_64/wheel
```

## Source Distribution

```
$ python setup.py sdist
running sdist
...
warning: check: missing required meta-data: url
warning: check: missing meta-data: either (author and
author_email) or (maintainer and maintainer_email) must be
supplied
...
Creating tar archive
removing 'helloworld-0.0.1' (and everything under it)
```

```python
# update setup.py
setup(
...
url="https://github.com/judy2k/helloworld",
author="Mark Smith",
author_email="mark.smith@vonage.com",
)
```

## Check manifest

run the following to add LICENSE and test files to distribution

```
$ pip install check-manifest
$ check-manifest --create
$ git add MANIFEST.in
```

## Build It

```
$ python [setup.py](http://setup.py/) bdist_wheel sdist

$ ls dist/
helloworld-0.0.1-py3-none-any.whl
helloworld-0.0.1.tar.gz
```

# Cookiecutter

Automated template for creation of a package structure

[https://github.com/ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)

```
$ pip install cookiecutter
$ cookiecutter gh:ionelmc/cookiecutter-pylibrary  

... Lots of questions ...
... Copy in your code and tests ...
... Some minor file tweaks ...
... DONE!
```