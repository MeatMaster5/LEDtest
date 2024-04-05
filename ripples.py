#"Hypnotic ripples" By Cha
#https://www.shadertoy.com/view/ldX3zr

from LED import *
from math import cos

#set_orientation(1)
set_window_scale(7)

W, H = get_width_adjusted(), get_height_adjusted()

center = (0.5,0.5)
speed = .04

def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 
  
def shader(x,y):
    inv_ar = H/W
    uv = (x / W, y / H)
    col = (uv[0], uv[1], 0.5 + 0.5 * math.sin(time.time()))

    texcol = [0.0, 0.0, 0.0]
    x = center[0] - uv[0]
    y = (center[1] - uv[1]) * inv_ar
    #r = -math.sqrt(x * x + y * y)
    r = -(x * x + y * y)
    z = 1.0 + 0.5 * math.sin((r + time.time() * speed) / 0.013)
    texcol[0] = z
    texcol[1] = z
    texcol[2] = z

    color = (clamp(255*col[0] * texcol[0],0,255), clamp(255*col[1] * texcol[1],0,255), clamp(255*col[2] * texcol[2],0,255))
    return color


while True:
    # draw each pixel
    for x in range(W):
        for y in range(H):
            
            draw_pixel(x,y,shader(x,y))

    draw()
