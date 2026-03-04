class Shopping:
    discount=10
    @classmethod
    def disc(cls,discount):
        cls.discount=discount
        print(cls.discount)
    def details(self,name,phoneno):#instance method
        self.name = name
        self.phoneno = phoneno
        print(f"your name is {self.name}")
        print(f"your contat no{self.phoneno}")
    @staticmethod
    def convey():
        print("thank you for shopping")
s1=Shopping()
s1.details('karthik',23178)
s1.disc(23)
s1.convey()
Shopping.convey()
Shopping.disc(56)



