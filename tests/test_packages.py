# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

import subprocess

import pytest


def shell(cmd, check=True, capture_output=False, modify=False):
    print(cmd)
    return subprocess.run(
        cmd, shell=True, check=check, capture_output=capture_output
    )


# checksums are not right because source is in this repo fail-fast is
# needed to make spack return a non zero error code when a dependency
# fails
install_cmd = 'spack install --no-checksum --fail-fast'


# Split into seperate lists because github actions runners have
# limited disk space
icx1_samples = [
    'cpp',
    'fortran',
    'sycl',
    'mkl',
    'mpi',
    'tbb',
]

icx2_samples = [
    'dal',
    'vpl',
    'ipp',
    'ippcp',
]


@pytest.mark.parametrize('sample', icx1_samples)
def test_icx_1(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%oneapi +{sample}')


@pytest.mark.parametrize('sample', icx2_samples)
def test_icx_2(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%oneapi +{sample}')


icc1_samples = [
    'cpp',
    'fortran',
    'mkl',
    'mpi',
    'tbb',
]

icc2_samples = [
    'dal',
    'ipp',
    'ippcp',
    'vpl',
]


@pytest.mark.parametrize('sample', icc1_samples)
def test_icc_1(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%intel +{sample}')


@pytest.mark.parametrize('sample', icc2_samples)
def test_icc_2(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%intel +{sample}')


# build with icx using virtual dependencies
virtual_components = [
    'tbb',
    'mkl',
    'mpi',
]


@pytest.mark.parametrize('component', virtual_components)
def test_virtual(clean, component):
    shell(f'{install_cmd} oneapi-test-basic +virtual +{component}')


# build with gcc
gcc1_samples = [
    'cpp',
    'fortran',
    'dal',
    'mkl',
    'mpi',
    'tbb',
]

gcc2_samples = [
    'ipp',
    'ippcp',
    'vpl',
]


@pytest.mark.parametrize('sample', gcc1_samples)
def test_gcc_1(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic +{sample}')
    if sample in virtual_components:
        shell(f'{install_cmd} oneapi-test-basic +virtual +{sample}')


@pytest.mark.parametrize('sample', gcc2_samples)
def test_gcc_2(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic +{sample}')
    if sample in virtual_components:
        shell(f'{install_cmd} oneapi-test-basic +virtual +{sample}')


@pytest.mark.parametrize('component', ['tbb'])
def test_load(component):
    package = f'intel-oneapi-{component}'
    out_file = f'{component}-sample.out'
    shell(
        '. spack/share/spack/setup-env.sh && '
        f'spack install {package} && '
        f'spack load {package} && '
        f'make -C samples {out_file}'
    )
