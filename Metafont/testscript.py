import fontforge

glypharray = [65, 66, 67, 68, 69, 70, 71]

fn = "";

testfont = fontforge.font()



for g in glypharray:
    fn = "{}.svg".format(g)
    g = testfont.createChar(g)
    g.importOutlines(fn)
    g.right_side_bearing = 0;



testfont.save('font.sfd')
