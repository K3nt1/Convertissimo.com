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
    modele='0123456789ABCDEF'
    for i in range(l):
        chiffre=0
        for j in range(16):
            if(hexa[l-i-1]==modele[j]):
                chiffre=j

        decimal+=multi*chiffre
        multi*=16
    return(decimal)

