
import numpy as np


class Environment( object ):
    """Base class for RL based environments
        
    This environment wraps the functionality of the simulator and
    visualizer, and exposes it through a standard API. Tasks are
    defined via Tasks objects, which are added into extensions of
    this class. This class is meant as an interface for other types
    of RL environments, namely:

    * Basic     :   An RL environment similar to the ones created by Gym
    * Multitask :   An RL environment that setups a set of different tasks 
                    for a single agent.

    """
    
    def __init__( self ) :
        super( Environment, self ).__init__()

        self._simulation = None
        self._visualizer = None

    def reset( self ) :
        if self._simulation :
            self._simulation.reset()

        if self._visualizer :
            self._visualizer.reset()

        return {}

    def step( self ):
        if self._simulation :
            self._simulation.step()

        return {}

    def render( self ) :
        if self._visualizer :
            self._visualizer.render()

    def _agents( self ) :
        if self._simulation :
            return self._simulation.agents()

        return []

    def _terrainGens( self ) :
        if self._simulation :
            return self._simulation.terrainGens()

        return []

    def _sensors( self ) :
        if self._simulation :
            return self._simulation.sensors()

        return []