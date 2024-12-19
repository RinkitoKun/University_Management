class Person:
    def __init__(self, name, email, password, phone, gender, address):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.gender = gender
        self.address = address

    def login(self, email, password):
        return self.email == email and self.password == password

    def logout(self):
        print(f"{self.name} has logged out.")
