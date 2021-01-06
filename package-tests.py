# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from subprocess import run


def check(cmd):
    print(cmd)
    run(cmd, shell=True, check=True)


specs = [
    'oneapi-test-basic%oneapi',
    # test virtual dependencies
    'oneapi-test-virtual%oneapi ^intel-oneapi-mpi ^intel-oneapi-mkl ^intel-oneapi-tbb',
    # use g++ and skip SYCL sample
    'oneapi-test-basic sycl=False',
]

for package in specs:
    check(f'spack install --no-checksum {package}')
