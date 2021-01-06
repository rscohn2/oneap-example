==================
oneapi-spack-tests
==================

The files here test oneapi support in spack. There are sample programs
to build in samples and some packages to install in repo.

To test, setup spack for use. Add the test repo::

  spack repo add ./repo




Sample program and spack package to install it to test

Simple example for oneapi components to verify build environment is
properly configured. Created for spack and other package managers.

Build::

  CXX=icpx make

Make targets: ``all``, ``clean``, ``test``, ``install``
