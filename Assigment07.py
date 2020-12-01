#-------------------------------------------------#
# Title: Pickling and error handling in grocery items
# Description: Demonstrates pickling and exception handling in one script
# ChangeLog: (who,when,what)
# K.Hyojin Dev, 11/30/2020 , created script
#-------------------------------------------------#

import pickle # dump and load

# Data -------------------------------------------- #
strFileName = 'grocery_data.dat'
lstitems = []
dicrow = {}
item = ''
cost = ''
# Processing -------------------------------------- #
class Processor:
    @staticmethod
    def adding_data(item, cost, list_of_data):
        dicrow = {"item": item, "cost": cost}
        list_of_data.append(dicrow)
        print(*list_of_data)
    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        objfile = open(file_name, "ab")
        pickle.dump(list_of_data, objfile)
        objfile.close()
    @staticmethod
    def read_data_from_file(file_name):
        try:
            objfile = open(file_name, "rb")
            list_of_data = pickle.load(objfile)
            objfile.close()
            return list_of_data
        except AttributeError:
            pass

class IO:
    @staticmethod
    def asking_add_data():
        item = input("What did you buy today? ")
        cost = input("How much was for the item? ")
        return item, cost

# main body#
while (True):
    print("""
    Menu of Options
    1) Add a new item
    2) Save Data to File
    3) Show current data
    4) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line for looks

    if (strChoice.strip() == "1"): # add data
        item, cost = IO.asking_add_data()
        Processor.adding_data(item, cost, lstitems)

    elif (strChoice.strip() == "2"): # save data
        print("Would you like to save data? ")
        answers = input("Enter 'y' and 'n': ")
        try:
            if answers == 'y':
                Processor.save_data_to_file(strFileName, lstitems)
                print("Saved!")
        except:
            print('Your data is not saved')

    elif (strChoice.strip() == "3"): # show current data
        print("Your current data is: ")
        print(Processor.read_data_from_file(strFileName))

    elif(strChoice.strip() == "4"):
        print("Do you want to exit the program? ")
        answers = input("Please press enter/return key to exit")
        break




