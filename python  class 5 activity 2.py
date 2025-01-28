class encapsulation:
    def __init__(self):
        self.__maxprice=500
    def show(self):
        print(self.__maxprice,"is maxprice")
    def newmaxprice(self,updated):
            self.__maxprice==updated
obj1=encapsulation()
obj1.show()
obj1.newmaxprice(400)
obj1.show()