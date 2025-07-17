# Resutrantname = "Karachi FOOD"
# Address = "NAzaimabab no 4 karachi"
# Speciality = "Every Thing"
# Ph_number = "0255245245545"
# city_name = "Karachi"
# is_fivestar = True
#
# print(f"Resutrant Name is {Resutrantname}.\nLocated in {Address}.\nSpeciality is{Speciality}.\nFor Contact{Ph_number}.\nCity is{city_name}.\nRating is{is_fivestar}")

# Resutrantname =input("Enter Restaurant name")
# Address =input("Enter Address")
# Speciality =input("Enter Speciality")
# Ph_number =input("Enter Ph_number")
# city_name =input("Enter city_name ")
# is_fivestar =input("Enter Rating")

print("DHOLU BHOLLU  Halwa Puri Shop")
Puris = int(input("How many puri do you want:"))
Cholay = int(input("How many Cholay do you want:"))
AlluPlats = int(input("How many AlluPlates do you want:"))
HAlwa = int(input("How many HAlwa do you want:"))
per_puri = 50
per_choly = 100
per_halwa = 150
per_alo = 80
puri_total = per_puri * Puris
puri_Cholay = per_choly * Cholay
puri_allu = per_alo * AlluPlats
puri_halwa = per_halwa * HAlwa
total_bill = puri_total + puri_Cholay +puri_allu+puri_halwa
print(f"Total Bill is :",total_bill)



tax = total_bill * 0.16
total = tax + total_bill
Discount = total * 0.5
Bill_after = Discount - total
print(f"total bill is : ", total_bill,"\ntax is :,",tax,"\ntotal is :",total,"\nDiscount is :",Discount,"\nAfter Discount total:",Bill_after)





