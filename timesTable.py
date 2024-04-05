from LED import *

set_window_scale(7)

W, H = get_width_adjusted(), get_height_adjusted()

#draw_text(4,4,"Hello World!",CYAN)

center = (W/2,H/2)
radius = 25
points = 1

def posOfNum(num):
    return (center[0]+math.cos(2*math.pi/points*num)*radius,center[1]+math.sin(2*math.pi/points*num)*radius)


direction = 1

multiplier = 0

while True:
    refresh()
    #color = (255 *(0.5 + 0.5*math.cos(time.time())),255*(0.5 + 0.5*math.cos(time.time()+2)),255*(0.5 + 0.5*math.cos(time.time()+4)))

    for i in range(1,points):
        pos = posOfNum(i)
        pos2 = posOfNum(multiplier*i)
        #color = (255,255,255)
        color = (255*(1-i/points),0,255*(i/points))
        draw_line(pos[0],pos[1],pos2[0],pos2[1],color)
        
    draw_text(5,H-10,"x"+str(multiplier),WHITE,6)
    draw_text(W-15,H-10,str(points),WHITE,6)

    #time.sleep(.01)
    points+=direction
    if points > 50:
        direction*=-1
    if points < 2:
        direction*=-1
        multiplier+=1
    
    if multiplier > 10:
        multiplier = 0
        
    draw()
