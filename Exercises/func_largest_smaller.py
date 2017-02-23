def largest_smaller(a,q):
   start = 0
   end = len(a)
   while start < end:
      middle = (start + end) / 2
      if a[middle] < q:
         start = middle + 1
      else:
         end = middle
   return a[end - 1]
   

def main():
   print largest_smaller([2,3,6,6,7,8], 6) #3
   print largest_smaller([2,3,6,6,7,8], 8) #7
   print largest_smaller([2,3,6,6,7,8], 9) #8
   print largest_smaller([2,3,6,6,7,8], 4) #3


if __name__ == "__main__":
   main()
