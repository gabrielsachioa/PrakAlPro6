n = int(input("Masukkan n: "))

def faktorial(n):
     if n == 0:
          return 1
     else:
        return n * faktorial(n - 1)

def perkalian_terbalik(): 
        for i in range(n, 0, -1):
            print(faktorial(i), end=" ")
            for j in range(i, 0, -1):
                print(j, end=" ")
            i -= 1    
            print()
           
perkalian_terbalik()