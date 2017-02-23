def reverse():
   line = []  
   s = raw_input()
   
   while s != "end":
      k = ""
      i = 0
      while i <len(s):
         k = s[i] + k
         i += 1
      line.append(k)
      s = raw_input()
   j = 0
   while j < len(line):
      print line[j]
      j += 1
   return line

def main():
   reverse()

if __name__ == "__main__":
   main()
