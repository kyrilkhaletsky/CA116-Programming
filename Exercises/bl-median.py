ints = []

def median():
   s = raw_input()
   while s != "end":
      s = int(s)
      ints.append(int(s))
      s = raw_input()

   i = 0
   while i < len(ints):
      k = i
      j = i + 1
      while j < len(ints):
         if ints[j] < ints[k]:
            k = j
         j = j + 1
      tmp = ints[k]
      ints[k] = ints[i]
      ints[i] = tmp
      i = i + 1

   index = len(ints) / 2

   print ints[index]

def main():
   median()

if __name__ == "__main__":
   main()
