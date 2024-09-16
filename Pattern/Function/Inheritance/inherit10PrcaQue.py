class a:
    def add(self):
        print("This is add class")

class b(a):
    def mul(self):
        print("This is mul class")

class c(b):
    def div(self):
        print("This is div class")

class d(c):
    def mod(self):
        print("This is mod class")
class g(d):
    def grand(self):
        print("This is all")
obs = c()
obs.div()
obd = d()
obd.mod()

# obs.add()
# obs.div();
# obs.mul();
# obs.grand()

# # obd.mul();
# # obd.add()
# # obd.mod()
# # obd.grand()