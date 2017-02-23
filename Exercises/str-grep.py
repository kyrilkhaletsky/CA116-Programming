import sys

needle = sys.argv[1]

s = ""

i = 0
output = ""
index = 0
 
while s != "end":
   s = raw_input()
   index = s.find(needle)
   if index >= 0:
      output = output + "\n" + s
print output
