# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from subprocess import run


def check(cmd):
    run(cmd, shell=True, check=True)


for package in [
    'oneapi-test-basic%oneapi',
    # test virtual dependencies
    'oneapi-test-virtual%oneapi ^intel-oneapi-mpi ^intel-oneapi-mkl ^intel-oneapi-tbb',
    # use g++ and skip SYCL sample
    'oneapi-test-basic sycl=False',
]:
    check(f'spack install --no-checksum {package}')
