import sys
n = sys.argv[1]
def binary():
   dec = 0
   index = len(n)
   i = len(n)
   while i > 0:
      dec = dec + int(n[i - 1]) * 2 ** (index - i)
      i -= 1
   print dec

def main():
   binary()

if __name__ == "__main__":
   main()
