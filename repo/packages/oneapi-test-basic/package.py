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

    variant('ilp64', default=False, description='Use ilp64')
    variant('virtual', default=False, description='Use virtual dependences')
    variant('all', default=False, description='Use all samples')
    samples = [
        'cpp',
        'dal',
        'dnn',
        'dpl',
        'fortran',
        'ipp',
        'ippcp',
        'mkl',
        'mpi',
        'sycl',
        'tbb',
        'vpl',
    ]
    components = [
        'dal',
        'dnn',
        'dpl',
        'ipp',
        'ippcp',
        'mkl',
        'mpi',
        'tbb',
        'vpl',
    ]
    for c in samples:
        variant(c, default=False, description=f'Test {c}')
        if c in components:
            depends_on(f'intel-oneapi-{c}', when=f'+{c} -virtual')
            depends_on(f'intel-oneapi-{c}', when='+all -virtual')
    depends_on(f'intel-oneapi-mpi +ilp64', when='+mpi -virtual +ilp64')
    depends_on(f'intel-oneapi-mkl +ilp64', when='+mkl -virtual +ilp64')

    depends_on('tbb ^intel-oneapi-tbb', when='+tbb +virtual')
    depends_on('mkl ^intel-oneapi-mkl', when='+mkl +virtual')
    depends_on('mpi ^intel-oneapi-mpi', when='+mpi +virtual')

    version('main')

    def install(self, spec, prefix):
        targets = []
        for c in OneapiTestBasic.samples:
            if '+all' in self.spec or f'+{c}' in self.spec:
                if c == 'mpi':
                    targets.append(
                        f'MPI_PREFIX={self.spec["mpi"].prefix}/mpi/latest'
                    )
                    targets.append(
                        f'MPI_LD_FLAGS={self.spec["mpi"].libs.ld_flags}'
                    )
                if c == 'mkl':
                    targets.append(
                        f'MKL_LD_FLAGS={self.spec["blas"].libs.ld_flags}'
                    )
                targets.append(f'{c}-sample.out')
        make(
            '-C',
            'samples',
            f'PREFIX={prefix}',
            *targets,
        )
