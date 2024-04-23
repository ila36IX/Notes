# fabric

```text
Fabric is a Python library used for interacting with SSH and computer systems [easily] to automate a wide range of tasks, varying from application deployment to general system administration.
```
## Installation

```bash
pip3 uninstall Fabric
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install build-essential
sudo apt-get install python3.4-dev
sudo apt-get install libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
```

## Usage

## "Run" command in remote server

```python
from fabric.api import *

env.user = 'username'
env.hosts = ['serverX', "15.123.55.1", "root@0.0.0."]

def host_type():
    run('uname -s')
```

To run the script:

```bash
bash -H host,... func1 func2
```
### Copy a directory to a remote machine.

```python
from fabric.api import *

env.hosts = ['userX@serverX']

def copy():
    # make sure the directory is there!
    run('mkdir -p /home/userX/mynewfolder')
    put('localdirectory', '/home/userX/mynewfolder')
```