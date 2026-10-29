class Patient:
    _name = ""
    _bill_amount = 0.0
    def __init__(self, name: str, bill_amount: float):
        self._name = name
        self._bill_amount = bill_amount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value: float):
        if value >= 0:
            self._bill_amount = value
        else:
            raise ValueError("Bill amount cannot be negative.")

    def calculate_bill(self):
        print (f"Original Bill: P{self._bill_amount}")
        print (f"Final Bill: P{self._bill_amount}")
    def pat_typ(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = self._bill_amount * 0.8
        print(f"Original Bill: P{self._bill_amount}")
        print (f"New bill: P{discount}")
    def pat_typ(self):
        return "Senior Patient"

class PhilHealthPatient(Patient):
    def calculate_bill(self) -> float:
        discount = 0.15
        return self.bill_amount * (1 - discount)

if __name__ == "__main__":
    patient1 = Patient("Alice", 1000.0)
    print(f"Patient: {patient1.name}")
    print(f"Patient Type: {patient1.pat_typ}")  
    print(f"Original Bill: ₱{patient1.bill_amount:.2f}")
    print(f"Final Bill (Regular): ₱{patient1.calculate_bill():.2f}\n")

    patient2 = SeniorPatient("Bob", 1000.0)
    print(f"Patient: {patient2.name}")
    print(f"Patient Type: {patient2.pat_typ}") 
    print(f"Original Bill: ₱{patient2.bill_amount:.2f}")
    print(f"Final Bill (Senior Citizen): ₱{patient2.calculate_bill():.2f}\n")

    patient3 = PhilHealthPatient("Charlie", 1000.0)
    print(f"Patient: {patient3.name}")
    print(f"Original Bill: ₱{patient3.bill_amount:.2f}")
    print(f"Final Bill (PhilHealth): ₱{patient3.calculate_bill():.2f}\n")
