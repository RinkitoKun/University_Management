from database import DatabaseConnection
from models.users import UserFactory
from models.course import Course
from models.schedule import Schedule
from models.room import Room
# from models.assignment import Assignment
# from models.attendance import Attendance

# Main Function
def main():
    db = DatabaseConnection()
    conn = db.conn

    print("Welcome to University Management System")
    while True:
        print("\nLogin Options:")
        print("1. Login as Staff")
        print("2. Login as Professor")
        print("3. Login as Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter email: ")
            password = input("Enter password: ")

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ? AND user_type = ?", (email, password, "Staff"))
            staff_data = cursor.fetchone()

            if staff_data:
                staff = UserFactory.create_user("Staff", *staff_data)
                print(f"Welcome {staff.name}")
                while True:
                    print("\nStaff Dashboard")
                    print("1. View Users")
                    print("2. Add User")
                    print("3. Update User")
                    print("4. Delete User")
                    print("5. Logout")

                    staff_choice = input("Enter your choice: ")

                    if staff_choice == "1":
                        user_type = input("Enter user type (Student/Professor/Staff): ")
                        staff.view_users(user_type, conn)
                    elif staff_choice == "2":
                        user_type = input("Enter user type (Student/Professor/Staff): ")
                        staff.add_user(user_type, conn)
                    elif staff_choice == "3":
                        user_type = input("Enter user type (Student/Professor/Staff): ")
                        staff.update_user(user_type, conn)
                    elif staff_choice == "4":
                        user_type = input("Enter user type (Student/Professor/Staff): ")
                        staff.delete_user(user_type, conn)
                    elif staff_choice == "5":
                        staff.logout()
                        break
                    else:
                        print("Invalid choice. Try again.")

            else:
                print("Invalid email or password.")

        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ? AND user_type = ?", (email, password, "Professor"))
            professor_data = cursor.fetchone()

            if professor_data:
                professor = UserFactory.create_user("Professor", *professor_data)
                print(f"Welcome {professor.name}")
                while True:
                    print("\nProfessor Dashboard")
                    print("1. View Assigned Courses")
                    print("2. Assign Course")
                    print("3. Logout")

                    professor_choice = input("Enter your choice: ")

                    if professor_choice == "1":
                        print(professor.view_courses(conn))
                    elif professor_choice == "2":
                        course = input("Enter course name: ")
                        professor.assign_course(course, conn)
                        print(f"Course '{course}' assigned successfully.")
                    elif professor_choice == "3":
                        professor.logout()
                        break
                    else:
                        print("Invalid choice. Try again.")

            else:
                print("Invalid email or password.")

        elif choice == "3":
            email = input("Enter email: ")
            password = input("Enter password: ")

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ? AND user_type = ?", (email, password, "Student"))
            student_data = cursor.fetchone()

            if student_data:
                student = UserFactory.create_user("Student", *student_data)
                print(f"Welcome {student.name}")
                while True:
                    print("\nStudent Dashboard")
                    print("1. View Enrolled Courses")
                    print("2. Enroll in a Course")
                    print("3. Logout")

                    student_choice = input("Enter your choice: ")

                    if student_choice == "1":
                        student.view_courses(conn)
                    elif student_choice == "2":
                        course = input("Enter course name: ")
                        student.enroll_course(course, conn)
                        print(f"Course '{course}' enrolled successfully.")
                    elif student_choice == "3":
                        student.logout()
                        break
                    else:
                        print("Invalid choice. Try again.")

            else:
                print("Invalid email or password.")

        elif choice == "4":
            print("Goodbye!")
            db.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
