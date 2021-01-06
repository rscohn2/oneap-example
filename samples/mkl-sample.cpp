#include <iostream>

#include "mkl.h"

int main() {
  int len = 200;
  char buf[len];
  
  mkl_get_version_string(buf, len);
  std::cout << buf << "\n";

  return 0;
}

