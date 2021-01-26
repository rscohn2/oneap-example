.. SPDX-FileCopyrightText: 2020 Intel Corporation
..
.. SPDX-License-Identifier: MIT

==================
oneapi-spack-tests
==================

.. image:: https://github.com/rscohn2/oneapi-spack-tests/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/rscohn2/oneapi-spack-tests/actions?query=workflow%3A.github%2Fworkflows%2Fci.yml

.. image:: https://api.reuse.software/badge/github.com/rscohn2/oneapi-spack-tests
   :target: https://api.reuse.software/info/github.com/rscohn2/oneapi-spack-tests
   :alt: REUSE status

The files here test oneapi support in spack. It installs compilers,
and uses the icpx and gcc to build programs that use the oneapi
libraries and SYCL. It uses a sample package that contains programs
that use oneAPI components.

It tests the following:

* intel-oneapi-* packages as dependencies
* include directories are accessible
* library directories are accessible
* packages provide correct configuration when used as a virtual
  provider
* environment variables are set

When appropriate, the tests are performed using both intel compilers
and gcc.

Setup spack::

  git clone https://github.com/spack/spack.git
  source spack/share/spack/setup-env.sh

Install prerequisites for testing::

  pip install -r requirements.txt

Run all tests::

  pre-commit run --all

Only run package tests::

  pre-commit run --all package-tests

The sample applications are in the samples_ directory. The spack
package that downloads/builds/installs the sample applications is in
the repo_ directory.

.. _samples:: samples
.. _repo:: repo
