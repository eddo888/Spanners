#!/usr/bin/env python

import codecs
from os import path
from setuptools import setup

pwd = path.abspath(path.dirname(__file__))
with open(path.join(pwd, 'README.md'), 'rb') as input:
    long_description = input.read()

version='1.0'
	
setup(
	name='Spanners',
	version=version,
	license='MIT',
    long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/eddo888/Spanners',
	download_url='https://github.com/eddo888/Spanners/archive/%s.tar.gz'%version,
	author='David Edson',
	author_email='eddo888@tpg.com.au',
	packages=[
		'Spanners',
	],
	install_requires=[
		'asciitree',
		'bs4',
		'arrow',
		'Baubles',
		'Perdy',
		'Argumental',
	],
	scripts=[
		'bin/squirrel.py',
		'bin/treeify.py',
	],
)
