

class Employee:
    

    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber

    #Mutators   
    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName
    
    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber

    #Accessors 

    def get_employeeName(self):
        return self.__employeeName
    
    def get_employeeNumber(self):
        return self.__employeeNumber
    

class productionWorker(Employee): 

    def __init__(self, employeeName, employeeNumber, shiftNumber, payRate):

        Employee.__init__(self, employeeName, employeeNumber)

        self.__shiftNumber = shiftNumber
        self.__payRate = payRate

    #Mutators 

    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber

    def set_payRate(self, payRate):
        self.__payRate = payRate

    # Accessors 

    def get_shiftNumber(self):
        return self.__shiftNumber
    
    def get_payRate(self):
        return self.__payRate

        