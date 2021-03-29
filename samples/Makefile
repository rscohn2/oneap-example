# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

FORTRAN_SAMPLES = fortran-sample
CPP_SAMPLES = cpp-sample mkl-sample tbb-sample dal-sample mpi-sample ipp-sample ippcp-sample vpl-sample
SYCL_SAMPLES = sycl-sample
PREFIX = /dev/null

SAMPLES = ${CPP_SAMPLES} ${SYCL_SAMPLES} ${FORTRAN_SAMPLES}
SAMPLE_OUTS = $(foreach s,${SAMPLES},${s}.out)

CXXFLAGS += -Wall

all: ${SAMPLES}

fortran-sample: fortran-sample.f90
	${FC}  $< -o $@
	cp $@ ${PREFIX}

fortran-sample.out: fortran-sample
	./$< > $@

cpp-sample: cpp-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@
	cp $@ ${PREFIX}

cpp-sample.out: cpp-sample
	./$< > $@

mkl-sample: mkl-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ ${MKL_LD_FLAGS}
	cp $@ ${PREFIX}

mkl-sample.out: mkl-sample
	./$< > $@

tbb-sample: tbb-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ -ltbb
	cp $@ ${PREFIX}

tbb-sample.out: tbb-sample
	./$< > $@

dal-sample: dal-sample.cpp
	${CXX} ${CXXFLAGS} -Wno-deprecated-copy -Wno-deprecated-declarations -Wno-unused-parameter $< -o $@ -lonedal_core -lonedal_sequential
	cp $@ ${PREFIX}

dal-sample.out: dal-sample
	./$< > $@

mpi-sample: mpi-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ -lmpi
	cp $@ ${PREFIX}

mpi-sample.out: mpi-sample
	# need to set up environment to run
	# mpirun ./$< > $@
	echo mpi test
	echo test > $@

sycl-sample: sycl-sample.cpp
	${CXX} ${CXXFLAGS} -fsycl -fsycl-unnamed-lambda $< -o $@
	cp $@ ${PREFIX}

sycl-sample.out: sycl-sample
	# need to set up environment to run
	# ./$< > $@
	echo sycl test
	echo test > $@

ipp-sample: ipp-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ -lippcore
	cp $@ ${PREFIX}

ipp-sample.out: ipp-sample
	./$< > $@

ippcp-sample: ippcp-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ -lippcp
	cp $@ ${PREFIX}

ippcp-sample.out: ippcp-sample
	./$< > $@

vpl-sample: vpl-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ -lmfx
	cp $@ ${PREFIX}

vpl-sample.out: vpl-sample
	./$< > $@

test: ${SAMPLE_OUTS}

clean:
	rm -f ${SAMPLES}
