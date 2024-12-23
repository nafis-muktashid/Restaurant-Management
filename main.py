from FoodItem import FoodItem
from  Menu import Menu
from User import Customer, Admin, Employee
from Resturants import Resturant
from Orders import Order

Garrison = Resturant("Hotel Garrison")

def customer_menu():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(Garrison)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(Garrison, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Option")




def admin_menu():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    print(f"Welcome {admin.name}")
    while True:
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = input("Enter Item Quantity: ")
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(Garrison, item)

        elif choice == 2:
            name = input("Enter Employee Name: ")
            phone = input("Enter Employee Phone: ")
            email = input("Enter Employee email : ")
            designation = input("Enter Employee designation: ")
            age = input("Enter Employee age: ")
            salary = input("Enter Employee salary: ")
            address = input("Enter Employee address: ")

            emp = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(Garrison, emp)

        elif choice == 3:
            admin.view_employee(Garrison)
        elif choice == 4:
            admin.view_menu(Garrison)
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.delete_item(Garrison, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Option")
            

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!!")