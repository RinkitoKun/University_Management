class Course:
    def __init__(self, courseID, courseName, courseDescription, creditHours, professorName, scheduleID):
        self.courseID = courseID
        self.courseName = courseName
        self.courseDescription = courseDescription
        self.creditHours = creditHours
        self.professorName = professorName
        self.scheduleID = scheduleID

    @staticmethod
    def create_course(courseID, courseName, courseDescription, creditHours, professorName, scheduleID, conn):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Course (courseID, courseName, courseDescription, creditHours, professorName, scheduleID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (courseID, courseName, courseDescription, creditHours, professorName, scheduleID))
        conn.commit()
        print(f"Course '{courseName}' created successfully.")

    @staticmethod
    def view_courses(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Course")
        courses = cursor.fetchall()
        return courses
