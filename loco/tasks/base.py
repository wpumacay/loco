
import abc
import numpy as np


class Task( object ) :

    def __init__( self ) :
        super( Task, self ).__init__()

    def reset( self, simulation ) :
        self._resetTask( simulation )

        return self._collectObservations()

    def step( self, simulation ) :
        _reward = self._collectReward( simulation )
        _observations = self._collectObservations( simulation )
        _finished = self._checkTermination( simulation )

        return { 'obs' : _observations,
                 'reward' : _reward,
                 'finished' : _finished }

    def _resetTask( self, simulation ) :
        raise NotImplementedError( 'Task::_resetTask> abstract method' )

    def _collectReward( self, simulation ) :
        raise NotImplementedError( 'Task::_collectReward> abstract method' )

    def _collectObservations( self, simulation ) :
        raise NotImplementedError( 'Task::_collectObservations> abstract method' )

    def _checkTermination( self, simulation ) :
        raise NotImplementedError( 'Task::_checkTermination> abstract method' )

