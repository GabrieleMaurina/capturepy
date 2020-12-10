#!/usr/bin/env python

import setuptools
import output_capture

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='output_capture',
	version=output_capture.__version__,
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='output_capture captures the standard output and the standard error of functions, methods and any blocks of code. It is useful when testing, debugging and working with libraries. Find out more at https://github.com/GabrieleMaurina/output_capture.'
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/capture_output',
	licence='MIT',
	py_modules=['capture_output'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
