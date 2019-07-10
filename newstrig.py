def st_rng(rawf):
    str1=''
    index=len(rawf)
    while index>0:
        str1=str1+rawf[index-1]
        index=index-1
    return str1
print(st_rng("ggdmin is good"))
