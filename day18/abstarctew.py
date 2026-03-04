from abc import ABC , abstractmethod
class Bank:
    def greet(self):
        print("your bank account details")
    @abstractmethod
    def depositlimit(self):
        pass
    def withdrawlimit(self):
        pass
class Salaryacc(Bank):
    def greet(self):
        print("your bank account details")
    def depositlimit(self):
        print("you has no limit")
    def withdrawlimit(self):
        print("you can withdrw between 20k-100k")
class Jointacc(Bank):
    def greet(self):
        print("your bank account details")
    def depositlimit(self):
        print("you has to deposit min 500 limit")
    def withdrawlimit(self):
        print("you can withdrw between 500 - 50k")
class Savingacc(Bank):
    def greet(self):
        print("your bank account details")
    def depositlimit(self):
        print("you has no limit")
    def withdrawlimit(self):
        print("you can withdrw between 20k-100k")
karthik= Salaryacc()
karthik.greet()
karthik.depositlimit()
karthik.withdrawlimit()
achuth = Savingacc()
achuth.greet()
achuth.depositlimit()
achuth.withdrawlimit()
harish_achuth = Jointacc()
harish_achuth .greet()
harish_achuth .depositlimit()
harish_achuth .withdrawlimit()
