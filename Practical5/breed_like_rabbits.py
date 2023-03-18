# inbreeding coefficient
#first generation has two rabbits
#one more generation, number of rabbits plus 2
#repeat until total number more than 100

n = 2 #origin number of rabbits
z = 1 #how many generations
while n <= 100:
    m = n * 2  #inbreeding coefficient
    n = m #total number of rabits
    z = z+1
    print (m)
if n > 100:
    print("it continues",z, "genenrations to over 100")

input()
