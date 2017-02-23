s = ""

i = 0
output = ""
index = 0
 
while s != "end":
   s = raw_input()
   index = s.find("A") and s.find("E") and s.find("I") and s.find ("O") and s.find("U")
   if index >= 0:
      output = output + "\n" + s
print output
