#!/usr/bin/env python

from distutils.core import setup, Command
import os
import os.path

setup(
    name='expiredict',
    version='1.7',
    description='Support Expire and Max length Dict',
    url='http://xiaorui.cc',
    author='ruifengyun',
    author_email='rfyiamcool@163.com',
    long_description=open('README.md').read(),
    packages=['expiredict'],
)
