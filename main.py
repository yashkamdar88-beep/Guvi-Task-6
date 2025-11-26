# ---------------------------------------------------------
#                BANK ACCOUNT SYSTEM (OOP)
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance=0):
        # Protected attributes for account number and balance
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self._balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money ensuring sufficient balance."""
        if amount <= 0:
            print("Withdraw amount must be positive!")
        elif amount > self._balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{self._balance}")

    def get_balance(self):
        """Return the current balance."""
        return self._balance


# ---------------------- SAVINGS ACCOUNT ----------------------

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Interest rate for savings

    def calculate_interest(self):
        """Calculate interest earned based on the current balance."""
        interest = self._balance * self.interest_rate
        print(f"Interest Earned: ₹{interest}")
        return interest


# ---------------------- CURRENT ACCOUNT ----------------------

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=1000):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance  # Minimum balance requirement

    def withdraw(self, amount):
        """Override withdraw to enforce minimum balance rule."""
        if amount <= 0:
            print("Withdraw amount must be positive!")
        elif self._balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ₹{amount}. Minimum balance of ₹{self.minimum_balance} must be maintained!")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{self._balance}")


# ------------------------- TESTING ACCOUNTS -------------------------

if __name__ == "__main__":

    print("\n--- SAVINGS ACCOUNT ---")
    s_acc = SavingsAccount("SA1001", 5000, 0.04)
    s_acc.deposit(2000)
    s_acc.withdraw(1000)
    s_acc.calculate_interest()
    print("Final Balance:", s_acc.get_balance())

    print("\n--- CURRENT ACCOUNT ---")
    c_acc = CurrentAccount("CA2001", 15000, 2000)
    c_acc.deposit(3000)
    c_acc.withdraw(14000)  # Not allowed due to minimum balance rule
    c_acc.withdraw(12000)  # Allowed
    print("Final Balance:", c_acc.get_balance())



# ---------------------------------------------------------
#                     EMPLOYEE MANAGEMENT
# ---------------------------------------------------------

class Employee:
    """Base employee class with a method meant to be overridden."""
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0  # Default implementation


# ----------------------- REGULAR EMPLOYEE -----------------------

class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        """Regular employee salary = base salary + bonus."""
        return self.base_salary + self.bonus


# ---------------------- CONTRACT EMPLOYEE ----------------------

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Contract employee salary = hourly rate × hours worked."""
        return self.hourly_rate * self.hours_worked


# --------------------------- MANAGER ----------------------------

class Manager(Employee):
    def __init__(self, name, base_salary, incentive, team_size):
        super().__init__(name)
        self.base_salary = base_salary
        self.incentive = incentive
        self.team_size = team_size

    def calculate_salary(self):
        """
        Manager salary = base + incentive + team allowance
        Team allowance example: ₹500 per team member
        """
        team_allowance = self.team_size * 500
        return self.base_salary + self.incentive + team_allowance


# ------------------------- TESTING EMPLOYEES -------------------------

employees = [
    RegularEmployee("Alice", 50000, 8000),
    ContractEmployee("Bob", 400, 120),
    Manager("Charlie", 70000, 15000, 10)
]

for emp in employees:
    print(f"{emp.name}'s Salary: {emp.calculate_salary()}")


# ---------------------------------------------------------
#                   VEHICLE RENTAL SYSTEM
# ---------------------------------------------------------

class Vehicle:
    """Base vehicle class with a method for rental cost calculation."""
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, duration):
        return 0  # To be overridden


# ------------------------------ CAR ------------------------------

class Car(Vehicle):
    def __init__(self, model, rental_rate, luxury_level):
        super().__init__(model, rental_rate)
        self.luxury_level = luxury_level  # standard | premium | luxury

    def calculate_rental(self, duration):
        """Car rental adds extra charge based on luxury level."""
        if self.luxury_level == "premium":
            extra = 300
        elif self.luxury_level == "luxury":
            extra = 600
        else:
            extra = 0
        return (self.rental_rate * duration) + extra


# ------------------------------ BIKE ------------------------------

class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_required=True):
        super().__init__(model, rental_rate)
        self.helmet_required = helmet_required

    def calculate_rental(self, duration):
        """Bike rental adds a small safety charge if helmet provided."""
        safety_charge = 50 if self.helmet_required else 0
        return (self.rental_rate * duration) + safety_charge


# ------------------------------ TRUCK ------------------------------

class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity  # in tons

    def calculate_rental(self, duration):
        """Truck rental adds capacity-based charge."""
        capacity_charge = self.load_capacity * 200
        return (self.rental_rate * duration) + capacity_charge


# -------------------------- TESTING VEHICLES --------------------------

vehicles = [
    Car("Toyota Innova", 1500, "premium"),
    Bike("Royal Enfield", 300, True),
    Truck("Tata Heavy Duty", 2500, 5)
]

duration = 6  # Renting for 6 hours

for vehicle in vehicles:
    print(f"{vehicle.model} Rental Cost for {duration} hours: {vehicle.calculate_rental(duration)}")
