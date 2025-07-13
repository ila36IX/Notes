
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
`:o`: Open file in split mode under tree
`:p`: Open a preview of the file in top of filetree

### Vim tree file operations
`p`: Opens a preview window.
`<C-w>z`: Closes the preview window.

`gh`: Toggles the hidden files.
`%`: Creates a file. Well... it actually doesn't, it just gives you the opportunity to create one. 
`R`: Renames a file
`mt`: Assign the "target directory" used by the move and copy commands.
`mf`: Marks a file or directory. Any action that can be performed on multiple files depend on these marks. So if you want to copy, move or delete files, you need to mark them.
`mc`: Copy the marked files in the target directory.
`mm`: Move the marked files to the target directory.
`mx`: Runs an external command on the marked files.
`D`: Deletes a file or an empty directory. 
`d`: Creates a directory.
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

Examples:

`f(dt)` will delete text inside ()  

### d-motion

`dip` delete between paragraph  
`{d}` delete between paragraph  
## Windows

`CTRL-w T`: Move current window to a new tab page   
`<C-w>s`: -- split  
`<C-w>`v: | split  
`<C-w>`o: Open only this window and hide splits  

## Tabs

`gt`: Go to next tab  
`gT`: Go to previous tab  
## Telescope

`CTRL-q` Send to quick fix list  

## Quick fix

`:h quickfix`  
 `:grep word **/.files*.c` will put all files in a quick fix list  
`:cdo s/true/false/gc` execute a command in all the buffers in quickfix  
### Opening and close quickfix

- `:copen`: open the quickfix  
- `:ccl` or `cclose`: to close the quick fix  
### Looping through quickfix

- `:cfir[st]`: go to first item  
- `:cla[st]`: go to last item  
- `:cn` or`cnext`: to go to next
- `:cp` or `cprev`: to go to previous item in the list
- `:cnf`: to go to next
- `:cpf`: to go to previous item in the list
## Marks

`m{A-Z0-9}`: Mark the current position of cursor as a bookmark  
`'{A-Z0-9}`: Jump to the mark {A-Z0-9} in the file where it was set  
## Buffers

`:h buffers`

`:ls`: list existing buffers  
`:b N`: 	Edit buffer [N] from the buffer list  
`:bn`: go to next buffer  
`:bp`: go to previous buffer  
`:e#`: go to previous buffer (repeating it will toggle between two buffers only)  

