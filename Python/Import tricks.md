
To handle what will e imported in the server in case where using `from package import *`:

```python
__all__ = [
    'mod1', 
    'mod2',    # <--- THOSE ARE STRINGS NOT TYPES!!
    'mod3',   
    'mod4'  
]
```