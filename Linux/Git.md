
```bash
async() {
    git reset --hard main
    git checkout main
    git pull
    git checkout ila
    git reset --hard main
    git push origin ila --force
}
```
