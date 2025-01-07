# 21 Number or Twently plus One Game 

# This is 21 Number or Twently plus one game is a game which progresses by counting up to 21 from one.
# The player who cals 21 will eliminate 
# We are writing code to play game between computer and a user who play this game.


# Author Details 

# Name  :  Er. Amar kumar 
# Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##


class TwentlyPlusOne: 
    _last = 0
    _current_squence = []
    _computer_allowed = 0

    # function to reset game state on lose or win
    def _resetGameState(self):
        self._last = 0
        self._current_squence = []
        self._computer_allowed = 0
   

    # check list contain numbers in consecutive manger or not       
    def _isValidSequene(self):
    
        if len(self._current_squence) <= 1: 
            return True
       
        for i in range(1, len(self._current_squence)):
            if self._current_squence[i] - self._current_squence[i-1] != 1 :
               return False 
       
        return True 
    
    # function to get nearest number for computer to fill numbers in list 

    def _get_neareast(self, nlast):
        if nlast >= 4:
           near  = nlast + (4 - nlast % 4)
        else:
           near = 4
    
        return near
    # print current numbers in list

    def _printSequence(self):
        print()
        print(self._current_squence)
    

    # print lose message for user 

    def _loseMessage(self):
        print("\nYou Lose the game !")
        shouldPlayGame()
        
    # display won message for user

    def _wonMessage(self):
        print("\nCongratulations !")
        print("\nYou won the game!")
        shouldPlayGame()

    # logic for playing game
    def play(self):
        self._resetGameState()
    
        try:
           
            choice = str(input ("If you want to start first then type F\nIf you want to play second then type S\n"))
    
            if choice == "F":
                while True: 
                    if self._last == 20:
                       self._loseMessage()
                    else: 
                        print("\nYour turn! ")
                       
                        ninputs = int(input("Enter how many numbers you want to add in list: \n"))

                        if ninputs > 0 and ninputs <= 4:
                           self._computer_allowed = 4 - ninputs 
                        else:
                           print("Wrong Input! You are disqualified from game! ")
                           self._loseMessage()
                   
                        i, j = 1, 1 
            
                        while i <= ninputs:
                            self._current_squence.append(int(input("\nEnter a Number: ")))
                            i += 1

                        self._last = self._current_squence[-1]

                        if self._isValidSequene():
                            if self._last == 21 : 
                               self._loseMessage() 
                            else: 
                                # computer turn 

                                while j <= self._computer_allowed:
                                    self._current_squence.append(self._last + 1)
                                    self._last += 1
                                    j += 1

                                print("\nCurrent numbers in list are following: ")
                                self._printSequence()
                                self._last = self._current_squence[-1]
                        else: 
                            print("\nYou did not enter input consecutive integers.")
                            self._loseMessage()
               
            elif choice == "S":
              
                self._computer_allowed = 1
                self._last = 0
              
             

                while self._last < 20:
                   
                    j = 1 
                   
                    while j <= self._computer_allowed:
                        self._current_squence.append(self._last + 1)
                        self._last += 1 
                        j += 1     
                    
                    print("\n\nCurrent numbers in list are following: ")
                    
                    self._printSequence()
                    self._last = self._current_squence[-1]   

                    if self._last == 20:
                       self._loseMessage()
                    else: 
                        print("\nYour turn! ")
                       
                        ninputs = int(input("\nEnter how many numbers you want to add in list: "))

                        i = 1 

                        while i <= ninputs:
                            self._current_squence.append(int(input("Enter a number: ")))
                            i += 1

                        self._last = self._current_squence[-1]

                        if self._isValidSequene():
                            near = self._get_neareast(self._last)
                            
                            self._computer_allowed = near - self._last
                        
                            if self._computer_allowed == 4:
                               self._computer_allowed = 3
                            else: 
                               self._computer_allowed = self._computer_allowed

                        else: 
                            print("\n You did not enter input consecutive integers.")
                            self._loseMessage()

                self._wonMessage()
                

            else: 
                print("Wrong Choice! Please select valid option!")
                self.play()         
        
        except KeyboardInterrupt:
           print()
           print("Bye, see you again !")
           exit()


# helper function to determine should play game or exit 

def shouldPlayGame():
    
    should_play = str(input("Do you want to play game? if yes then type YES otherwise press any key to exit\n"))
    
    if should_play == "YES":
        print("\nBest of luck!")
        game = TwentlyPlusOne()
        game.play()

    else:
        print("\nThank you! See you again! ")
        exit()

if __name__ == '__main__':
    print("Hi, You're welcome at Twently plus One Game !")
    shouldPlayGame()


## End of a Game ## 