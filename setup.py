#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-textual-snapshot',
    version='0.1.0',
    author='Darren Burns',
    author_email='darren@textualize.io',
    maintainer='Darren Burns',
    maintainer_email='darren@textualize.io',
    license='MIT',
    url='https://github.com/darrenburns/pytest-textual-snapshot',
    description='Snapshot testing for Textual apps',
    long_description=read('README.md'),
    py_modules=['pytest_textual_snapshot'],
    python_requires='>=3.6',
    install_requires=[
        'pytest>=7.0.0',
        'rich>=12.0.0',
        'textual>=0.28.0',
        'syrupy>=3.0.0',
        'jinja2>=3.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'textual-snapshot = pytest_textual_snapshot',
        ],
    },
)
