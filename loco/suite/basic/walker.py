
import numpy as np

from loco.tasks import base
from loco.envs import basic

SUITE = {}

def walk( envDictArgs = None, taskDictArgs = None ) :
    _envKwargs = ( envDictArgs or {} ).copy()
    _envKwargs['modelName'] = 'walker'
    _envKwargs['modelFormat'] = 'mjcf'
    _envKwargs['startpos'] = [0, 0, 2]

    _taskKwargs = ( taskDictArgs or {} ).copy()

    _task = WalkerTask( 'agent_0' )
    _env = basic.BasicEnvironment( _task, 'agent_0', **_envKwargs )

    return _env

def stand( envDictArgs = None, taskDictArgs = None ) :
    _envKwargs = ( envDictArgs or {} ).copy()
    _envKwargs['modelName'] = 'walker'
    _envKwargs['modelFormat'] = 'mjcf'
    _envKwargs['startpos'] = [0, 0, 2]

    _taskKwargs = ( taskDictArgs or {} ).copy()

    _task = WalkerTask( 'agent_0' )
    _env = basic.BasicEnvironment( _task, 'agent_0', **_envKwargs )

    return _env

SUITE['walk'] = walk
SUITE['stand'] = stand

# @HINT: perhaps to chain various tasks we could use decorators (not python ...
#        decorators, but the pattern) such that we chain a simple task, with ...
#        a more complicated one, and reuse as needed (forward, height, ...).
#
#        Task( HeightConstraintTask( ForwardWalkTask() ) )

class WalkerTask( base.Task ) :

    def __init__( self, agentName ) :
        super( WalkerTask, self ).__init__()

        self._agentName = agentName

    def _resetTask( self, scenario, simulation, visualizer ) :
        # @TODO: Reset to an initial distribution
        pass

    def _collectReward( self, scenario, simulation, visualizer ) :
        # @TODO: Collect rewards according to the dm_control paper, and some ...
        # other sources (rllab, gym-roboschool, gym-mujocopy)
        return 0.0

    def _collectObservations( self, scenario, simulation, visualizer ) :
        # @TODO: Collect observations according to various sources
        return {}

    def _checkTermination( self, scenario, simulation, visualizer ) :
        # @TODO: Check termination according to various sources
        return False
