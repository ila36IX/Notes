The manual page for each system call documents the possible return values of the
call, showing which value(s) indicate an error. Usually, an error is indicated by a
return of –1. Thus, a system call can be checked with code such as the following:

```c
fd = open(pathname, flags, mode);
if (fd == -1)
{
	/* Code to handle the error */
}
/* system call to open a file */
if (close(fd) == -1)
{
/* Code to handle the error */
}
```

When a system call fails, it sets the global integer variable `errno` to a positive value
that identifies the specific error.

> `#include <stdio.h>`
> `void perror(const char *msg);`

Simple usage:

```c
fd = open(pathname, flags, mode);
if (fd == -1)
{
	perror(pathname);
	exit(EXIT_FAILURE);
}
```

The strerror() function returns the error string corresponding to the error number
given in its errnum argument.

> `#include <string.h>`
> `char *strerror(int errnum);`
> Returns pointer to error string corresponding to errnum

