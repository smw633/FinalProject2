add_library('minim')
import os
path = os.getcwd()
player = Minim(this)


class Creature():
    def __init__(self,x,y,r,g,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.w=w
        self.h=h
        self.F=F
        self.f=0
        self.img = loadImage(path+"/images/"+img)
        self.dir = 1


    def placeOnScreen():
        pass
        # the place on the screen should be in the middle ish??

    def update(self):

        self.x += self.vx
        self.y += self.vy

        # needs to update with the key pressed or released 
        #if moved down then new g will be the place its at
        #needs if collided with the books or balls
    def display(self):
        self.update()
        
        if self.vx != 0:
            self.f = (self.f+0.3)%self.F

        if self.dir > 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
        elif self.dir < 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h) 


class Bird(Creature):
    def __init__(self):
        Creature.__init__(self,x,y,r,g,img,w,h,F)






    def update(self):

        if self.keyHandler[LEFT] == True:
            self.vx = -5
            self.dir = -1
        elif self.keyHandler[RIGHT] == True:
            self.vx = 5
            self.dir = 1
        elif self.keyHandler[UP] == True:
            self.vy = -5
        elif self.keyHandler[DOWN] == True:
            self.vy = 5

        self.x += self.vx
        self.y += self.vy



    
class Book(Creature):#book is an enemie
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)

    points = []
    # going to create a list of points that are in a lost and then the book will go to these new points

    def update(self):
        pass
        # new position will be the new points


    def display(self):
        self.update()

class Book2(Book):#book2 is an enemie (same attributes as book just different)
    def __init__(self,x,y,r,g,img,w,h,F):
        Book.__init__(self,x,y,r,g,img,w,h,F)

    points = []
    # going to create a list of points that are in a lost and then the book will go to these new points

    def update(self):
        pass
        # new position will be the new points



    def display(self):
        self.update()


class Ball():
    def __init__(self):
        self.x = x
        self.y = y
        self.r = r
        self.img = loadImage(path+"/images"+img)
        self.g = g
        self.b = "no" #this will indicate whether the ball will bounce or not 


    def update(self):

    def display(self):



class BB(Ball): #basketball
    def __init__(self):
        Ball.__init__(x,y,r,img,g,b):






    def update(self):

    def display(self):
        

class PB(Ball): #pool ball
    def __init__(self):
        Ball.__init__(x,y,r,img,g,b):


    def update(self):

    def display(self):


class Game():
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.state = "yes"
        
        self.bird =



        self.booklist = [] # will add 2 different books to list
        for b in range(3):
            self.booklist.append(Book,,,,)
        for c in range(3):
            self.booklist.append(Book2,,,)

        self.basketballs = []
        for i in range (3):
            self.basketballs.append(BB,,,,)

        self.poolballs = []
        for j in range (5):
            self.poolballs.append(PB) #- need to chose random ball either here or in class



    def display(self):

        for i in self.basketballs:
            i.display()

        for j in self.poolballs:
            j.display()

        for b in self.booklist:
            #randomize which ones are picked to be displayed

    self.bird.display()




#time aspect


#g = Game(w,h,g)

def setup():
    size(g.w,g.h)
    background(0)

def draw():
    if g.state == 'menu':
        background(0)
        textSize(36)
        fill(255)
        rect(g.w//2, g.h//2, 250,50)
        # code for the choices 



    elif g.state == 'play':



    #box for the time
    #box for the books collected 


pass

def mouseClicked():
    #need coordinates if clicked in box of play then will play
    if g.state == 'menu' and and : # between ands are rectangle
        g.state = "play" #reassigning the state to play

    pass

def keyPressed():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=True
    elif keyCode == UP:
        g.bird.keyHandler[UP]=True
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= True



def keyReleased():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=False
    elif keyCode == UP:
        g.bird.keyHandler[UP]=False
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= False
