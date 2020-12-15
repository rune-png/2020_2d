from random import randint
rod = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
sort = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
gron =  [0]
balance = 1000
start_indsats = int(input("Indsats? "))
indsats = start_indsats
goal = 2000
while balance < goal and balance > indsats:
    balance -= indsats
    spil = randint(0,36)
    if spil % 2 == 0:
        pass
    if spil in rod:
        print("Det blev rød")
        balance += 2* indsats
        indsats = start_indsats
    else:
        print("Du tabte")
        indsats *= 2

print("Du endte med {} kroner på lommen".format(balance))
