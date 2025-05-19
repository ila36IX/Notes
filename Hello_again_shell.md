
### Resources

- [Crafting Interpreters](https://craftinginterpreters.com/contents.html)
- [Implementing a Job Control Shell](https://www.gnu.org/software/libc/manual/html_mono/libc.html#Implementing-a-Shell)
- [Posix standereds for shell](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html)
- [POSIX Shell Tutorial](https://www.grymoire.com/Unix/Sh.html#uh-24)
- [POSIX Shell Tutorial](https://www.grymoire.com/Unix/Sh.html#uh-24)
- [The Architecture of BASH](https://aosabook.org/en/v1/bash.html)
- [Create an AST from bash in C](https://stackoverflow.com/questions/52666511/create-an-ast-from-bash-in-c)
- [Lexical analysis - Wikipedia](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Abstract syntax tree - Wikipedia](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Tutorial - Write a Shell in C • Stephen Brennan](https://brennan.io/2015/01/16/write-a-shell-in-c/)


- [Harvard: shell grammar](https://cs61.seas.harvard.edu/site/2021/Shell/#shell-grammar)


## 1. Lex

To create the shell, first we'll have to use a technique called __lexical analysis__ which  is the process of taking the raw input string `"ls -l /home"` and breaking it down into these meaningful `(token-type, token-value)` pairs.

Each of these pairs `(COMMAND, "ls")`, `(OPTION, "-l")`, and `(PATH, "/home")` – is a **lexical token**.

[__Lexical analysis__](https://www.youtube.com/watch?v=sJKFLcsysVs): breaking the input into individual words or __“tokens”__;
__Syntax analysis__: parsing the phrase structure of the program;
__Semantic analysis__: calculating the inputl;

TOKENS
```
BUILIN
COMMAND
PATH
REDIRECTION
PIPELINE
SQSTR
DQSTR
```

```bash
cat << EOF > file | wc -c | tr -d " " > file2
```

```bash
                         __ PIPELINE__
                     ___/              \____
                    /                       \
            COMMAND                    __ PIPELINE _
          /        \                  /             \
    ARGUMENTS   REDIRECTIONS      COMMAND         _ COMMAND __
        |          |     |           |           /            \
       cat        <<     >       ARGUMENTS    ARGUMENTS   REDIRECTIONS
                   |     |         |   |      |   |   |        |
                 "..."  file      wc  -c      tr  -d " "       >
                                                               |
                                                             file2
```


Symbol table:

| lexem                                           | Token class      |     |
| ----------------------------------------------- | ---------------- | --- |
| \|                                              | PIPE             |     |
| `>>`, `<<`,`>`.`<`                              | REDIRECTION      |     |
| `"Testing"`                                     | SINGLE_QUOTE_STR |     |
| `testing`                                       | DOUBLE_QUOTE_STR |     |
| `echo`,`cd`,`pwd`,`export`,`unset`,`env`,`exit` | KEYWORD          |     |
| word                                            | `abcdef`         |     |

quote 


```
$ echo testing > b is everything > c
$ cat b
testing is everything
$ cat c
testing is everything
```

```bash
|
||
&&
>> 
>
<
<<
"xxxx"
'xxxxx'
$xxxx
$?
echo
cd
pwd
export
unset
env
exit
*
```

```txt
commandline ::= (empty)
          |  conditional
          |  conditional ";" commandline
          |  conditional "&" commandline

conditional ::=  pipeline
          |   conditional "&&" pipeline
          |   conditional "||" pipeline

pipeline ::=  command
          |   pipeline "|" command

command  ::=  word
          |   redirection
          |   command word
          |   command redirection

redirection  ::=  redirectionop filename
redirectionop  ::=  "<"  |  ">"  |  ">>" | "<<"
```