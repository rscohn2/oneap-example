# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

# flake8: noqa

from spack import *


class OneapiTestBasic(Package):
    """Test oneapi package for spack."""

    homepage = "https://github.com/rscohn2/oneapi-spack-tests"
    url = "https://github.com/rscohn2/oneapi-spack-tests/tarball/main"

    maintainers = ["rscohn2"]

    variant('virtual', default=False, description='Use virtual dependences')
    variant('all', default=False, description='Use all samples')
    samples = ['cpp', 'fortran', 'sycl', 'mkl', 'tbb', 'dal', 'mpi', 'ipp']
    components = ['tbb', 'dal', 'mkl', 'mpi', 'ipp']
    for c in samples:
        variant(c, default=False, description=f'Test {c}')
        if c in components:
            depends_on(f'intel-oneapi-{c}', when=f'+{c}')
            depends_on(f'intel-oneapi-{c}', when='+all')

    depends_on('tbb', when='+tbb +virtual')
    depends_on('mkl', when='+mkl +virtual')
    depends_on('mpi', when='+mpi +virtual')

    version(
        '0.1',
        sha256='1a3294b10711cb84da1dca07c0f176b'
        '0b1c01273fde2f5cc836cd8f60c4d3a3c',
    )

    def install(self, spec, prefix):
        targets = []
        for c in OneapiTestBasic.samples:
            if '+all' in self.spec or f'+{c}' in self.spec:
                targets.append(f'{c}-sample.out')
        make('-C', 'samples', "PREFIX={0}".format(prefix), *targets)
