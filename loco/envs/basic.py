
# Base environment
from loco.envs import base
# Functionality to create the simulation (tysoc package)
import pytysoc


class BasicEnvironment( base.Environment ) :

    def __init__( self, 
                  task,
                  agentName, 
                  modelName = 'humanoid',
                  modelFormat = 'mjcf',
                  startpos = [0, 0, 2],
                  physics = pytysoc.BACKENDS.PHYSICS.MUJOCO,
                  graphics = pytysoc.BACKENDS.RENDERING.GLVIZ ):

        super( BasicEnvironment, self ).__init__()

        self._agentName = agentName
        self._modelName = modelName
        self._modelFormat = modelFormat

        self._task = task
        self._startpos = startpos
        self._physicsBackendId = physics
        self._graphicsBackendId = graphics

        self._runtime = pytysoc.createRuntime( physicsBackend = self._physicsBackendId,
                                               renderingBackend = self._graphicsBackendId,
                                               workingDir = pytysoc.PATHS.WORKING_DIR )

        self._agent = pytysoc.createAgent( self._agentName,
                                           self._modelName,
                                           self._modelFormat,
                                           self._startpos )

        self._terraingen = pytysoc.createStaticTerrainGen( 'floorGenerator' )
        self._terraingen.createPrimitive( 'box',            # name
                                          [10, 10, 0.1],    # dimensions
                                          [0, 0, -0.05],    # position
                                          [0, 0, 0],        # orientation (euler)
                                          [0.2, 0.3, 0.4],  # color
                                          'chessboard' )    # texture

        self._sensorName = 'sensor_' + agentName + '_intrinsics'
        self._sensorIntrinsics = pytysoc.createSensorIntrinsics( self._sensorName,
                                                                 self._agent )

        self._scenario = pytysoc.createScenario()
        self._scenario.addAgent( self._agent )
        self._scenario.addTerrainGen( self._terraingen )
        self._scenario.addSensor( self._sensorIntrinsics )

        self._simulation = self._runtime.createSimulation( self._scenario )
        self._simulation.initialize()

        self._visualizer = self._runtime.createVisualizer( self._scenario )
        self._visualizer.initialize()

    def reset( self ) :
        _obs = super( BasicEnvironment, self ).reset()

        if self._task :
            _obs = self._task.reset( self._scenario, self._simulation, self._visualizer )
        
        return _obs

    def step( self, actions = None ) :
        _stepInfo = super( BasicEnvironment, self ).step()

        if ( actions is not None ) and ( self._agent ) :
            self._agent.setActions( actions )

        if self._task :
            _stepInfo = self._task.step( self._scenario, self._simulation, self._visualizer )

        return _stepInfo

    def actionDim( self ) :
        if self._agent :
            return self._agent.getActionDim()

        return 0