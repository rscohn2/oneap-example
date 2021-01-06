========================
 oneapi-test-spack-repo
========================

This repo contains packages that are used to test oneapi spack
integration.

Testing Spack
=============

1. Install spack
2. Clone this repo
3. Add it to spack::

     spack repo add oneapi-test-spack-repo

4. List the tests::

     spack list oneapi-test

5. Install basic package using oneapi compiler

     spack install oneapi-test-basic%oneapi
