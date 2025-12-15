## Keywords

### Copy constructor

```c++
A(A &)
```

__Super class__

__SubClass__

__Class visibility specifier__
(public, protected...)

__Class components__ 
All private and public entities of the class

__Class type compatibility__
- Objects of the subclass have at least the same capabilities as the superclass objects
- Objects of the superclass may not have the same capabilities as the subclass objects
- Objects of the superclass are compatible with objects of the subclass**
- Objects of the subclass are not compatible with objects of the superclass

__DownCasting__:  treat a pointer to a superclass (Pet) as a pointer to its subclass (Dog).
__UpperCasting__: Treat a pointer to a subclass (Dog) as a pointer to its superclass (Pet).

__Automatic variable__
Any ordinary-value/object that allocated in the stack.

```c++
std::string automatic_variable;
```
__Polymorphism__

The ability to present the same interface for differing underlying forms.
In cpp standard it refers to it in type theory by the provision of a single interface to entities of different types.

```cpp
class Instrument {
public:
    // "virtual" means: "Look at the actual object type at runtime"
    virtual void make_sound() = 0; 
};

class Guitar : public Instrument {
public:
    void make_sound() override { cout << "Strum\n"; }
};

class Piano : public Instrument {
public:
    void make_sound() override { cout << "Plink\n"; }
};

// The Polymorphism:
// This function can take Guitar object or Piano object
// and it will call the right method.
void play_sound(Instrument* inst) {
    inst->make_sound();
}
```

__Nominal Subtyping (strict Subtyping)__

In C++, the names of the types and their explicitly declared relationships (inheritance) matter most.

Interface inheritance: to allow different derived classes to be used interchangeably through
the interface provided by a common base class

In C++ Term this is often called Runtime Polymorphism or Dynamic Polymorphism.

Basically C++ wants to guarantee safety at compile time before the program runs.

Not for example python uses __Structural Subtyping (duck typing)__: the names don't matter. The relationships don't matter. Only the structure (the fact that you have a `.speak()` method) matters.

### Polymorphic type

A type with virtual functions is called a polymorphic type or (more precisely) a run-time polymorphic type.

```c++
class PolyType {
	virtual print() {
		std::cout << "This function can be override by its driven\n";
	}
}
```

### Virtual function table

Clearly, to implement polymorphism, the compiler must store some kind of type information in each object of class Employee and use it to call the right version of the virtual function print().
In a typical implementation, the space taken is just enough to hold a pointer the usual implementation technique is for the compiler to convert the name of a virtual function into an index into a table of pointers to functions. That table is usually called the virtual function table or simply the vtbl. Each class with virtual functions has its own vtbl identifying its virtual functions.