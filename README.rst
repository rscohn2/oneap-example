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
libraries and SYCL.

Setup spack::

  git clone https://github.com/spack/spack.git
  source spack/share/spack/setup-env.sh

Install prerequisites for testing::

  pip install -r requirements.txt

Run tests::

  pre-commit run --all

Rerun package tests::

  pre-commit run --all package-tests
