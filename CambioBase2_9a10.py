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

def test_C_CB_base10():
    assert C_CB_base10(1110,2)==14
    assert C_CB_base10(456,3)==36+15+6
    assert C_CB_base10(6764,4)==524
    assert C_CB_base10(31,5)==16
    assert C_CB_base10(31545,6)==4313
    assert C_CB_base10(315,7)==159
    assert C_CB_base10(716,8)==462
    assert C_CB_base10(69,9)==63
    print ("Profe lo logramos :D")
test_C_CB_base10()