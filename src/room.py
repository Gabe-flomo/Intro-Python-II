# Implement a class to hold room information. This should have name and
# description attributes.
import numpy as np
from player import Player 
from random import sample

class Room:
    def __init__(self,roomtype,desc):
        self.roomtype = roomtype
        self.description = desc
        self.room = {
                    "outside":{"size":(50,50), "door":[(4,49),(10,49),(10,1),(24,49),(29,1),(24,0),(22,1)]},
                    "foyer":{"size":(25,75), "door":[(19,74),(10,74),(10,74),(24,74),(2,1),(53,1),(22,1)]},
                    "overlook":{"size":(15,15),"door":[(4,14),(10,14),(10,1),(14,14),(9,1),(4,1),(2,1)]},
                    "treasure":{"size":(20,20),"door":[(8,19),(14,19),(10,1),(24,19),(14,1),(9,1),(6,1)]}
                    }
        self.table = np.full((0,0),0)
        self.next_room = ["foyer","overlook","treasure"]
        self.door_location = self.spawn_door()
        
    def create_room(self):
        '''
        this function creates the matrix for the room based on the room the player is in
        then returns that matrix as a table.
        '''
        roomsize = self.room[self.roomtype]["size"]
        self.table = np.full(roomsize," ")
        return self.table

    def draw(self,player,bound,drawcount):
        '''
        this functions draws both the room and the position of the player when theyre in
        the room and updates everytime the player moves.
        '''
        roomsize = self.room[self.roomtype]['size']
        print(f"Room size: {roomsize}\n")
        print(f"Door location: {self.door_location}")
        

        x,y = player.position
        dx,dy = self.door_location
        # if you go out of bounds it recreates the room
        if bound:
            self.create_room()
            attempts = player.damage()
            return attempts
        else: 
            # at the players x,y position draw a P
            self.table[x,y] = "P"
            if drawcount == 0:
                self.table[dx,dy] = "D"
        

            for line in self.table:
                print(*line)
            
            if (player.position[0] == self.door_location[0]) and (player.position[1] == self.door_location[1]):
                print("You found the door")
                return self.next_room[1]

            # trace the previous path
            X,Y = player.path.pop()
            self.table[X,Y] = "."

            return False

    def spawn_door(self):
        door_location = sample(self.room[self.roomtype]["door"],1)[0]
        return door_location
        
        



def check():
    valid = ["w","a","s","d","q"]
    
    while True:
        com = input("Enter a Direction: ")
        if com not in valid:
            print("Invalid response")

        else:
            return com


player = Player("Gabe",'overlook')
room = Room(player.current_room,'long hall')
room.create_room()
drawcount = 0
while True:
    
    com = check()
    if com.lower() == "q":
        break
    else:
        bound = player.move(com.lower(),room)
        attempts = room.draw(player,bound,drawcount)
        drawcount += 1
        
        if attempts in ["foyer","overlook","treasure"]:
            print("New room")
            player = Player("Gabe",attempts)
            room = Room(player.current_room,"desc")
            room.create_room()
            drawcount = 0
        elif attempts:
            break

    


