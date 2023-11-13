import math

#1
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def circumference(self):
        return self.perimeter()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

#2

class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest calculated. New balance: ${self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")

#3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        if self.fuel_efficiency > 0:
            mileage = distance / self.fuel_efficiency
            print(f"The car can travel {mileage:.2f} miles on {distance:.2f} gallons of fuel.")
        else:
            print("Fuel efficiency not specified.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        if self.fuel_efficiency > 0:
            mileage = distance / self.fuel_efficiency
            print(f"The motorcycle can travel {mileage:.2f} miles on {distance:.2f} gallons of fuel.")
        else:
            print("Fuel efficiency not specified.")

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self, load_weight):
        if self.towing_capacity > 0:
            if load_weight <= self.towing_capacity:
                print(f"The truck can tow {load_weight} pounds.")
            else:
                print(f"Exceeds towing capacity. The truck can tow up to {self.towing_capacity} pounds.")
        else:
            print("Towing capacity not specified.")

#4      
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager, Salary: ${self.salary}, Department: {self.department}")

    def approve_leave(self):
        print(f"{self.name} (Manager) has approved the leave.")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer, Salary: ${self.salary}, Programming Language: {self.programming_language}")

    def code(self):
        print(f"{self.name} (Engineer) is coding in {self.programming_language}.")

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson, Salary: ${self.salary}, Sales Target: ${self.sales_target}")

    def make_sale(self, amount):
        if amount >= self.sales_target:
            print(f"{self.name} (Salesperson) has achieved the sales target!")
        else:
            print(f"{self.name} (Salesperson) made a sale of ${amount}.")

#5

class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} inches.")

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def swim(self):
        print(f"{self.name} is swimming.")

#6
class LibraryItem:
    def __init__(self, title, author_or_director, item_id, checked_out=False):
        self.title = title
        self.author_or_director = author_or_director
        self.item_id = item_id
        self.checked_out = checked_out

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author/Director: {self.author_or_director}")
        print(f"Item ID: {self.item_id}")
        print(f"Status: {'Checked Out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, checked_out=False):
        super().__init__(title, author, item_id, checked_out)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration, checked_out=False):
        super().__init__(title, director, item_id, checked_out)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number, checked_out=False):
        super().__init__(title, publisher, item_id, checked_out)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")
