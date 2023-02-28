**Status**: I've just started working on the project again. Breaking changes might happen during the following months. I'm currently working on
getting the framework ready for use as it was back in 2019, but with a completely refactored codebase.

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

*Comming soon*

### Usage (Outdated)

Below is a minimal description of how to use the framework. I will be adding
more documentation and moving around various components of the API. A simple
example for the Ant-v2 environment (similar to Gym) consists of the following
script:

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
