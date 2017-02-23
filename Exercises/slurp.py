
def slurp_lines():
   lines = []
   s = raw_input()
   while s != "end":
      lines.append(s)
      s = raw_input()
   return lines

def slurp_ints():
   lines = []
   n = raw_input()
   while n != "end":
      lines.append(int(n))
      n = raw_input()
   return lines

def print_list(a):
   i = 0
   while i < len(a):
      print a[i]
      i += 1

def main():
   print slurp_lines()
   a = slurp_ints()
   print a
   print_list(a)

if __name__ == "__main__":
   main()
