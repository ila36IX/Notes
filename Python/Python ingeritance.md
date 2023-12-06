

![](https://media.tenor.com/1SwdfIZZkx4AAAAd/wes-dst.gif)

# Attributes Function

## `setattr`:

- **Syntax:** `setattr(object, name, value)`

- **Usage:**
  - Sets the attribute with the given name on the specified object.
  - Useful for dynamically adding attributes during runtime.

- **Example:**
  ```python
  setattr(obj, 'new_attribute', 42)
  ```

## `getattr`:

- **Syntax:** `getattr(object, name[, default])`

- **Usage:**
  - Gets the value of the attribute with the given name from the specified object.
  - Allows optional default value if the attribute is not found.

- **Example:**
  ```python
  value = getattr(obj, 'existing_attribute', default_value)
  ```

## `hasattr`:

- **Syntax:** `hasattr(object, attribute)`

- **Usage:**
  - The hasattr() function returns True if the specified object has the specified attribute, otherwise False.

- **Example:**

  ```python
  x = hasattr(Person, 'age')
  ```

#### Note

> An instance with the attribute **__dict__** means that it can take other attributes using **setattr**. To check whether you can add a new attribute to an object before attempting to do so, you can use this way:

```python
if hasattr(obj, "__dict__"):
    # Now you have the right to add as many attributes as you want
```

## `__eq__` and `__ne__`

### Introduction:

In Python, `__eq__` and `__ne__` are special methods that define the behavior of equality and inequality comparisons for objects.

### `__eq__` (Equal):

- **Purpose:**
  - Defines the behavior of the equality operator `==`.

- **Usage:**
  - Override this method to customize how instances of a class are compared for equality.

- **Example:**
  ```python
  def __eq__(self, other):
      return self.attribute == other.attribute
  ```

### `__ne__` (Not Equal):

- **Purpose:**
  - Defines the behavior of the inequality operator `!=`.

- **Usage:**
  - Override this method to customize how instances of a class are compared for inequality.

- **Example:**
  ```python
  def __ne__(self, other):
      return self.attribute != other.attribute
  ```

### `__slots__`:

- **Purpose:**
  - Defines a tuple of attribute names that are allowed for instances of a class.

- **Usage:**
  - Limits the attributes a class instance can have to those specified in `__slots__`.
  - Improves memory usage compared to dynamically adding attributes.

- **Example:**
  ```python
  class MyClass:
      __slots__ = ('attribute1', 'attribute2')
  ```

## Inheritance:

```python
class Person:
    # ...

class Employee(Person):
    # ...
```

```python
class Bird:
    def flight(self):
        print("Most birds can fly.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
```

```python
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        # print(self.__c)  # Raises AttributeError
```