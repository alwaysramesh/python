class Emp:
    def __init__(self):
        self.bs = 65000
        self.tax = 0

    def show(self):
        print("Basic Salary is:", self.bs)
        ta = self.bs * 0.20
        print("The TA of employee:", ta)

        da = self.bs * 0.35
        print("The DA of employee:", da)

        hra = self.bs * 0.25
        print("The HRA of employee:", hra)

        pf = self.bs * 0.125
        print("The PF of employee:", pf)

        gs = self.bs + ta + da + hra - pf

        if gs >= 120000:
            self.tax = gs * 0.3
            print("Your tax is:", self.tax)
        elif gs >= 100000:
            self.tax = gs * 0.2
            print("Your tax:", self.tax)
        elif gs >= 85000:
            self.tax = gs * 0.1
            print("Your tax:", self.tax)

        gst = gs - self.tax
        print("Gross Salary of employee:", gst)

def main():
    obj = Emp()
    obj.show()

if __name__ == "__main__":
    main()
