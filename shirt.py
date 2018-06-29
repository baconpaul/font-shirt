# pip3 install svgwrite first if you want it to work

import json
import svgwrite

from svgwrite import mm

with open('dat/Keypunch029.json') as f:
    data = json.load(f)


def drawltr(dwg, ltr, x0, y0):
    ltrbox = dwg.add(dwg.g(id='ltrbox'))
    yi = 1
    for l in ltr:
        xi = 1
        for c in l:
            # set presentation attributes at object creation as SVG-Attributes
            circle = dwg.circle(center=((xi * 5 + x0) * mm, (yi * 5 + y0) * mm), r='2.5mm')
            if c == '#':
                circle.fill('red').stroke('black', width=1)
            else:
                circle.fill('white').stroke('gray', width=0.2)
            ltrbox.add(circle)
            xi = xi + 1
        yi = yi + 1


dwg = svgwrite.Drawing(filename='out/carson-shirt.svg')

y0 = 0
for l in ['EBCDIC', 'OR', 'GTFO']:
    x0 = 0

    for c in l:
        drawltr(dwg, data[c], x0, y0)
        x0 += 30
    y0 += 40

dwg.save()
