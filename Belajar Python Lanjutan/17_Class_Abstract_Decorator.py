from abc import ABC,abstractmethod

class Button(ABC):

    def __init__(self,link):
        self.link = link

    @abstractmethod
    def click(self):
        pass

    #jika variabel tidak diketahui, bisa gunakan @property untuk melakukan setter getter di class lain
    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        #print("Go to {}".format(self.link))
        print("Go to {}".format(self.__linkgaktahu))

    @Button.link.setter
    def link(self,input):
        self.__linkgaktahu = input

    @link.getter
    def link(self):
        return self.__linkgaktahu



k1 = PushButton("www.seblakmerah.com")

k1.click()

