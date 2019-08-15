#!/bin/sh

# --------------------------------------------------------------------- #
# script/setup: Sets up this repo by cloning all required dependencies  #
# --------------------------------------------------------------------- #

echo "======== Setting up submodules -> ext/* ==========="

# rendering engine for visualizer
echo "==> Cloning wpumacay/cat1 @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/cat1.git ext/cat1

# using own imgui version to add some extra cmake-files
echo "==> Cloning wpumacay/imgui @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/imgui.git ext/imgui

# used for generating pytysoc|python bindings
echo "==> Cloning pybind/pybind11 @ github - master branch"
git submodule add --depth=1 https://github.com/pybind/pybind11.git ext/pybind11

# using own bullet3 version without all the assets and stuff
echo "==> Cloning wpumacay/bullet3 @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/bullet3.git ext/bullet3

echo "======== Setting up submodules -> core ============"

# core interface of this library (recall this repo is an extension with support for bullet)
echo "==> Cloning wpumacay/tysoc @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/tysoc.git core

echo "======= Setting up submodules -> physics/* ========"

# tysoc-mujoco backend functionality
echo "==> Cloning wpumacay/tysocMjc @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/tysocMjc.git physics/mujoco

# tysoc-bullet backend functionality
echo "==> Cloning wpumacay/tysocBullet @ github - master branch"
git submodule add --depth=1 https://github.com/wpumacay/tysocBullet.git physics/bullet
