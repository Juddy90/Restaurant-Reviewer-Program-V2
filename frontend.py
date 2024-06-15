import sys

#This class has been created to hold the Program's front end functionality. Its
#name clearly defines what it does in that it acts as the FrontEndUI
class FrontEndUI:
    #This contructor has been created to initiate the varibales for the restaurant
    #data. These variables are then able to be used throughout the program.
    def __init__(self,backEndManager):

        self.__program_manager=backEndManager
        self.run_program=self.run_program()

   
    #This method was created to run the overall program. This method calls on
    #multiple methods allow the program to function. Its name clearly
    #explains that it runs the program.
    def run_program(self):
        #Intro has been created to hold the value of the introduction so it
        #could be printed in one section without exceeding the limit of python's
        #80 column limit
        intro = ("\n"*80)
        intro += ("This program has been designed to allow you to ")
        intro += ("submit feeback for restaurants.\n")
        intro +=("\n"*10)

        sys.stdout.write(intro)

        #This try except has been created to show an error if the program is
        #unable to find the data.csv file.
        try:
            self.__program_manager.load_csv()
        except:
            sys.stdout.write("\n"*5+"Error: Could not load file"+
                             ", incorrect values in file"+"\n"*5)

        #Choice is the variable that holds the user's menu selection choice.
        #Its name is clear and defines what value it holds inside.
        choice=self.display_menu()

        #This while loop will run while the user's choice is not 5. Each
        #sends the user to a different function of the program and if they
        #select 5 the while loop will end and the program will close.
        while(choice!=5):
            if choice == 1:
                sys.stdout.write("\n"*80)
                self.add_entry()
            elif choice == 2:
                sys.stdout.write("\n"*80)
                self.display_entries()
            elif choice == 3:
                sys.stdout.write("\n"*80)
                self.remove_data()
            elif choice == 4:
                sys.stdout.write("\n"*80)
                self.save_all_data()
            else:
                FrontEndUI.get_string("That is not an option. Click return to continue\n")

            choice=self.display_menu()

        sys.stdout.write("\n"*80)
        sys.stdout.write("Thank you for using this program!\n")

    #This method displays the menu to the user. It name clearly defines what it
    #does.
    def display_menu(self):
        #The display_menu variable has been created so that the program is able
        #to display each line presented to use user without being restricted
        #by python's maximimum 80 column limit.
        display_menu=("\n[1] Add New Restaurant Rating\n")
        display_menu+=("[2] Display Existing Ratings\n")
        display_menu+=("[3] Remove A Rating\n")
        display_menu+=("[4] Save All Changes\n")
        display_menu+=("[5] Exit\n\n")

        sys.stdout.write(display_menu)

        #The user_choice variable is used to stored the users choice from the
        #get_int method. This value will be returned and used elsewhere in the
        #program.
        user_choice = self.get_int("Choose an option ")

        return user_choice

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program.
    #This is a static method as the method will not need to change.
    @staticmethod
    def get_string(prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = sys.stdin.readline().strip()
        return response

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program
    def get_int(self,prompt):

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = None

        #This while loop was created to ensure that a user inputed a correct
        #input. While the user is inputing an incorrect value, they will be
        #prompted to try again.
        while(response == None):
            try:
                response=int(FrontEndUI.get_string(prompt))
            except:
                prompt = "Must select a whole \"number\". Try again: "

            return response

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program
    def get_float(self,prompt):

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = None

        #This while loop was created to ensure that a user inputed a correct
        #input. While the user is inputing an incorrect value, they will be
        #prompted to try again.
        while(response == None):
            try:
                response = float(FrontEndUI.get_string(prompt))
            except:
                prompt = "Must be a number value. Try again: "
            return response
                         
    #This method has been created to enable the user to input new data into the
    #program. This method will ask the user to input the required values and
    #then append them to the list.
    def add_entry(self):
        
        restaurant_name = FrontEndUI.get_string("\nPlease enter restaurant: "
                                                ).lower()
        suburb_data = FrontEndUI.get_string("\nEnter the suburb: ").lower()

        sys.stdout.write("\nThe following are out of 10\n")
        
        food_data = self.get_float("\nEnter the Food Rating: ")
        service_data = self.get_float("\nEnter the Service Rating: ")
        cost_data = self.get_float("\nEnter the Cost Rating: ")

        sys.stdout.write("\nOverall rating must be a whole number out of 10\n")
        
        overall_data = self.get_int("\nEnter your Overall Rating: ")


        #This try/except will attempt to append the inputed data to the list
        #and if unsuccesful will show an error message
        try:
            self.__program_manager.append_to_list(restaurant_name,suburb_data,
                                                   food_data,service_data,
                                                   cost_data,overall_data)

            sys.stdout.write("\n"*80+"Data succesfully added"+"\n"*20)
        
        except:
            sys.stdout.write("\n"*5+"Error: That didnt work, try again"+"\n"*5)           


    #This method was created to be able to display all values to the user. The
    #name of this method was chosen as it clearly defines its actions.
    def display_entries(self):
        x=0

        #This while loop will continue to run as long as x is lower then the
        #amount of entries in the list. Everytime it searches and displays an
        #item, x will have 1 added to it so it will stop once all are displayed
        while(x<self.__program_manager.get_list_len):


            for data in self.__program_manager.get_restaurant_rating():
                sys.stdout.write("\nRestaurant: "+data.restaurant+
                                 "\nLocation: "+(data.suburb_location)+
                                 "\nFood Rating: "+str(data.food_rating)+
                                 "/10\nService Rating: "+
                                 str(data.service_rating)+
                                 "/10\nCost Rating: "+str(data.cost_rating)+
                                 "/10\nOverall Rating: "+
                                 str(data.overall_rating)+"/10\n\n")
            
                x+=1
        sys.stdout.write("Click enter to continue")
        sys.stdin.readline()
        sys.stdout.write("\n"*80)
                
    #This method has been created to allow the user to save all new data into
    #the csv file. The name was chosen as it clearly explains it will save
    #all data
    def save_all_data(self):
        x=0
        try:
            data_file = open("data.csv","w")

            #This while loop will continue to run as long as x is lower than
            #the length of the restaurant data list found in backend
            #This allows the method to write all new data into the CSV
            while(x<self.__program_manager.get_list_len):
                data_file.write(self.__program_manager.get_restaurant_rating()
                                [x].restaurant+",")
                data_file.write((self.__program_manager.get_restaurant_rating()
                                 [x].suburb_location)+",")
                data_file.write(str(self.__program_manager.get_restaurant_rating()
                                    [x].food_rating)+",")
                data_file.write(str(self.__program_manager.get_restaurant_rating()
                                    [x].service_rating)+",")
                data_file.write(str(self.__program_manager.get_restaurant_rating()
                                    [x].cost_rating)+",")
                data_file.write(str(self.__program_manager.get_restaurant_rating()
                                    [x].overall_rating)+"\n")
                x += 1
            data_file.close()
            sys.stdout.write("Data has been saved! Click enter to continue")
            sys.stdin.readline()
            sys.stdout.write("\n"*80)
        except:
            sys.stdout.write("Error, could not save")
        
    #This method was created to remove data from the list. When is is called on
    #the method will have the user search for a restaurant and delete any
    #matching entries.
    def remove_data(self):
            if (self.__program_manager.get_list_len<=0):
                sys.stdout.write("There are no entries yet, add entry first!\n")
                return
            #search_restaurant is a variable being used to hold the value of the
            #restaurant the user is searching for to delete.
            search_restaurant = FrontEndUI.get_string("What entry do you want to delete? "
                                           ).lower()

            x=0
            #This while loop will run while x is less then the number of entries
            #in the list. As it searches each line and removing any entries it
            #will add 1 to x for each line it searches ensuring it stops once all
            #are searched
            while(x<self.__program_manager.get_list_len):
                if (search_restaurant == self.__program_manager.
                    get_restaurant_rating()[x].restaurant):

                    del (self.__program_manager.get_restaurant_rating()[x])

                    x-=1
                    
                x += 1

            sys.stdout.write("\n"*80+"Data succesfully deleted"+"\n"*20)
    
