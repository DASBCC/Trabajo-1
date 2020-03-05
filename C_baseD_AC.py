def C_baseD_AC(n,base):
   cadenaConversion = "0123456789"
   if n < base:
      return cadenaConversion[n]
   else:
      return C_baseD_AC(n//base,base) + cadenaConversion[n%base]

print(C_baseD_AC(77,3))
