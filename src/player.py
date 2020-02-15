# Write a class to hold player information, e.g. what room they are in
# currently.
import os
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class Player:
    def __init__(self,name,room):
        self.name = name
        self.current_room = room
        self.x = 1
        self.y = 1
        self.moves = {
            "w":self.up,
            "a":self.left,
            "s":self.down,
            "d":self.right
        }
        self.position = (self.x,self.y)
        self.path = []
        self.tries = 3
    
    def up(self):
        '''
        W
        '''
        
        self.x -= 1
        self.position = (self.x,self.y)
        print("Moved Up")
        return self
    
    def left(self):
        '''
        A
        '''
        self.y -= 1
        self.position = (self.x,self.y)
        print("Moved Left")
        return self
    
    def down(self):
        '''
        S
        '''
        
        self.x += 1
        self.position = (self.x,self.y)
        print("Moved Down")
        return self

    def right(self):
        '''
        D
        '''
        self.y += 1
        self.position = (self.x,self.y)
        print("Moved Right")
        return self

    def move(self,drct,room):
        os.system("CLS")
        drct = drct.lower()
        size = room.room[self.current_room]["size"]
        try:
            self.moves[drct]()
            self.path.append(self.position)
            if (self.x <= 0 or self.y <= 0) or (self.x >= size[0] or self.y >= size[1]):
                print("You went out of bounds")
                raise ValueError("Out of bounds")
            else:
                print(f"Current Position: {self.position}")
                return False
        except ValueError:
            self.x = 1
            self.y = 1
            self.position = (1,1)
            
            print("Returning to position (1,1)")
            return True
    
    def damage(self):
        
        if self.tries == 1:
            print("You have no attempts left")
            return True

        else:
            self.tries -= 1
            print(f"You have {self.tries} attempts left") 
            return False
        

    


