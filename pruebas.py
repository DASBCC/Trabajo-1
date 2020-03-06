from CambioBase10a2_9 import C_baseD_AC
from CambioBase2_9a10 import C_CB_base10

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

def test_C_baseD_AC():
   assert C_baseD_AC(38,2)=="100110"
   assert C_baseD_AC(38,3)=="1102"
   assert C_baseD_AC(38,4)=="212"
   assert C_baseD_AC(382,5)=="3012"
   assert C_baseD_AC(382,6)=="1434"
   assert C_baseD_AC(382,7)=="1054"
   assert C_baseD_AC(382,8)=="576"
   assert C_baseD_AC(382,9)=="464"
   print ("Lo logramos profe :D")
test_C_baseD_AC()