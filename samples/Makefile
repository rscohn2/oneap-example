# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

VPL_LD_FLAGS ?= -lvpl
IPPCP_LD_FLAGS ?= -lippcp
IPP_LD_FLAGS ?= -lippcore
DAL_LD_FLAGS ?= -lonedal_core -lonedal_sequential
TBB_LD_FLAGS ?= -ltbb
DNN_LD_FLAGS ?= -ldnnl
IGC_LD_FLAGS ?= -ligc
SCALAPACK_LD_FLAGS ?= -lmkl_scalapack_lp64 -lmkl_cdft_core -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lmkl_blacs_intelmpi_lp64

FORTRAN_SAMPLES = fortran-sample
CPP_SAMPLES = cpp-sample mkl-sample tbb-sample dal-sample mpi-sample ipp-sample ippcp-sample vpl-sample dnn-sample scalapack-sample
SYCL_SAMPLES = sycl-sample
SYCL_ARGS = -fsycl -fsycl-unnamed-lambda
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

scalapack-sample: scalapack-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ ${SCALAPACK_LD_FLAGS} -lmpi
	cp $@ ${PREFIX}

scalapack-sample.out: scalapack-sample
	# need to set up environment to run
	echo mpirun ./$< > $@

tbb-sample: tbb-sample.cpp
	echo checking compiler
	touch x.cpp
	${CXX} -v -c x.cpp
	${CXX} ${CXXFLAGS} $< -o $@ ${TBB_LD_FLAGS}
	cp $@ ${PREFIX}

tbb-sample.out: tbb-sample
	./$< > $@

igc-sample: igc-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ ${IGC_LD_FLAGS}
	cp $@ ${PREFIX}

igc-sample.out: igc-sample
	./$< > $@

dal-sample: dal-sample.cpp
	${CXX} ${CXXFLAGS} -Wno-deprecated-copy -Wno-deprecated-declarations -Wno-unused-parameter $< -o $@ ${DAL_LD_FLAGS}
	cp $@ ${PREFIX}

dal-sample.out: dal-sample
	./$< > $@

mpi-sample: mpi-sample.cpp
	# Check if environment is set up
	ls ${I_MPI_ROOT}/lib/debug_mt
	${CXX} ${CXXFLAGS} $< -o $@ ${MPI_LD_FLAGS}
	${MPI_PREFIX}/bin/mpigcc $< -o $@.mpigcc
	cp $@ $@.mpigcc ${PREFIX}

mpi-sample.out: mpi-sample
	# need to set up environment to run
	# mpirun ./$< > $@
	echo mpi test
	echo test > $@

sycl-sample: sycl-sample.cpp
	${CXX} ${CXXFLAGS} ${SYCL_ARGS} $< -o $@
	cp $@ ${PREFIX}

sycl-sample.out: sycl-sample
	# need to set up environment to run
	# ./$< > $@
	echo sycl test
	echo test > $@

dpl-sample: dpl-sample.cpp
	${CXX} ${CXXFLAGS} ${SYCL_ARGS} $< -o $@
	cp $@ ${PREFIX}

dpl-sample.out: dpl-sample
	# need to set up environment to run
	# ./$< > $@
	echo sycl test
	echo test > $@

ipp-sample: ipp-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ ${IPP_LD_FLAGS}
	cp $@ ${PREFIX}

ipp-sample.out: ipp-sample
	./$< > $@

ippcp-sample: ippcp-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ ${IPPCP_LD_FLAGS}
	cp $@ ${PREFIX}

ippcp-sample.out: ippcp-sample
	./$< > $@

vpl-sample: vpl-sample.cpp
	${CXX} ${CXXFLAGS}  $< -o $@ ${VPL_LD_FLAGS}
	cp $@ ${PREFIX}

vpl-sample.out: vpl-sample
	./$< > $@

dnn-sample: dnn-sample.cpp
	${CXX} ${CXXFLAGS} ${SYCL_ARGS} $< -o $@ ${DNN_LD_FLAGS}
	cp $@ ${PREFIX}

dnn-sample.out: dnn-sample
	./$< > $@

test: ${SAMPLE_OUTS}

clean:
	rm -f ${SAMPLES}
