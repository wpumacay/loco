
# Configure dependencies
message( "Configuring external dependencies" )

# build spdlog as a shared library
set( SPDLOG_BUILD_SHARED ON CACHE BOOL "Build shared library" )
# avoid building cat1 examples
set( CAT1_BUILD_EXAMPLES OFF CACHE BOOL "Do not build cat1 examples" )

add_subdirectory( imgui )
add_subdirectory( spdlog )
add_subdirectory( cat1 )
add_subdirectory( pybind11 )

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

add_subdirectory( bullet3 )