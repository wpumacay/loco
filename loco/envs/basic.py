
# Base environment
from loco.envs import base
# Functionality to create the simulation (tysoc package)
import pytysoc


class BasicEnvironment( base.Environment ) :

    def __init__( self, 
                  agentName = 'humanoid', 
                  task = None,
                  physics = pytysoc.BACKENDS.PHYSICS.MUJOCO,
                  graphics = pytysoc.BACKENDS.RENDERING.GLVIZ ):

        super( BasicEnvironment, self ).__init__()

        self._agentName = agentName
        self._agentTemplate = agentName
        self._startpos = [0, 0, 2]
        self._task = task
        self._physicsBackendId = physics
        self._graphicsBackendId = graphics

        self._runtime = pytysoc.createRuntime( physicsBackend = self._physicsBackendId,
                                               renderingBackend = self._graphicsBackendId,
                                               workingDir = pytysoc.PATHS.WORKING_DIR )

        self._agent = pytysoc.createAgent( self._agentName,
                                           self._agentTemplate,
                                           self._startpos )

        self._terraingen = pytysoc.createStaticTerrainGen( 'floorGenerator' )
        self._terraingen.createPrimitive( 'plane',          # namae
                                          [10, 10, 0.1],    # dimensions
                                          [0, 0, 0],        # position
                                          [0, 0, 0],        # orientation (euler)
                                          [0.2, 0.3, 0.4],  # color
                                          'chessboard' )    # texture

        self._scenario = pytysoc.createScenario()
        _scenario.addAgent( self._agent )
        _scenario.addTerrainGen( self._terraingen )

        self._simulation = self._runtime.createSimulation( self._scenario )
        self._simulation.initialize()

        self._visualizer = self._runtime.createVisualizer( self._scenario )
        self._visualizer.initialize()

    def reset( self ) :
        _obs = super( BasicEnvironment, self ).reset()

        if self._task :
            _obs = self._task.reset( self._simulation )
        
        return _obs

    def step( self ) :
        _stepInfo = super( BasicEnvironment, self ).step()

        if self._task :
            _stepInfo = self._task.step( self._simulation )

        return _stepInfo