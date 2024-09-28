class p:
    def add(self):
        print("This is add class")

class s(p):
    def div(self):
        print("This is div class")

class d(p):
    def mod(self):
        print("This is mod class")
obs = s()
obd = d()

obs.add()
obs.div()

obd.add()
obd.mod()