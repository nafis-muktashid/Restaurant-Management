from Menu import Menu



class Resturant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        
    def view_employee(self):
        for e in self.employees:
            print(e.name, e.phone, e.email, e.address)
