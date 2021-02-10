#PART 1
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()
first = input('Select first service:\n')
second = input('Select second service:\n')

#PART 2
if first == "-":
    first == 'No service'
else:
    first = first.lower()
    if first == ('Oil change'):
        first = first.capitalize() + ',' + ' $35'
    elif first == ('Tire rotation'):
        first = first.capitalize() + ',' + ' $19'
    elif first == ('Car wash'):
        first = first.capitalize() + ',' + ' $7'
    else:
        first = first.capitalize() + ',' + ' $12'

if second == "-":
    second == 'No service'
else:
    second = second.lower()
    if second == ('Oil change'):
        second = second.capitalize() + ',' + ' $35'
    elif second == ('Tire rotation'):
        second = second.capitalize() + ',' + ' $19'
    elif second == ('Car wash'):
        second = second.capitalize() + ',' + ' $7'
    else:
        second = second.capitalize() + ',' + ' $12'
#PART 3
print()
print("Davy's auto shop invoice")
print()
print('Service 1:', first)
print('Service 2:', second)

#PART 4
callback_price1 = 0
callback_price2 = 0
if (first == "No service"):
    callback_price1 = 0
else:
    callback_price1 = first.split("$")[1]
if(second == "No service"):
    callback_price2 = 0
else:
    callback_price2 = second.split("$")[1]

total = int(callback_price1) + int(callback_price2)
print()
print('Total: $' +str(total))
