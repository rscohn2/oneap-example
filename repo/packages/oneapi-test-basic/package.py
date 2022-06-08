# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

# flake8: noqa

from spack import *


class OneapiTestBasic(Package):
    """Test oneapi package for spack."""

    homepage = "https://github.com/rscohn2/oneapi-spack-tests"
    git = "https://github.com/rscohn2/oneapi-spack-tests.git"
    version('main', branch='main')
    version('igc-test', branch='dev/igc')

    maintainers = ["rscohn2"]

    variant(
        'external-libfabric',
        default=False,
        description='Use external libfabric with mpi',
    )
    variant('scalapack', default=False, description=f'Test scalapack')
    variant('ilp64', default=False, description='Use ilp64')
    variant('virtual', default=False, description='Use virtual dependences')
    variant('all', default=False, description='Use all samples')
    samples = [
        'cpp',
        'dal',
        'dnn',
        'dpl',
        'fortran',
        'igc',
        'ipp',
        'ippcp',
        'mkl',
        'mpi',
        'scalapack',
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
    depends_on(
        f'intel-oneapi-mpi +external-libfabric',
        when='+mpi -virtual +external-libfabric',
    )
    depends_on(f'intel-oneapi-mpi +ilp64', when='+mpi -virtual +ilp64')
    depends_on(f'intel-oneapi-mkl +ilp64', when='+mkl -virtual +ilp64')

    depends_on('igc', when='+igc +virtual')
    depends_on('tbb', when='+tbb +virtual')
    depends_on('mkl', when='+mkl +virtual')
    depends_on('mpi', when='+mpi +virtual')
    depends_on('scalapack', when='+scalapack +virtual')

    version('main')

    def install(self, spec, prefix):
        targets = []
        for c in OneapiTestBasic.samples:
            if '+all' in self.spec or f'+{c}' in self.spec:
                if c == 'mpi':
                    targets.append(
                        f'MPI_PREFIX={self.spec["mpi"].prefix}/mpi/latest'
                    )
                if c in ['scalapack', 'mkl', 'mpi', 'igc']:
                    targets.append(
                        f'{c.upper()}_LD_FLAGS={self.spec[c].libs.ld_flags}'
                    )
                targets.append(f'{c}-sample.out')
        make(
            '-C',
            'samples',
            f'PREFIX={prefix}',
            *targets,
        )
