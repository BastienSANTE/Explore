#!/usr/bin/env python3

import os
import os.path
import subprocess
import shutil
#import fontforge
import time

svgfolder : str = "../MFExport/"

latin1 = {
    "set": "Latin1",
    "file": "../Glyphs/Latin1/",
    "range_start": 0,
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
            shutil.move(output_name, svgfolder + output_name)
            #subprocess.run(["mv", output_name, (svgfolder)])
        else:
            print(f"File {fullpath} does not exist")



exportMFGlyphs(latin1)

time.sleep(1)

testfont = fontforge.font()

for g in range(65, 127):
    filename = "{}.svg".format(g)
    if os.path.isfile(svgfolder + filename):   
        g = testfont.createChar(g)
        g.importOutlines(svgfolder + filename)
        g.right_side_bearing = 0
    else:
        print(f"SVG file {filename} does not exist.")

        
testfont.save("Explore.sfd")
testfont.generate("Explore.ttf")
