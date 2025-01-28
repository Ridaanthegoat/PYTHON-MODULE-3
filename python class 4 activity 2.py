from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class snake(Animal):
        def move(self):
            print("i crawl and eat rats")
    
class Human(Animal):
        def move(self):
            print("i am intelligent and smart")

class cat(Animal):
        def move(self):
            print("i drink milk")

class dog(Animal):
        def move(self):
            print("i scare cats")

a=snake()
a.move()

b=Human()
b.move()

c=cat()
c.move()

d=dog()
d.move()
    
    
    
