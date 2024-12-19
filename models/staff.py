from models.person import Person  # Import the Person class

class Staff(Person):  # Inherit from Person
    def __init__(self, staff_id, name, email, password, phone, gender, address, position="General"):
        # Call the parent class constructor
        super().__init__(name, email, password, phone, gender, address)
        self.staff_id = staff_id
        self.position = position

    def view_users(self, user_type, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_type = ?", (user_type,))
        users = cursor.fetchall()
        if users:
            for user in users:
                print(user)
        else:
            print(f"No {user_type}s found.")

    def add_user(self, user_type, conn):
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        phone = input("Enter Phone: ")
        gender = input("Enter Gender: ")
        address = input("Enter Address: ")

        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (id, name, email, password, phone, gender, address, user_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id, name, email, password, phone, gender, address, user_type))
        conn.commit()
        print(f"{user_type} added successfully.")

    def update_user(self, user_type, conn):
        id = input(f"Enter the ID of the {user_type} to update: ")
        name = input("Enter New Name: ")
        email = input("Enter New Email: ")
        password = input("Enter New Password: ")
        phone = input("Enter New Phone: ")
        gender = input("Enter New Gender: ")
        address = input("Enter New Address: ")

        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Users
            SET name = ?, email = ?, password = ?, phone = ?, gender = ?, address = ?
            WHERE id = ? AND user_type = ?
        ''', (name, email, password, phone, gender, address, id, user_type))
        conn.commit()
        print(f"{user_type} updated successfully.")

    def delete_user(self, user_type, conn):
        id = input(f"Enter the ID of the {user_type} to delete: ")

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE id = ? AND user_type = ?", (id, user_type))
        conn.commit()
        print(f"{user_type} deleted successfully.")

    def logout(self):
        print("Logged out successfully.")
