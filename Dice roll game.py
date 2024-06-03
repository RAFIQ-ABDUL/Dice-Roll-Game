import random
def roll ():
    value=random.randrange(1,6)
    return value

print("Dice Roll Game")
try: 
 numberofplayers=int(input("Enter Number of Players between 2 or 3"))
 if (numberofplayers<2 and numberofplayers>3):
    print("Please Enter value 2 0r 3")
except ValueError:
   print("Invalid input enter integer")

player_scores=[0 for y in range(numberofplayers)]
print("Decide wining score")
max_score=int(input("Write wining score smaller the score sooner will game end"))
while max(player_scores)<max_score:
 for x in range(0,numberofplayers):
   print("Player",x+1,"turn")
   current_score=player_scores[x]
   while True:
      print("Want to roll dice? if yes enter '1'")
      wish=int(input("Write your answer"))
      if wish!=1:
         break
      else:
       score=roll()
       print("You rolled",score)
       if score==1:
         print("you rolled 1 and all your points become zero")
         current_score=0
         break
       else:
        current_score=current_score+score
        if (current_score==max_score or current_score>max_score):
          break
      print("Your current score is",current_score)
   player_scores[x]=current_score
   print("Player",x+1,"score is",player_scores[x])
   if (current_score==max_score or current_score>max_score):
          break

print("Player Number",[x+1],"win game")
         

