def switch(n):
        if (n == 1):
                return("Rock")
        if (n == 2):
                return("paper")
        if (n == 3):
                return("scissor")
hc=0
cc=0
select=1
while select == 1: 
        import random
        player = int(input ("choose rock(1)/paper(2)/scissor(3)"))
        computer=random.randint(1,3)
        if((player == 1 and computer ==2) or
        (player ==2 and computer ==3) or
        (player ==3 and computer ==1)):
                hc=hc+1
                print("you chose " +  str(switch(player))  +" and computer choose " + str(switch(computer))  +" winner winner chicken dinner, human score "+ str(hc)+ " computer score "+ str(cc))
                Select=int(input("Yes(1)/No(2)"))
        elif player == computer:
                print("tie,one more")
                print("you chose " +  str(switch(player))  +" and computer choose " + str(switch(computer))  +" winner winner chicken dinner, human score "+ str(hc)+ " computer score "+ str(cc))
                Select=int(input("Yes(1)/No(2)"))
        else:
                cc=cc+1
                print("lose you choose " +  str(switch(player))  + "computer choose" + str(switch(computer)))
                print("one more game?")
                Select=int(input("Yes(1)/No(2)"))

else: end
