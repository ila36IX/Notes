
### Replace files between branches

To replace the `Makefile` with `makefile` version in main you can the the following:

```sh
git checkout main -- Makefile
```

### Or:

```sh
git merge main --no-commit
git checkout --theirs Makefile  # Keep the main branch's Makefile
git add Makefile
git commit -m "Merge main into parse (keeping main's Makefile)"
```

### View file in other branch

```sh
git show main:Makefile
```