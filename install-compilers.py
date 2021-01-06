# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from subprocess import run


def check(cmd):
    print(cmd)
    run(cmd, shell=True, check=True)


check('spack install intel-oneapi-compilers')
check(
    'spack compiler add `spack location -i intel-oneapi-compilers`/compiler/latest/linux/bin'
)
check(
    'spack compiler add `spack location -i intel-oneapi-compilers`/compiler/latest/linux/bin/intel64'
)
