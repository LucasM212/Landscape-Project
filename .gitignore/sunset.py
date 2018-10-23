height2 = -100
x = 320
x2 = -100
x3 = 640
height3 = 240

def setup():
    size(640, 480)
    
def draw():
    
    global x
    global height2
    global x2
    global x3
    global height3
    
    if height2 >= 640:
        height2 = -100
    height2 += 1
    
    if x2 >= 800:
        x2 = -100
    x2 += 1
    
    if x3 <= -100:
        x3 = 640
    x3 -= 1
    
    background(139, 90, 0)
    
    noStroke()
    fill(255,255,0)
    ellipse(x, height2, 100, 100)
    
    fill(255, 255, 255)
    ellipse(x2, height/2, 50, 50)
    ellipse(x2+30, height/2, 50, 50)
    ellipse(x2+10, height/2-20, 50, 50)
    
    fill(255, 255, 255)
    ellipse(x3, height3, 50, 50)
    ellipse(x3+30, height3, 50, 50)
    ellipse(x3+10, height3-20, 50, 50)
