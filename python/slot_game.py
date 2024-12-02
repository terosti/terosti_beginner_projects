
import random
import time


def spinrow(bet, balance):
    random.seed()
    result = []
    balance = balance - bet
    for i in range(0, 3):
        result.append(random.randint(0, 4))
    return result, balance

def printrow(result):

    for i in range(0, 3):
        if result[i] == 0:
            print("🍉", end=' ')
        if result[i] == 1:
            print("🍒", end=' ')
        if result[i] == 2:
            print("🍋", end=' ')
        if result[i] == 3:
            print("🔔", end=' ')
        if result[i] == 4:
            print("⭐", end=' ')
    

def get_payout(result, balance, bet):
    if result[0] == 4 and result[1] == 4 and result[2] == 4:
        print("jackpot!")
        balance = balance + bet*100
    if (result[0] == 4 and result[1] == 4 and result[2] != 4)\
        or (result[0] == 4 and result[1] != 4 and result[2] == 4)\
        or (result[0]!= 4 and result[1] == 4 and result[2] == 4):
        balance = balance + bet*10
    if result[0] == 0 and result[1] == 0 and result[2] == 0:
        balance = balance + bet*2
    if result[0] == 1 and result[1] == 1 and result[2] == 1:
        balance = balance + bet*2
    if result[0] == 2 and result[1] == 2 and result[2] == 2:
        balance = balance + bet*2
    if result[0] == 3 and result[1] == 3 and result[2] == 3:
        balance = balance + bet*20
    return balance


    

def main():
    balance = 100
    bet = 1

    print("************************")
    print("welcome to python slots!")
    print("symbols: 🍉🍒🔔🍋⭐")
    print("************************")
    print("press p to start playing")

    while balance > 0:
        print(f"current bet:${bet}")
        print(f"current balance:${balance}")
        print("press s to spin")
        print("press q to quit")
        print("press b to change bet")
        inp = input()
        if inp == 'b':
            betin = input("enter a bet ")
            if not betin.isdigit():
                print("invalid input")
            else:
                betin = int(betin)
            if betin > balance:
                print("insufficient funds")
            elif betin < 0:
                print("bet can't be 0 or negative")
            else:
                bet = betin
        
        if inp =='q':
            break
        
        if inp =='s':
            if balance < 0:
                print("insufficent funds")
            else: 
                result, balance = spinrow(bet, balance)    
                printrow(result)
                balance = get_payout(result, balance, bet)
    
if __name__ == '__main__':
    main()
            