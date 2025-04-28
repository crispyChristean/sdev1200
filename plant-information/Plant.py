class Plant:

    def __init__(self, plantType, cost):
        self.__plantType = plantType
        self.__cost = cost

    #Mutators
    def set_plantType(self, plantType):
        self.__plantType = plantType

    def set_cost(self, cost):
        self.__cost = cost
    #Accessors 
    def get_plantType(self):
        return self.__plantType
    
    def get_cost(self):
        return self.__cost 

    def get_info(self):
        print(f'--------------\
              \nPLANT INFO\
              \nType of Flower: {self.__plantType}\
              \nCost: {self.__cost}\
              \n--------------')
        
class Flower(Plant):
    #Initializing
    def __init__(self, plantType, cost, annual, color):

        Plant.__init__(self, plantType, cost)
        self.__annual = annual 
        self.__color = color 
    #Mutators 
    def set_annual(self, annaul):
        if annaul != bool:
            print("NOT A VALID ARGUMENT TO PASS")
            exit()
        else:
            self.__annual = annaul

    def set_color(self, color):
        self.__color = color
    #Accessors
    def get_annual(self):
        return self.__annual

    def get_color(self):
        return self.__color

    #Other Methods
    def get_info(self):
        print(f'--------------\
              \nPLANT INFO\
              \nType of Flower: {self._Plant__plantType}\
              \nCost: {self._Plant__cost}\
              \nIs it Annual: {self.__annual}\
              \nType of Color: {self.__color}\
              \n--------------')
        #I finally figured it out, the reason why I was having trouble
        #getting the attributes worling is because when it's called the 
        #program interprets .__ as an attribute in the subclass than from the 
        #superclass. 
        