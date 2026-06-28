# 🎭 Abstraction in Python

---

## 🔶 What is Abstraction?

Abstraction means **showing only what's necessary** and **hiding all the complex details** underneath.

- Users interact with simple interfaces, while the complicated logic stays hidden.
- In Python abstraction can be implemented through *abstract classes* and *abstract methods* provided by the abc module.
 
Think of it as a **contract** — subclasses must follow certain rules, but HOW they follow them is their choice.

```python
# Abstraction: Users see only what they need
# Implementation details are hidden inside the class
```

---

## 🔶 Real-World Analogy : Restaurant Menu

**Without Abstraction:** Customer sees everything
- Raw ingredients
- How the cook prepares dishes
- Kitchen temperature controls
- Supplier details
- Too much information!

**With Abstraction:** Customer sees only what matters
- Menu items (Interface)
- Price (What to pay)
- That's it!
- Cooking process is hidden

---


## 🔶 Abstraction in Python: Abstract Base Classes

Use the `abc` module to create abstract classes:

```python
from abc import ABC, abstractmethod

class ServiceProvider(ABC):
    @abstractmethod
    def deliver_service(self):
        pass
    
    @abstractmethod
    def track_status(self):
        pass
```

**Key points:**
- Classes inheriting from `ABC` can have abstract methods
- Subclasses MUST implement all abstract methods
- You CANNOT create an instance of an abstract class

---

## 🔶 Example 1: Food Delivery Services

Different services, same interface:

```python
from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def place_order(self, dish_name, address):
        pass
    
    @abstractmethod
    def track_delivery(self):
        pass

class BiryaniHut(DeliveryService):
    def place_order(self, dish_name, address):
        print(f"🍛 {dish_name} order placed via BiryaniHut to {address}")
    
    def track_delivery(self):
        print("📍 Your order is 10 minutes away")

class PizzaPlanet(DeliveryService):
    def place_order(self, dish_name, address):
        print(f"🍕 {dish_name} order placed via PizzaPlanet to {address}")
    
    def track_delivery(self):
        print("📍 Your order is 15 minutes away")

# User doesn't care HOW delivery works, only THAT it works
def order_food(service: DeliveryService, dish, address):
    service.place_order(dish, address)
    service.track_delivery()

order_food(BiryaniHut(), "Biryani", "Karachi")
order_food(PizzaPlanet(), "Pizza", "Lahore")
```

**Output:**
```
🍛 Biryani order placed via BiryaniHut to Karachi
📍 Your order is 10 minutes away
🍕 Pizza order placed via PizzaPlanet to Lahore
📍 Your order is 15 minutes away
```

---

## 🔶 Example 2: Banking Systems

Different bank types, same operations:

```python
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def open_account(self, name):
        pass
    
    @abstractmethod
    def process_loan(self, amount):
        pass

class PakistanBank(Bank):
    def open_account(self, name):
        print(f"✅ Account opened at Pakistan Bank for {name}")
    
    def process_loan(self, amount):
        print(f"💰 Loan of Rs.{amount} approved by Pakistan Bank")

class IslamicBank(Bank):
    def open_account(self, name):
        print(f"✅ Shariah-compliant account opened for {name}")
    
    def process_loan(self, amount):
        print(f"💰 Halal loan of Rs.{amount} approved")

# Different banks, same interface
def apply_for_service(bank: Bank, customer_name, loan_amount):
    bank.open_account(customer_name)
    bank.process_loan(loan_amount)

apply_for_service(PakistanBank(), "Ali", 100000)
apply_for_service(IslamicBank(), "Sara", 200000)
```

---

## 🔶 Why Use Abstraction?

| Benefit | Explanation |
|---------|-------------|
| **Simplicity** | Users see only essential features |
| **Enforcement** | Subclasses MUST implement required methods |
| **Flexibility** | Can swap implementations without breaking code |
| **Maintainability** | Internal changes don't affect user code |
| **Consistency** | All subclasses follow the same contract |

---

## 🔶 Abstraction vs Encapsulation

Easy to confuse! Here's the difference:

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| **Focus** | What a class DOES | How data is HIDDEN |
| **Purpose** | Hide implementation | Protect data from misuse |
| **Achieved by** | Abstract classes & methods | Public/Private/Protected members |
| **Example** | `@abstractmethod` | `self.__private_var` |

**Simple way to remember:**
- **Abstraction** = Hide the HOW
- **Encapsulation** = Hide the WHAT (the data)

---

## 🔶 Both Together: Complete Example

```python
from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name):
        self.__name = name        # Encapsulation: private data
        self.__marks = []         # Encapsulation: hidden list
    
    @abstractmethod
    def submit_assignment(self):
        pass
    
    @abstractmethod
    def take_exam(self):
        pass
    
    # Encapsulation: controlled access to private data
    def add_marks(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
    
    def get_average(self):
        return sum(self.__marks) / len(self.__marks) if self.__marks else 0

class UniversityStudent(Student):
    def submit_assignment(self):
        print("📝 Assignment submitted to university portal")
    
    def take_exam(self):
        print("📚 Exam taken in exam hall")

class OnlineStudent(Student):
    def submit_assignment(self):
        print("💻 Assignment submitted via online platform")
    
    def take_exam(self):
        print("🖥️ Exam taken via proctored system")

# Using both abstraction and encapsulation
def register_student(student: Student, marks_list):
    student.submit_assignment()
    student.take_exam()
    for mark in marks_list:
        student.add_marks(mark)
    print(f"Average: {student.get_average():.1f}")

print("University Student:")
register_student(UniversityStudent(), [85, 90, 88])

print("\nOnline Student:")
register_student(OnlineStudent(), [92, 88, 95])
```

**Output:**
```
University Student:
📝 Assignment submitted to university portal
📚 Exam taken in exam hall
Average: 87.7

Online Student:
💻 Assignment submitted via online platform
🖥️ Exam taken via proctored system
Average: 91.7
```


---

## 🔶 Key Rules to Remember

✅ **DO:**
- Define abstract methods that subclasses MUST implement
- Use abstract classes to enforce a contract
- Keep abstract methods focused on what to do, not how

❌ **DON'T:**
- Try to instantiate an abstract class directly
- Create abstract methods in non-abstract classes
- Make everything abstract (use it when you need multiple implementations)

---