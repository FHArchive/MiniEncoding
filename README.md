[![Github top language](https://img.shields.io/github/languages/top/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[proj-id].svg?style=for-the-badge)](https://www.codacy.com/gh/FHPythonUtils/MiniEncoding)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/MiniEncoding.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/miniencoding.svg?style=for-the-badge)](https://pypi.org/project/miniencoding/)
[![PyPI Version](https://img.shields.io/pypi/v/miniencoding.svg?style=for-the-badge)](https://pypi.org/project/miniencoding/)

<!-- omit in TOC -->
# MiniEncoding

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">


Ascii representations. Stores ascii as a bitarray in ascii8 form.


## Encodings

### miniencoding.asciibytes AsciiBytes

| Encoding    |  To   | From  |
| :---------- | :---: | :---: |
| Ascii8      |   ✔   |   ✔   |
| Ascii7      |   ✔   |   ✔   |
| DecSixBit   |   ✔   |   ✔   |
| ICL*        |   ✔   |   ✔   |
| SixBitAscii |   ✔   |   ✔   |


```txt
* ↑ and	← not supported instead uses ^ and _
```

### miniencoding.tables

Encode to a charset with:
```python
def toCharset(charset, string, toUpper=False):
	"""Convert unicode text to various charsets using a lookup table

	Args:
		charset (string): lookup table
		string (string): unicode string to convert
		toUpper (bool, optional): Make chars uppercase before converting
		(intended for 6 bit charsets or charsets that do not support uppercase).
		Defaults to False.

	Returns:
		bytes: sequence of bytes (split into bits of length
	"""
```

Decode from a charset to Unicode with:
```python
def toUnicode(charset, bytestream):
	"""Convert text encoded with various charsets to unicode using a charset
	lookup table

	Args:
		charset (string): lookup table
		bytestream (bytes): sequence of bytes (split into bits of length
		log2(len(charset))) to convert

	Returns:
		string: unicode string
	"""
```

Available charsets (or make your own):
```python
# CDC 1604: Magnetic tape BCD codes
CDC1604_MAGTAPE
# CDC 1604: Punched card codes
CDC1604_PUNCHCARD
# CDC 1612: Printer codes (business applications)
CDC1612
# DEC SIXBIT
DEC_SIXBIT
# ECMA-1
EMCA1
# ICL Mainframes
ICL
# SixBit ASCII (used by AIS)
SIXBIT
# GOST 10859 § 6-bit code: with only Cyrillic upper case letters
GOST
# GSM 7-bit default alphabet and extension table of 3GPP TS 23.038 / GSM 03.38
GSM7
# ASCII
ASCII7
```

For more info see
https://en.wikipedia.org/wiki/Six-bit_character_code#Types_of_six-bit_codes

- [Encodings](#encodings)
	- [miniencoding.asciibytes AsciiBytes](#miniencodingasciibytes-asciibytes)
	- [miniencoding.tables](#miniencodingtables)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Download](#download-1)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Install With PIP

```python
pip install miniencoding
```

Head to https://pypi.org/project/miniencoding/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/MiniEncoding
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing
Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security
Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale
The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
