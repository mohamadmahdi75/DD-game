import random
import os
import sys
import time

class game:

    

    CELL=[
        (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),

        (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),

        (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),

        (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),

        (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),

        (0,5),(1,5),(2,5),(3,5),(4,5),(5,5) 


    ]


    def __init__(self,name):
        self.name=name
        self.play_again=False


    def choose_location(self):
        return random.sample(self.CELL,3) 

    def go(self,move,player):
        x,y=player

        if move=="w":
            y=y-1

        if move=='s':
            y=y+1

        if move=='a':
            x=x-1

        if move=="d":
            x=x+1
        
        if x>5:
            return  5, y

        if x<0:
            return 0,y

        if y>5:
            return x,5

        if y<0:
            return x,0            

        return x,y    
    
    def map(self,player):

        print(" _"*6)
        for cell in self.CELL:
            x,y=cell
            if x<5:
                if cell==player:
                    print("|*",end="")
                else:    
                    print("|_",end="")

                

            else:
                if cell==player:
                    print("|*|")
                else:

                    print("|_|")

    def all_moves(self,player):
        all_move=[" left,",' right,',' up,',' down,']

        x,y=player

        if y==0  :
            all_move.remove(" up,")

        if y==5:
            all_move.remove(" down,")    

        if x==0:
            all_move.remove(" left,")

        if x==5:
            all_move.remove(" right,")    



        return all_move        


    
    def play_game(self):


        if self.play_again == True:
            os.system("cls")
            print("welcome back {}!!!!".format(self.name))
            time.sleep(2)

        player,monster,door=self.choose_location()

        while True:
            os.system("cls")
            print('you can go:',''.join(self.all_moves(player)))
            self.map(player)
            move=input("=>").lower()
            os.system("cls")
            player=self.go(move,player)
            if player==monster:
                print("ohhh the monster catch you dear!!!")
                a=input("do you want to play agin? y/n ").lower()
                if a=="yes" or a=="y":
                    self.play_again=True
                    self.play_game()
                else:
                    print("good bye {},have a nice life!!!".format(self.name))
                    sys.exit()

            elif player==door:
                print("you win!!")
                a=input("do you want to play agin? y/n ").lower()
                if a=="yes" or a=="y":
                    self.play_again=True
                    self.play_game()
                else:
                    self.play_again=False
                    print("good bye {},have a nice life!!!".format(self.name))
                    sys.exit()




          
mohamad=game(input("enter your name: "))
mohamad.play_game()  