# Never Forget a Test

[See more](https://realpython.com/python-testing/)
#### [Cheat sheet](https://www.pythonsheets.com/notes/python-tests.html)

When you don't test all the possible cases that your program could face:

![](https://media.tenor.com/XRB_msTBnvcAAAAC/that-didnt-really-work-out-pretty-boy.gif)

Thankfully, we have `Doctest` and `unittest`.

---
## Writing Doctests

### Using the `testmod` Function

Doctests are written in the docstring of a function, method, or module. They look like interactive Python sessions. Here's an example:

```python
# File name: example.py

def add(a, b):
    """
    Function to add two numbers.

    Usage:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

The following line is used to set a condition for the script to run only when the script is run directly. When used as a module, the included script lines within this condition will not be interpreted.

```python
if __name__ == "__main__":
```

If you run `example.py` directly from the command line, [doctest](https://docs.python.org/3.4/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") works its magic:

```bash
python example.py
```

There’s no output! That’s normal, and it means all the examples worked. Pass `-v` to the script, and [doctest](https://docs.python.org/3.4/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") prints a detailed log of what it’s trying and prints a summary at the end:

```bash
python example.py -v
```

### Using the `testfile` Function

Sometimes, you might want to test code in a specific file. `testfile` allows you to do just that:

```python
# File name: example.py

import doctest  
if __name__ == "__main__":
    doctest.testfile("example_tests.txt")
```

```python
# File name: example_tests.txt

>>> from example import add
>>> add(5, 9)
14
>>> add(10, 119)
129
>>> add(8, "string")
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Tracebacks

These two snippets of Tracebacks are the same from the doctest perspective:

```python
# Snippet 1

Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/no/such/path/doctest_tracebacks.py", line 14, in this_raises
    raise RuntimeError('here is the error')
RuntimeError: here is the error

# Snippet 2
Traceback (most recent call last):
RuntimeError: here is the error
```

Why does it act like this? 
Simply because the entire body of the traceback is ignored by doctest.

### Working Around Whitespace

Look at that function that prints two lines separated by a blank line:

```python
def print_two_lines():
    """
    >>> print_two_lines()
    line 1

    line 2
    """
    print("line 1\nline 2")
```

Doctest interprets the blank line after the line containing `line 1` in the docstring as the end of the sample output. So, that will cause the test to fail (It expected two lines of output and it got one). To match the blank lines, replace them in the sample input with the string `<BLANKLINE>`. Based on that, the following code will not complain about any errors.

```python
def print_two_lines():
    """
    >>> print_two_lines()
    line 1
    <BLANKLINE>
    line 2
    """
    print("line 1\nline 2")
```

## Unittest

#### file organisation

Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`

First, you have to write your own function that will be tested. In our example, that function's name will be `divide`. Its purpose is to calculate the result of the division operation of two numbers. The following is the function code:

```python
def divide(a, b):
    return a / b
```

To test this function, we can use the `unittest` module. It needs to be imported into a separate file which will contain all the tests. Yes, it's that easy. Don't forget to grab some snacks and let's watch it do its MAGIC! as follows:

```python
# File name: test_divide 

from file_name import divide
import unittest

class TestName(unittest.TestCase):
    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(50, 5), 10)
        self.assertAlmostEqual(divide(1000, 1000), 1)
        self.assertRaises(ZeroDivisionError, divide, (1, 0))
        
        # This does the same as the line above, it is simpler
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
```

Note: _The test file should be named like: test_name.py or name_test.py_

Then run this command:

```bash
python3 -m unittest test_divide

# Or you can request an auto-discovery
python -m unittest discover
```

After running this command, the standard output will likely contain something like this:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

This is a good sign because the last word, `OK`, means everything went as expected. But let's change the `test_divide` file by adding another line to our `TestName` class:

```python
        self.assertRaises(ZeroDivisionError, divide, (1, 0))
        
        # This does the same as the line above, it is more simpler!
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
```

Finally, be aware of the function `setUp` which will initialize the variables that will be tested in every test method. Don't forget the DRY rule (Don't Repeat Yourself).

```python
def setUpModule():
        print("setup module")

def tearDownModule():
        print("teardown module")

class TestFib(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.n = 10
    def tearDown(self):
        print("tearDown")
        del self.n
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)
    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)
```
## Documentation

A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, method, or function.

This is the way to see a file's documentation:

```sh
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").module.method.__doc__)'
```

