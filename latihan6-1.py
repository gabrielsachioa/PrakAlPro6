n = int(input("Masukkan n: "))

def prima_terdekat(n):
    if n <= 1:
        return "Bukan Prima"
    elif n == 3:
        return 2
    else:
        angka = 0
        for i in range(n):
            if i % 2 == 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                    else:
                        angka = i
        return angka

print(prima_terdekat(n))
