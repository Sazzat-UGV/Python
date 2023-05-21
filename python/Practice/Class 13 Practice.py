class Student:
    def __init__(self,name,age,cgpa,roll):
        self.name=name
        self.age=age
        self.cgpa=cgpa
        self.roll=roll
        self._hand_cash=5000 #This is Private Proparty

    def increment_age(self,age_to_be_increment):
        self.age=self.age+age_to_be_increment

    def purchase_something(self,amount):
        self._hand_cash=self._hand_cash-amount
        return f"Now you 've only {self._hand_cash} taka"
        
    def __del__(self):
        print("Destructor Called")

student1=Student("Asikul Islam Sazzat", 24 , 3.86, 12011016)
print(student1.name)
print(student1.age)
print(student1.cgpa)
print(student1.roll)
student1.increment_age(6)
print(student1.age)
print(student1.purchase_something(750))