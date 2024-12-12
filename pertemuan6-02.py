#Menghitung Luas dan keliling lingkaran dengan jari-jari yang dimasukkan oleh pengguna

#input
r = float(input("Masukkan Jari-jari :"))


#Proses
import math 
luas = round(math.pi*r**2)
kel = round(2*math.pi*r)


#Output
print(f"Luas = "+str(luas)+"cm²")
print("Keliling = "+str(kel)+"cm")


