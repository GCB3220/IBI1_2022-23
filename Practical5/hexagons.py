z = 1 # how many hexagons
for z in range (1,6): # 1 to 5
    x = 2 * z * (2 * z - 1) / 2
    print(x)
    z = z+1 #add a hexagon
print ("over")




# used to calculate h
b = 1
while b == 1: # continue use
    n = eval(input("n = "))
    h = 2*n*(2*n-1)/2 # calculate h
    print(h) # answer
input ()
