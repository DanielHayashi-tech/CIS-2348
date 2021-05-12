# Daniel Hayashi
#1763814

import csv
from operator import itemgetter
# Creating a list to hold CSV data

a = []
b = []
c = []

# Adding the data to the lists from each csv file
with open("ManufacturerList.csv") as mainlist:
    ml = csv.reader(mainlist)
    for line in ml:
        a.append(line)

with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        b.append(line)

with open("ServiceDatesList.csv") as clist:
    sl = csv.reader(clist)
    for line in sl:
        c.append(line)

# sorting each list by the order ID in order to get them all lining up properly
new_a = (sorted(a, key=itemgetter(0)))
new_b = (sorted(b, key=itemgetter(0)))
new_c = (sorted(c, key=itemgetter(0)))

# appending the missing prices and service dates to the main list
for x in range(0, len(new_a)):
    new_a[x].append(b[x][1])

for x in range(0, len(new_a)):
    new_a[x].append(c[x][1])

final_list = new_a

full_inventory = (sorted(final_list, key=itemgetter(1)))

# writing the Full Inventory file with the full inventory list
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

# Making a list for each item type
item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

# lookign in each list for specific item types and appending them to their own lists
for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])

# Writing a file for each item type
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
    for x in range(0, len(laptop_list)):
        liwrite.writerow(laptop_list[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
    for x in range(0, len(phone_list)):
        piwrite.writerow(phone_list[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
    for x in range(0, len(tower_list)):
        tiwrite.writerow(tower_list[x])

# Made a list for damaged products

damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

# writing a damaged products file
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])

# Asking the user for their manufacturer and item type
user_manuf = str(input("Enter your manufacturer: "))
user_type = str(input("Please enter your item type: "))
your_item = []

# Q is the exit value so while the input does not equal q, execute the program

while (user_manuf != "q"):
    for x in range(0, len(final_list)):
        if user_manuf in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])

# If nothign was added to the list that means the product does not exist
    if len(your_item) != 0:
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)

        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

user_manuf = str(input("Enter your manufacturer, or q to exit query:"))
user_type = str(input("Please enter your item type: "))

b = []
c = []

# Adding the data to the lists from each csv file
with open("ManufacturerList.csv") as mainlist:
    ml = csv.reader(mainlist)
    for line in ml:
        a.append(line)

with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        b.append(line)

with open("ServiceDatesList.csv") as clist:
    sl = csv.reader(clist)
    for line in sl:
        c.append(line)

# sorting each list by the order ID in order to get them all lining up properly
new_a = (sorted(a, key=itemgetter(0)))
new_b = (sorted(b, key=itemgetter(0)))
new_c = (sorted(c, key=itemgetter(0)))

# appending the missing prices and service dates to the main list
for x in range(0, len(new_a)):
    new_a[x].append(b[x][1])

for x in range(0, len(new_a)):
    new_a[x].append(c[x][1])

final_list = new_a

full_inventory = (sorted(final_list, key=itemgetter(1)))

# writing the Full Inventory file with the full inventory list
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

# Making a list for each item type
item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

# lookign in each list for specific item types and appending them to their own lists
for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])

# Writing a file for each item type
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
    for x in range(0, len(laptop_list)):
        liwrite.writerow(laptop_list[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
    for x in range(0, len(phone_list)):
        piwrite.writerow(phone_list[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
    for x in range(0, len(tower_list)):
        tiwrite.writerow(tower_list[x])

# Made a list for damaged products

damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

# writing a damaged products file
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])

# Asking the user for their manufacturer and item type
user_manuf = str(input("Enter your manufacturer: "))
user_type = str(input("Please enter your item type: "))


your_item = []

# Q is the exit value so while the input does not equal q, execute the program

while (user_manuf != "q"):
    for x in range(0, len(final_list)):
        if user_manuf in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])

# If nothign was added to the list that means the product does not exist
    if len(your_item) != 0:
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)
        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

user_manuf = str(input("Enter your manufacturer, or q to exit query:"))

user_type = str(input("Please enter your item type: "))

