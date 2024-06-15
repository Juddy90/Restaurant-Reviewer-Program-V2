#This class has been called restaurant data as it holds the variables for the
#list stored in the RestaurantManager class. The class name was chosen as it
#clearly explains what it does
class RestaurantData:

    __restaurant = None
    #The restaurant variable was created to store the name of the restaurant
    #the user is creating. It clearly defines the information that will be held in it
    __suburb_location = None
    #As the above variable, suburb_location stored the name of the suburb
    __food_rating = 0
    #As above, the food_rating stores the rating of food quality.
    __service_rating = 0
    #As above, the service_rating stores the value of service quality.
    __cost_rating = 0
    #As above, the cost_rating stores the value of value for money.
    __overall_rating = 0
    #As above, the overall_rating stores the value of overall rating.

    
    #This contructor has been created to initiate the varibales for the restaurant
    #data. These variables are then able to be used throughout the program.
    def __init__(self,restaurant_name,suburb_data,food_data,service_data,
                 cost_data,overall_data):

        self.__restaurant=restaurant_name
        self.__suburb_location=suburb_data
        self.__food_rating=food_data
        self.__service_rating=service_data
        self.__cost_rating=cost_data
        self.__overall_rating=overall_data

    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def restaurant(self):
        return self.__restaurant
    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def suburb_location(self):
        return self.__suburb_location
    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def food_rating(self):
        return self.__food_rating
    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def service_rating(self):
        return self.__service_rating
    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def cost_rating(self):
        return self.__cost_rating
    #This getter has been created as the varibales are private. This getter allows
    #the rest of the program to access this data.
    @property
    def overall_rating(self):
        return self.__overall_rating

    #This setter has been created to allow the program to raise an error if the
    #value entered is a negative value.
    @food_rating.setter
    def food_rating(self, new_food_rating):
        if(new_food_rating < 0):
            raise ValueError ("Value cannot be below 0")
        self.__food_rating = new_food_rating
    #This setter has been created to allow the program to raise an error if the
    #value entered is a negative value.
    @service_rating.setter
    def service_rating(self, new_service_rating):
        if(new_service_rating < 0):
            raise ValueError ("Value cannot be below 0")
        self.__service_rating = new_service_rating
    #This setter has been created to allow the program to raise an error if the
    #value entered is a negative value.
    @cost_rating.setter
    def cost_rating(self, new_cost_rating):
        if(new_cost_rating < 0):
            raise ValueError ("Value cannot be below 0")
        self.__cost_rating = new_cost_rating
    #This setter has been created to allow the program to raise an error if the
    #value entered is a negative value.
    @overall_rating.setter
    def overall_rating(self, new_overall_rating):
        if(new_overall_rating < 0):
            raise ValueError ("Value cannot be below 0")
        self.__overall_rating = new_overall_rating

#The BackEndManmager class holds the list where all user inputs will be stored
#It also holds the backend features of the program manager and is instrumental
#in the program running.
class BackEndManager():
    #This contructor has been created to initiate the list for for the
    #program and allow the backend to use the file_name specified in the
    #application file.
    def __init__(self,file_name):

        #This list has been set to private and is called restaurant rating as
        #this is where all information entered by the user will be stored
        self.__restaurant_rating=[]
        #This variable has been created to use the file name specified in the application
        #file.
        self.__file_name=file_name
        
    #This method has been created to be able to use the list in the rest of
    #the program as the list has been set to private.
    def get_restaurant_rating(self):
        return self.__restaurant_rating
    #This method has been created to allow the rest of the program to use this value
    #in while loops. This method has been created as static as the value should not
    #change while being used.
    @property
    def get_list_len(self):
        return len(self.__restaurant_rating)
        
    #This method has been created to load and read the csv file storing
    #all data from this program. Its name clearly defines what it does.
    def load_csv(self):

        with open(self.__file_name,"r") as data_file:
            for line in data_file:
                #This variable has been created to store all data inputed
                #directly from the csv. It has been called fields as it
                #clearly defines the imported fields from the CSV.
                fields = line.strip().split(",")
                #restaurant_name has been created to hold the value imported
                #from the csv's first column which is restaurants
                restaurant_name = fields[0]
                #suburb_data has been created to hold the value imported
                #from the csv's second column which is the suburb data
                suburb_data = fields[1]
                #food_data has been created to hold the value imported
                #from the csv's third column which is the food quality
                food_data = fields[2]
                #service_data has been created to hold the value imported
                #from the csv's fourth column which is service rating
                service_data = fields[3]
                #cost_data has been created to hold the value imported
                #from the csv's fifth column which is value for money rating
                cost_data = fields[4]
                #overall_rating has been created to hold the value imported
                #from the csv's sixth column which was the restaurants
                #overall rating
                overall_data = fields[5]
                self.append_to_list(restaurant_name,suburb_data,food_data,
                                    service_data,cost_data,overall_data)

    #This method was created to append the imported data from the csv into
    #the restaurant_rating list above. It clearly defines its actions as append_
    #to_list
    def append_to_list(self,restaurant_name,suburb_data,food_data,service_data,
                       cost_data,overall_data):

        restaurant_data = RestaurantData(restaurant_name,suburb_data,food_data,service_data,
                                         cost_data,overall_data)

        self.__restaurant_rating.append(restaurant_data)
