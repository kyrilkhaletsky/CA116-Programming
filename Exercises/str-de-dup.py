import sys

s = sys.argv[1]
y = s[0]

i = 1

while i <len(s):
   if not (s[i] == s[i-1]):
      y += s[i]
   i += 1
print y
 
      
      
   
