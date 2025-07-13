# Lexer

![Imgur](https://i.imgur.com/pVV17oz.png)

The lexer is responsible for taking raw input string `"ls -l /home"` and breaking it down into these meaningful tokens such as:

- **Operators**: `|`, `>>`, `<<`, `&&`, `||`, `>`, `<`
- **Words**: Any sequence of characters not identified as an operator or special delimiter.
- **Quoted Strings**: Handles both double (`"..."`) and single (`'...'`) quoted strings, preserving their content.

## Tests

**Note:** Your source code must not contain any `main` function.

```sh
cd tests
make all # to run all tests
make lexer # to test only the lexer
# more command is comming
```

Available tests are:

`make lexer`: Check if the lexer is producing the expected tokens with expected length and type and white space surrounded  