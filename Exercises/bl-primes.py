import sys
n = int(sys.argv[1])

def primes():
   k = 2
   i = 0
   while k < n and i < k:
      if k == 2:
         print k
      i = 2
      while k % i != 0 and i < k:
         i += 1
         if i == k:
            print k
      k += 1

def main():
   primes()

if __name__ == "__main__":
   main()
