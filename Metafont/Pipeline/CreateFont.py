#!/usr/bin/env python3

import os
import os.path
import subprocess
#import fontforge
import time

svgfolder : str = "../MFExport/"

latin1 = {
    "set": "Latin1",
    "file": "../Glyphs/Latin1/",
    "range_start": 65,
    "range_end": 128
}


def exportMFGlyphs(dict):
    for id in range(dict["range_start"], dict["range_end"]):

        input_name = str(id) + ".mf"
        output_name = str(id) + ".svg"
        
        fullpath = (dict["file"] + input_name)
        
        if os.path.isfile(fullpath):
            print(f"File {id}.mf exists. Starting MPost for SVG export")
            subprocess.run(["mpost", "-mem=mfplain", fullpath])
            
            print(f"Moving {output_name} to export folder")
            subprocess.run(["mv", output_name, (svgfolder)])
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
