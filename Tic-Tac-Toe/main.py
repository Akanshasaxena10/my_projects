''''application of
for loop
while loop
functions
'''


def sum(a,b,c):##over-writing the sum function
    return a+b+c


'''created the game board'''
def printBoard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five ='X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    print(f'{zero} | {one} | {two}')
    print(f'--|---|--')
    print(f'{three} | {four} | {five}')
    print(f'--|---|--')
    print(f'{six} | {seven} | {eight}')
    print(f'--|---|--')
    
'''function to define winner---all possible sets to win in list array'''
def checkWin(xState , zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    
    for win in wins:##for 
        if (sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            print('X Won The Match')
            return 1
        if (sum(zState[win[0]],zState[win[1]],zState[win[2]]) == 3):
            print('O Won The Match')
            return 0
    return -1
        
        
'''To run the game created a main and placed in if loop'''
if __name__ == '__main__':  
    xState = [0,0,0,0,0,0,0,0,0]##'x' eight place play possibility
    zState = [0,0,0,0,0,0,0,0,0]## 'o' eight place play possibility
    turn = 1 # 1 for X and 0 for O.
    print('Welcome To Tic Tac Toe World')
    print("X's Turn")
    
    while(True):##while loop to confirm
         printBoard(xState,zState) 
         if(turn == 1):
            print("X's Chance")
            value = int(input('Please Enter a value: '))
            xState  [value] = 1
         else:
            print("O's Chance")
            value = int(input('Please Enter a value: '))
            zState  [value] = 1
            
         cwin = checkWin(xState,zState)##calling the checkWin function.
         if (cwin != -1):
            print('Match Over')
            break         
         turn = 1 - turn 
          #break    
         
              
             
   
    
    
    