#!/usr/bin/env python

from distutils.core import setup, Command
import os
import os.path

setup(
    name='expiredict',
    version='3.0',
    description='Support Expire and Max length Dict',
    url='http://xiaorui.cc',
    author='ruifengyun',
    author_email='rfyiamcool@163.com',
    long_description=open('README.md').read(),
    packages=['expiredict'],
    license = "MIT",
    keywords = "Expire ttl Dict Max Dict author fengyun",
    classifiers = [
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
        ]
)
