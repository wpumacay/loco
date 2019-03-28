
import abc
import numpy as np


class Task( object ) :

    def __init__( self ) :
        super( Task, self ).__init__()

    def reset( self, scenario, simulation, visualizer ) :
        self._resetTask( scenario, simulation, visualizer )

        return self._collectObservations( scenario, simulation, visualizer )

    def step( self, scenario, simulation, visualizer ) :
        _reward = self._collectReward( scenario, simulation, visualizer )
        _observations = self._collectObservations( scenario, simulation, visualizer )
        _finished = self._checkTermination( scenario, simulation, visualizer )

        return { 'obs' : _observations,
                 'reward' : _reward,
                 'finished' : _finished }

    def _resetTask( self, scenario, simulation, visualizer ) :
        raise NotImplementedError( 'Task::_resetTask> abstract method' )

    def _collectReward( self, scenario, simulation, visualizer ) :
        raise NotImplementedError( 'Task::_collectReward> abstract method' )

    def _collectObservations( self, scenario, simulation, visualizer ) :
        raise NotImplementedError( 'Task::_collectObservations> abstract method' )

    def _checkTermination( self, scenario, simulation, visualizer ) :
        raise NotImplementedError( 'Task::_checkTermination> abstract method' )

