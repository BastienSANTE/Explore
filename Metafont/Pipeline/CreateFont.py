#!/usr/bin/env python3

import os
import os.path
import subprocess
#import fontforge
import time

latin1 = {
    "set": "Latin1",
    "file": "../Glyphs/Latin1/",
    "range_start": 65,
    "range_end": 90
}


def exportMFGlyphs(dict):
    for id in range(dict["range_start"], dict["range_end"]):

        fullpath = (dict["file"] + str(id) + ".mf")
        
        if os.path.isfile(fullpath):
            print("File exists. Starting MPost for SVG export")
            subprocess.run(f"mpost -mem=mfplain {fullpath}")
            
        else:
            print(f"File {fullpath} does not exist")



exportMFGlyphs(latin1)

time.sleep(1)



"""
for g in range(65, 90):
    filename = "{}.svg".format(g)
    g = testfont.createChar(g)
    g.importOutlines(filename)
    g.right_side_bearing = 0

    

testfont.save("Explore.sfd")
testfont.generate("Explore.ttf")
"""
