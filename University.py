# # main.py
# import sqlite3
# from staff import Staff
# from student import Student
# from professor import Professor
#
# # Database connection setup
# conn = sqlite3.connect('university.db')
# cursor = conn.cursor()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Users (
#         id TEXT PRIMARY KEY,
#         name TEXT,
#         email TEXT UNIQUE,
#         password TEXT,
#         phone TEXT,
#         gender TEXT,
#         address TEXT,
#         user_type TEXT
#     )
# ''')
# conn.commit()
#
# def main():
#     print("Welcome to University Management System")
#     while True:
#         print("\n1. Login as Staff")
#         print("2. Exit")
#
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             email = input("Enter email: ")
#             password = input("Enter password: ")
#             staff = Staff("STA0001", "Admin", email, password, "1234567890", "Male", "Admin Address")
#
#             if staff.login(email, password):
#                 print(f"Welcome {staff.name}")
#                 while True:
#                     print("\nStaff Dashboard")
#                     print("1. View Users")
#                     print("2. Add User")
#                     print("3. Update User")
#                     print("4. Delete User")
#                     print("5. Logout")
#
#                     staff_choice = input("Enter your choice: ")
#                     if staff_choice == "1":
#                         user_type = input("Enter user type (Student/Professor/Staff): ")
#                         staff.view_users(user_type, conn)
#                     elif staff_choice == "2":
#                         user_type = input("Enter user type (Student/Professor/Staff): ")
#                         staff.add_user(user_type, conn)
#                     elif staff_choice == "3":
#                         user_type = input("Enter user type (Student/Professor/Staff): ")
#                         staff.update_user(user_type, conn)
#                     elif staff_choice == "4":
#                         user_type = input("Enter user type (Student/Professor/Staff): ")
#                         staff.delete_user(user_type, conn)
#                     elif staff_choice == "5":
#                         staff.logout()
#                         break
#                     else:
#                         print("Invalid choice. Try again.")
#             else:
#                 print("Invalid login details.")
#         elif choice == "2":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.")
#
# if __name__ == "__main__":
#     main()
