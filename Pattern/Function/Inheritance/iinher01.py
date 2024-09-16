class papa:
    def add(self, a,b):
        print(a+b)
    def minus(self, a,b):
        print(a-b)
class son(papa):
    def mul(self, a,b):
        print(a*b)

class grandson(son):
    def show(self):
        print("This is  grand son class ")

obj = grandson()
obj.add(12,12)
obj.mul(12,12)
obj.minus(12,12)
obj.show()