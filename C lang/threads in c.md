# Threads in c

![Imgur](https://i.imgur.com/p3UDwrl.png)

A process contains at least one thread, with the single-threaded process being a special case that operates using just one thread. To improve performance, you can utilize the POSIX threads interface (pthread library) to create additional threads within a single process, enabling concurrent execution (parallel jobs).

### Threads creation

```c
#include <pthread.h>

int pthread_create(
	pthread_t *thread, // thread identifier
	const pthread_attr_t *attr, // usually null
	void *(*start)(void *), // callback
	void *arg // callback args
);
```
> Returns 0 on success, or a positive error number on error
 
 Here is simple example when you can run a function twice:
 
```c
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void* routine()
{
    printf("Thread doing something...\n");
    sleep(3);
    printf("Thread finishes.\n");
}

int main(int argc, char* argv[])
{
    pthread_t p1, p2;

	// thread are created and running...
    if (pthread_create(&p1, NULL, &routine, NULL) != 0) {
        return 1;
    }
    if (pthread_create(&p2, NULL, &routine, NULL) != 0) {
        return 2;
    }
	// stop the execution untill the thread finishes
    if (pthread_join(p1, NULL) != 0) {
        return 3;
    }
    if (pthread_join(p2, NULL) != 0) {
        return 4;
    }
    return 0;
}
```

### Processes vs Threads

You can achieve the concurrency by using `fork`  and create multi-processes that do the jobs  simultaneously, but this have the following limitations:

- Child process creations are expansive (it duplicates the entire various process attributes)
- It is difficult to share information between processes.

For Threads:

- Sharing information between threads is easy and fast. It is just a matter of copying
data into shared (global or heap) variables.
- Thread creation is faster than process creation—typically, **x10** faster or
better.

### Threads and errno

If a thread made a function call that returned an error in a global `errno` variable, then this would confuse other threads that might also be making function calls and checking `errno`. In other words, race conditions would result. Therefore, in threaded programs, each thread has its own `errno` value.

```c
#include <limits.h>
#include <pthread.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

#define THREADS 2

void *sys_call_fail1(void *n) {
        void *p;

        p = calloc(LONG_MAX, 1);
        perror("thread 1: ");

        return (p);
}

void *sys_call_fail2(void *n) {
        void *p;

        kill(SIGUSR1, INT_MAX);
        perror("thread 2: ");
        return (p);
}

int main() {
        pthread_t threads[THREADS];

        pthread_create(&threads[0], NULL, sys_call_fail1, NULL);
        pthread_create(&threads[1], NULL, sys_call_fail2, NULL);

        pthread_join(threads[0], NULL);
        pthread_join(threads[1], NULL);
}
```

The output of this program shows that even though `errno` value has changed, but it remains the expected value for each thread:

```txt
thread 2: : Invalid argument
thread 1: : Cannot allocate memory
```

### Multi-threads process

Create multi-threads and run them concurrently: 
```c
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#define THREADS_NBR

void* thread()
{
    printf("Thread doing something...\n");
    sleep(3);
    printf("Thread finishes.\n");
}

int main(int argc, char* argv[])
{
    pthread_t threads[THREADS_NBR];

	// thread are created and running...
	for (int i = 0; i < THREADS_NBR)
	{
		// it taks a pointer to pthread_t
	    if (pthread_create(threads + i, NULL, thread, NULL) != 0) {
			perror("Error")
	        return 1;
	    }
	}
	for (int i = 0; i < THREADS_NBR)
	{
	    if (pthread_join(p1, NULL) != 0) {
			perror("Error")
	        return 3;
	    }
	}
    return 0;
}
```

### Passing argument

```c
int *thread_argument;

thread_argument = malloc(4);
*thread_argument = 98;

pthread_create(threads, NULL, (void **) &thread_argument, NULL);
```
### Getting value from thread after execution

```c
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define THREADS 100

void *test()
{
        int *return_value = malloc(sizeof(int));
        return_value[0] = 69;
        return (return_value);
}

int main()
{
        pthread_t threads[THREADS];
        int *expected_return_value_from_thread;

        pthread_create(threads, NULL, test, NULL);
        pthread_join(threads[0], (void **) &expected_return_value_from_thread);

        printf("Expected = %d\n", *expected_return_value_from_thread);
}
```

### Mutex

```c
#include <pthread.h>
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```
> Both return 0 on success, or a positive error number on error

To lock a `mutex`, we specify the mutex in a call to `pthread_mutex_lock()`. If the mutex is currently unlocked, this call locks the mutex and returns immediately. If the mutex is currently locked by another thread, then `pthread_mutex_lock()` blocks until the mutex is unlocked, at which point it locks the mutex and returns.

```c
#include <limits.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define THREADS 2

pthread_mutex_t mtx;
int g_inc = 0;

void    exit_err(char *msg)
{
        perror(msg);
        exit(1);
}

void *start(void *arg) {
        int j;
        int inc = 0;
        for (j = 0; j < 10000000; j++) {
                inc++;
                if (pthread_mutex_lock(&mtx) != 0)
                        exit_err("Mutex_lock");
                g_inc++;
                if (pthread_mutex_unlock(&mtx) != 0)
                        exit_err("Mutex_unlock");
        };
        return (NULL);
}

int main() {
        pthread_t threads[THREADS];

        pthread_mutex_init(&mtx, NULL);

        pthread_create(&threads[0], NULL, start, NULL);
        pthread_create(&threads[1], NULL, start, NULL);

        pthread_join(threads[0], NULL);
        pthread_join(threads[1], NULL);

        printf("Global: %d\n", g_inc);
        pthread_mutex_destroy(&mtx);
        exit(0);
}
```