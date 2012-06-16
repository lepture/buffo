#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup
install_requires = []
try:
    import argparse  # python 2.7+ support argparse
except ImportError:
    install_requires.append('argparse')


import buffo
from email.utils import parseaddr
author, author_email = parseaddr(buffo.__author__)

setup(
    name='buffo',
    version=buffo.__version__,
    author=author,
    author_email=author_email,
    url=buffo.__homepage__,
    packages=['buffo'],
    description='FTP Library for human',
    license='BSD License',
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    **kwargs
)
