#include <CL/sycl.hpp>

int main() {
  int data_size = 100;

  sycl::queue q;
  int *a = sycl::malloc_shared<int>(data_size, q);
  

  q.parallel_for(data_size, [=](auto id) { a[id] = 1; }).wait();
}
