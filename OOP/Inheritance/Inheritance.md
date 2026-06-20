# 📌 Inheritance in Python

---

## 🔶 What is Inheritance?

Inheritance is when you have a **parent class** with some common features, and **child classes** that use those features and add their own unique stuff.

Instead of writing the same code multiple times, you write it once in the parent and let children use it.

```python
# Without inheritance — repeating code
class Doctor:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Engineer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# With inheritance — write once, use many times
class Professional:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Doctor(Professional):
    def prescribe(self):
        print("Prescribing medicine...")

class Engineer(Professional):
    def build(self):
        print("Building infrastructure...")
```

---

## 🔶 Types of Inheritance :

### 1️⃣ Single Inheritance

**One child, one parent.**

**Original Analogy: Student learning from a tutor**

A student gets all knowledge from one tutor. The student learns what the tutor teaches but can add their own skills through practice.

```python
class Tutor:
    def teach_math(self):
        print("Teaching algebra...")

class Student(Tutor):
    def practice(self):
        print("Student practicing...")

student = Student()
student.teach_math()
student.practice()
```

**Output:**
```
Teaching algebra...
Student practicing...
```

---

### 2️⃣ Multiple Inheritance

**One child, multiple parents.**

**Original Analogy: Recipe combining techniques**

You learn baking from a pastry chef and seasoning from a spice merchant. You combine both skills to create amazing fusion dishes.

```python
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")
    
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    
    def take_photo(self):
        print(f"Taking {self.megapixels}MP photo")
    
    def record_video(self):
        print(f"Recording video with {self.megapixels}MP camera")

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, megapixels, storage):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, megapixels)
        self.storage = storage
    
    def open_app(self, app_name):
        print(f"Opening {app_name}")

my_phone = Smartphone("Samsung", "Galaxy S24", 108, "256GB")
my_phone.call("03001234567")
my_phone.send_sms("Hello!")
my_phone.take_photo()
my_phone.record_video()
my_phone.open_app("Instagram")
```

**Output:**
```
Calling 03001234567 from Samsung Galaxy S24
Sending SMS: Hello!
Taking 108MP photo
Recording video with 108MP camera
Opening Instagram
```

---

### 3️⃣ Multilevel Inheritance

**Grandparent → Parent → Child hierarchy.**

**Original Analogy: Company organizational structure**

CEO (grandparent) → Manager (parent) → Team Lead (child). Each level has more specific responsibilities.

```python
class CEO:
    def strategic_plan(self):
        print("CEO making strategy...")

class Manager(CEO):
    def manage_team(self):
        print("Manager overseeing team...")

class TeamLead(Manager):
    def assign_tasks(self):
        print("Team lead assigning work...")

lead = TeamLead()
lead.strategic_plan()
lead.manage_team()
lead.assign_tasks()
```

**Output:**
```
CEO making strategy...
Manager overseeing team...
Team lead assigning work...
```

---

### 4️⃣ Hierarchical Inheritance

**Multiple children, one parent.**

**Original Analogy: Different branches of a bank**

Head office (parent) → Savings branch (child) → Loan branch (child). All branches follow head office rules but have specialized services.

```python
class BankService:
    def __init__(self, branch_name):
        self.branch_name = branch_name

class SavingsAccount(BankService):
    def save_money(self):
        print(f"{self.branch_name} - Save money")

class LoanService(BankService):
    def give_loan(self):
        print(f"{self.branch_name} - Give loan")

savings = SavingsAccount("Downtown")
loan = LoanService("Uptown")

savings.save_money()
loan.give_loan()
```

**Output:**
```
Downtown - Save money
Uptown - Give loan
```

---

### 5️⃣ Hybrid Inheritance

**A mix of multiple + multilevel + hierarchical.**

**Original Analogy: Multi-skilled athlete**

An athlete learns running from a track coach, swimming from a water coach, and combines both to become a triathlon champion.

```python
class TrackCoach:
    def run_training(self):
        print("Track training...")

class WaterCoach:
    def swim_training(self):
        print("Water training...")

class StrengthCoach:
    def strength_training(self):
        print("Strength training...")

class TriathlonAthlete(TrackCoach, WaterCoach, StrengthCoach):
    def compete(self):
        self.run_training()
        self.swim_training()
        self.strength_training()
        print("Ready to compete!")

athlete = TriathlonAthlete()
athlete.compete()
```

**Output:**
```
Track training...
Water training...
Strength training...
Ready to compete!
```

---

## 🔶 What is `super()`?

`super()` lets a child class **borrow** methods from its parent class instead of rewriting them.

**Original Analogy: Building on your parent's foundation**

Your parents built a strong house foundation. You don't rebuild the foundation — you use it and add your own rooms on top.

```python
class House:
    def __init__(self, location, rooms):
        self.location = location
        self.rooms = rooms

class MyHouse(House):
    def __init__(self, location, rooms, garden):
        super().__init__(location, rooms)
        self.garden = garden

house = MyHouse("Karachi", 5, "Yes")
print(f"Location: {house.location}, Rooms: {house.rooms}, Garden: {house.garden}")
```

**Output:**
```
Location: Karachi, Rooms: 5, Garden: Yes
```

---

## 🔶 Why use `super()` instead of hardcoding parent class?

### ❌ Bad Way — Hardcoding parent name:

```python
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class SavingsBank(Bank):
    def __init__(self, name, balance, interest):
        Bank.__init__(self, name, balance)  # Hardcoded!
        self.interest = interest
```

**Problems:**
- If you rename `Bank` to `BankAccount`, code breaks everywhere
- Messy with multiple inheritance
- Hard to maintain

### ✅ Good Way — Using `super()`:

```python
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class SavingsBank(Bank):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)  # Flexible!
        self.interest = interest
        
    def show_details(self):
        print(f"Bank: {self.name}, Balance: {self.balance}, Interest: {self.interest}%")

account = SavingsBank("Ali's Account", 50000, 5)
account.show_details()
```

**Output:**
```
Bank: Ali's Account, Balance: 50000, Interest: 5%
```

**Why it's better:**
- Parent name can change, code still works
- Works great with multiple inheritance
- Clean and professional

---

## 🔶 Calling Parent Methods with `super()`

```python
class Restaurant:
    def prepare_food(self):
        print("Preparing base ingredients...")

class KarachiRestaurant(Restaurant):
    def prepare_food(self):
        super().prepare_food()
        print("Adding Karachi spices...")

restaurant = KarachiRestaurant()
restaurant.prepare_food()
```

**Output:**
```
Preparing base ingredients...
Adding Karachi spices...
```

---

