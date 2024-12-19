from models.schedule import Schedule
from models.course import Course  # Assuming a Course class exists
from models.room import Room  # Import Room class
from models.person import Person 

class Student(Person):
    def __init__(self, student_id, name, email, password, phone, gender, address):
        super().__init__(name, email, password, phone, gender, address)
        self.student_id = student_id
        self.enrolled_courses = []  # List of courses the student is enrolled in
        self.schedule = Schedule()  # Associate the schedule with the student

    def enroll_course(self, course, room):
        """Enroll a student in a course with an associated room"""
        self.enrolled_courses.append(course)
        self.schedule.add_course(course, room)

    def view_courses(self):
        return self.enrolled_courses

    def view_schedule(self):
        """Student can view their schedule with rooms"""
        self.schedule.view_schedule()
