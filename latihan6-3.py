tinggi = int(input("Tinggi: "))
lebar = int(input("Lebar: "))

def deret_dinamis(tinggi, lebar):
    if tinggi <= 0 or lebar <= 0:
        print("Tidak valid")
    else:
        counter = 0
        for i in range(1, tinggi + 1):
            for j in range(1, lebar + 1):
                counter += 1
                print(counter,"",end='')
            print()

deret_dinamis(tinggi, lebar)