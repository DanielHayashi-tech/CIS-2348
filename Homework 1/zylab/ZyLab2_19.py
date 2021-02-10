lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print()
print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave))

#PART 2
print()
how_many = float(input('How many servings would you like to make?\n'))
print('Lemonade ingredients - yields {:.2f} servings'.format(how_many))
print('{:.2f} cup(s) lemon juice'.format(lemon*how_many/servings))
print('{:.2f} cup(s) water'.format(water*how_many/servings))
print('{:.2f} cup(s) agave nectar'.format(agave*how_many/servings))

#PART 3
print()
print('Lemonade ingredients - yields {:.2f} servings'.format(how_many))
print('{:.2f} gallon(s) lemon juice'.format(lemon*how_many/servings/16))
print('{:.2f} gallon(s) water'.format(water*how_many/servings/16))
print('{:.2f} gallon(s) agave nectar'.format(agave*how_many/servings/16))
