#!/usr/bin/env python

'''
Capturepy captures the standard output and the standard error of functions, methods and any blocks of code. It is useful when testing, debugging and working with libraries. Find out more at https://github.com/GabrieleMaurina/capturepy.
'''

import sys
from io import StringIO
from functools import partial

__author__ = 'Gabriele Maurina'
__copyright__ = 'Copyright 2020, Gabriele Maurina'
__credits__ = 'Gabriele Maurina'
__license__ = 'MIT'
__version__ = '1.0.3'
__maintainer__ = 'Gabriele Maurina'
__email__ = 'gabrielemaurina95@gmail.com'
__status__ = 'Production'

class Capture:
	'''
	A class to decorate functions and methods to capture their standard output and standard error.
	'''
	def __init__(self, function=None, stdout=True, stderr=True):
		self.function = function
		self.stdout = stdout
		self.stderr = stderr
		self.__stdout = sys.stdout
		self.__stderr = sys.stderr
		self.__string = StringIO()

	def __call__(self, *args, **kwargs):
		if self.function:
			self.start()
			res = self.function(*args, **kwargs)
			self.stop()
			return self.get(), res
		else:
			self.function = args[0]
			return self

	def start(self):
		'''
		Starts capturing the output.
		'''
		self.__string = StringIO()
		if self.stdout:
			self.__stdout = sys.stdout
			sys.stdout = self.__string
		if self.stderr:
			self.__stderr = sys.stderr
			sys.stderr = self.__string

	def stop(self):
		'''
		Stops capturing the output.
		'''
		if self.stdout: sys.stdout = self.__stdout
		if self.stderr: sys.stderr = self.__stderr

	def get(self):
		'''
		Returns captured string.
		'''
		return self.__string.getvalue()

	def __enter__(self):
		self.start()
		return self

	def __exit__(self, *_):
		self.stop()
	
	def __get__(self, instance, owner=None):
		return partial(self.__call__, instance)

if __name__ == '__main__':
	help(__import__(__name__))
