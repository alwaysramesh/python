class car:
    comp = ''
    mod = ''
    price = 0

    def get_car_detail(self,a,b,c):
        self.comp = a
        self.mod = b
        self.price = c
    def show(self):
        print("CAR company : ", self.comp)
        print("CAR Modal : ", self.mod)
        print("CAR Price : ", self.price)
        print("----------------------------------")
        print()

mycar = car()
mycar.get_car_detail("Audi","Q9",599)
mycar.show()

mycar2 = car()
mycar2.get_car_detail("Lambo","Tarzon",12345)
mycar2.show()

mycar3 = car()
mycar3.get_car_detail("maruti","Alto",150)
mycar3.show()



# add car averagae  2)make function(method) and add how mach far go car 3) aver*methodmake 


#Q.2 a class calculator make 6 difff function which take one or two take pairameter deppend 


'''construtor is a special 
 type of function which is declare by init'''