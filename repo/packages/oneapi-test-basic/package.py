# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class OneapiTestBasic(Package):
    """Test oneapi package for spack."""

    homepage = 'https://github.com/rscohn2/oneapi-spack-tests'
    url = 'https://github.com/rscohn2/oneapi-spack-tests/tarball/main'

    maintainers = ['rscohn2']

    variant('sycl', default=True, description='Include tests that depend on SYCL support in the compiler')

    version('0.1', sha256='655421c3018ed5bcf26a89ab03cc226328cc36f3cfedaba95a01d6fed6579d12')

    depends_on('intel-oneapi-dal')
    depends_on('intel-oneapi-tbb')
    depends_on('intel-oneapi-mkl')
    depends_on('intel-oneapi-mpi')

    def install(self, spec, prefix):
        sycl = '+sycl' in self.spec
        sycl_samples = '' if scyl else 'SYCL_SAMPLES='
        make('-C', 'samples', sycl_samples)
        make('-C', 'samples', 'install', 'PREFIX={0}'.format(prefix), sycl_samples)
