class a:
    def add(self):
        print("This is add class")

class b:
    def mul(self):
        print("This is mul class")

class c(a, b):
    def div(self):
        print("This is div class")

class d(c):
    def mod(self):
        print("This is mod class")

class g(d):
    def grand(self):
        print("This is all")

obs = c()
obd = d()


obs.add()
obs.div()
obs.mul()


obd.mul()
obd.add()
obd.mod()

