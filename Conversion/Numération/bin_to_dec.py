def bin_to_dec(binaire):
    l=len(binaire)
    decimal=0
    multi=1
    for i in range(l):
        if(binaire[l-i-1]=='1'):
            decimal+=multi
        multi*=2
    return(decimal)

def hexa_to_dec(hexa):
    l=len(hexa)
    decimal=0
    multi=1
    for i in range(l):
        chiffre=0
        if(hexa[l-i-1]=='1'):
            chiffre=1
        if(hexa[l-i-1]=='2'):
            chiffre=2
        if(hexa[l-i-1]=='3'):
            chiffre=3
        if(hexa[l-i-1]=='4'):
            chiffre=4
        if(hexa[l-i-1]=='5'):
            chiffre=5
        if(hexa[l-i-1]=='6'):
            chiffre=6
        if(hexa[l-i-1]=='7'):
            chiffre=7
        if(hexa[l-i-1]=='8'):
            chiffre=8
        if(hexa[l-i-1]=='9'):
            chiffre=9
        if(hexa[l-i-1]=='A'):
            chiffre=10
        if(hexa[l-i-1]=='B'):
            chiffre=11
        if(hexa[l-i-1]=='C'):
            chiffre=12
        if(hexa[l-i-1]=='D'):
            chiffre=13
        if(hexa[l-i-1]=='E'):
            chiffre=14
        if(hexa[l-i-1]=='F'):
            chiffre=15

        decimal+=multi*chiffre
        multi*=16
    return(decimal)

