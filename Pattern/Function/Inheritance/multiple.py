class p:
    def add(self):
        print("This is add class")

class m:
    def mul(self):
        print("This is mul class")

class s(m,p):
    def div(self):
        print("This is div class")

class d(m,p):
    def mod(self):
        print("This is mod class")
obs = s();
obd = d();

obs.add()
obs.div();
obs.mul();

obd.mul();
obd.add()
obd.mod()