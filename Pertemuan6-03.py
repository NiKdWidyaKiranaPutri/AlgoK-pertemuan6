""" buatlah program menghitung rumus pitagoras
dengan menggunakan fungsi matematika """

#input
a = 7
b = 5

#proses
import math

c_kuadrat = a**2 + b**2
c = round(math.sqrt(c_kuadrat),2)


#output
print("c² = "+str(c_kuadrat))
print("c = "+str(c))
