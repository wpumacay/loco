
import numpy as np

import pytysoc
from loco.suite import basic

## _env = basic.load( 'walker', 'walk', { 'physics': pytysoc.BACKENDS.PHYSICS.MUJOCO } )
_env = basic.load( 'walker', 'walk', { 'physics': pytysoc.BACKENDS.PHYSICS.BULLET } )

while True :
    _u = -1.0 + 2.0 * np.random.random( ( _env.actionDim(), ) )

    _env.step( _u )
    _env.render()