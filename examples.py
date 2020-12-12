from capturepy import Capture
import sys




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
print()





print('Capture only stdout of function using the Capture decorator.')

@Capture(stderr=False)
def my_func():
	print('first', end='')
	print('second', file=sys.stderr)

stdout, result = my_func()
print('The captured stdout is:')
print(stdout)
print('The function returned:')
print(result)
print()





print('Separately capture stdout and stderr of function using the Capture decorator.')

@Capture(stderr=False)
@Capture(stdout=False)
def my_func():
	print('first', end='')
	print('second', end = '', file=sys.stderr)

stdout, (stderr, result) = my_func()
print('The captured stdout is:')
print(stdout)
print('The captured stderr is:')
print(stderr)
print('The function returned:')
print(result)
print()





print('Capture only stderr of code using the "with" statement.')

with Capture(stdout=False) as capture:
	print('first')
	print('second', end='', file=sys.stderr)
	stderr = capture.get()

print('The captured stderr is:')
print(stderr)
print()





print('Capture stdout and stderr of code using the Capture object.')

capture = Capture()
capture.start()
print('first')
print('second', end='', file=sys.stderr)
capture.stop()
print('The captured output is:')
print(capture.get())
print()





print('Capture stdout and stderr of function using the Capture object.')

def my_func(a, b):
	print('first')
	print('second', end='', file=sys.stderr)
	return a + b

capture = Capture(function=my_func)
output, result = capture(3, 5)
print('The captured output is:')
print(output)
print('The function returned:')
print(result)
print()





print('Capture only stdout of method using the Capture decorator.')

class Foo:
	def __init__(self, a):
		self.a = a
	@Capture(stderr=False)
	def foo(self, b):
		print('first', end='')
		print('second', file=sys.stderr)
		return self.a * b

stdout, result = Foo(3).foo(7)
print('The captured stdout is:')
print(stdout)
print('The method returned:')
print(result)
print()
