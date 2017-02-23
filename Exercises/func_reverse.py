a = [4, 3, 2, 1]

def reverse(a):
   j = 0
   i = len(a) - 1
   while j < len(a) / 2:
      tmp = a[j]
      a[j] = a[i]
      a[i] = tmp
      j += 1
      i -= 1
   return a
def main():
   print reverse(a)

if __name__ == "__main__":
   main()
