# inbreeding coefficient
n = 2 # origin number of rabbit
z = 1 # how many generations
while n <= 100:
    m = n * 2  # inbreeding coefficient
    n = m
    z = z+1
    print (m)
if n > 100:
    print("it continues",z, "genenrations to over 100")

input()
