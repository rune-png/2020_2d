from random import randint

penge = 1000
start_indsats = 10
indsats = start_indsats
n=0

input("Klar?")

while penge >= indsats and penge < 2000:
    n += 1
    #Gør en indsats
    penge -= indsats

    #Kør med rouletten
    spil = randint(0,37)

    #Hvad blev resultatet?
    if spil == 0:
        print("Grøn!")
        indsats *= 2
    elif spil in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        print('Rød!')
        penge += 2*indsats
        indsats = start_indsats
    elif spil in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]:
        print('Sort!')
        indsats *= 2

    print("Saldo: {}".format(penge))


print("Du endte med {} på lommen efter {} spil.".format(penge, n))
