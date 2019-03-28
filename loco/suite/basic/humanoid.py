
import numpy as np

from loco.tasks import base
from loco.envs import basic


def walk( envKwargs ) :
    _task = HumanoidTask()
    _env = basic.BasicEnvironment( 'humanoid', _task, **envKwargs )

    return _env

def stand( envKwargs ) :
    _task = HumanoidTask()
    _env = basic.BasicEnvironment( 'humanoid', _task, **envKwargs )

    return _env


# @HINT: perhaps to chain various tasks we could use decorators (not python ...
#        decorators, but the pattern) such that we chain a simple task, with ...
#        a more complicated one, and reuse as needed (forward, height, ...).
#
#        Task( HeightConstraintTask( ForwardWalkTask() ) )

class HumanoidTask( base.Task ) :

    def __init__( self ) :
        super( HumanoidTask, self ).__init__()

    def _resetTask( self, simulation ) :
        # @TODO: Reset to an initial distribution
        pass

    def _collectReward( self, simulation ) :
        # @TODO: Collect rewards according to the dm_control paper, and some ...
        # other sources (rllab, gym-roboschool, gym-mujocopy)
        return 0.0

    def _collectObservations( self, simulation ) :
        # @TODO: Collect observations according to various sources
        return {}

    def _checkTermination( self, simulation ) :
        # @TODO: Check termination according to various sources
        return False
