import sys
lines = sys.stdin.readlines()

def anonymizer():
   names = {}
   i = 0
   j = 1
   while i < len(lines):
      line = lines[i]
      details = line.split()
      name = details[3]
      if name not in names:
         names[name] = "user-" + str(j)
         j += 1
      print " ".join(details[0:3]), names[name], " ".join(details[4:])
      i += 1
   return lines

def main():
   anonymizer()

if __name__ == "__main__":
   main()

