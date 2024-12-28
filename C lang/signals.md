# C signals

A signal is the way of communicating between processes, The arrival of a signal informs a process that some event or exceptional condition has occurred.
Each signal type is identified by a different integer, defined with symbolic names of
the form SIGxxxx.
Signals are sent to a process by the kernel, by another process (with suitable
permissions), or by the process itself. For example, the kernel may send a signal to
a process when one of the following occurs:
- the user typed the interrupt character (usually Control-C) on the keyboard;
- one of the process’s children has terminated;
- a timer (alarm clock) set by the process has expired; or
- the process attempted to access an invalid memory address.
For example a segmentation fault that accrues when a program tries to access invalid memory area is indicator of receiving a `SEGV` signal by the kernel, by default a pogrom that receives a `SEGV` will terminates, but overriding this behaviors is possible by adding a specific handler function for this event.

The only signal that can not change its handler is the `SIGKILL`, it integer representation is '9'.

```
kill -9 <pid>
```

`kill` here doesn't always mean killing the process, it's used to send a signal to a process (not all signals meant to terminate the process).

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

int main()
{
	int pid = fork();

	if (pid == -1)
		return (1);
	// child process with the id of pid will run
	if (pid == 0)
	{
		while (1)
		{
			printf("Hello alien! 😄\n");
			usleep(100000);
		}
	}
	else
	{
		// the parent process will wait 1s and than terminates its child precess
		sleep(1);
		// sending segkill signal to the pid process
		kill(pid, SIGKILL);
		printf("Dye mf!");
		wait(NULL);
	}
	return (0);
}

```

## Control stop/continue a process

In this program the program the child process will receive a stop signal, and will stop `1s` and then will continue its execution `1s` than get killed by its parent. 

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>


int main()
{
	int pid = fork();

	if (pid == -1)
		return (1);
	if (pid == 0)
	{
		while (1)
		{
			printf("Hello alien!\n");
			usleep(100000);
		}
	}
	else
	{
		kill(pid, SIGSTOP);
		printf("Process is in asleep\n");
		sleep(1);
		kill(pid, SIGCONT);
		sleep(1);
		kill(pid, SIGKILL);
		printf("Dye haney!");
		wait(NULL);
	}
	return (0);
}
```


## Meet your sender

It important sometimes to get who the sender is (its `pid`) so we can send back signals to acknowledges the receiving of the signal.
To do this you can use `sigaction` function as the following:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void handle_bit(int signo, siginfo_t *info, void *context) {
    // Declare a variable to store the sender's process ID
    pid_t sender_pid;

    // Extract the sender's process ID from the siginfo_t structure
    sender_pid = info->si_pid; 

    // Send a SIGUSR1 signal back to the sender
    kill(sender_pid, SIGUSR1); 
}

int main() {
    struct sigaction sa = {0}; 
    
    // the programm will call `handle_bit` if it revcieved a signal
    sa.sa_sigaction = handle_bit; 

    // Enable SA_SIGINFO flag to receive more information about the signal
    sa.sa_flags = SA_SIGINFO; 
    // Register the signal handler for SIGUSR1
    sigaction(SIGUSR1, &sa, NULL); 

    // stop the program intill it recieves a signal
    while (1) {
        pause(); 
    }

    return 0;
}
```

## You probably do not know `SEGV` well

Ever had your code crash with a segfault and thought "Oh great, the system's angry at me again"? Well, it turns out that is just the default behavior of your program, that makes you believe in that, you can easily  get a segfault and make your code still running!

### What's Really Happening?

The reason why the code segFault is when the kernel spots unauthorized memory access to a memory, in order to communicate that to your process (remember what signal is? _a way to communicate between processes_) the kernel sends a `SEGV` to you program.

> signals are just the kernel's way of sliding into your program's DMs :)

![Imgur](https://i.imgur.com/tEkftxm.png)

### Taking Control of Signals

Almost every signal in your system can be caught and handled - yes, even those scary ones like:
- `SIGBUS` (bad memory access)
- `SIGFPE` (floating point exception)
- `SIGILL` (illegal instruction)
- `SIGSEGV` (segmentation violation)
### The Untouchables

However, there are two rebellious signals that refuse to be tamed:

1. `SIGKILL (9)`: The ultimate terminator - cannot be caught, blocked, or ignored
2. `SIGSTOP`: The freeze ray - suspends execution and won't take no for an answer

> `SIGKILL` are the serious side of the kernel

### Lets say Hi to a segFault

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

/**
 *
 * Example of how to handle a SEGV, and make the program
 * behiave in a different way
 */
void segfaultHandler(int sig)
{
	printf("Signals every where\n");
	exit(1); // Exit the program
}

int main()
{
	// Register the signal handler for SIGSEGV
	signal(SIGSEGV, segfaultHandler);
	printf("Hello SEGV!\n");

	int *ptr = NULL;
	// unauthorized memory access 
	*ptr = 42;
}
```

Now Let's have some more fun, how about segfaulting a random running program?

```c
// main.c
#include <stdio.h>
#include <unistd.h>

int main()
{
	// print the PID of the process
	printf("PID: %d\n", getpid());
	// Stops the process untill it recives a signal
	pause();
	return 0;
}
```

```sh
gcc main.c -o run && ./run
PID: 271354
# the program will keep excuting
```

In other terminal:

```bash
kill -SEGV 271354
```

See? you program got the following:

![Imgur](https://i.imgur.com/iWpeCbl.png)

## My implementation in short

My idea was to send signals `SIGUSR1` and `SIGUSR2` to represent `1` and `0`. It worked in some cases but failed in others. There is always a possibility of losing a signal, which makes the rest of the payload meaningless. Why?

Linux systems do NOT queue signals when you already have pending signals of the same type!

So, I tried using a bigger delay between sending signals. That reduced the chance of losing signals but caused a massive performance issue. Increasing the delay made sending larger messages possible but very slow (e.g., it took more than `10s` to send just 1600 characters).

That was not the solution. The next idea was to send each bit and wait for the server to acknowledge receiving it. This approach did the trick and, surprisingly, was more performant than I expected—it allowed me to send 16,000 characters in just 1 second.