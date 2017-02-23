def bsearch(a,q):
   start = 0
   end = len(a)
   while start < end:
      middle = (start + end) / 2
      if a[middle] < q:
         start = middle + 1
      else:
         end = middle
   return start

def main():
   print bsearch([2,3,6,6,7,8], 1) #0
   print bsearch([2,3,6,6,7,8], 2) #0
   print bsearch([2,3,6,6,7,8], 6) #2
   print bsearch([2,3,6,6,7,8], 8) #5
   print bsearch([2,3,6,6,7,8], 9) #6
   print bsearch([2,3,6,6,7,8], 4) #2

if __name__ == "__main__":
   main()
