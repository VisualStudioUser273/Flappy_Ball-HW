import pgzrun

WIDTH=800
HEIGHT=800
GRAVITY = 2000.00 #pixels per second 
class Ball():
    def __init__(self,initialx,initialy,radius,color):
        self.x=initialx
        self.y=initialy
        self.r=radius
        self.c=color
        self.vx = 200
        self.vy = 0



    def drawcircle(self): 
            screen.draw.filled_circle((self.x,self.y),self.r,self.c)


ball1=Ball(50,60,30,'Orange')
ball2=Ball(150,20,47,'Purple')
ball3=Ball(542,10,30,'Blue' )

def draw():
    screen.fill(color='ForestGreen')
    ball1.drawcircle()
    ball2.drawcircle()
    ball3.drawcircle()



def update(dt):
     uy = ball1.vy
     uy = ball2.vy
     uy = ball3.vy
     ball1.vy += GRAVITY * dt    
     ball1.y += (uy + ball1.vy) *0.5* dt
   
     ball2.y += GRAVITY * dt    
     ball2.y += (uy + ball2.vy) *0.5* dt
     ball3.y += GRAVITY * dt
     ball3.y += (uy + ball3.vy) *0.5* dt
     if ball1.x<0 or ball1.x>800:
          ball1.vx=-ball1.vx



                               
     if ball1.y>800:
          ball1.vy = -ball1.vy*0.9
          ball1.y=800


     if ball2.y>800:
          ball2.vy = -ball2.vy*0.7892
          ball2.y=800

     if ball2.x<0 or ball2.x>800:
         ball2.vx=-ball2.vx

     if ball3.y>800:
          ball3.vy = -ball3.vy*0.7892
          ball2.y=-ball2.vx


     if ball3.x<0 or ball3.x>800:
          ball3.vx=-ball3.vx

     ball1.x+= ball1.vx*dt 
     ball2.x+= ball2.vx*dt
     ball3.x+= ball3.vx*dt
              

    
def on_key_down(key):
     if key == keys.SPACE:
          ball1.vy = -500

     if key == keys.UP:
          ball2.vy = -600


     if key == keys.DOWN:
          ball3.vy=-200



            
pgzrun.go()    