// SPDX-FileCopyrightText: 2020 Intel Corporation
//
// SPDX-License-Identifier: MIT

#include <iostream>

#include "ippcp.h"

int main() {
  const IppLibraryVersion *lib;

  /* Get IPP Cryptography library version info */
  lib = ippcpGetLibVersion();
  std::cout << lib->Name << " " << lib->Version << std::endl;

  return 0;
}
