Use mutable data mamber to fix constness constrains

Manually initialize objects of built-in type, because C++ only sometimes
initializes them itself.

In a constructor, prefer use of the member initialization list to as signment
inside the body of the constructor. List data members in the initialization
list in the same order they’re declared in the class.

Avoid initialization order problems across translation units by re placing
non-local static objects with local static objects.

To disallow functionality automatically provided by compilers, declare the
corresponding member functions private and give no implementations. Using a
base class like Uncopyable is one way to do this.
