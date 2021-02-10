import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
wall_area = height*width

#PART 2
paint_colors_cost={'red':35,'blue':25,'green':23}

gallon = 350
paint_needed = wall_area/gallon
cans = math.ceil(paint_needed)
print("Wall area: " + str(wall_area) + " square feet")
print("Paint needed: {:.2f} gallons".format(paint_needed))

#PART 3
print("Cans needed: " + str(cans) + " can(s)")

#PART 4
color=input("\nChoose a color to paint the wall:\n")
cost=cans * paint_colors_cost[color.lower()]
print ("Cost of purchasing " + str(color) + " paint: $" + str(cost))

