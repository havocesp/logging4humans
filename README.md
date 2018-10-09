# Logging4Humans

 - Author: Daniel J. Umpierez
 - License: MIT
 - Version: 0.1.1

## Description

Logging4Humans is a Python 3 application logging library designed
for humans beans.

## Installation
### Using `pip`

```sh
# `pip` command by supplying the github project repo URL.
$ pip install --process-dependencies-link git+https://github.com/havocesp/logging4humans
```



## Usage

```py
>>> from logging4humans import Logger
>>> log = Logger('app', 'INFO')
>>> log.info('Starting application ...')
"[Oct-23 23:10:04][app][INFO] Starting application ..."
```

## Changelog

Project history changes.

### 0.1.1
 - Added `.gitignore` file to project.
 - Fixed Logger import error from root "logging4hummans" package.

### 0.1.0

 - Initial version.

## TODO
 - [ ] Show diff between refreshes.

