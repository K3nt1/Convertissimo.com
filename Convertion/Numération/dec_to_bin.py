def dec_to_bin(dec):
    rep=''
    while(dec>0):
        if (dec%2==1):
            rep='1'+rep
        else:
            rep='0'+rep
        dec=dec//2
    return(rep)