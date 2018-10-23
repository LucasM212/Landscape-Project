height2 = -100
x = 320
x2 = -100

def setup():
    size(640, 480)
    
def draw():
    
    global x
    global height2
    global x2
    
    if height2 >= 480:
        height2 = -100
    height2 += 2
    
    if x2 >= 640:
        x2 = -100
    x2 += 2
    
    background(139, 90, 0)
    
    noStroke()
    fill(255,255,0)
    ellipse(x, height2, 100, 100)
    
    fill(255, 255, 255)
    ellipse(x2, height/2, 50, 50)
    ellipse(x2+30, height/2, 50, 50)
    ellipse(x2+10, height/2-20, 50, 50)
