PyBunny - Your SSH-Jupyter Proxy Hop Friend!
============================================

![Python](https://img.shields.io/badge/python-3.6-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![saythanks](https://img.shields.io/badge/Lab-Shen%20Group-ff69b4.svg)](https://www.computchem.org/)

<p align="center">
  <img width="800" height="600" src="images/bunny.gif">
</p>


Bunny is a ssh proxy jumping for jupyter notebooks. If you are in a situation similar to mine where you want to port
forward a jupyter notebook from your mini cluster machine but is not ssh accessible so you need a gateway that is SSH
accessible and you are going to port forward through several machines. Well I wrote a python package for it. 

```
    HOST A (local machine) -> HOST B (gateway) -> HOST C (execute jupyter)
    
```
**Note**: you must have authorized keys in your SSH between every Host added into the Bunny.

Quick Start
===========

Running the bunny is pretty easy. To initialize a class you pass the `python_env` variable to dictate which python env
is going to be running the jupyter notebook. The `notebook_launch_command` is your exact launch command to run the jupyter 
notebook - mine is exampled down below and the `port` you execute your notebook on.

    
```
    from pybunny.bunny import Bunny
    
    bunny = Bunny(
        python_env='/path/to/env/python',
        notebook_launch_command='jupyter notebook --no-browser --NotebookApp.token=""',
        port='8889'
    )
    
```

Next add your hops between the bunnies, with the user, hostname, and the name of the gateway. If this is the last server
in your chain to run the notebook then add the `proxy_jump` argument if

```

    bunny.add_hop('hop1', hostname='XX.XX.XXX.XXX', user='poor_graduate_student')
    bunny.add_hop('notebook', hostname='fakeemail@someuniversity.edu', user='poor_graduate_student', proxy_jump = True)
    
```

When your configurations are set then write the SSH Config, this is a local `bunny_config` file generated that contains
the bunny configuration. 

```

    bunny.write()

```

which generates something like this:

```
    
    Host hop1
    
      HostName XX.XXX.XXX.XXX
      User poor_graduate_student
    
    Host notebook
      HostName fakeemail@someuniversity.edu
      User poor_graduate_student
      ProxyJump XX.XX.XXX.XXX
      RequestTTY force
      LocalForward 8889 127.0.0.1:8889
      RemoteCommand /path/to/env/python jupyter notebook --no-browser --NotebookApp.token="" --port=8889

```

The last command will be the `run()` function which will execute the `SSH` connection across your gateways. Under the hood
it runs the ```SSH -F bunny_config name``` so as long as your have `SSH` installed we should be good and your process will run.


```
    
    bunny.run()
    
```

If all successful we should be generating something like this:

```

[I 20:46:00.555 NotebookApp] JupyterLab extension loaded from anaconda3/lib/python3.7/site-packages/jupyterlab
[I 20:46:00.555 NotebookApp] JupyterLab application directory is /jupyter/lab
[I 20:46:00.557 NotebookApp] Serving notebooks from local directory: /rotation
[I 20:46:00.557 NotebookApp] The Jupyter Notebook is running at:
[I 20:46:00.557 NotebookApp] http://localhost:8889/
[I 20:46:00.557 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[I 20:46:04.084 NotebookApp] 302 GET / (127.0.0.1) 1.00ms
[E 20:46:04.166 NotebookApp] Could not open static file ''
[W 20:46:04.503 NotebookApp] 404 GET /static/components/react/react-dom.production.min.js (127.0.0.1) 14.90ms referer=http://localhost:8889/tree?
```

Announcements
=============

-   Work has began Jan 9th

Installation 
============

Bunny is going to be distribute via PyPi and as the content store grows we can expand it to other pieces of software
making it accessible to all regardless of what you use. Alternatively, you could have a glance at the source code and copy/paste
it yourself.

To install the reader 

```

python -m pip install bunny

```

Structure of Bunny
==================

Currently, the main subpackages are:

- **bunny**: Bunny Main Class


Genesis
=======

Bunny was created because I am forced to port forward my jupyter notebooks through a gateway server and there is no way 
around it due to bureaucracy.

- Lead Developer [Suliman Sharif](http://sulstice.github.io/)


* * * * *

External links
==============


