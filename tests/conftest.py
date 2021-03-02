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


def output_to_list(output):
    return output.strip().decode('utf-8').split('\n')


def oneapi_packages():
    res = shell('spack list | grep intel-oneapi', capture_output=True)
    return output_to_list(res.stdout)


@pytest.fixture
def all_packages():
    return oneapi_packages()


@pytest.fixture(scope='session')
def clean():
    shell('spack uninstall --all -y oneapi-test-basic', check=False)
