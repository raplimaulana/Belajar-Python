class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.info = "name\t : {}\nhealth\t : {}".format(self.__name,self.__health)       --ini ilang, setara method yg di @property
        #jika menggunakan cara diatas variabel bisa diubah user.  jika di buat private, data tidak bisa ditampilkan

        ##self.__info = "name\t : {}\nhealth\t : {}".format(self.__name, self.__health)   --ini diisi, setara dengan #@property

    #method tapi dianggap seperti variable
    @property
    def info(self):
        return "name\t : {}\nhealth\t : {}".format(self.name,self.__health)

    ##@property         --jadi mirip mehod getter bila menggunakan cara ini
    ##def info(self):
        ##return self.__info

    def getHealth(self):
        return self.__health

hero1 = Hero("Ursa",100,50)

print(hero1.info)
print()

hero1.name = "Razor"
print(hero1.info)