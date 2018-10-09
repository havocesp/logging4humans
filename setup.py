# -*- coding: utf-8 -*-
from distutils.core import setup

import logging4humans as l4h

setup(
    name='logging4humans',
    version=l4h.__version__,
    packages=['logging4humans'],
    url=l4h.__site__,
    license=l4h.__license__,
    author=l4h.__author__,
    author_email=l4h.__email__,
    description=l4h.__description__,
    keywords=l4h.__keywords__
)
