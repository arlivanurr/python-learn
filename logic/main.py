'''
# +++++3-----10+++++
inputUser = float(input("masukkan angka kurang dari 3\natau \nlebih dari 10\n:"))

# +++++++3-------
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

#-------10+++++++
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++3-----10+++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan =", isCorrect)

#-----3+++++10-----
print("\n",10*"=","\n")
inputUser = float(input("masukkan angka lebih dari 3\natau \nkurang dari 10\n:"))

#-----3+++++++
isLebihDari = inputUser > 3
print("Lebih Dari 3 =", isLebihDari)

#++++++10------
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

#-----3+++++10-----
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan =", isCorrect)
'''

#-----0++++++5-------8+++++++11------
inputUser = float(input("masukkan angka\n:"))

data1 = inputUser > 0
data2 = inputUser < 5
data3 = inputUser > 8
data4 = inputUser < 11

hasil1 = data1 and data2
hasil2 = data3 and data4

hasilData = hasil1 or hasil2
print("Lebih dari 0 =", data1)
print("Kurang dari 5 =", data2)
print("Lebih dari 8 =", data3)
print("Kurang dari 11 =", data4)
print("Angka yang anda masukkan =", hasilData)

#+++++0------5++++++8------11+++++
inputUser = float(input("masukkan angka\n:"))

data1 = inputUser < 0
data2 = inputUser > 5
data3 = inputUser < 8
data4 = inputUser > 11

hasil1 = data1 or data4
hasil2 = data2 and data3

hasilData = hasil1 or hasil2
print("Lebih dari 0 =", data1)
print("Kurang dari 5 =", data2)
print("Lebih dari 8 =", data3)
print("Kurang dari 11 =", data4)
print("Angka yang anda masukkan =", hasilData)
