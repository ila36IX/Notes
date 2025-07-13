
### Replace files between branches

To replace the `Makefile` with `makefile` version in main you can the the following:

```sh
git checkout main -- Makefile
```

or you can do it like this:

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

## Reset branch to match the remote

To discard local commits and reset branch to match the remote branch:

```sh
git fetch origin
git reset --hard origin/branch-name
```
## Make branch match another branch

This will reset main branch to be match exactly the exec branch

```sh
git checkout main
git reset --hard exec
git push origin main --force
```

## Clean the working direcetory

```sh
git clean -n # dry clean
git clean -dfxi
```

`-n`: Don’t actually remove anything, just show what would be done
`-i`: do it interactively
`-f`: force
`-d`: include directories 