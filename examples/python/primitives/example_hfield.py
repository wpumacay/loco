
import sys
import numpy as np
from scipy import ndimage
import tysoc_bindings as tysocpp
import pytysoc

NUM_BOXES       = 1
NUM_SPHERES     = 1
NUM_CYLINDERS   = 1
NUM_CAPSULES    = 1
NUM_MESHES      = 1

## PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.MUJOCO
## PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.BULLET
PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.RAISIM

def createHfield( name, position ) :
    ## nxSamples = 50
    ## nySamples = 50
    ## xExtent = 5.0
    ## yExtent = 5.0

    ## _x = xExtent * np.linspace( -0.5, 0.5, nxSamples )
    ## _y = yExtent * np.linspace( -0.5, 0.5, nySamples )
    ## _xx, _yy = np.meshgrid( _x, _y )
    ## _zz = 10.0 * ( _xx ** 2 + _yy ** 2 ) / ( xExtent ** 2 + yExtent ** 2 )

    # Adapted from dm_control quadruped.py
    #  https://github.com/deepmind/dm_control/blob/master/dm_control/suite/quadruped.py

    nxSamples = 50
    nySamples = 50
    xExtent = 10.0
    yExtent = 10.0

    _TERRAIN_SMOOTHNESS = 0.15  # 0.0: maximally bumpy; 1.0: completely smooth.
    _TERRAIN_BUMP_SCALE = 2  # Spatial scale of terrain bumps (in meters).

    # Sinusoidal bowl shape.
    _xx, _yy = np.ogrid[-1:1:nxSamples*1j, -1:1:nySamples*1j]
    radius = np.clip( np.sqrt( _xx ** 2 + _yy ** 2 ), .04, 1 )
    bowl_shape = .5 - np.cos( 2 * np.pi * radius ) / 2
    # Random smooth bumps.
    terrain_size = 2 * xExtent
    bump_res = int( terrain_size / _TERRAIN_BUMP_SCALE )
    bumps = np.random.uniform( _TERRAIN_SMOOTHNESS, 1, ( bump_res, bump_res ) )
    smooth_bumps = ndimage.zoom( bumps, nxSamples / float( bump_res ) )
    # Terrain is elementwise product.
    _zz = bowl_shape * smooth_bumps

    _maxHeight = np.max( _zz )
    _heightData = ( _zz / _maxHeight ).ravel()

    _heightFieldData = tysocpp.PyHeightFieldData()
    _heightFieldData.nWidthSamples = nxSamples
    _heightFieldData.nDepthSamples = nySamples
    _heightFieldData.heightData = _heightData

    _collisionData = tysocpp.PyCollisionData()
    _collisionData.type = tysocpp.eShapeType.HFIELD
    _collisionData.size = [ xExtent, yExtent, _maxHeight ]
    _collisionData.hdata = _heightFieldData

    _visualData = tysocpp.PyVisualData()
    _visualData.type = tysocpp.eShapeType.HFIELD
    _visualData.size = [ xExtent, yExtent, _maxHeight ]
    _visualData.hdata = _heightFieldData

    _visualData.ambient = [ 0.2, 0.3, 0.4 ]
    _visualData.diffuse = [ 0.2, 0.3, 0.4 ]
    _visualData.specular = [ 0.2, 0.3, 0.4 ]
    _visualData.shininess = 50.0

    _bodyData = tysocpp.PyBodyData()
    _bodyData.dyntype = tysocpp.eDynamicsType.STATIC
    _bodyData.collision = _collisionData
    _bodyData.visual = _visualData

    return tysocpp.PyBody( name, _bodyData, position, [ 0.0, 0.0, 0.0 ] )

def createSingleBody( name, shape, size, position, rotation = [0.0, 0.0, 0.0], color = [0.7, 0.5, 0.3], filename= '' ) :
    _collisionData = tysocpp.PyCollisionData()
    _collisionData.type = shape
    _collisionData.size = size
    if shape == tysocpp.eShapeType.MESH :
        _collisionData.filename = filename

    _visualData = tysocpp.PyVisualData()
    _visualData.type = shape
    _visualData.size = size
    _visualData.ambient = color
    _visualData.diffuse = color
    _visualData.specular = color
    _visualData.shininess = 50.0
    if shape == tysocpp.eShapeType.MESH :
        _visualData.filename = filename

    _bodyData = tysocpp.PyBodyData()
    _bodyData.dyntype = tysocpp.eDynamicsType.DYNAMIC
    _bodyData.collision = _collisionData
    _bodyData.visual = _visualData

    return tysocpp.PyBody( name, _bodyData, position, rotation )

if __name__ == '__main__' :

    if len( sys.argv ) > 1 :
        if sys.argv[1].lower() == 'mujoco' :
            PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.MUJOCO
        elif sys.argv[1].lower() == 'bullet' :
            PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.BULLET
        elif sys.argv[1].lower() == 'raisim' :
            PHYSICS_BACKEND = pytysoc.BACKENDS.PHYSICS.RAISIM

    np.random.seed( 0 )
    _scenario = tysocpp.PyScenario()
    
    _hfield = createHfield( "terrain_0", [ 0.0, 0.0, 0.0 ] )
    _scenario.addBody( _hfield )
    
    for i in range( NUM_BOXES ) :
        _scenario.addBody( createSingleBody( 'box_' + str( i ), tysocpp.eShapeType.BOX, [0.2, 0.2, 0.2], np.concatenate((6.0 * (np.random.rand( 2 ) - 0.5), [3.0])) ) )

    for i in range( NUM_SPHERES ) :
        _scenario.addBody( createSingleBody( 'sphere_' + str( i ), tysocpp.eShapeType.SPHERE, [0.1, 0.1, 0.1], np.concatenate((6.0 * (np.random.rand( 2 ) - 0.5), [3.0])) ) )

    for i in range( NUM_CYLINDERS ) :
        _scenario.addBody( createSingleBody( 'cylinder_' + str( i ), tysocpp.eShapeType.CYLINDER, [0.1, 0.2, 0.2], np.concatenate((6.0 * (np.random.rand( 2 ) - 0.5), [3.0])) ) )

    for i in range( NUM_CAPSULES ) :
        _scenario.addBody( createSingleBody( 'capsule_' + str( i ), tysocpp.eShapeType.CAPSULE, [0.1, 0.2, 0.2], np.concatenate((6.0 * (np.random.rand( 2 ) - 0.5), [3.0])) ) )

    #### for i in range( NUM_MESHES ) :
    ####     _mesh_filename = '/home/gregor/Documents/repos/loco_workspace/loco/core/res/meshes/' + ( 'monkey.obj' if PHYSICS_BACKEND == pytysoc.BACKENDS.PHYSICS.RAISIM else 'monkey.stl' )
    ####     _scenario.addBody( createSingleBody( 'mesh_' + str( i ), tysocpp.eShapeType.MESH, [0.2, 0.2, 0.2], np.concatenate((6.0 * (np.random.rand( 2 ) - 0.5), [3.0])), filename = _mesh_filename ) )

    _runtime = pytysoc.createRuntime( physicsBackend = PHYSICS_BACKEND,
                                      renderingBackend = pytysoc.BACKENDS.RENDERING.GLVIZ )
    
    _simulation = _runtime.createSimulation( _scenario )
    _visualizer = _runtime.createVisualizer( _scenario )
    
    _simulation.initialize()
    _visualizer.initialize()
    
    _simulation.step()
    _visualizer.render()

    _running = False
    
    while _visualizer.isActive() :
    
        if _visualizer.checkSingleKeyPress( tysocpp.KEY_P ) :
            _running = not _running
        elif _visualizer.checkSingleKeyPress( tysocpp.KEY_R ) :
            _simulation.reset()
        elif _visualizer.checkSingleKeyPress( tysocpp.KEY_ESCAPE ) :
            break

        if _running :
            _simulation.step()
    
        _visualizer.render()