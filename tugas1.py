print ("Di sebuah hutan, ada dua kelici yang sedang merencanakan acara makan besar")
print ("Kelinci hitam : Kita harus mempersiapkan makanan untuk 20 tamu. Jika kita ingin membuat 5 porsi makanan, berapa banyak makanan yang perlu kita siapkan? ")

print ("Kelinci putih : Kita harus menghitung total porsi. Jadi, jika 20 tamu dan masing-masing dapat 5 porsi, kita kalikan saja.")
tamu = int(input("Berapa tamu yang akan datang?"))
makanan = int (input("Berapa porsi yang disiapkan?"))
print ("Jadi, 20 kali 5 sama dengan?")
print (tamu * makanan)

print ("Kelinci hitam : Baik, jadi kita perlu menyiapkan 100 porsi. Bagaimana dengan minuman? Aku pikir kita juga perlu menyediakan 3 gelas minuman untuk setiap tamu")
print ("Kelinci putih : Itu berarti kita harus mempersiapkan 20 tamu dikali 3 gelas")
tamu = int(input("Berapa tamu yang akan datang?"))
gelas = int(input("Berapa gelas minuman yang harus disiapkan?"))
print ("Jadi, 20 kali 3 sama dengan?")
print (tamu * gelas)

print ("Kelinci hitam : Oke, jadi kita butuh 100 porsi makanan dan 60 gelas minuman. Sekarang, kita juga ingin menyiapkan kue. Jika kita membeli 3 kue dan setiap kue bisa dibagi untuk 8 orang, berapa banyak orang yang bisa kita layani dengan kue tersebut?")
print ("Kelinci putih : Kita kalikan saja jumlah kue dengan jumlah tamu per kue")
kue = int(input("Berapa kue yang dibeli?"))
tamu = int(input("Berapa tamu yang harus di bagi setiap kue?"))
print ("Jadi, 3 kue dikali 8 tamu sama dengan?")
print (kue * tamu)

print ("Kelinci hitam : Berarti kue kita cukup untuk semua tamu. Jika kita mengundang 5 tamu lagi, kita harus memikirkan tambahan makanan atau minuman. Berapa total tamu kita sekarang?")
print ("Kelinci putih : Tentu! Jika sebelumnya ada 20 tamu dan kita menambah 5 tamu, berarti totalnya?")
tamu1 = int(input("Berapa tamu sebelumnya?"))
tamu2 = int(input("Berapa tamu tambahan?"))
print ("Jadi, jumlah total tamu adalah")
print (tamu1 + tamu2)

print ("Kelinci hitam : Kita perlu menyesuaikan jumlah porsi makanan dan minuman untuk 25 tamu. Jika kita tetap ingin 5 porsi makanan per tamu, berapa total porsi yang perlu kita siapkan?")
print ("Kelinci putih : Jadi, 25 tamu dikali 5 porsi sama dengan?")
tamu = int(input("Berapa tamu yang akan disuguhkan makanan dan minuman?"))
porsi = int(input("Berapa porsi yang disuguhkan setiap tamu?"))
print (tamu * porsi)

print ("Kelinci hitam : Baiklah, kita sudah punya semua informasi yang kita butuhkan untuk acara kita!")

print("Nah, dialog tersebut maka dapat diketahui jumlah tokoh tersebut berjumlah?")
a = int(input("Masukan angka : "))
if a == 2:
 print("iya, tokoh pada dialog tersebut berjumlah 2")
else:
    print("bukan, seharusnya tokoh pada dialog tersebut berjumlah 2")
