#!/usr/bin/env python3

import os
import os.path
import subprocess
import shutil
import fontforge
import time

from collections import deque

svgfolder : str = "../MFExport/"

latin1 = {
    "set": "Latin1",
    "file": "../Glyphs/Latin1/",
    "range_start": 0,
    "range_end": 128
}


currentfont = fontforge.font()
monowidth = 600

for currentglyph in range(0, 127):
    filename = "{}.svg".format(currentglyph)
    if os.path.isfile(svgfolder + filename):

        # Create a "buffer glyph" to import boxed drawings
        tempglyph = currentfont.createChar(1)

        tempglyph.importOutlines(svgfolder + filename, scale=True)

        # Iterate through contours except 1st one (the bounding box)
        contour_layer = tempglyph.foreground
        contour_list = contour_layer.__iter__()
        
        # Move the glyph so that the lower left corner of
        # the bounding box aligns with the X origin of
        # the final glyph

        # Create actual glyph with correct code
        finalglyph = currentfont.createChar(currentglyph)
        finalfg = finalglyph.foreground

        contours = len(contour_layer)
        print(f"Glyph {currentglyph} has {contours} paths including BBox")

        # Get distance from left side of BBox to glyph origin
        # -> Get contour list -> last contour -> 1st point -> X value
        bbox_origin = contour_layer[contours - 1][0].x
        bbox_right = contour_layer[contours - 1][1].x
        
        print(f"BBox is {bbox_origin} units from X origin")

        # Create matrix to move all contours as to align BBox
        # to glyph origin
        origin_align_matrix = psMat.translate(bbox_origin, 0)
        
        # Copy all contours one by one
        for i in range(contours - 1):
                finalglyph.foreground += contour_layer[i]
                print(contour_layer[i])
                
        print(contour_layer[contours - 1])
        finalglyph.foreground.transform(origin_align_matrix)
                
        # Set metrics width of glyph to match bounding box
        # Add the bounding box coordinate to the other side
        # to get the true width
        finalglyph.width = (int)(bbox_right - bbox_origin)
        
        #finalglyph.width = monowidth
        
        # Clear buffer for next glyph
        tempglyph.clear()
    else:
        print(f"SVG file {filename} does not exist.")

        
currentfont.save("Explore_Test.sfd")
