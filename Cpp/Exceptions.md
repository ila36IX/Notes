## Catch by reference

The main reason is to prevent object slicing.

```cpp
#include <iostream>
#include <string>
#include <exception>

class SpecialException : public std::exception { // 1
public:
    virtual const char* what() const throw() {
       return "SpecialException";
    }
};

void a() {
    try {
        throw SpecialException(); // 2
    } catch (std::exception e) { // 3
        // std::cout << "exception caught in a(): " << e.what() << '\n';
        throw; // 4
    }
}

int main () {
    try {
        a();
    } catch (const std::exception &e) { //5
        // std::cout << "exception caught in main(): " << e.what() << '\n';
    }
}
```

This will log:

```cpp
exception caught in a(): std::exception
exception caught in main(): SpecialException
```

Which mean its necessary to catch exceptions by reference to avoid compiler doing optimizations and slicing  parts from the original exception. 

When you rethrow an exception simply by calling `throw;`, it will rethrow the original exception. There is no move, no copy taking place, if you’d check the address of the exception from catch to catch it would be the same - that’s something impossible if you caught by value as it already makes a copy. And here lies the point. Catching by value makes a copy of the exception. But you don’t rethrow the copy. You rethrow the original exception that was copied

## Exception swallower 

 Exception swallower is an anti-pattern where an exception is caught but neither handled nor re-thrown, causing the program to fail silently.
 
```cpp
try {
    do_something();
} catch (...) {
    // Exception caught and ignored
}
```

## Stack unwinding

Stack unwinding is the process of removing function call frames from the call stack at runtime. During this process, local objects are destroyed in the reverse order of their creation.  **This guarantees cleanup of stack-based resources**.

Stack unwinding happens:

- Normally, when a function returns.
- During *exception* handling, when an exception is thrown and control transfers to a matching catch block.

The process will be terminated if an exception have been thrown during stack unwinding.


