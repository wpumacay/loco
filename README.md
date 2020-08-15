**Status**: Heavy development (you might run into crashes as the library is being developed, sorry in advance)

# Loco: A locomotion framework for RL research

[![Build Status](https://travis-ci.com/wpumacay/loco.svg?branch=master)](https://travis-ci.com/wpumacay/loco)

![gif-ant-sample](https://media.giphy.com/media/u48REyy0BzCUzbLyXC/giphy.gif)

![gif-demo-sample](https://media.giphy.com/media/ZDEAQSUraLao0fOhHi/giphy.gif)

This is a locomotion framework that is intended to provide a new set of benchmarks 
for RL research in locomotion by allowing the user to create a wide range of
diverse and complex environments. The core framework is engine-agnostic (it is not
coupled to a specific physics engine), and allows to support a wide variety of
physics engine. For now it support MuJoCo, and I'm currently working in support
for Bullet as well (and PhysX in approx. July/August).

## Setting up the project

So far the framework has been tested in Ubuntu 16.04 and MacOS.

### Dependencies

1. Install the following dependencies:

On Ubuntu 16.04 :

```shell
    $ sudo apt-get install make cmake pkg-config
    $ sudo apt-get install libassimp-dev libglfw3-dev libglew-dev
```

On MacOS :

```shell
    $ brew install glew
    $ brew install glfw
    $ brew install pkg-config
    $ brew install assimp
```

2. Install [MuJoCo](https://www.roboti.us/index.html) in your system (to have MuJoCo 
   as an available backend). The build rules expect the MuJoCo libraries to be
   extracted in `~/.mujoco/mujoco200_linux` ( or `~/.mujoco/mujoco200_macos` for macOS ), 
   and the license key placed in `~/.mujoco/mjkey.txt` ( the same path `~/.mujoco/mjkey.txt` for macOS ).

3. It is recommended that you use a virtual environment. Using conda, create
   the following environment:

```shell
    $ conda create -n loco_env python=3.6
    $ source activate loco_env
```

4. (MacOS) During runtime, the linker tries to find the libraries in `@executable_path`, so
   a fix for this is to add the path `~/.mujoco/mujoco200_macos` to your `DYLD_LIBRARY_PATH`.

```shell
    $ export DYLD_LIBRARY_PATH=~/.mujoco/mujoco200_macos:$DYLD_LIBRARY_PATH
```

### Building

1. Clone the repository with all its submodules:

```shell
    $ git clone https://github.com/wpumacay/loco.git
    $ cd loco
    $ git submodule update --init --recursive
```

2. Then just run the setup script, and the library will be built and installed
   in the appropiate conda environment. (Please, avoid using *pip* because there
   is a linking error I'm working currently trying to fix)

```shell
    $ python setup.py install
```

### Usage

Below is a minimal description of how to use the framework. I will be adding
more documentation and moving around various components of the API.

A simple example for the Ant-v2 environment (similar to Gym) consists of the
following script:

```python

import numpy as np

from loco.suite import basic

_env = basic.load( 'humanoid', 'walk' )

while True :
    _u = -1.0 + 2.0 * np.random.random( ( _env.actionDim(), ) )

    _env.step( _u )
    _env.render()

```

Some more examples can be found [here](https://github.com/wpumacay/tysocMjc/tree/5cfd6106cd550e221b516f9b57b5623d3571f6b9/examples/python).
