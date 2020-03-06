def C_baseD_AC(n,base):
   cadenaConversion = "0123456789"
   if n < base:
      return cadenaConversion[n]
   else:
      return C_baseD_AC(n//base,base) + cadenaConversion[n%base]

print (C_baseD_AC(382,9))
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