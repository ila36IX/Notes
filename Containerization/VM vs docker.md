x![](https://i.imgur.com/KyIzju4.jpeg)
# Docker vs VM
### External resources

- [Docker vs VM: What's the Difference, and Why You Care!](https://www.youtube.com/watch?v=D82C7JS_2iw)
- [Containers From Scratch • Liz Rice • GOTO 2018](https://www.youtube.com/watch?v=8fi7uSYlOdc)
- [Documentation/cgroup-v1/cpusets.txt](https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt)

Both VM/docker let you take bundle of software including the OS and all your configured application and package them up in reusable way.  

## VM

Virtualization uses hypervisor which manages hardware so more than one operating system can run on it at once, there are two kinds:  

__Type 1 Heypervisor ("Bare Metal")__: Runs directly in the physical hardware with no host OS underneath.  
- Example of Hypervisor software: [PROXMOX](https://www.proxmox.com/en/), Windows HyperV, bare ESXi  

__Type 2 Hypervisor__: Runs as an application within the standard OS  that creates a simulated hardware environment

NOTE: **emulators** are not considered type 2 hypervisor, the emulators often emulating hardware registers and CPU instructions in software to run code for architectures that do not exist. In contrast, a **hosted hypervisor** execute most instructions on native hardware, relying on the host OS for resource allocation.

## Docker

Instead of using VM snapshots you can containerize the environment using docker configuration files by expressing all the installation steps and dependencies within it.

With docker you have a configuration file that represents your development environment which can be pulled and run in any system in the world that has docker installed in it.

Containers are lightweight and start faster then VMS.

VM approach offers full isolation with its own OS.
Docker containers can achieve ring **zero escalation** which can give it full access to the entire system.


## Virtual Machines vs. Docker Containers

**Architecture**
- VM: includes a full guest OS (kernel + userland) running on virtualized hardware via a hypervisor
- Docker: packages just the app + its dependencies, and shares the host machine's kernel directly

**Isolation**
- VM: hardware-level isolation — each VM has its own kernel, completely separate from the host and other VMs
- Docker: process-level isolation using kernel features (namespaces, cgroups) — stronger than a plain process, weaker than a VM

**Startup time**
- VM: 30 seconds to a few minutes (booting a full OS)
- Docker: typically under a second, sometimes a couple seconds

**Resource usage**
- VM: RAM/CPU/disk are reserved per VM, often whether it's actively using them or not
- Docker: shares the host's resources dynamically; you can cap limits but nothing is "locked away" unused

**Image/footprint size**
- VM: gigabytes (whole OS included)
- Docker: megabytes to low gigabytes (no OS kernel, often minimal base images like Alpine)

**Security boundary**
- VM: a compromised VM is contained to that VM — the hypervisor is a hard boundary
- Docker: a kernel-level exploit (container escape) can potentially reach the host and every other container, since the kernel is shared

**Portability**
- VM: portable across any host with a compatible hypervisor, but the image is large and OS-specific
- Docker: highly portable same image runs anywhere Docker (or a compatible runtime) is installed, "build once, run anywhere"

**OS flexibility**
- VM: guest OS can differ entirely from the host (Windows VM on a Linux host, etc.)
- Docker: container must share the host's kernel type — Linux containers need a Linux kernel (Docker Desktop on Mac/Windows works around this by running a lightweight Linux VM under the hood)

**Density**
- VM: typically tens of VMs per physical host, depending on resources
- Docker: hundreds to thousands of containers per host, since there's no OS duplication

**Typical use case**
- VM: full-stack environments, legacy apps, multi-tenant infrastructure needing hard isolation, running different OSes on one machine
- Docker: microservices, CI/CD pipelines, horizontally scaled stateless apps, local dev environments

**Persistence/state management**
- VM: state lives inside the VM disk image by default
- Docker: containers are meant to be ephemeral/stateless; persistent data is handled separately via volumes

**Networking**
- VM: gets its own virtual NIC, behaves like a fully separate machine on the network
- Docker: uses lighter-weight virtual networks (bridge, overlay, host mode) managed by the container runtime

**Orchestration**
- VM: managed by hypervisor platforms (vSphere, Proxmox, Hyper-V)
- Docker: managed by container orchestrators (Kubernetes, Docker Swarm, ECS)

## What is Docker?

Docker is an open source project for building, shipping, and running programs. It is a command-
line program, a background process, and a set of remote services that take a logistical
approach to solving common software problems and simplifying your experience
installing, running, publishing, and removing software. It accomplishes this by using
an operating system technology called containers.

Keywords:
Compose configuration
Build context (Dockerfile execution)
Runtime environment
