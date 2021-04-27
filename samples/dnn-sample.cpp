// SPDX-FileCopyrightText: 2021 Intel Corporation
//
// SPDX-License-Identifier: MIT

#include <iostream>

#include "dnnl.hpp"

int main() {

  if (dnnl::engine::get_count(dnnl::engine::kind::gpu) == 0) {
    std::cout << "No GPU found, please run the application on CPU."
              << std::endl;
  } else {
    std::cout << "Number of GPUs on the system "
              << dnnl::engine::get_count(dnnl::engine::kind::gpu) << std::endl;
  }
  return 0;
}
