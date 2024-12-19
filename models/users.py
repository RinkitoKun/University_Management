from models.professor import Professor
from models.staff import Staff
from models.student import Student
from database import DatabaseConnection

class UserFactory:
    @staticmethod
    def create_user(user_type, *user_data):
        if user_type == "Professor":
            return Professor(*user_data)
        elif user_type == "Staff":
            return Staff(*user_data)
        elif user_type == "Student":
            return Student(*user_data)
        else:
            raise ValueError("Invalid user type.")

# Professor (in professor.py)
from models.person import Person

class Professor(Person):
    def __init__(self, professor_id, name, email, password, phone, gender, address, specialization):
        super().__init__(name, email, password, phone, gender, address)
        self.professor_id = professor_id
        self.specialization = specialization
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def view_courses(self):
        return self.assigned_courses

# Staff (in staff.py)
from models.person import Person
import sqlite3

class Staff(Person):
    def __init__(self, staff_id, name, email, password, phone, gender, address, position="General"):
        super().__init__(name, email, password, phone, gender, address)
        self.staff_id = staff_id
        self.position = position

    def view_users(self, user_type, conn):
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, name, email, phone, gender, address FROM Users WHERE user_type = ?
        ''', (user_type,))
        users = cursor.fetchall()

        print(f"\n{user_type} Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Phone: {user[3]}, Gender: {user[4]}, Address: {user[5]}")

    def add_user(self, user_type, conn):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        phone = input("Enter phone: ")
        gender = input("Enter gender: ")
        address = input("Enter address: ")

        user_id = self.generate_user_id(user_type, conn)

        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Users (id, name, email, password, phone, gender, address, user_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, name, email, password, phone, gender, address, user_type))
            conn.commit()
            print(f"{user_type} added successfully with ID: {user_id}.")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")

    def update_user(self, user_type, conn):
        user_id = input("Enter the user ID to update: ")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM Users WHERE id = ? AND user_type = ?
        ''', (user_id, user_type))
        user = cursor.fetchone()

        if user:
            print(f"Updating {user_type}: {user[1]} (ID: {user_id})")
            name = input(f"Enter new name (current: {user[1]}): ") or user[1]
            email = input(f"Enter new email (current: {user[2]}): ") or user[2]
            phone = input(f"Enter new phone (current: {user[3]}): ") or user[3]
            gender = input(f"Enter new gender (current: {user[4]}): ") or user[4]
            address = input(f"Enter new address (current: {user[5]}): ") or user[5]

            cursor.execute('''
                UPDATE Users SET name = ?, email = ?, phone = ?, gender = ?, address = ?
                WHERE id = ? AND user_type = ?
            ''', (name, email, phone, gender, address, user_id, user_type))
            conn.commit()
            print(f"{user_type} updated successfully.")
        else:
            print(f"{user_type} with ID {user_id} not found.")

    def delete_user(self, user_type, conn):
        user_id = input("Enter the user ID to delete: ")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM Users WHERE id = ? AND user_type = ?
        ''', (user_id, user_type))
        user = cursor.fetchone()

        if user:
            confirm = input(f"Are you sure you want to delete {user[1]} (ID: {user_id})? (yes/no): ")
            if confirm.lower() == "yes":
                cursor.execute('''
                    DELETE FROM Users WHERE id = ? AND user_type = ?
                ''', (user_id, user_type))
                conn.commit()
                print(f"{user_type} deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"{user_type} with ID {user_id} not found.")

    @staticmethod
    def generate_user_id(user_type, conn):
        prefix = {"Student": "STU", "Professor": "PRO", "Staff": "STA"}[user_type]
        cursor = conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM Users WHERE user_type = ?
        ''', (user_type,))
        count = cursor.fetchone()[0]
        return f"{prefix}{str(count + 1).zfill(4)}"

# Student (in student.py)
from models.person import Person

class Student(Person):
    def __init__(self, student_id, name, email, password, phone, gender, address):
        super().__init__(name, email, password, phone, gender, address)
        self.student_id = student_id
        self.enrolled_courses = LinkedList()

    def view_courses(self):
        return self.enrolled_courses.display()  # Assuming display() is implemented for LinkedList

    def enroll_course(self, course):
        self.enrolled_courses.append(course)  