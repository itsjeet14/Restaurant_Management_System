import random

class Admin:
    food_list = []

    def food_id(self):
        return random.randint(1, 100)
        
    def add_food(self):
        name = input("Enter Food Name: ")
        id = self.food_id()
        quantity = input("Enter Quantity: ")
        price = float(input("Enter Price: "))

        lst = {'id': id, 'name': name, 'quantity': quantity, 'price': price}
        self.food_list.append(lst)

    def view_food_list(self):
        if len(self.food_list) == 0:
            print("Food List is Empty")
        else:
            for i in self.food_list:
                print(i)