import numpy as np
Ele = [i  for i in range(0, 9)]
arr = np.array(Ele, dtype=str).reshape((3, 3))

def disp():

  print("| {} | {} | {} |".format(arr[0][0],arr[0][1],arr[0][2]))
  print("--------------")
  print("| {} | {} | {} |".format(arr[1][0],arr[1][1],arr[1][2]))
  print("--------------")
  print("| {} | {} | {} |".format(arr[2][0],arr[2][1],arr[2][2]))
  print("--------------")
def move(index,player):
  px =index//3
  py= index%3
  if player == 1:
    if arr[px][py] =='O':
      print("Position Marked By Player 2 Previously")
      return False
    arr[px][py] = 'X'
  else:
    if arr[px][py] =='X':
      print("Position Marked By Player 1 Previously")
      return False
    arr[px][py]= 'O'
  return True

def u_input(player):
  print("Enter Move for Player {}".format(player))
  index = int(input())
  return index

def game_status():
  if arr[0][0]==arr[0][1]==arr[0][2]:
    return True
  if arr[1][0]==arr[1][1]==arr[1][2]:
    return True
  if arr[2][0]==arr[2][1]==arr[2][2]:
    return True
  if arr[0][1]==arr[1][1]==arr[2][1]:
    return True
  if arr[0][2]==arr[1][2]==arr[2][2]:
    return True
  if arr[0][0]==arr[1][0]==arr[2][0]:
    return True
  if arr[0][0]==arr[1][1]==arr[2][2]:
    return True
  if arr[0][2]==arr[1][1]==arr[2][0]:
    return True
  return False


disp()
i=0
while i<9:
  if(i%2==0):
    player =1
  else:
    player =2
  index = u_input(player)  # Get the user input for the current player
  if move(index, player):
    disp()
    i+=1
    if game_status():
        print("Player {} Wins".format(player))
        break

if game_status()==False:
  print("Game is Draw")
press = int(input("Enter 1 to play again "))
if press == 1:
  disp()
