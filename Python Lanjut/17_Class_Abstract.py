#abc = Abstract Base Class
from abc import ABC,abstractmethod

class Button(ABC):

    #class yang menginheritance Button harus memiliki method click, jika tidak akan terjadi error
    @abstractmethod
    def click(self):
        pass

class pushButton(Button):

    def click(self):
        print("push button click")

class selectButton(Button):

    def click(self):
        print("radio button click")

x1 = pushButton()
x1.click()
