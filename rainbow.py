from LED import *
from math import cos

W, H = get_width_adjusted(), get_height_adjusted()

def shader(x,y):
    uv = (x/W,y/H)
    color = (255 *(0.5 + 0.5*cos(time.time()+uv[0])),255*(0.5 + 0.5*cos(time.time()+uv[1]+2)),255*(0.5 + 0.5*cos(time.time()+uv[0]+4)))
    return color

while True:
    # draw each pixel
    for x in range(W):
        for y in range(H):
            
            draw_pixel(x,y,shader(x,y))

    draw()
