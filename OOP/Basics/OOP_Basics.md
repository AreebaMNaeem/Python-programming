# 🏗️ Object-Oriented Programming (OOP) Basics

---

## 🔶 What is OOP?

For the code you've written so far, you've used **functions** to organize things. OOP (Object-Oriented Programming) takes organization further by **bundling data and functions together**.

Instead of having separate functions floating around, you create **classes** that hold both the data and the operations that work on that data.

```python
# Old way — separate data and functions
name = "Ali"
age = 25
salary = 50000

def display_info(n, a, s):
    print(f"{n} is {a} years old, earning Rs.{s}")

display_info(name, age, salary)
```

```python
# OOP way — data and functions together in a class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display_info(self):
        print(f"{self.name} is {self.age} years old, earning Rs.{self.salary}")

employee = Employee("Ali", 25, 50000)
employee.display_info()
```

Both work. But OOP is **more organized** and **easier to expand** when you have many related pieces.

---

## 🔶 What is a Class?

A **class** is like a **blueprint or template** used to create objects. It defines the structure — what data **(attributes)** each thing should have and what actions **(methods)** it can perform.

### ➡️ Analogy: Building a House

Before you build an actual house, you need:
- A blueprint that shows the layout
- Plans for how many rooms, doors, windows
- The design rules everyone must follow

That blueprint is **not a real house**. It's just instructions. You can't live in a blueprint.

---

## 🔶 What is an Object?

An **object** is a **real, concrete creation** or the **instance of the class** that follows the class blueprint. It has actual values and can perform actual actions.


## Example:
```python
# Class — just the design/blueprint
class House:
    def __init__(self, owner, rooms, color):
        self.owner = owner
        self.rooms = rooms
        self.color = color
    
    def describe(self):
        print(f"{self.owner}'s house is {self.color} with {self.rooms} rooms")
```

The class `House` says: "Every house will have an owner, number of rooms, and a color. And every house can describe itself."

But there's no actual house yet. It's just a definition.

```python
# Objects — actual houses created from the blueprint
house1 = House("Ali", 4, "White")
house2 = House("Sara", 5, "Red")
house3 = House("Bilal", 3, "Blue")

house1.describe()
house2.describe()
house3.describe()
```

**Output:**
```
Ali's house is White with 4 rooms
Sara's house is Red with 5 rooms
Bilal's house is Blue with 3 rooms
```

Each object is **different** (different owners, colors, rooms) but **follows the same structure** (all are houses).

---

## 🔶 Basic Syntax:

```
class ClassName:
    def __init__(self, parameters):
        self.attribute = parameters
    
    def method(self):
        pass
```

### ➡️ Breaking it down:

- `class ClassName` : Define a class named ClassName   
- `__init__(self, parameters)` : Special method that runs automatically when creating an object  
- `self.attribute` : Create an attribute (data) for this object   
- `def method(self)` : Create a method (function) that the object can perform 



---

## 🔶 Understanding `self`:

`self` is a special variable that means **"this specific object"** or **"this particular instance"**.

### ➡️ Analogy: Restaurant Order Slip

Imagine you're at a restaurant. Each order slip has:
- Customer name
- Food ordered
- Table number

When the chef looks at **this** slip, they say: "For **this** customer, cook **this** food and put it at **this** table."


```python
class RestaurantOrder:
    def __init__(self, customer, food, table):
        self.customer = customer
        self.food = food
        self.table = table
    
    def prepare(self):
        print(f"Preparing {self.food} for {self.customer} at table {self.table}")

order1 = RestaurantOrder("Zara", "Biryani", 5)
order2 = RestaurantOrder("Hassan", "Karahi", 3)

order1.prepare()
order2.prepare()
```

**Output:**
```
Preparing Biryani for Zara at table 5
Preparing Karahi for Hassan at table 3
```

When you call `order1.prepare()`, Python knows to use `order1`'s data. Inside the method, `self` is automatically `order1`.

---

## 🔶 The `__init__` Method : 

`__init__` (pronounced "dunder init") is a **special method** that runs automatically the moment you create a new object.

It's like the **startup process** — it initializes everything the object needs to begin working.

### ➡️ Analogy: Filling Out a New SIM Card Form

When you get a new SIM card from a mobile shop:

- The shopkeeper asks for your name
- He asks for your CNIC number
- He asks which package you want (call, SMS, internet)
- He registers all this info against your new number, and it's ready to use

This registration step is like __init__. It runs once automatically the moment a new SIM (object) is created.

```python
class SimCard:
    def __init__(self, name, package):
        self.name = name
        self.package = package
    
    def show_info(self):
        print(f"SIM Owner: {self.name}, Package: {self.package}")

sim1 = SimCard("Sara", "Monthly Internet")
sim1.show_info()
```

**Output:**
```
SIM Owner: Sara, Package: Monthly Internet
```

When you write `SimCard("Sara", "Monthly Internet")`, Python automatically calls `__init__`. It sets up the name and package. 

> 💡 **Important:** Never call `__init__` manually. It runs automatically when you create an object.

---

## 🔶 Attributes vs Methods :

**Attributes** = Data/Properties (what the object **has**)

**Methods** = Functions (what the object **can do**)

```python
class Car:
    def __init__(self, brand, color, fuel):
        # ATTRIBUTES — data about the car
        self.brand = brand
        self.color = color
        self.fuel = fuel
    
    # METHODS — things the car can do
    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            print(f"{self.brand} is driving. Fuel: {self.fuel}%")
        else:
            print("No fuel! Can't drive.")
    
    def refuel(self):
        self.fuel = 100
        print(f"{self.brand} refueled to 100%")

car = Car("Toyota", "Blue", 50)

# Accessing attributes
print(car.brand)
print(car.color)

# Calling methods
car.drive()
car.refuel()
```

**Output:**
```
Toyota
Blue
Toyota is driving. Fuel: 40%
Toyota refueled to 100%
```

---
