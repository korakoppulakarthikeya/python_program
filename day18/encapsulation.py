class Linkedin:
    def __init__(self,username,password,friends):
        self.username = username#public
        self.__password = password#protected
        self._friends = friends#private
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
    @property
    def friendslist(self):
        return self._friends
    @friendslist.setter
    def friendslist(self,new_friends):
        self._friends = new_friends

karthik= Linkedin('korakoopula karthikeya','Karthikya@923',89)
print(f"username :{karthik.username}")
print(f"your passkey is :{karthik.getpassword()} ")
karthik.setpassword('Bunny')
print(karthik.getpassword())
karthik.friendslist = 98
print(karthik.friendslist)