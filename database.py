import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect("university.db")
            cls._instance.cursor = cls._instance.conn.cursor()
            cls._instance.setup_tables()
            cls._instance.add_default_users()
        return cls._instance

    def setup_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE,
                password TEXT,
                phone TEXT,
                gender TEXT,
                address TEXT,
                user_type TEXT
            )
        ''')

        # Course Table with Foreign Key to Users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Course (
                courseID TEXT PRIMARY KEY,
                courseName TEXT,
                courseDescription TEXT,
                creditHours INTEGER,
                professorID TEXT,
                scheduleID TEXT,
                FOREIGN KEY (professorID) REFERENCES Users (id) ON DELETE CASCADE,
                FOREIGN KEY (scheduleID) REFERENCES Schedule (scheduleID) ON DELETE SET NULL
            )
        ''')

        # Schedule Table with no Foreign Keys
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Schedule (
                scheduleID TEXT PRIMARY KEY,
                dayOfWeek TEXT,
                startTime TEXT,
                endTime TEXT,
                roomID TEXT,
                FOREIGN KEY (roomID) REFERENCES Room (roomID) ON DELETE SET NULL
            )
        ''')

        # Room Table with no Foreign Keys
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Room (
                roomID TEXT PRIMARY KEY,
                roomType TEXT,
                location TEXT
            )
        ''')

        # Assignment Table with Foreign Key to Course
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Assignment (
                assignmentID TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                dueDate TEXT,
                maxMarks INTEGER,
                courseID TEXT,
                FOREIGN KEY (courseID) REFERENCES Course (courseID) ON DELETE CASCADE
            )
        ''')

        # Attendance Table with Foreign Key to Course
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Attendance (
                attendanceID TEXT PRIMARY KEY,
                totalClasses INTEGER,
                studentName TEXT,
                courseID TEXT,
                classesAttended INTEGER,
                attendancePercentage REAL,
                FOREIGN KEY (courseID) REFERENCES Course (courseID) ON DELETE CASCADE
            )
        ''')

        self.conn.commit()

    def add_default_users(self):
        self.cursor.execute('''
            INSERT OR IGNORE INTO Users (id, name, email, password, phone, gender, address, user_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ("STA001", "Admin", "staff@gmail.com", "123", "1112223333", "Male", "Admin Street", "Staff"))
        self.conn.commit()

    def close(self):
        self.conn.close()
