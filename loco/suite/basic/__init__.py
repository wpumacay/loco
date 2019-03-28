
import inspect

from loco.suite.basic import humanoid
from loco.suite.basic import ant
from loco.suite.basic import dog
from loco.suite.basic import raptor

# based in controlsuite's factory mechanism. See the following part of their code:
# https://github.com/deepmind/dm_control/blob/978230f1376de1826c430dd3dfc0e3c7f742f5fe/dm_control/suite/__init__.py#L92
# Their code is really neat :).

# Find all environments (key: envName, value: factory method). The way it works ...
# is by search among all imported modules (humanoid, ant, ...), and those who ...
# define their factory methods (for environment creation) in the SUITE object ...
# are "loaded" into this dict of available domains. The factory method is ...
# in charge of creating the environemtn and the task requested by the user.
_ENVIRONMENTS = { name: module for name, module in locals().items()
                  if inspect.ismodule( module ) and hasattr( module, 'SUITE' ) }

# @TODO: change environemnt by domain in the namig convention, and environmentArgs ...
# by scenarioArgs as well.

def load( envName, taskName, envDictArgs = None, taskDictArgs = None ) :
    if envName not in _ENVIRONMENTS :
        _errorMsg = 'Environment {!r} does not exist.'
        raise ValueError( _errorMsg.format( envName ) )

    _envModule = _ENVIRONMENTS[ envName ]

    if taskName not in _envModule.SUITE :
        _errorMsg = 'Task {!r} does not exist for environment {!r}.'
        raise ValueError( _errorMsg.format( taskName, envName ) )

    _envCreator = _envModule.SUITE[ taskName ]

    envDictArgs = envDictArgs or {}
    taskDictArgs = taskDictArgs or {}

    _env = _envCreator( envDictArgs = envDictArgs, taskDictArgs = taskDictArgs )

    return _env