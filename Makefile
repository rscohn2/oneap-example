SAMPLES = mkl-sample tbb-sample dal-sample mpi-sample sycl-sample

CXXFLAGS += -W

all: ${SAMPLES}

mkl-sample: mkl-sample.cpp
	${CXX} ${CXXFLAGS} -DMKL_ILP64 $< -o $@ -lmkl_intel_ilp64 -lmkl_sequential -lmkl_core

tbb-sample: tbb-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ -ltbb

dal-sample: dal-sample.cpp
	${CXX} ${CXXFLAGS} -Wno-deprecated-declarations -Wno-unused-parameter $< -o $@ -lonedal_core -lonedal_sequential

mpi-sample: mpi-sample.cpp
	${CXX} ${CXXFLAGS} $< -o $@ -lmpi

sycl-sample: sycl-sample.cpp
	${CXX} ${CXXFLAGS} -fsycl -fsycl-unnamed-lambda $< -o $@

install:
	cp ${SAMPLES} ${prefix}

test: ${SAMPLES}
	./mkl-sample
	./tbb-sample
	./dal-sample
	./sycl-sample
	mpirun ./mpi-sample

clean:
	rm -f ${SAMPLES}

