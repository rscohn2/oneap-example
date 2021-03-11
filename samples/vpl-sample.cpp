// SPDX-FileCopyrightText: 2020 Intel Corporation
//
// SPDX-License-Identifier: MIT

#include <stdio.h>

#include "vpl/mfxdispatcher.h"
#include "vpl/mfxvideo.h"

int main()
{

    mfxLoader loader = NULL;
    mfxU32 framenum = 0;

    // Initialize VPL session for video processing
    loader = MFXLoad();

    printf("%s\n", "MFXLoad failed"); 
    MFXUnload(loader);
    printf("Number of frames = %d\n", framenum);

    return 0;
}
