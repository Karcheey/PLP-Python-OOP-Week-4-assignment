# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Parent Class
class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' by {self.author}"

# Child Class (inherits from Publication)
class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)  # call parent constructor
        self.pages = pages

    # Method to show book details
    def book_details(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Example usage
book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("Things Fall Apart", "Chinua Achebe", 209)

print(book1.info())          # From parent class
print(book1.book_details())  # From child class

print(book2.info())
print(book2.book_details())


# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
# while Plane.move() prints "Flying" ✈️).

# Parent Class
class Vehicle:
    def move(self):
        return "This vehicle moves in some way."

# Child Classes with Polymorphism
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Bike(Vehicle):
    def move(self):
        return "Riding 🚴"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage
vehicles = [Car(), Bike(), Plane(), Boat()]

for v in vehicles:
    print(v.move())



import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
