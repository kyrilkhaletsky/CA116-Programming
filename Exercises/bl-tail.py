import sys
n = int(sys.argv[1])

def tail():
   s = raw_input()
   lines = []

   while s != "end":
      lines.append(s)
      s = raw_input()

   if n < len(lines):
      i = len(lines) - n
      while i != len(lines):
         print lines[i]
         i += 1

   else:
      j = 0
      while j < len(lines):
         print lines[j]
         j += 1

def main():
   tail()

if __name__ == "__main__":
   main()
