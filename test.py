from subprocess import run

# test compiler and all libraries with icpc
run('spack install oneapi-test-basic%oneapi', shell=True)

# use virtual dependences for mpi and mkl
run('spack install oneapi-test-virtual%oneapi ^intel-oneapi-mpi ^intel-oneapi-mkl', shell=True)

# test libraries with g++
run('spack install oneapi-test-basic sycl=False', shell=True)

