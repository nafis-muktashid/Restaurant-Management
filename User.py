from abc import ABC
from Orders import Order



class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, resturant):
        resturant.menu.show_menu()

    def add_to_cart(self, resturant, item_name, quantity):
        item = resturant.menu.find_item(item_name)
        if item:
            if quantity < item.quantity:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
            else:
                print("Item quantity Exceeded")

        else:
            print("No Item Found")

    def view_cart(self):
        print("-----VIEW CART--------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} Paid")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, resturant, employee):
        resturant.add_employee(employee)
        
    def view_employee(self, resturant):
        print("Employees List!")
        resturant.view_employee()

    def add_new_item(self, resturant, item):
        resturant.menu.add_menu_item(item)

    def delete_item(self, resturant, item):
        resturant.menu.remove_item(item)
    
    def view_menu(self, resturant):
        resturant.menu.show_menu()