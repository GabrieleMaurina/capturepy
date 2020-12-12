# capturepy

Capturepy captures the standard output and the standard error of functions, methods and any blocks of code. It is useful when testing, debugging and working with libraries.

### Install

`pip install capturepy`

It requires python 3.8 or higher.

### Usage

See the examples.py file for a complete list of examples.

This module is based on the class Capture, which can be use as a decorator, or with the 'with' statement.

Here are some examples:

##### Capturing output of function
```python
from capturepy import Capture
print('Capture stdout and stderr of function using the Capture decorator.')

@Capture
def my_func(x):
	print('first')
	print('second', end='', file=sys.stderr)
	return x**2

output, result = my_func(4)
print('The captured output is:')
print(output)
print('The function returned:')
print(result)
```

##### Capturing only standard error of code using "with" statement
```python
from capturepy import Capture
print('Capture only stderr of code using the "with" statement.')

with Capture(stdout=False) as capture:
	print('first')
	print('second', end='', file=sys.stderr)
	stderr = capture.get()

print('The captured stderr is:')
print(stderr)
```
