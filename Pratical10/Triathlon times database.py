class triathlon:
    def __init__(self, name, location, swim_time, cycle_time, run_time):
        total_time = int(swim_time)+int(cycle_time)+int(run_time)
        self.n = name
        self.l = location
        self.s = swim_time
        self.c = cycle_time
        self.r = run_time
        self.t = total_time
    def prt(self):
        print("Name:", self.n, " Location:", self.l, " Swim time:", self.s, " Cycle time:", self.c,
              " Run time:", self.r, " Total time:", self.t)

y = triathlon ("n", "l", 1, 2, 3) #a sample
y.prt()

while 1 == 1:
    x = triathlon(input("the althelate's name is: "), input("where test triathlon: "), input("swim time: "),
              input("cycle time: "), input("run time:"))
    x.prt()
