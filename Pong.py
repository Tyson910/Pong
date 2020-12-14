'''
Tyson Suttle (Tyson910)
CSC 131
10.31.18
create ping pong program
'''

from tkinter import *

class pong(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Game of Pong")
        self.grid()
        #creating lives count
        self.lifeCount = 5
        self.livesFrame = Frame(self)
        self.livesFrame.grid(row = 0)
        self.livesLabel = Label(self.livesFrame, text = 'Lives left:   ' + str(self.lifeCount),
                                width = -800)
        self.livesLabel.grid()
        
        #creating canvas
        self.gameFrame = Frame(self)
        self.gameFrame.grid(row = 1)
        self.length = 800
        self.height = 400
        self.canvas1 = Canvas(self.gameFrame, width = self.length, height = self.height, bg = 'black')
        self.canvas1.grid()
        #initial coordinates  
        self.ball_x1 = 30
        self.ball_y1 = 10
        self.ball_x2 = 10
        self.ball_y2 = 30
        self.paddle_x1 = 360
        self.paddle_y1 = 380
        self.paddle_x2 = 440
        self.paddle_y2 = 400
        #creating circle
        self.canvas1.create_oval(self.ball_x1,self.ball_y1, self.ball_x2, self.ball_y2,
                                 fill = "green", tags = 'ball' )
        #tracking ball
        #circle coordinates
        self._dx = 2
        self._dy = 2
        self.right_x = self.ball_x2
        self.left_x = self.ball_x1
        self.bottom_y = self.ball_y2
        self.top_y = self.ball_y1
        #paddle coordinates
        self.paddleTop = self.paddle_y1
        self.paddleLeft = self.paddle_x1
        self.paddleRight = self.paddle_x2
        self._paddleDx = 5
        self._horizontalDirection = 'east'
        self._verticalDirection = 'south'
        #create paddle bar
        self.canvas1.create_rectangle(self.paddleLeft, self.paddleTop, self.paddleRight, 400, fill = 'white', tag = 'paddle')    
        #paddle bar controls
        self.canvas1.bind("<Key>", self.paddleNavigation)
        self.canvas1.focus_set() # Set canvas in focus

        #initiate gameplay
        self.play()
        
    def play(self):
        while self.lifeCount >= 0:
            #moves ball to the right
            if self._horizontalDirection == 'east' :
                    #keeping track of ball
                    self.right_x += self._dx
                    self.left_x += self._dx
                    #changing horizontal direction 
                    if self.right_x >= self.length:
                        self._horizontalDirection = 'west'
                        
                    #animation function 
                    self.eastMovement()                         
                
            #moves ball to the left
            if self._horizontalDirection == 'west' :
                    #keeping track of ball
                    self.right_x -= self._dx
                    self.left_x -= self._dx
                    #changing horizontal direction
                    if self.left_x <= 0:
                        self._horizontalDirection = 'east'
                        
                    #animation function    
                    self.westMovement()
                    
            if self.lifeCount <= 0 :
                #deleting ball and staring in corner
                self.canvas1.delete('ball') 
                #creating new circle
                self.canvas1.create_oval(self.ball_x1,self.ball_y1, self.ball_x2, self.ball_y2,
                                 fill = "green", tags = 'ball2' )
            else:
                self.livesLabel = Label(self.livesFrame, text = 'Sorry you lost!',
                        width = -800)


#creating animation for pong ball                        
    def westMovement(self):
        #decides vertical direction
        self.northSouthMovement()
        #creating animation    
        if self._verticalDirection == 'south':
            self.top_y += self._dy
            self.bottom_y += self._dy
            self.canvas1.move("ball", -self._dx, self._dy)
            self.canvas1.after(15)
            self.canvas1.update()
            if (self.bottom_y >= self.height) and (self.isBallInPaddle() == False) :
                    self.lifeCount -= 1
                    self.livesLabel.config(text = 'Lives left:   ' + str(self.lifeCount)) 
        elif self._verticalDirection == 'north':
            self.top_y -= self._dy
            self.bottom_y -= self._dy
            self.canvas1.move("ball", -self._dx, -self._dy)
            self.canvas1.after(15)
            self.canvas1.update()

    def eastMovement(self):
        #decides vertical direction
        self.northSouthMovement()        
        #creating animation
        if self._verticalDirection == 'south':
            self.top_y += self._dy
            self.bottom_y += self._dy
            self.canvas1.move("ball", self._dx, self._dy)
            self.canvas1.after(15)
            self.canvas1.update()

            if (self.bottom_y >= self.height) and (self.isBallInPaddle() == False) :
                    self.lifeCount -= 1
                    self.livesLabel.config(text = 'Lives left:   ' + str(self.lifeCount)) 
                                                
        elif self._verticalDirection == 'north':
            self.top_y -= self._dy
            self.bottom_y -= self._dy
            self.canvas1.move("ball", self._dx, -self._dy)
            self.canvas1.after(15)
            self.canvas1.update()
            
    def northSouthMovement(self):
        #changing vertical direction
        if self.isBallInPaddle() == True:
            if self.bottom_y >= self.paddleTop:
                self._verticalDirection = 'north'
            elif self.bottom_y <= 0:
                self._verticalDirection = 'south'
        else:
            if self.bottom_y >= self.height:
                self._verticalDirection = 'north'
            elif self.bottom_y <= 0:
                self._verticalDirection = 'south'

    def isBallInPaddle(self):
        #prevents player from losing life if inside the paddle parameters
        if (self.paddleLeft <= self.left_x <= self.paddleRight) and (self.paddleRight >= self.right_x >= self.paddleLeft):
            return True
        else:
            return False
        
        #lets user control paddle with arrow keys
    def paddleNavigation(self,event):
        if event.keysym == 'Right' and (self.paddleRight <= self.length):
            self.paddleRight += self._paddleDx
            self.paddleLeft  += self._paddleDx
            self.canvas1.move('paddle', self._paddleDx, 0)
            self.canvas1.after(15)
            self.canvas1.update()
        elif event.keysym == 'Left' and (self.paddleLeft >= 0) :
            self.paddleRight -= self._paddleDx
            self.paddleLeft  -= self._paddleDx
            self.canvas1.move('paddle', -self._paddleDx, 0)
            self.canvas1.after(15)
            self.canvas1.update()
 
def main():
    pong().mainloop()

main()
