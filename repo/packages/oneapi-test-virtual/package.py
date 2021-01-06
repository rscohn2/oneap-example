# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install oneapi-example-git
#
# You can edit this file again by typing:
#
#     spack edit oneapi-example-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class OneapiTestVirtual(Package):
    """Test oneapi package for spack."""

    homepage = 'https://github.com/rscohn2/oneapi-example'

    maintainers = ['rscohn2']

    version('0.1', sha256='655421c3018ed5bcf26a89ab03cc226328cc36f3cfedaba95a01d6fed6579d12')

    depends_on('intel-oneapi-dal')
    depends_on('intel-oneapi-tbb')
    depends_on('mkl')
    depends_on('mpi')

    def url_for_version(self, version):
        url = 'https://github.com/rscohn2/oneapi-example/archive/v{0}.tar.gz'
        return url.format(version)

    def install(self, spec, prefix):
        make()
        make('install', 'prefix={0}'.format(prefix))
