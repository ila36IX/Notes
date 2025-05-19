
# Object-Oriented Programming

![](https://pythoncodeshark.files.wordpress.com/2014/01/oop-meme.jpg)

To get access to a private property, and get around encapsulation concept, use this:

```python
Base._Base__privateProperty = 69
```

## 1. Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm that uses objects and classes for organizing code. In OOP, objects are instances of classes, which encapsulate data and behavior. This paradigm promotes concepts like abstraction, encapsulation, inheritance, and polymorphism.

## 2. Class vs. Instance Attributes

In Python, classes are used to create objects. A class can have both class attributes and instance attributes. 

- **Class Attributes:** These attributes are shared by all instances of the class. They are defined inside the class but outside any class method.
  
  ```python
class MyClass:
	class_attribute = "I am a class attribute"
  ```

- **Instance Attributes:** These attributes are specific to each instance of the class. They are defined inside the class methods using the `self` keyword.

```python
class MyClass:
	def __init__(self, instance_attribute):
		self.instance_attribute = instance_attribute
```
## 3. Properties vs. Getters and Setters

In Python, properties, getters, and setters are techniques to control the access and modification of class attributes.

- **Properties:** Properties allow you to define getter, setter, and deleter methods using the `@property`, `@<attribute>.setter`, and `@<attribute>.deleter` decorators, respectively.

```python
class MyClass:
	def __init__(self, value):
		self._value = value
	@property
	def value(self):
		return self._valu
    @value.setter
    def value(self, new_value):
        self._value = new_value
```

- **Getters and Setters:** Getters and setters are traditional methods used for accessing and modifying attributes. They provide more control over attribute behavior.

  ```python
  class MyClass:
      def __init__(self, value):
          self._value = value

      def get_value(self):
          return self._value

      def set_value(self, new_value):
          self._value = new_value
  ```

## 4. Python's `str()` vs. `repr()`

In Python, `str()` and `repr()` are built-in functions used for producing a string representation of an object. They serve different purposes:

- **`str()`:** This function is used to create a user-friendly, readable string representation of an object. It's generally used for display purposes.

  ```python
  class MyClass:
      def __str__(self):
          return "This is a MyClass object"
  ```

- **`repr()`:** This function is used to create an unambiguous string representation of an object. It's mainly used for debugging and development purposes.

  ```python
  class MyClass:
      def __repr__(self):
          return "MyClass()"
  ```

Feel free to explore these concepts further and experiment with different implementations in your Python projects. Happy coding!
### Resources

- [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Python's str() vs. repr()](https://shipit.dev/posts/python-str-vs-repr.html)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)

---

