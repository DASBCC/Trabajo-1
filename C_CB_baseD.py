def CD(a):
    if a<10:
        return 1
    else:
        return 1 + CD(a//10)

def C_CB_base10 (n, base):
    if n<10:
        return n 
    else:
        return (n//10**(CD(n)-1))* base ** (CD(n)-1) + C_CB_base10(n%10**(CD(n)-1), base)

print (C_CB_base10(574,8))