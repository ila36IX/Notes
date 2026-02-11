## Compile-Time Polymorphism (Static Binding)

Compile-time `polymorphism`, also known as early binding or static binding, occurs when the compiler determines which function or operation to invoke during the compilation phase. The compiler resolves the call based on the arguments passed or the template parameters provided.

There are two primary forms of static polymorphism in C++:

1. **Ad-hoc Polymorphism (Function/Operator Overloading):** Multiple functions share the same name but distinct signatures (parameter types or counts). The compiler selects the correct overload via overload resolution rules defined in the standard.

2. **Parametric Polymorphism (Templates):** Functions or classes are written generically. The compiler generates concrete implementations (instantiations) for each unique type used.

> The memory address of the function is determined at compile time.

## Run-Time Polymorphism (Dynamic Binding)

Run-time polymorphism, or late binding, occurs when the decision of which function to execute is deferred until the program is running. This is achieved through inheritance and virtual functions.

**Mechanism (The vtable):** To implement this, C++ compilers typically use a **Virtual Method Table (vtable)**.

1. Every class containing virtual functions has a hidden pointer, the `vptr`, which points to a static table of function pointers (the vtable) for that class.
    
2. When a virtual function is called through a base class pointer or reference, the program performs an indirection: it follows the object's `vptr` to the correct vtable and looks up the specific function address.

> The function address is resolved at runtime based on the actual type of the object pointed to, not the type of the pointer/reference.