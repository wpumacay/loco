
import numpy as np

from loco.suite import basic

_env = basic.load( 'humanoid', 'walk' )

while True :
    _u = -1.0 + 2.0 * np.random.random( ( _env.actionDim(), ) )

    _env.step( _u )
    _env.render()