.. SPDX-FileCopyrightText: 2020 Intel Corporation
..
.. SPDX-License-Identifier: MIT

==================
oneapi-spack-tests
==================

.. image:: https://github.com/rscohn2/oneapi-spack-tests/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/rscohn2/oneapi-spack-tests/actions?query=workflow%3A.github%2Fworkflows%2Fci.yml

.. image:: https://github.com/rscohn2/oneapi-spack-tests/workflows/.github/workflows/checks.yml/badge.svg
   :target: https://github.com/rscohn2/oneapi-spack-tests/actions?query=workflow%3A.github%2Fworkflows%2Fchecks.yml

.. image:: https://api.reuse.software/badge/github.com/rscohn2/oneapi-spack-tests
   :target: https://api.reuse.software/info/github.com/rscohn2/oneapi-spack-tests
   :alt: REUSE status

The files here test oneapi support in spack. It installs compilers,
and uses the icpx and gcc to build programs that use the oneapi
libraries and SYCL.

Setup spack and install compilers::

  git clone https://github.com/spack/spack.git
  source spack/share/spack/setup-env.sh
  spack install intel-oneapi-compilers
  spack compiler add `spack location -i intel-oneapi-compilers`/compiler/latest/linux/bin
  spack compiler add `spack location -i intel-oneapi-compilers`/compiler/latest/linux/bin/intel64

Add the spack repo with test packages::

  spack repo add ./repo
  python test.py
