#Christian Espinoza
#03/2/2025
#File to contain the class and subclass needed for shift supervisor 

class Employee:

    def __init__(self, name, identification, department, job_title):
        self.__name = name
        self.__identificaiton = identification
        self.__department = department
        self.__job_title = job_title 

    def displayEmployees(self):
        print('\n')
        print(f'Employee INFO\n------------\n\
              {self.__name} \t {self.__identificaiton} \
              \t{self.__department} \t {self.__job_title}')

    def displayEmployee_v2(self):

        print(f'Employee Info\
              \nName: {self.__name}\
              \n ID: {self.__identificaiton}\
              \n Department: {self.__department}\
              \n Title: {self.__job_title}')
        
    #Mutators
    def set_name(self, name):
        self.__name = name
    
    def set_identification(self, identification):
        self.__identificaiton = identification

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    #Accessors
    def get_name(self):
        return self.__name
    
    def get_identification(self):
        return self.__identificaiton

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title 

class shiftSupervisor(Employee):
  #Initialiing all attributes, includes the employee initializer

    def __init__(self, name, identification, department, job_title, annual_salary, annual_prodBonus):
        super().__init__(name, identification, department, job_title)
        self.__annual_salary = annual_salary
        self.__annual_prodBonus = annual_prodBonus
        #All methods and attributes are inherited from the superclass
    #Mutators
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_prodBonus(self, annual_prodBonus):
        self.__annual_prodBonus = annual_prodBonus
    #Accessors 
    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_prodBonus(self):
        return self.__annual_prodBonus
    

    def display_supervisor(self):
        print('\n')
        print('SHIFT SUPERVISOR')
        print('----------------')
        print("Name: ", self.get_name())
        print("ID: ", self.get_identification())
        print("Department: ", self.get_department())
        print("Job Title: ", self.get_job_title())
        print("Salary: ", self.get_annual_salary())
        print("Production Bonus: ", self.get_annual_prodBonus())