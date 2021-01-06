spack install oneapi-test-basic with_gcc=True
spack install oneapi-test-basic%oneapi
spack install oneapi-test-virtual%oneapi ^intel-oneapi-mpi ^intel-oneapi-mkl
