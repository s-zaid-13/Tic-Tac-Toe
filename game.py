
# 3-by-3 Grid
n=3
grid = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8
}
def display():
    count=0
    print("**********")
    for key in grid.keys():
        print(grid[key],end='')
        count+=1
        if(count==3):
            print("\n_________")
            count=0
        else:
            print(' | ',end='')
    print("**********")

def turn(grid,player):
    while(True):
        pos=int(input("Choose a valid position in Tic tac toe: "))
        if  pos<n*n and grid[pos]!='Y' and grid[pos]!='X' :
            grid[pos]=player
            return




def checkWin(grid,player):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[1,4,8],[2,4,6]]
    for part in wins:
        found=True
        for pos in part:
            if grid[pos]!=player:
                found=False
                break
        if found:
            return found
    return False

def greet(msg):
    print("-------------------------------")
    print(f"||   {msg}  ||")
    print("-------------------------------")

def tieStyle(msg):  
    print("------------------------------")
    print(f"||        {msg}      ||")
    print("------------------------------")
def winStyle(msg):  
    print("------------------------------")
    print(f"||        {msg}       ||")
    print("------------------------------")



# print("-------------------------------")
# print("||   Welcome to Tic-Tac-Toe  ||")
# print("-------------------------------")
greet("Welcome to Tic-Tac-Toe")
player='X'
for _ in grid.keys():
    display()
    print(f"{player}'s Turn: ")
    turn(grid,player)
    if(checkWin(grid,player)):
        display()
        winStyle(f"Winner is {player}")
        exit()
    if(player=='X'):
        player='O'
    else:
        player='X'
display()
tieStyle("Game is Tied")





