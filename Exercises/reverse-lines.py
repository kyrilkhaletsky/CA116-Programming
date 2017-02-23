s = raw_input()  #line
lines = []

while s != "end":
   lines.append(s)
   s = raw_input()
  
while 0 < len(lines):
   print lines.pop()
   
