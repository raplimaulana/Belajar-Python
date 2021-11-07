class Hero:
    #private variable
    __jumlah = 0

    def __init__(self,name,health):
        self.__name = name
        Hero.__jumlah += 1

    #method ini hanya bisa dipakai oleh object
    def getJumlah(self):
        return Hero.__jumlah

    #method ini hanya bisa dipakai oleh class
    #tidak memiliki argument
    def getJumlah1():
        return Hero.__jumlah

    #static method

    #1. bisa dipamggil secara langsung tanpa harus membuat instan object dari kelas yang bersangkutan.
    #   dengan kata lain agar methodnya dapat digunakan bersama oleh object ataupun class
    #2. static method kurang lebih hampir sama dengan fungsi biasa, hanya saja ia diletakkan dalam sebuah kelas.
    #3. static method tidak memiliki informasi apa pun selain dari parameter yang diterimanya.
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    #class method (.self versi class)

    #mirip dengan static method hanya saja memiliki parameter
    #1. parameter pertama dari @classmethod selalu merupakan kelasnya sendiri.
    #2. misalkan class method dengan nama getJumlah3() berada dalam kelas Hero,
    #   maka parameter pertama (yaitu parameter cls) adalah kelas Hero.
    #3. parameter pertama tidak harus bernama cls, bisa bernama apa saja akan tetapi isinya tetap sama yaitu kelasnya sendiri,
    # berbeda dengan static method yang tidak memiliki parameter tambahan apa pun kecuali parameter asli.
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

hero1 = Hero("Ursa",150)
hero2 = Hero("Razor",100)
hero3 = Hero("Dragon",200)

print(hero1.getJumlah())
print(Hero.getJumlah1())
print()

print(hero1.getJumlah2())
print(Hero.getJumlah2())
print()

print(Hero.getJumlah3())
print()

print(Hero.healthbaru(100))
print(hero1.healthbaru(500))
