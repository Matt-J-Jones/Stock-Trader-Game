import random
from os import system

loop = True
turn = 0

class player:
    cash = 2000
class EXAMPLESTOCK:
    name = "GME"    #The Name of the stock
    oq = 45         #The quantity at IPO
    v = 800         #The total value of the stock
    h = 0           #The amount held by the player
    sv = 0          #The value per share
    ch = 0          #The change in value per turn
class GME:
    name = "GME"
    oq = 45
    v = 800
    h = 0
    sv = 0
    ch = 0
class NOK:
    name = "NOK"
    oq = 75
    v = 1100
    h = 0
    sv = 0
    ch = 0
class BB:
    name = "BB"
    oq = 80
    v = 1200
    h = 0
    sv = 0
    ch = 0
class BTC:
    name = "BTC"
    oq = 5
    v = 500
    h = 0
    sv = 0
    ch = 0
class DOGE:
    name = "DOGE"
    oq = 100
    v = 250
    h = 0
    sv = 0
    ch = 0


def genNewValue(share):
    oldValue = share.sv
    crash = random.randint(1,15)
    if crash == 7:
        share.sv = 0.01
    else:
        share.sv = (share.v + random.randint(-500, 500)) / share.oq
        if share.sv <= 0:
            share.sv = 0.01
    valueChange = share.sv - oldValue
    valueChange = round(valueChange, 2)
    share.ch = valueChange

def printShare(share):
    print(share.name,"Shares Held:", share.h)
    share.sv = round(share.sv, 3)
    print(share.name,"Share value each:", share.sv, "(Change:",share.ch,")", "\n")

def buyShares(share):
    buy = input("Qty of shares to buy?: ")
    buy = int(buy)
    if player.cash < 0:
        print("You do not have enough liquid assets, consider selling some shares")
    else:
        share.h = share.h + buy
        player.cash = player.cash - (buy * share.sv)

    player.cash = round(player.cash, 2)

    print("Cash:", player.cash)
    print("Total Shares Held:", share.h)

def sellShares(share):
    sell = input("Qty of shares to sell?: ")
    sell = int(sell)

    share.h = share.h - sell
    player.cash = player.cash + (sell * share.sv)

    print("Cash:", player.cash)
    print("Total Shares Held:", share.h)

def endgame(share):
    total = share.sv * share.h
    total = round(total, 2)
    print("You sold", share.name, "for £", total)
    player.cash = player.cash + total

def addinterest():
    if player.cash < 0:
        odAmount = player.cash * -1
        percent = (odAmount / 100) * 25
        
        print("Your bank has applied an overdraft fine of 25%")
        print("You have been charged £", percent)

        player.cash = player.cash - percent
        player.cash = round(player.cash, 2)

def clear():
    system('cls')

while loop: 
    clear()
    turn = turn + 1
    end_turn = 10
    print('\n')
    
    genNewValue(GME)
    printShare(GME)
    genNewValue(NOK)
    printShare(NOK)
    genNewValue(BB)
    printShare(BB)
    genNewValue(BTC)
    printShare(BTC)
    genNewValue(DOGE)
    printShare(DOGE)

    print("Turn", turn)
    if turn == end_turn:
        print("This is your last turn")
    elif turn == (end_turn-1):
        print("You have 1 turn remaining")
    else:
        turn_remain = end_turn - turn
        print("you have", turn_remain,"turns remaining")
    addinterest()
    player.cash = round(player.cash, 2)
    print("\nCash:", player.cash)

    bs = input("Do you want to Buy or Sell?")

    if bs == "Buy" or bs == "buy" or bs == "BUY":
        toBuy = input("Enter Name of Share to Buy: ")
        if toBuy == "GME":
            buyShares(GME)
        elif toBuy == "NOK":
            buyShares(NOK)
        elif toBuy == "BB":
            buyShares(BB)
        elif toBuy == "BTC":
            buyShares(BTC)
        elif toBuy == "DOGE":
            buyShares(DOGE)
    elif bs == "Sell" or bs == "sell" or bs == "SELL":
        toSell = input("Enter Name of Share to Sell: ")
        if toSell == "GME":
            sellShares(GME)
        elif toSell == "NOK":
            sellShares(NOK)
        elif toSell == "BTC":
            sellShares(BTC)
        elif toSell == "DOGE":
            sellShares(DOGE)
        elif toSell == "BB":
            sellShares(BB)


    end=input("Next Turn?")
    if end=="end" or turn >= 10:
        loop=False
    else:
        loop=True
clear()
print("You Sold All Your Remaing Shares:\n")

endgame(GME)
endgame(NOK)
endgame(BB)
endgame(BTC)
endgame(DOGE)

player.cash = round(player.cash, 2)
print("\nYour final total is: £", player.cash)
input("\nPress Enter to Exit")