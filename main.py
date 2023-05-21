from operation import Admin
import sys

class Main:
    def execution(self, choice):
        if choice == 1:
            print("-----Add Food-----")
            obj.add_food()
        if choice == 2:
            print("-----View Food List-----")
            obj.view_food_list()
        if choice == 0:
            print("Thank you!!!")
            sys.exit()

if __name__ == '__main__':
    obj = Admin()
    objmain = Main()
    while True:
        choice = int(input("Enter\n1. Add Food\n2. View Food List\n0. Exit\n"))
        objmain.execution(choice)