[Vim Fundamentals](https://theprimeagen.github.io/vim-fundamentals/)
[Articles about Vim](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/table-of-contents)
## Registers

```
:h reg
```

To show what the content of the registers `args`:

```
:reg {args}
```

## Vim Tree default plugin

```
vim .
```

`:Ex`: Go back to tree view and live the buffer open
`:Vex`: Open tree in right
`:Sex`: open tree in under the current buffer

`<C-w>s`: -- split
`<C-w>`v: | split
`<C-w>`o: Open only this window and hide splits

## Motions

### f-motion

f{char}	 To the occurrence of {char} to the right. The cursor is placed on {char}.
F{char}	 To the occurrence of {char} to the left. The cursor is placed on {char}.
`,` :	Repeat latest f, F [count] times.
`;` :	Repeat latest f, F in opposite direction [count] times 

### t-motion

t{char} To the occurrence of {char} to the right. The cursor is placed before {char}.
T{char}	To the occurrence of {char} to the left. The cursor is placed before {char}.
`,` :	Repeat latest f, F [count] times.
`;` :	Repeat latest f, F in opposite direction [count] times 

exapmles:
`f(dt)` will delete text inside ()


## Quick fix

`:grep word **/.files*.c` will put all files in a quick fix list

- `:cn` or`cnext`: to go to next
- `:cp` or `cprev`: to go to previous item in the list
- `:ccl` or `cclose`: to close the quick fix
- `:copen`: open the quickfix
