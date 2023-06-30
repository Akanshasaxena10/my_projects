'''created the game board'''
def printBoard(xState,zState):
    zero = {'X'}
    print(f'0 | 1 | 2')
    print(f'--|---|--')
    print(f'3 | 4 | 5')
    print(f'--|---|--')
    print(f'6 | 7 | 8')
    print(f'--|---|--')
    
'''To run the game created a main and placed in if loop'''
if __name__ == '__main__':  
    xState = [0,0,0,0,0,0,0,0]##'x' eight place play possibility
    zState = [0,0,0,0,0,0,0,0]## 'o' eight place play possibility
    turn = 1 # X for player-1 and 0 for the  player-2.
    print('Welcome To Tic Tac Toe World')
    print("Player-1's Turn")
    
while(True):
     printBoard(xState,zState) 
     if(turn == 1):
         print("Player-1's Chance")
         value = int(input('Please Enter a value: '))
         xState  [value] = 1
     else:
         print("Player-2's Chance")
         value = int(input('Please Enter a value: '))
         zState  [value] = 1
         
     break     
              
             
   
    
    
    