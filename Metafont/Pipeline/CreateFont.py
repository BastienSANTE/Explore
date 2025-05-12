#!/usr/bin/env python3

import os
import os.path
import subprocess
#import fontforge
import time

glyphdict = {
    "file": "ExploreSans.mf",
    "range_start": 65,
    "range_end": 90
}

source_dir = "../Glyphs/"
source_file = "ExploreSans.mf"

def exportMFGlyphs(dict):
    subprocess.run(["mpost", "&mfplain", source_file])

    
print("Going to" + source_dir + source_file)
if os.path.isfile(source_dir + source_file):
    print("File is present. Starting SVG export")
    exportMFGlyphs(glyphdict)
else:
    print("File is missing")

    
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
