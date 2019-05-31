
cmake_minimum_required( VERSION 3.0.0 )

set( CMAKE_CXX_STANDARD 11 )

if ( NOT CMAKE_LIBRARY_OUTPUT_DIRECTORY )
    message( "LOCO> Sending generated libs to OWN build directory" )
    set( CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/libs" )
else()
    message( "LOCO> Sending generated libs to EXTERNAL build directory" )
endif()

message( "LOCO> LIBRARY_OUT_DIR: ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}" )

# Configure the external dependencies
add_subdirectory( ext/pybind11 )
add_subdirectory( ext/imgui )
add_subdirectory( ext/cat1 )

# remove bullet examples from build
set( BUILD_BULLET2_DEMOS OFF CACHE BOOL "Do not build bullet-2 demos" )
set( BUILD_CPU_DEMOS OFF CACHE BOOL "Do not build bullet cpu demos" )
set( BUILD_EGL OFF CACHE BOOL "Do not build bullet-EGL" )
set( USE_DOUBLE_PRECISION OFF CACHE BOOL "Do not build with double precision support (@TODO: fixing TScalar->double)" )
set( BUILD_EXTRAS OFF CACHE BOOL "Do not build bullet-extras" )
set( BUILD_CLSOCKET OFF CACHE BOOL "Do not build bullet-clsocket" )
set( BUILD_OPENGL3_DEMOS OFF CACHE BOOL "Do not build bullet-opengl3-demos" )
set( BUILD_UNIT_TESTS OFF CACHE BOOL "Do not build bullet-unittests" )
set( BUILD_SHARED_LIBS ON CACHE BOOL "Force shared libs" )
add_subdirectory( ext/bullet )

# Configure core functionality
add_subdirectory( core )
# Configure physics backends
add_subdirectory( physics/mujoco )
add_subdirectory( physics/bullet )

# Configure loco project **********************************************************************************

# get properties defined in core library
get_property( VAR_TYSOC_PATH_RESOURCES              GLOBAL PROPERTY PROP_TYSOC_PATH_RESOURCES )
get_property( VAR_TYSOC_PATH_WORKING_DIR            GLOBAL PROPERTY PROP_TYSOC_PATH_WORKING_DIR )
get_property( VAR_TYSOC_PATH_MJCF_TEMPLATES         GLOBAL PROPERTY PROP_TYSOC_PATH_MJCF_TEMPLATES )
get_property( VAR_TYSOC_PATH_URDF_TEMPLATES         GLOBAL PROPERTY PROP_TYSOC_PATH_URDF_TEMPLATES )
get_property( VAR_TYSOC_PATH_RLSIM_TEMPLATES        GLOBAL PROPERTY PROP_TYSOC_PATH_RLSIM_TEMPLATES )
get_property( VAR_TYSOC_BACKEND_GRAPHICS_GLVIZ      GLOBAL PROPERTY PROP_TYSOC_BACKEND_GRAPHICS_GLVIZ )
get_property( VAR_TYSOC_BACKEND_GRAPHICS_MJCVIZ     GLOBAL PROPERTY PROP_TYSOC_BACKEND_GRAPHICS_MJCVIZ )
get_property( VAR_TYSOC_BACKEND_PHYSICS_MUJOCO      GLOBAL PROPERTY PROP_TYSOC_BACKEND_PHYSICS_MUJOCO )

# repeat definitions from core library, as they are not propagated up
add_definitions( -DTYSOC_PATH_RESOURCES="${VAR_TYSOC_PATH_RESOURCES}" )
add_definitions( -DTYSOC_PATH_WORKING_DIR="${VAR_TYSOC_PATH_WORKING_DIR}" )
add_definitions( -DTYSOC_PATH_MJCF_TEMPLATES="${VAR_TYSOC_PATH_MJCF_TEMPLATES}" )
add_definitions( -DTYSOC_PATH_URDF_TEMPLATES="${VAR_TYSOC_PATH_URDF_TEMPLATES}" )
add_definitions( -DTYSOC_PATH_RLSIM_TEMPLATES="${VAR_TYSOC_PATH_RLSIM_TEMPLATES}" )
add_definitions( -DTYSOC_BACKEND_GRAPHICS_GLVIZ="${VAR_TYSOC_BACKEND_GRAPHICS_GLVIZ}" )
add_definitions( -DTYSOC_BACKEND_GRAPHICS_MJCVIZ="${VAR_TYSOC_BACKEND_GRAPHICS_MJCVIZ}" )
add_definitions( -DTYSOC_BACKEND_PHYSICS_MUJOCO="${VAR_TYSOC_BACKEND_PHYSICS_MUJOCO}" )

# test all properties
message( "PROP_TYSOC_PATH_RESOURCES:            ${VAR_TYSOC_PATH_RESOURCES}" )
message( "PROP_TYSOC_PATH_WORKING_DIR:          ${VAR_TYSOC_PATH_WORKING_DIR}" )
message( "PROP_TYSOC_PATH_MJCF_TEMPLATES:       ${VAR_TYSOC_PATH_MJCF_TEMPLATES}" )
message( "PROP_TYSOC_PATH_URDF_TEMPLATES:       ${VAR_TYSOC_PATH_URDF_TEMPLATES}" )
message( "PROP_TYSOC_PATH_RLSIM_TEMPLATES:      ${VAR_TYSOC_PATH_RLSIM_TEMPLATES}" )
message( "PROP_TYSOC_BACKEND_GRAPHICS_GLVIZ:    ${VAR_TYSOC_BACKEND_GRAPHICS_GLVIZ}" )
message( "PROP_TYSOC_BACKEND_GRAPHICS_MJCVIZ:   ${VAR_TYSOC_BACKEND_GRAPHICS_MJCVIZ}" )
message( "PROP_TYSOC_BACKEND_PHYSICS_MUJOCO:    ${VAR_TYSOC_BACKEND_PHYSICS_MUJOCO}" )

# *********************************************************************************************************

# add all dependencies to include path
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/core/include" )
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/core/ext/json" )
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/core/ext/tinyxml2" )
include_directories( "${CMAKE_CURRENT_SOURCE_DIR}/physics/mujoco/include" )

# ****************************************************************************
