import fontforge

filename : str = ""

testfont = fontforge.font()


for g in range(65, 90):
    filename = "{}.svg".format(g)
    g = testfont.createChar(g)
    g.importOutlines(filename)
    g.right_side_bearing = 0


testfont.save('Explore.sfd')
