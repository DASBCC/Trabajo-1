def C_baseD_AC(n,base):
   cadenaConversion = "0123456789"
   if n < base:
      return cadenaConversion[n]
   else:
      return C_baseD_AC(n//base,base) + cadenaConversion[n%base]

print (C_baseD_AC(38,3))
def test_C_baseD_AC():
   assert C_baseD_AC(38,3)==1102
   print ("Prueba")
test_C_baseD_AC()