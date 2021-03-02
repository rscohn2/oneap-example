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


install_cmd = 'spack install --no-checksum'


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
]


@pytest.mark.parametrize('sample', icx1_samples)
def test_icx1(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%oneapi +{sample}')


@pytest.mark.parametrize('sample', icx2_samples)
def test_icx2(clean, sample):
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
]


@pytest.mark.parametrize('sample', icc1_samples)
def test_icc1(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic%intel +{sample}')


@pytest.mark.parametrize('sample', icc2_samples)
def test_icc2(clean, sample):
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
gcc_samples = [
    'cpp',
    'fortran',
    'dal',
    'mkl',
    'mpi',
    'tbb',
]


@pytest.mark.parametrize('sample', gcc_samples)
def test_gcc(clean, sample):
    shell(f'{install_cmd} oneapi-test-basic +{sample}')


@pytest.mark.skip(reason='spack load does not work from python shell')
def test_load(all_packages):
    oneapi_packages = [f'{p}%gcc' for p in all_packages]
    package_list = ' '.join(oneapi_packages)
    shell(f'spack install {package_list}')
    shell(f'spack load {package_list}')
