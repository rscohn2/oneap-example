// SPDX-FileCopyrightText: 2020 Intel Corporation
//
// SPDX-License-Identifier: MIT

#include <iostream>

#include "ippcore.h"

int main() {
  const IppLibraryVersion *lib;

  /* Get IPP library version info */
  lib = ippGetLibVersion();
  std::cout << lib->Name << " " << lib->Version << std::endl;

  return 0;
}
