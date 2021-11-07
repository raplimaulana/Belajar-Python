from datetime import date

class Employee:
    def __init__(self,name,salary,day,month,year):
        self.__name = name
        self.__salary = salary
        self.__day = day
        self.__month = month
        self.__year = year
        self.__hireday = date.today().strftime('%d-%m-%y')

    @property
    def name(self):
        pass

    @property
    def hireDay(self):
        pass

    @property
    def salary(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @hireDay.getter
    def hireDay(self):
        return self.__hireday

    @salary.getter
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,input):
        self.__raise = int(self.__salary * (input/100))
        self.__salary += self.__raise

class Manager(Employee):
    def __init__(self,name,salary,day,month,year):
        super().__init__(name,salary,day,month,year)
        __bonus = 0

    @property
    def bonus(self):
        pass

    @bonus.setter
    def bonus(self,bonus):
        self.__bonus += bonus

    @bonus.getter
    def bonus(self):
        return self.__bonus

    @Employee.salary.setter
    def salary(self,input):
        self.__salaryBase = self.salary()



newManager = Manager("Steven",80000,15,12,1987)
newEmployee = Employee("Donni",50000,1,10,1997)

newEmployee.salary = 10

print("Nama Pegawai : {} \nSalary : {}  ".format(newEmployee.name,newEmployee.salary))
print("Nama Boss : {} \nSalary : {}  ".format(newManager.name,newManager.salary))

