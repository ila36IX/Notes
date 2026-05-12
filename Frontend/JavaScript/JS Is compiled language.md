
# The flow of a JS source program

![](https://i.imgur.com/llRc3cs.png)

1. After a program leaves a developer’s editor, it gets transpired by Babel, then packed by Webpack (and perhaps half a dozen other build processes), then it gets delivered in that very different form to a JS engine. 
2. The JS engine parses the code to an AST. 
3. Then the engine converts that AST to a kind-of byte code, a binary intermediate representation (IR), which is then refined/converted even further by the optimizing JIT compiler.
4. Finally, the JS VM executes the program.